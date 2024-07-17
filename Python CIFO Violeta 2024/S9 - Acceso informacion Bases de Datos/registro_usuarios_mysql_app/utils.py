def conexion_a_mysql():
    import mysql.connector
    connex = mysql.connector.connect(
        user="root",
        password="",
        host="localhost",
        database="app"
    )
    # mensaje de error en la conex MySQL
    if connex.is_connected():
        return connex
    else:
        print("Ha habido un error en la conex. a MySQL")
    
def set_data_mysql(usuarioObj):
    connex = conexion_a_mysql()
    cursor = connex.cursor()
    # Evitar inyeccion SQL (seguridad)
    query = "insert into usuarios values (null, %s, %s, %s, %s)"
    cursor.execute(query, (usuarioObj.dni, usuarioObj.nombre, usuarioObj.email, usuarioObj.password))
    connex.commit()
    connex.close()
    cursor.close()

def get_data_mysql():
    connex = conexion_a_mysql()
    cursor = connex.cursor()
    query = "select * from usuarios"
    cursor.execute(query)
    usuarios = cursor.fetchall()
    connex.close()
    cursor.close()
    return usuarios

def get_one_data_mysql(dni):
    connex = conexion_a_mysql()
    cursor = connex.cursor()
    query = "select * from usuarios where dni = %s"
    cursor.execute(query, (dni,))
    usuario = cursor.fetchall()
    cursor.close()
    connex.close()
    return usuario

# def delete_one_data_mysql(dni):
#     if get_one_data_mysql(dni):
#         # lo borro
#         connex = conexion_a_mysql()
#         cursor = connex.cursor()
#         query = "delete from usuarios where dni = %s"
#         cursor.execute(query, (dni,))
#         connex.commit()
#         cursor.close()
#         return True
#     else:
#         return False

def delete_one_data_mysql(dni):
    connex = conexion_a_mysql()
    cursor = connex.cursor()
    query = "delete from usuarios where dni = %s"
    cursor.execute(query, (dni,))
    connex.commit()
    filas_afectadas = cursor.rowcount
    cursor.close()
    connex.close()
    if filas_afectadas > 0:
        return True
    else:
        return False


