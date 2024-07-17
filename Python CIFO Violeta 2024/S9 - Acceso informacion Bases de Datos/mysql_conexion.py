# Acesso a servidor MySQL
# Para conectarnos a un servidor MySQL utilizamos un modulo que nos facilita esta tarea.
# Mediante el gestor de módulos de Python "PIP" instalamos este modulo y lo importamos:
# pip install mysql-connector-python
# https://dev.mysql.com/doc/connector-python/en/connector-python-example-connecting.html
import mysql.connector
# Establecemos conexion en nuestro caso (Xampp)
connex = mysql.connector.connect(
    user="root",
    password="",
    host="localhost",
    database="prueba"
)
# Creamos cursor que nos permite ejecutar codigo SQL (create, select, insert....)
cursor = connex.cursor()
# vacia la tabla de registros
cursor.execute("truncate table mis_datos")

# Insertamos un registro en la tabla "mis_datos"
cursor.execute("insert into mis_datos values(null, 'Hola mundo!')")
cursor.execute("insert into mis_datos values(null, 'Hello world!')")
# Se realiza commit (accion)
connex.commit()
# Cerrar 
cursor.close()

# Creamos un nuevo cursor para realizar una cosulta
cursor2 = connex.cursor()
cursor2.execute("select * from mis_datos")
datos = cursor2.fetchall()
print(datos)