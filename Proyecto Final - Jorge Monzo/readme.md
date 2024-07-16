# API REST (servidor web) 

# Estructura de proyecto
/apirest_base/
   |--/sql               ->scripts qSQL para la estructura de la DB
   |--/app.py            ->Punto de entrada de la apirest(toda la lógica del servidor web)
   |--/database.py       ->Clase con la lógica de interacción a MySQL
   |--/dice.py           ->Clase con la lógica para la tirada de dados
   |--/utils             ->Clase con las REGEXP para verificar DNI, password y email
   |--/requirements.txt  ->Archivo que contiene todos los módulos necesarios para la app

## requirements.txt: El comando que ejecutamos para que lea todos los módulos (dependencias) de este archivo y los instale en nuestro proyecto
```
pip install -r requirements.txt
```
# Crear entorno virtual y activalor
```
python -m venv venv
```
venv\Scripts\activate
```

# Pasos Desarrollo
1- Crear el archivo "sql/database.sql" que contiene la estructura de la basa de datos en MySQL (DB relacional). Esta tabla solo contiene un campo data en el que interactua la api rest

2- Desarrollar la Clase "Database" en "/database.py"
   - Constructor: Crea la conexión a MySQL
   - 3 métodos: Que realizan las acciones de "CONSUTA/EJECUCIÓN/CERRAR CONEXIÓN"

3- Desarrollar al API REST
   1- Añadir los import que necesita el módulo
   2- Desarrollamos la clase ApiRestBase
      a- método que gestiona las cabeceras (información que viaja junto al paquete (request, response))



# Peticiones CRUD (create/read/upate/delete)
# GET: http://localhost:3000/users -> Devuelve todos usuarios de la tabla "userdb" cRud
      -body: None
# GET: http://localhost:3000/allroll -> Devuelve todas la tiradas de todos los usuarios de la tabla "dicesdb" cRud
      -body: None
# GET: http://localhost:3000/getroll/id -> Devuelve todas la tiradas de un usuario de la tabla "dicedb" cRud
      -body: None
# GET: http://localhost:3000/winner -> Devuelve el usuario con mayor número de tiradas ganadas de la tabla "dicedb" cRud
      -body: None

# POST: http://localhost:3000/user -> Crea/inserta un usaurio en la tabla "userdb" Crud
      -body (json):{"username":"dato_tipo_text","dni":"dato_tipo_text","email":"dato_tipo_text","password":"dato_tipo_text"}
# POST: http://localhost:3000/rolldice -> Crea/inserta una tirada para un usaurio en la tabla "dicesd" Crud
      -body (json):{"user_id": dato_tipo_int}

# PUT: http://localhost:3000/upuser -> Actualiza los datos (str) en la tabla "userdb" crUd
      -body (json): {"username":"dato_tipo_text"}
      -body (json): {"dni":"dato_tipo_text"}
      -body (json): {"email":"dato_tipo_text"}

# DELETE: http://localhost:3000/deluser -> Borra un usario en la tabla "userdb" cruD
      -body (json): {"id":id_del_usuario_a_borrar} 
# DELETE: http://localhost:3000/deldice -> Borra todas las tiradas un usario en la tabla "dicesdb" cruD
      -body (json): {"id_user": id_del_usuario_a_borrar}
