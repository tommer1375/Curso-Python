drop database if exists biblioteca;
create database if not exists biblioteca;
use biblioteca;

create table usuarios(
    dni varchar(9) not null primary key,
    email varchar(50) not null,
    nombre varchar(50) not null,
    apellido varchar(50) not null
);

create table libros(
    isbn varchar(20) not null primary key,
    titulo varchar(50) not null,
    autor varchar(50) not null,
    genero varchar(50) not null
);

create table prestamos(
    id int not null primary key auto_increment,
    dni_usuario varchar(9) not null,
    isbn_libro varchar(13) not null,
    fecha_prestamo date not null,
    foreign key (dni_usuario) references usuarios(dni),
    foreign key (isbn_libro) references libros(isbn)
);