DROP DATABASE IF EXISTS apirest_jorge;
CREATE DATABASE apirest_jorge; 
USE apirest_jorge; 

CREATE TABLE userdb (
    id INT PRIMARY KEY AUTO_INCREMENT NOT NULL, 
    username VARCHAR(255) NOT NULL,
    dni VARCHAR(9) UNIQUE NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);

CREATE TABLE dicesdb (
    id INT PRIMARY KEY AUTO_INCREMENT NOT NULL, 
    id_user INT NOT NULL,
    dice1 INT NOT NULL,
    dice2 INT NOT NULL,
    total_dices INT NOT NULL,
    win BOOLEAN NOT NULL,
    FOREIGN KEY (id_user) REFERENCES userdb(id)
);