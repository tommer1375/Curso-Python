# Crear y escribir en un archivo de texto (en la carpeta raiz del proyecto)
with open("saludo.txt", "w") as file:
    file.write("Hola mundo\n")
    file.write("Hello world\n")

# Crear y escribir en un archivo de texto (en carpeta creada manualmente dentro de una subcarpeta)
with open("archivos/saludo.txt", "w") as file:
    file.write("Hola mundo\n")
    file.write("Hello world\n")

# Crear y escribir en un archivo de texto (en carpeta creada desde Python)
import os # operating system
os.makedirs("archivos_python", exist_ok=True)
with open("archivos_python/saludo.txt", "w") as file:
    file.write("Hola mundo\n")
    file.write("Hello world\n")

# Abrir y leer un archivo de texto
with open("saludo.txt", "r") as file:
    content = file.read()
    print(content)

# Eliminar un archivo
os.remove("saludo.txt")

# Comprobar si un archivo existe
existe = os.path.exists("saludo.txt") 
print(existe)

# Crear, abrir y leer un archivo csv
import csv
with open("archivos_python/datos.csv", "w", newline="") as file:
    writer = csv.writer(file) # creamos el objeto que nos permite crear contenido csv
    writer.writerow(["Nombre", "Ciudad"])
    writer.writerow(["Pepe", "Barcelona"])
    writer.writerow(["María", "Badalona"])

with open("archivos_python/datos.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
        print(row[1]) # ciudad

# Crear, abrir y leer un archivo JSON
import json
data = {
    "Nombre": "Pepe",
    "Ciudad": "Barcelona"    
}
# escribir
with open("archivos_python/datos.json", "w") as file:
    # conversion de dict -> json
    json.dump(data, file)

# leer
with open("archivos_python/datos.json", "r") as file:
    datos = json.load(file)
    print(datos)
    print(type(datos)) # class -> dict

# Simulacion de Database (json) de la biblioteca
librosDB = [{
    "titulo": "a",
    "autor": "a",
    "isbn": "1234567890123",
    "genero": "a"
},{
    "titulo": "b",
    "autor": "b",
    "isbn": "1234567890121",
    "genero": "b"
}]

# escribir
with open("archivos_python/librosDB.json", "w") as file:
    # conversion de dict -> json
    json.dump(librosDB, file)

# validar si existe un titulo de libro en la database
with open("archivos_python/librosDB.json", "r") as file:
    datos = json.load(file)
    for libro in datos:
        if libro["titulo"] == "a":
            print("El libro 'a' existe")
            break
    
    
    











































