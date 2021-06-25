create database trayectoria_escolar;
use trayectoria_escolar;

create table tipo_usuario(
  id tinyint(1) unsigned not null auto_increment,
  usuario varchar(20) not null,
  primary key(id) 
);

create table usuario(
  id int unsigned not null auto_increment,
  usuario varchar(20) not null,
  nombres varchar(20) not null,
  apellidos varchar(20) not null,
  password char(120) not null,
  tipo_usuario tinyint(1) unsigned not null,
  primary key(id),
  foreign key (tipo_usuario) references tipo_usuario(id)
);

insert into tipo_usuario(usuario) values('Administrador'), ('Client');

insert into usuario(usuario, nombres, apellidos, password, tipo_usuario)
values ('2017123026', 'Jorge Alberto', 'Garcia Estrada', 'pbkdf2:sha256:260000$drnY9ksi9BZwmW2O$9c0f70ac804982253886e4181815beb9901624ef5d441e0e6c05a175bb4197bb', 1);

-- SELECT U.id, U.usuario, T.id, T.usuario FROM usuario U JOIN tipo_usuario T 
--             ON U.tipo_usuario = T.id
--             WHERE U.id = 1;