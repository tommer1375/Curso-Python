import mysql.connector
from mysql.connector import Error


class Database:
    def __init__(self):
       try:
        self.connection=mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="apirest_jorge"
        )
       except Error as e:
        print ("Error en MySQL: "+str(e))    
       
       self.cursor=self.connection.cursor()

    #Método consulta
    def query(self, sql, params=None):
        self.cursor.execute(sql, params)
        return self.cursor.fetchall()
    
    #método ejecución
    def execute(self, sql, params=None):
        self.cursor.execute(sql, params)
        self.connection.commit()
        return self.cursor.rowcount
    
    #método cerrar
    def close(self):
        self.cursor.close()
        self.connection.close()
    
    def query_one(self, sql, params=None):
       self.cursor.execute(sql, params)
       return self.cursor.fetchone()
    
