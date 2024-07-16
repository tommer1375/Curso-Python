from http.server import BaseHTTPRequestHandler, HTTPServer
import json, bcrypt
import utils

from database import Database
from dices import DoRoll


class ApiRestBase(BaseHTTPRequestHandler):
    

    def set_headers(self, status_code=200):
        self.send_response(status_code)
        self.send_header("Content-type", "application/json")
        self.end_headers()

    def do_POST(self):
        if self.path=="/user":
            
                content_lenght =int(self.headers["Content-length"]) 
                post_data=self.rfile.read(content_lenght) 
                datauser=json.loads(post_data.decode("utf-8"))
            
                dni=datauser["dni"]
                email = datauser["email"]
                password=datauser["password"]
               
                if not utils.check_email(email):
                        self.set_headers()
                        response=json.dumps({"Error":"Email incorrecto"}).encode("utf-8")
                        self.wfile.write(response)
                        return
                if not utils.check_dni(dni):
                        self.set_headers()
                        response=json.dumps({"Error":"DNI incorrecto"}).encode("utf-8")
                        self.wfile.write(response)
                        return
                if not utils.check_password(password):
                        self.set_headers()
                        response=json.dumps({"Error":"Password incorrecto (Debe contener mínimo 8 caracteres, 1 mayúscula, 1 minúscul y 1 número)"}).encode("utf-8")
                        self.wfile.write(response)
                        return
              
                db=Database()
                hashed_password = bcrypt.hashpw(datauser["password"].encode('utf-8'), bcrypt.gensalt())
                query = "INSERT INTO userdb (id, username, dni, email, password) VALUES (null, %s, %s, %s, %s)"
                try:
                    db.execute(query,(datauser["username"], datauser["dni"], datauser["email"], hashed_password))
                    db.close()
                    self.set_headers(201) 
                    self.wfile.write(json.dumps({"Mensaje":"Usuario guardado en MySQL."}).encode("utf-8"))      
                except Exception as e:
                  if "1062" in str(e):
                    self.set_headers(200) 
                    self.wfile.write(json.dumps({"Mensaje":"DNI o email ya existen en la tabla de datos"}).encode("utf-8"))   

        elif self.path=="/rolldice":
            content_lenght =int(self.headers["Content-Length"]) 
            post_data=self.rfile.read(content_lenght) 
            datauser=json.loads(post_data.decode("utf-8"))

            db=Database()
            dice1, dice2, total_dice, win=DoRoll.dice_roll()
            response = {
            "dice1": dice1,
            "dice2": dice2,
            "total_dice": total_dice,
            "win": win  }
            query="INSERT INTO dicesdb (id, id_user, dice1, dice2, total_dices, win) VALUES (NULL, %s, %s, %s, %s, %s)"
            db.execute(query,(datauser["user_id"], response["dice1"],response["dice2"],response["total_dice"],response["win"]))
            db.close()
            self.set_headers(201) 
            self.wfile.write(json.dumps(response).encode("utf-8"))
            self.wfile.write(json.dumps({"Mensaje":"Tirada guardada."}).encode("utf-8"))
        else:
            self.set_headers(400) 
            self.wfile.write(json.dumps({"Error":"Ruta no encontrada."}).encode("utf-8")) #devolvemos un mensaje en formato JSON al cliente

    def do_GET(self):
        db=Database() 
        if self.path=="/users":
            datausers=db.query("select * from userdb")
            if not datausers:
                    self.set_headers(400) 
                    self.wfile.write(json.dumps({"Error":"No hay usuarios"}).encode("utf-8")) 
                    return
            datauser_dic=[
                {"id":users[0],
                 "username":users[1],
                 "dni":users[2],
                 "email":users[3],
                 "password":users[4]
                }
                for users in datausers
                ]    
            self.set_headers()
            self.wfile.write(json.dumps(datauser_dic).encode("utf-8"))
        elif self.path=="/allroll":
            datadices=db.query("select * from dicesdb")
            if not datadices:
                    self.set_headers(400) 
                    self.wfile.write(json.dumps({"Error":"No hay tiradas"}).encode("utf-8")) 
                    return
            datadices_dic=[
                {"id":dice[0],
                 "id_user":dice[1],
                 "dice1":dice[2],
                 "dice2":dice[3],
                 "total_dice":dice[4],
                 "win":dice[5]
                }
                for dice in datadices
                ]    
            self.set_headers()
            self.wfile.write(json.dumps(datadices_dic).encode("utf-8"))
        elif self.path.startswith("/getroll/"):
            user_id = int(self.path.split("/")[-1])
            query = "SELECT dicesdb.* FROM dicesdb JOIN userdb ON dicesdb.id_user = userdb.id WHERE userdb.id = %s"
            datadices = db.query(query, (user_id,))
            if not datadices:
                self.set_headers(400)
                self.wfile.write(json.dumps({"Error": "No hay tiradas para el usuario con el ID proporcionado"}).encode("utf-8"))
                return
            datadices_dic = [
                {
                    "id": dice[0],
                    "id_user": dice[1],
                    "dice1": dice[2],
                    "dice2": dice[3],
                    "total_dice": dice[4],
                    "win": dice[5]
                }
                for dice in datadices
            ]
            self.set_headers()
            self.wfile.write(json.dumps(datadices_dic).encode("utf-8"))

        elif self.path=="/winner":
            datadices=db.query_one("SELECT u.username, COUNT(*) AS total_wins FROM userdb u JOIN dicesdb d ON u.id = d.id_user WHERE d.win = true GROUP BY u.username ORDER BY total_wins DESC LIMIT 1;")
            if not datadices:
                    self.set_headers(400) 
                    self.wfile.write(json.dumps({"Error":"No hay tiradas"}).encode("utf-8")) 
                    return
            datadices_dic = {
            "username": datadices[0],
            "total_win": datadices[1]
            }
            self.set_headers()
            self.wfile.write(json.dumps(datadices_dic).encode("utf-8"))
        else:
            self.set_headers(400) 
            self.wfile.write(json.dumps({"Error":"Ruta no encontrada"}).encode("utf-8")) 
   
    def do_DELETE(self):
        if self.path=="/deluser":
            content_lenght =int(self.headers["Content-length"]) 
            post_data=self.rfile.read(content_lenght) 
            datauser=json.loads(post_data.decode("utf-8"))
            db=Database()
            try:
                rows=db.execute("delete from userdb where id=%s", (datauser["id"],))
                db.close()
                if rows>0: 
                    self.set_headers(200)
                    self.wfile.write(json.dumps({"Mensaje":"Usuario borrado en MySQL."}).encode("utf-8"))
                else:
                    self.set_headers(400) 
                    self.wfile.write(json.dumps({"Error":"Usuario no encontrado"}).encode("utf-8")) 
            except Exception as e:
                    self.set_headers(200)
                    self.wfile.write(json.dumps({"Error":"No se puede borrar usuarios con tiradas."}).encode("utf-8"))
            
        elif self.path=="/deldice":
            content_lenght =int(self.headers["Content-length"]) 
            post_data=self.rfile.read(content_lenght) 
            datauser=json.loads(post_data.decode("utf-8"))
            db=Database()
            rows=db.execute("delete from dicesdb where id_user=%s", (datauser["id_user"],))
            db.close()
            if rows>0: 
                self.set_headers(200)
                self.wfile.write(json.dumps({"Mensaje":"Tiradas de usuario borradas en MySQL."}).encode("utf-8"))
            else:
                self.set_headers(400) 
                self.wfile.write(json.dumps({"Error":"Usuario no encontrado"}).encode("utf-8")) 
        else:
            self.set_headers(400) 
            self.wfile.write(json.dumps({"error":"Ruta no encontrada"}).encode("utf-8")) 


    def do_PUT(self):
        if self.path=="/upuser":
            content_lenght =int(self.headers["Content-length"]) 
            post_data=self.rfile.read(content_lenght) 
            datauser=json.loads(post_data.decode("utf-8"))
            db=Database()
            if "username" in datauser:
                rows=db.execute("update userdb set username=%s where id=%s", (datauser["username"], datauser["id"]))
                db.close()
                if rows>0:           
                    self.set_headers(200) 
                    self.wfile.write(json.dumps({"Mensaje":"Dato actualizado en MySQL."}).encode("utf-8"))
                else:
                    self.set_headers(200) 
                    self.wfile.write(json.dumps({"Mensaje":"Estás introduciendo el mismo dato."}).encode("utf-8"))
        
            elif "email" in datauser:
                email = datauser["email"]
                if not utils.check_email(email):
                    self.set_headers()
                    response=json.dumps({"Error":"Email incorrecto"}).encode("utf-8")
                    self.wfile.write(response)
                    return
                rows=db.execute("update userdb set email=%s where id=%s", (datauser["email"], datauser["id"]))
                db.close()
                if rows>0:           
                    self.set_headers(200) 
                    self.wfile.write(json.dumps({"Mensaje":"Dato actualizado en MySQL."}).encode("utf-8"))
                else:
                    self.set_headers(200) 
                    self.wfile.write(json.dumps({"Mensaje":"Estás introduciendo el mismo dato."}).encode("utf-8"))
            elif "dni" in datauser:
                dni=datauser["dni"]
                if not utils.check_dni(dni):
                    self.set_headers()
                    response=json.dumps({"Error":"DNI incorrecto"}).encode("utf-8")
                    self.wfile.write(response)
                    return
                rows=db.execute("update userdb set dni=%s where id=%s", (datauser["dni"], datauser["id"]))
                db.close()
                if rows>0:           
                    self.set_headers(200) 
                    self.wfile.write(json.dumps({"Mensaje":"Dato actualizado en MySQL."}).encode("utf-8"))
                else:
                    self.set_headers(200) 
                    self.wfile.write(json.dumps({"Mensaje":"Estás introduciendo el mismo dato."}).encode("utf-8"))    
            else:
                self.set_headers(400) 
                self.wfile.write(json.dumps({"error":"Usuario no encontrado"}).encode("utf-8")) 
        else:
            self.set_headers(400) 
            self.wfile.write(json.dumps({"error":"Ruta no encontrada"}).encode("utf-8")) 

def run(server_class=HTTPServer, handle_class=ApiRestBase, port=3000):
   server_address=("localhost",port)
   httpd=server_class(server_address, handle_class)
   print(f"ApiRest escuchando por el puerto {port}, listo para iniciar el juego...")
   httpd.serve_forever()
   
run()