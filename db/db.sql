DROP DATABASE IF EXISTS t_e;
CREATE DATABASE t_e;
USE t_e;

CREATE TABLE tipo_usuario(
  id TINYINT(1) UNSIGNED NOT NULL AUTO_INCREMENT,
  usuario VARCHAR(20) NOT NULL,
  PRIMARY KEY(id) 
);

CREATE TABLE usuario(
  id INT UNSIGNED NOT NULL AUTO_INCREMENT,
  usuario VARCHAR(20) NOT NULL,
  nombres VARCHAR(20) NOT NULL,
  apellido_p VARCHAR(20) NOT NULL,
  apellido_m VARCHAR(20) NOT NULL,
  password CHAR(120) NOT NULL,
  tipo_usuario TINYINT(1) UNSIGNED NOT NULL,
  FOREIGN KEY (tipo_usuario) REFERENCES tipo_usuario(id),
  PRIMARY KEY(id)
);

CREATE TABLE semestre(
  id INT NOT NULL AUTO_INCREMENT,
  nombre VARCHAR(50) NOT NULL,
  PRIMARY KEY(id)
);

CREATE TABLE grupo(
  id INT NOT NULL,
  semestre INT NOT NULL,
  FOREIGN KEY (semestre) REFERENCES semestre(id),
  PRIMARY KEY(id)
);

CREATE TABLE docente(
  id INT(10) NOT NULL,
  nombres VARCHAR(50) NOT NULL,
  apellido_p VARCHAR(50),
  apellido_m VARCHAR(50),
  PRIMARY KEY(id)
);

CREATE TABLE materia(
  id INT NOT NULL AUTO_INCREMENT,
  nombre VARCHAR(50) NOT NULL,
  n_creditos INT NOT NULL,
  id_grupo INT NOT NULL,
  id_docente INT NOT NULL,  
  FOREIGN KEY(id_grupo) REFERENCES grupo(id),
  FOREIGN KEY(id_docente) REFERENCES docente(id),
  PRIMARY KEY(id)
);

CREATE TABLE alumno(
  id INT(10) NOT NULL,
  nombres VARCHAR(50) NOT NULL,
  apellido_p VARCHAR(50) NOT NULL,
  apellido_m VARCHAR(50) NOT NULL,
  genero CHAR(1) NOT NULL,
  status BOOLEAN NOT NULL,
  id_grupo INT NOT NULL,
  FOREIGN KEY(id_grupo) REFERENCES grupo(id),
  PRIMARY KEY(id)
);

CREATE TABLE tipo_evaluacion(
  id INT NOT NULL AUTO_INCREMENT NOT NULL,
  nombre VARCHAR(20) NOT NULL,
  PRIMARY KEY(id)
);

CREATE TABLE evaluacion(
  id INT NOT NULL AUTO_INCREMENT,
  parcial INT NOT NULL,
  fecha DATE NOT NULL,
  calificacion DECIMAL(2,2),
  id_tipo_evaluacion INT NOT NULL,
  id_materia INT NOT NULL,
  id_alumno INT NOT NULL,
  FOREIGN KEY(id_tipo_evaluacion) REFERENCES tipo_evaluacion(id),
  FOREIGN KEY(id_alumno) REFERENCES alumno(id),
  FOREIGN KEY(id_materia) REFERENCES materia(id),
  PRIMARY KEY(id)
);

-- CREATE TABLE docentes(
--   id int not null auto_increment,
--   Profesión varchar(150) not null,
--   Nombres varchar(150) not null,
--   Telefono varchar(20) not null,
--   Email varchar (100) not null,
--   Materias_impartidas varchar (250) not null,
--   Horas varchar (50) not null,
--   primary key(id)
-- );