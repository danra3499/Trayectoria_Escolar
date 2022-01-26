USE t_e;

INSERT INTO tipo_usuario(usuario) VALUES('Administrador'), ('docente');

INSERT INTO usuario(usuario, nombres, apellido_p, apellido_m, password, tipo_usuario)
VALUES ('2017123026', 'Jorge', 'Garcia' , 'Estrada', 'pbkdf2:sha256:260000$drnY9ksi9BZwmW2O$9c0f70ac804982253886e4181815beb9901624ef5d441e0e6c05a175bb4197bb', 1),
('2017123062', 'Alberto', 'Estrada' , 'Garcia', 'pbkdf2:sha256:260000$qVvqPAm1NwwP7Len$c5ad32952ce9b239f22a9e93f5a4ee5b39989e2bcc9b2888c21d0885939a9e29', 2);

INSERT INTO semestre(nombre) VALUES
('primer semestre'),
('segundo semestre'), 
('tercero semestre'), 
('cuarto semestre'), 
('quinto semestre'), 
('sexto semestre'), 
('septimo semestre'), 
('octavo semestre');

-- GRUPOS
INSERT INTO grupo(id, semestre) VALUES
(3101, 1), (3102, 1), (3111, 1),
(3201, 2), (3202, 2), (3211, 2), 
(3301, 3), (3302, 3), (3311, 3),
(3401, 4), (3402, 4), (3411, 4), 
(3501, 5), (3502, 5), (3511, 5),
(3601, 6), (3602, 6), (3611, 6), 
(3701, 7), (3702, 7), (3711, 7),
(3801, 8), (3802, 8), (3811, 8);

INSERT INTO alumno(id, nombres, apellido_p, apellido_m, genero, status, id_grupo) VALUES
(2017123089, 'Alonso', 'Guadarrama', 'Ruiz', 'M', true, 3801),
(2018123078, 'Fernanda', 'Millan', 'Rodriguez', 'F', true, 3601),
(2019123009, 'Alejandro', 'Ocampo', 'Madero', 'M', true, 3401),
(2020123056, 'Angel', 'Cruz', 'Salinas', 'M', true, 3201),
(2021123001, 'Alejandra', 'Martinez', 'Sanchez', 'F', true, 3101),
(2021127893, 'Baneza', 'Carlo', 'Acevedo', 'F', true, 3101);

INSERT INTO docente(id, nombres, apellido_p, apellido_m) VALUES
(1284373821, 'Chespirito', 'Cegobiano', 'Ruiz'),
(1392749212, 'Joaquin', 'Guzman', 'Loera'),
(1284390284, 'Enrique', 'Pena', 'Nieto'),
(1473826428, 'Vicente', 'Fox', 'Chapucero'),
(1492848201, 'Felipe', 'Calderon', 'Inojoza'),
(1394628402, 'Enrrique', 'Salinas', 'DeGortari');


-- MATERIAS
INSERT INTO materia(nombre, n_creditos, id_grupo, id_docente) VALUES
-- SEMESTRE 1
('CALCULO DIFERENCIAL', 5, 3101, 1284373821),
('FUNDAMENTOS DE PROGRAMACION', 5, 3101, 1473826428),
('TALLER DE ETICA', 4, 3101, 1492848201), 
('MATEMATICAS DISC', 5, 3101, 1284390284),
('TALLER DE ADMINISTRACION', 4, 3101, 1392749212),
('FUNDAMENTOS DE INVESTIGACION', 4, 3101, 1394628402),
-- SEMESTRE 2
('CALCULO INTEGRAL', 5, 3201, 1394628402),
('PROGRAMACION ORIENTADA A OBJETOS', 5, 3201, 1492848201),
('CONTABILIDAD FINANCIERA', 4, 3201, 1473826428), 
('QUIMICA', 4, 3201, 1284390284),
('ALGEBRA LINEAL', 5, 3201, 1392749212),
('PROBABILIDAD Y ESTADISTICA', 5, 3201, 1284373821);

