# VALIDACIONES 
# TODO: RegExp (dni, nombre, email, password)

import os
import json

# Obtener el ruta del directorio actual y la de nuestra base datos
directorio_proyecto = os.path.dirname(os.path.abspath(__file__))
directorio_database = os.path.join(directorio_proyecto, "database")
# Crear el directorio si no existe
if not os.path.exists(directorio_database):
    os.makedirs(directorio_database)
ruta_fichero = os.path.join(directorio_database, "usuarios.json")

# DATABASE (json format)
def set_data_json(usuarioOBJ):

    dataFromJSON = get_data_json() # devuelve una lista con la db

    if not dataFromJSON:
        dataFromJSON = []
    else:
        # validar dni o email ya registrado
        for usuarioDB in dataFromJSON:
            if usuarioDB["dni"] == usuarioOBJ.dni or usuarioDB["email"] == usuarioOBJ.email:
                print("DNI o Email ya registrado")
                return

    dataFromJSON.append(usuarioOBJ.__dict__)

    with open(ruta_fichero, "w", encoding="utf-8") as file:
        json.dump(dataFromJSON, file, ensure_ascii=False, indent=4)

def get_data_json():
    if os.path.exists(ruta_fichero):
        with open(ruta_fichero, "r", encoding="utf-8") as file:
            listDB = json.load(file)
            return listDB 
    else:
        return [] # lista vacia
    

def delete_data_json(dni):

    dataFromJSON = get_data_json()

    for usuarioDB in dataFromJSON:
        if usuarioDB["dni"] == dni:
            dataFromJSON.remove(usuarioDB)
            with open(ruta_fichero, "w", encoding="utf-8") as file:
                json.dump(dataFromJSON, file, ensure_ascii=False, indent=4)
            return True
    return False
        
def find_data_json(dni):

    dataFromJSON = get_data_json()

    for usuarioDB in dataFromJSON:
        if usuarioDB["dni"] == dni:
            return usuarioDB
    return []    