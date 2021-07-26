create database t_e;
use t_e;

create table tipo_usuario(
  id tinyint(1) unsigned not null auto_increment,
  usuario varchar(20) not null,
  primary key(id) 
);

create table usuario(
  id int unsigned not null auto_increment,
  usuario varchar(20) not null,
  nombres varchar(20) not null,-- normalizar apellidos
  apellidos varchar(20) not null,
  password char(120) not null,
  tipo_usuario tinyint(1) unsigned not null,
  primary key(id),
  foreign key (tipo_usuario) references tipo_usuario(id)
);

CREATE TABLE semestre(
  id INT NOT NULL AUTO_INCREMENT,
  nombre VARCHAR(50) NOT NULL,
  PRIMARY KEY(id)
);

CREATE TABLE grupo(
  id INT NOT NULL AUTO_INCREMENT,
  semestre INT NOT NULL,
  foreign key (semestre) REFERENCES semestre(id),
  PRIMARY KEY(id)
);

CREATE TABLE alumno(
  id INT(10) NOT NULL,
  nombres VARCHAR(50) NOT NULL,
  apellido_p VARCHAR(50) NOT NULL,
  apellido_m VARCHAR(50) NOT NULL,
  genero CHAR(1) NOT NULL,
  status BOOLEAN NOT NULL,
  id_semestre INT NOT NULL,
  id_grupo INT NOT NULL,
  FOREIGN KEY(id_semestre) REFERENCES semestre(id),
  FOREIGN KEY(id_grupo) REFERENCES grupo(id),
  PRIMARY KEY(id)
);

CREATE TABLE materia(
  id INT NOT NULL AUTO_INCREMENT,
  nombre VARCHAR(50) NOT NULL,
  n_creditos INT NOT NULL,
  id_semestre INT NOT NULL,
  FOREIGN KEY(id_semestre) REFERENCES semestre(id),
  PRIMARY KEY(id)
);

CREATE TABLE evaluacion(
  id INT NOT NULL AUTO_INCREMENT,
  parcial INT NOT NULL,
  fecha DATE NOT NULL,
  id_materia INT NOT NULL,
  id_alumno INT NOT NULL,
  nota DECIMAL(5, 2) NOT NULL,
  FOREIGN KEY(id_materia) REFERENCES materia(id),
  FOREIGN KEY(id_alumno) REFERENCES alumno(id),
  PRIMARY KEY(id)
);

insert into tipo_usuario(usuario) values('Administrador'), ('docente');
insert into usuario(usuario, nombres, apellidos, password, tipo_usuario)
values ('2017123026', 'Jorge Alberto', 'Garcia Estrada', 'pbkdf2:sha256:260000$drnY9ksi9BZwmW2O$9c0f70ac804982253886e4181815beb9901624ef5d441e0e6c05a175bb4197bb', 1);

insert into semestre(nombre) values('primer semestre'), ('segundo semestre'), ('tercero semestre'), 
('cuartosemestre'), ('quinto semestre'), ('sexto semestre'), ('septimo semestre'), ('octavo semestre');

-- GRUPOS
insert into grupo(id, semestre) values(3101, 1), (3102, 1), (3111, 1),
(3201, 2), (3202, 2), (3211, 2), (3301, 3), (3302, 3), (3311, 3),
(3401, 4), (3402, 4), (3411, 4), (3501, 5), (3502, 5), (3511, 5),
(3601, 6), (3602, 6), (3611, 6), (3701, 7), (3702, 7), (3711, 7),
(3801, 8), (3802, 8), (3811, 8);

-- MATERIAS
insert into materia(nombre, n_creditos, id_semestre) values
-- SEMESTRE 1
('CALCULO DIFERENCIAL', 5, 1),
('FUNDAMENTOS DE PROGRAMACION', 5, 1),
('TALLER DE ETICA', 4, 1), 
('MATEMATICAS DISCRETAS', 5, 1),
('TALLER DE ADMINISTRACION', 4, 1),
('FUNDAMENTOS DE INVESTIGACION', 4, 1),
-- SEMESTRE 2
('CALCULO INTEGRAL', 5, 2),
('PROGRAMACION ORIENTADA A OBJETOS', 5, 2),
('CONTABILIDAD FINANCIERA', 4, 2), 
('QUIMICA', 4, 2),
('ALGEBRA LINEAL', 5, 2),
('PROBABILIDAD Y ESTADISTICA', 5, 2),
-- SEMESTRE 3
('CALCULO VECTORIAL', 5, 3),
('ESTRUTURA DE DATOS', 5, 3),
('CULTURA EMPRESARIAL', 4, 3), 
('INVESTIGACION DE OPERACIONES', 4, 3),
('SISTEMAS OPERATIVOS', 4, 3),
('FISICA GENERAL', 5, 3),
-- SEMESTRE 4
('ECUACIONES DIFERENCIALES', 5, 4),
('METODOS NUMERICOS', 4, 4),
('TOPICOS AVANZADOS DE PROGRAMACION', 5, 4), 
('FUNDAMENTOS DE BASES DE DATOS', 5, 4),
('TALLER DE SISTEMAS OPERATIVOS', 4, 4),
('PRINCIPIOS ELECTRICOS Y APLICACIONES DIGITALES', 5, 4),
-- SEMESTRE 5
('DESARROLLO SUSTENTABLE', 5, 5),
('FUNDAMENTOS DE TELECOMUNICACIONES', 4, 5),
('TALLER DE BASES DE DATOS', 4, 5), 
('SIMULACION', 5, 5),
('FUNDAMENTOS DE INGENIERIA DE SOFTWARE', 4, 5),
('ARQUITECTURA DE COMPUTADORAS', 5, 5),
('INGENIERIA DE REQUERIMIENTOS', 4, 5),
-- SEMESTRE 6
('LENGUAJES Y AUTOMATAS I', 5, 6),
('REDES DE COMPUTADORA', 5, 6),
('ADMINISTRACION DE BASES DE DATOS', 5, 6), 
('GRAFICACION', 4, 6),
('INGENIERIA DE SOFTWARE', 5, 6),
('LENGUAJES DE INTERFAZ', 4, 6),
('ARQUITECTURA Y DISENIO DE SOFTWARE', 4, 6),
-- SEMESTRE 7
('LENGUAJES Y AUTOMATAS II', 5, 7),
('CONMUTACIÓN Y ENRUTAMIENTO DE REDES DE DATOS', 5, 7),
('TALLER DE INVESTIGACION I', 4, 7), 
('GESTION DE PROYECTOS DE SOFTWARE', 6, 7),
('SISTEMAS PROGRAMABLES', 5, 7),
('PROCESO PERSONAL PARA EL DESARROLLO DE SOFTWARE', 5, 7),
('MODELO DE DESARROLLO INTEGRAL CMMI', 4, 7),
-- SEMESTRE 8
('PROGRAMACION LOGICA Y FUNCIONAL', 4, 8),
('ADMINISTRACION REDES', 4, 8),
('TALLER DE INVESTIGACION II', 4, 8), 
('PROGRAMACION WEB', 5, 8),
('INTELIGENCIA ARTIFICIAL', 4, 8),
('VERIFICACION Y VALIDACION', 5, 8),
('PROGRAMACION EN MOVILES', 5, 8);