INSERT INTO tipo_evaluacion(nombre) VALUES ('Curso normal'), ('Segunda oportunidad'), ('Recurse'), ('Especial');

-- INDICES
--IAO
INSERT INTO `iao` (`id_IAO`, `nivel_IAO`, `categoria_IAO`) VALUES
(1, '>=0,<=80', 'BAJO'),
(2, '>=80,<90', 'REGULAR'),
(3, '>=100', 'ALTO');

--IAC
INSERT INTO `iac` (`id_IAC`, `nivel_IAC`, `categoria_IAC`) VALUES
(1, '>=0,<85', 'BAJO'),
(2, '>=85,<100', 'REGULAR'),
(3, '>=100', 'ALTO');

--IPE
INSERT INTO `ipe` (`id_IPE`, `nivel_IPE`, `categoria_IPE`) VALUES
(1, '>=0,<80', 'BAJO'),
(2, '>=80,<90', 'REGULAR'),
(3, '>=90,<=100', 'ALTO');

--IDE
INSERT INTO `ide` (`id`, `id_IDE`, `categoria_IDE`, `categoria_IAO`, `categoria_IAC`, `categoria_IPE`) VALUES
(1, 1, 'BAJO', 1, 1, 1),
(2, 1, 'BAJO', 1, 1, 2),
(3, 1, 'BAJO', 1, 1, 3),
(4, 1, 'BAJO', 1, 2, 1),
(5, 1, 'BAJO', 1, 2, 2),
(6, 1, 'BAJO', 1, 2, 3),
(7, 1, 'BAJO', 1, 3, 1),
(8, 1, 'BAJO', 2, 1, 1),
(9, 1, 'BAJO', 2, 1, 2),
(10, 1, 'BAJO', 2, 2, 1),
(11, 1, 'BAJO', 3, 1, 1),
(12, 2, 'REGULAR', 2, 1, 3),
(13, 2, 'REGULAR', 1, 3, 2),
(14, 2, 'REGULAR', 1, 3, 3),
(15, 2, 'REGULAR', 2, 2, 2),
(16, 2, 'REGULAR', 2, 2, 3),
(17, 2, 'REGULAR', 2, 3, 1),
(18, 2, 'REGULAR', 3, 1, 2),
(19, 2, 'REGULAR', 3, 1, 3),
(20, 2, 'REGULAR', 3, 2, 1),
(21, 2, 'REGULAR', 3, 2, 2),
(22, 2, 'REGULAR', 3, 3, 1),
(23, 2, 'REGULAR', 2, 3, 2),
(24, 3, 'ALTO', 2, 3, 3),
(25, 3, 'ALTO', 3, 2, 3),
(26, 3, 'ALTO', 3, 3, 2),
(27, 3, 'ALTO', 3, 3, 3);

-- ISE
INSERT INTO `ise` (`id_ISE`, `nivel_ISE`, `categoria_ISE`) VALUES
(1, '>=0,<85', 'REZAGO'),
(2, '>=85,<100', 'IRREGULAR'),
(3, '>=100', 'ÓPTIMO');

--IRE
INSERT INTO `ire` (`id`, `id_IRE`, `categoria_IRE`, `categoria_IDE`, `categoria_ISE`) VALUES
('1', '1', 'RIESGO ALTO', '1', '1'),
('2', '1', 'RIESGO ALTO', '12', '1'),
('3', '1', 'RIESGO ALTO', '1','2'),
('4', '2', 'RIESGO MODERADO', '24', '1'),
('5', '2', 'RIESGO MODERADO', '12', '2'),
('6', '2', 'RIESGO MODERADO', '24', '2'),
('7', '2', 'RIESGO MODERADO', '1', '3'),
('8', '3', 'SIN RIESGO', '12', '3'),
('9', '3', 'SIN RIESGO', '24', '3');

