# Excepciones: Una excepción es un error que ocurre durante la ejecución de un programa. Cuando se produce una excepción, el programa se detiene y Python captura esa excepción. Mediante este manejo de errores podemos controlar cualquier evento o error.

# sintaxis:
# try: 
#     # codigo que puede lanzar una excpeción 
# except Exception as e:
#     # codigo que se ejecuta si se lanza excepcion
# finally: 
#     # Codigo que se ejecuta siempre, es opcional y es habitual para printar que se liberado recursos, cerrado conexiones, o ficheros...

# Ejemplo 1:
try: 
    # x = 4
    print(x)
except Exception as e:
    print("Error: " + str(e))
finally:
    print("Finalizado")

# Ejemplo 2:
try:
    print(1/0)
except Exception as e:
    print("Error: " + str(e))

# Ejemplo 3: Consumo de recurso asincrono
# try: 
#     # temporizador (simula tiempo de consumo)
#     import time
#     time.sleep(5)
# except Exception as e:
#     print("Error: " + str(e))
# finally:
#     print("El recurso ha finalizado")

# Ejemplo 4: Conexion a base de datos MySQL
import mysql.connector
from mysql.connector import Error 
# Las excepciones de un modulo que se han instalado mediante PIP, se gestionan con sus propias Clases, en este caso lo podemos ver su documentacion:
# https://dev.mysql.com/doc/connector-python/en/connector-python-api-errors-error.html
# suponemos una funcion (utils.py) que conecta a un server MySQL
def get_connection():
    try:
        connex = mysql.connector.connect(
            user="root",
            password="",
            host="localhost",
        )
        if connex.is_connected():
            print("Conexion a MySQL correcta!")
    except Error as e:
        # print("Error en la conexión a MySQL: " + str(e))
        print("Error code:", e.errno)        # error number
        print("SQLSTATE value:", e.sqlstate) # SQLSTATE value
        print("Error message:", e.msg)       # error message

get_connection()








