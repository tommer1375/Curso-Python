# API REST (Servidor Web) base que nos sirve para desarrollar el proyecto final de curso de Python.

# Estructura Proyecto
/apirest_base/
    |------- /sql             ->  Scripts SQL para la estructura de la DB
    |------- app.py           ->  Punto de entrada de la apirest (lógica servidor web)
    |------- database.py      ->  Clase con lógica de interacción a MySQL
    |------- requirements.txt ->  Archivo que contiene todos los módulos necesarios para la app

## requirements.txt: El comando que ejecutamos para que lea todos los módulos (dependencias) de este archivo y los instale en nuestro proyecto:
```
pip install -r requirements.txt
```

# Crear entorno virtual y activarlo
```
python -m venv venv
```
```
venv\Scripts\activate
```

# PASOS DESARROLLO
1- Crear el archivo "sql/database.sql" que contiene la estructura de la base de datos en MySQL (DB relacional). Esta base de datos contiene solamente una tabla con un campo "dato" en el que interactua la api rest.

2- Desarrollar la Clase "Database" en "/database.py":
    - Constructor: Crea la conexion a MySQL
    - 3 métodos: Que realizan las acciones de "CONSULTA", "EJECUCIÓN" y "CERRAR CONEXIÓN"

3- Desarrollar la API REST en "/app.py" 
    1- Añadir los imports que necesita este modulo
    2- Desarrollamos la Clase "ApiRestBase"
        1- Método que gestiona las cabeceras (informacion que viaja junto al paquete (request, response))
        2- Método que gestiona la peticion GET
        3- Método que gestiona la peticion POST
        3- Método que gestiona la peticion DELETE


# Peticiones CRUD (create/read/update/delete)
# GET: http://localhost:3000/datos -> Devuelve todos los datos de la tabla "datos" (cRud)
    - body: None

# POST: http://localhost:3000/dato -> Crea/inserta un dato (str) en la tabla "datos" (Crud)
    - body (json): { "mensaje": "dato_tipo_texto" } 

# PUT: http://localhost:3000/dato -> Actualiza un dato (str) en la tabla "datos" (crUd)
    - body (json): { id:"id_del_dato_a_act", "mensaje": "dato_tipo_texto_act" }

# DELETE: http://localhost:3000/dato -> Borra un dato (str) en la tabla "datos" (crUd)
    - body (json): { id:"id_del_dato_a_borrar" } 