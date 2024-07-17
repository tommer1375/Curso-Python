drop database if exists prueba; -- Borra la base de datos "prueba" si existe
create database prueba; -- Crear la base de datos "prueba"
use prueba; -- selecciona la base de datos "prueba"

-- Creamos la tabla mis_datos
create table mis_datos(
    -- campo id (llave primaria): campo con valor único
    -- se autoincrementa automaticamente 1,2,3,4,5...
    id int primary key auto_increment,
    dato varchar(255) -- cadena de caracteres de contenido variable 
);





