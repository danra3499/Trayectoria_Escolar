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
  clave VARCHAR(50) NOT NULL,
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

CREATE TABLE iao(
id_IAO INT NOT NULL,
nivel_IAO VARCHAR (35) NOT NULL,
categoria_IAO VARCHAR (25) NOT NULL,
PRIMARY KEY(id_IAO)
);

CREATE TABLE iac(
id_IAC INT NOT NULL,
nivel_IAC VARCHAR (35) NOT NULL,
categoria_IAC VARCHAR (25) NOT NULL,
PRIMARY KEY(id_IAC)
);

CREATE TABLE ipe(
id_IPE INT NOT NULL,
nivel_IPE VARCHAR (35) NOT NULL,
categoria_IPE VARCHAR (25) NOT NULL,
PRIMARY KEY(id_IPE)
);

CREATE TABLE ide(
id INT NOT NULL,
id_IDE INT(3) NOT NULL,
categoria_IDE VARCHAR (25) NOT NULL,
categoria_IAO INT NOT NULL,
categoria_IAC INT NOT NULL,
categoria_IPE INT NOT NULL,
FOREIGN KEY(categoria_IAO) REFERENCES iao(id_IAO),
FOREIGN KEY(categoria_IAC) REFERENCES iac(id_IAC),
FOREIGN KEY(categoria_IPE) REFERENCES ipe(id_IPE),
PRIMARY KEY(id)
);

CREATE TABLE ise(
id_ISE int not null,
nivel_ISE varchar (35) not null,
categoria_ISE varchar (25) not null,
primary key(id_ISE)
);

CREATE TABLE ire(
id int(11) not null,
id_IRE int(3) not null,
categoria_IRE varchar(25)NOT NULL,
categoria_IDE int(11) NOT NULL,
categoria_ISE int(11) NOT NULL,
FOREIGN KEY(categoria_IDE) REFERENCES ide(id_IDE),
FOREIGN KEY(categoria_ISE) REFERENCES ise(id_ISE),
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