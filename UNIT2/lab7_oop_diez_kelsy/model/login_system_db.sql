CREATE DATABASE IF NOT EXISTS login_system_db;
USE login_system_db;

CREATE TABLE IF NOT EXISTS users (
    id_user INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(256) NOT NULL,
    nombre VARCHAR(50) NOT NULL
);

INSERT INTO users (username, password, nombre) VALUES ('admin', 'admin123', 'Superadmin');