-- -- MATERIAS
-- insert into materia(nombre, n_creditos, id_semestre) values
-- -- SEMESTRE 1
-- ('CALCULO DIFERENCIAL', 5, 1),
-- ('FUNDAMENTOS DE PROGRAMACION', 5, 1),
-- ('TALLER DE ETICA', 4, 1), 
-- ('MATEMATICAS DISCRETAS', 5, 1),
-- ('TALLER DE ADMINISTRACION', 4, 1),
-- ('FUNDAMENTOS DE INVESTIGACION', 4, 1),
-- -- SEMESTRE 2
-- ('CALCULO INTEGRAL', 5, 2),
-- ('PROGRAMACION ORIENTADA A OBJETOS', 5, 2),
-- ('CONTABILIDAD FINANCIERA', 4, 2), 
-- ('QUIMICA', 4, 2),
-- ('ALGEBRA LINEAL', 5, 2),
-- ('PROBABILIDAD Y ESTADISTICA', 5, 2),
-- -- SEMESTRE 3
-- ('CALCULO VECTORIAL', 5, 3),
-- ('ESTRUTURA DE DATOS', 5, 3),
-- ('CULTURA EMPRESARIAL', 4, 3), 
-- ('INVESTIGACION DE OPERACIONES', 4, 3),
-- ('SISTEMAS OPERATIVOS', 4, 3),
-- ('FISICA GENERAL', 5, 3),
-- -- SEMESTRE 4
-- ('ECUACIONES DIFERENCIALES', 5, 4),
-- ('METODOS NUMERICOS', 4, 4),
-- ('TOPICOS AVANZADOS DE PROGRAMACION', 5, 4), 
-- ('FUNDAMENTOS DE BASES DE DATOS', 5, 4),
-- ('TALLER DE SISTEMAS OPERATIVOS', 4, 4),
-- ('PRINCIPIOS ELECTRICOS Y APLICACIONES DIGITALES', 5, 4),
-- -- SEMESTRE 5
-- ('DESARROLLO SUSTENTABLE', 5, 5),
-- ('FUNDAMENTOS DE TELECOMUNICACIONES', 4, 5),
-- ('TALLER DE BASES DE DATOS', 4, 5), 
-- ('SIMULACION', 5, 5),
-- ('FUNDAMENTOS DE INGENIERIA DE SOFTWARE', 4, 5),
-- ('ARQUITECTURA DE COMPUTADORAS', 5, 5),
-- ('INGENIERIA DE REQUERIMIENTOS', 4, 5),
-- -- SEMESTRE 6
-- ('LENGUAJES Y AUTOMATAS I', 5, 6),
-- ('REDES DE COMPUTADORA', 5, 6),
-- ('ADMINISTRACION DE BASES DE DATOS', 5, 6), 
-- ('GRAFICACION', 4, 6),
-- ('INGENIERIA DE SOFTWARE', 5, 6),
-- ('LENGUAJES DE INTERFAZ', 4, 6),
-- ('ARQUITECTURA Y DISENIO DE SOFTWARE', 4, 6),
-- -- SEMESTRE 7
-- ('LENGUAJES Y AUTOMATAS II', 5, 7),
-- ('CONMUTACIÓN Y ENRUTAMIENTO DE REDES DE DATOS', 5, 7),
-- ('TALLER DE INVESTIGACION I', 4, 7), 
-- ('GESTION DE PROYECTOS DE SOFTWARE', 6, 7),
-- ('SISTEMAS PROGRAMABLES', 5, 7),
-- ('PROCESO PERSONAL PARA EL DESARROLLO DE SOFTWARE', 5, 7),
-- ('MODELO DE DESARROLLO INTEGRAL CMMI', 4, 7),
-- -- SEMESTRE 8
-- ('PROGRAMACION LOGICA Y FUNCIONAL', 4, 8),
-- ('ADMINISTRACION REDES', 4, 8),
-- ('TALLER DE INVESTIGACION II', 4, 8), 
-- ('PROGRAMACION WEB', 5, 8),
-- ('INTELIGENCIA ARTIFICIAL', 4, 8),
-- ('VERIFICACION Y VALIDACION', 5, 8),
-- ('PROGRAMACION EN MOVILES', 5, 8);