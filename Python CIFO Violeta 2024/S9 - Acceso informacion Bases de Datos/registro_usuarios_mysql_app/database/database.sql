drop database if exists app;
create database app;
use app;

create table usuarios(
    id int primary key auto_increment,
    dni char(9),
    nombre varchar(255),
    email varchar(255),
    password varchar(255)
);