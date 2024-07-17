# importar modulos necesarios
from http.server import BaseHTTPRequestHandler, HTTPServer
import json, bcrypt, utils
# modulo database
from database import Database

class ApiRestBase(BaseHTTPRequestHandler):
    # metodo que gestiona las cabeceras
    def set_headers(self, status_code=200):
        self.send_response(status_code)
        self.send_header("Content-type", "application/json")
        self.end_headers()
    
    def do_GET(self):
        db = Database() # instancia
        if self.path == "/datos":
            resultado = db.query("select * from datos")
            resultadoFormat = [
                {
                    "id": mensaje[0],
                    "mensaje": mensaje[1]
                }
                for mensaje in resultado 
            ]
            self.set_headers()
            self.wfile.write(json.dumps(resultadoFormat).encode("utf-8"))
        else:
            self.set_headers(404) # envio un 404 al metodo de cabeceras
            # devolvemos un mensaje en formato JSON al cliente
            self.wfile.write(json.dumps({"error": "Ruta no encontrada"}).encode("utf-8"))

    def do_POST(self):
        if self.path == "/dato":
            # recogemos el dato del cliente
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)
            mensaje = json.loads(post_data)
            # validaciones
            # email = mensaje["email"]
            # if not utils.validarEmail(email):
            #     self.set_headers(400) # bad request
            #     response = json.dumps({"error": "Email incorrecto"}).encode("utf-8")
            #     self.wfile.write(response)
            #     return
            
            db = Database() # instancia a Database
            # llamamos al metodo "execute" con el formato de consulta que evita inyeccion de SQL
            db.execute("insert into datos values (default, %s)", (mensaje["mensaje"],))
            db.close()
            self.set_headers(201) # envio un 201 (recurso creado) al metodo de cabeceras
            # devolvemos un mensaje en formato JSON al cliente
            response = json.dumps({"mensaje": "Dato almacenado en MySQL ok!"}).encode("utf-8")
            self.wfile.write(response)

        else:
            self.set_headers(404) # envio un 404 al metodo de cabeceras
            # devolvemos un mensaje en formato JSON al cliente
            self.wfile.write(json.dumps({"error": "Ruta no encontrada"}).encode("utf-8"))
    
    def do_PUT(self):
        if self.path == "/dato":
            # recogemos el dato del cliente
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)
            mensaje = json.loads(post_data)

            db = Database() # instancia a Database
            # llamamos al metodo "execute" con el formato de consulta que evita inyeccion de SQL
            rows = db.execute("update datos set dato = %s where id = %s", (mensaje["mensaje"], mensaje["id"]))
            db.close()
            if rows > 0:
                self.set_headers(200) # envio un 201 (recurso creado) al metodo de cabeceras
                # devolvemos un mensaje en formato JSON al cliente
                response = json.dumps({"mensaje": "Dato actualizado ok!"}).encode("utf-8")
                self.wfile.write(response)
            else: 
                self.set_headers(404) # envio un 404 (no encontro ID)
                self.wfile.write(json.dumps({"error": "Mensaje no encontrado"}).encode("utf-8"))

        else:
            self.set_headers(404) # envio un 404 al metodo de cabeceras
            # devolvemos un mensaje en formato JSON al cliente
            self.wfile.write(json.dumps({"error": "Ruta no encontrada"}).encode("utf-8"))
    
    def do_DELETE(self):
        if self.path == "/dato":
            # recogemos el dato del cliente
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)
            mensaje = json.loads(post_data)

            db = Database() # instancia a Database
            # llamamos al metodo "execute" con el formato de consulta que evita inyeccion de SQL
            rows = db.execute("delete from datos where id = %s", (mensaje["id"],))
            db.close()
            if rows > 0:
                self.set_headers(200) # envio un 201 (recurso creado) al metodo de cabeceras
                # devolvemos un mensaje en formato JSON al cliente
                response = json.dumps({"mensaje": "Dato borrado ok!"}).encode("utf-8")
                self.wfile.write(response)
            else: 
                self.set_headers(404) # envio un 404 (no encontro ID)
                self.wfile.write(json.dumps({"error": "Mensaje no encontrado"}).encode("utf-8"))
        else:
            self.set_headers(404) # envio un 404 al metodo de cabeceras
            # devolvemos un mensaje en formato JSON al cliente
            self.wfile.write(json.dumps({"error": "Ruta no encontrada"}).encode("utf-8"))


def run():
    server_address = ("localhost", 3000)
    server = HTTPServer(server_address, ApiRestBase)
    print("Servidor Localhost escuchando peticiones por el puerto 3000")
    server.serve_forever()

run()


