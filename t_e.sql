-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 08-05-2024 a las 06:38:26
-- Versión del servidor: 10.4.25-MariaDB
-- Versión de PHP: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `t_e`
--

DELIMITER $$
--
-- Procedimientos
--
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_actualizar_iac` (IN `id_alum` INT)   begin

 declare v_eval int;
 declare v_evalordinario int;
 declare v_porc float;
 declare v_porcordinario float;


 select count(e.id) NoEvaluaciones
 into v_eval
 from
 evaluacion e
 where e.id_alumno = id_alum;

 select count(id)
 into v_evalordinario
 from
 evaluacion
 where
 id_alumno = id_alum
 and calificacion >= 70;

 select 100/v_eval into v_porc;

 select v_porc * v_evalordinario into v_porcordinario;



if(v_porcordinario >= 0 and v_porcordinario < 80) then

   UPDATE alumno_indice SET iac = 'BAJO' where id_alumno = id_alum;

elseif (v_porcordinario >= 80 and v_porcordinario < 90) then

   UPDATE alumno_indice SET iac = 'REGULAR' where id_alumno = id_alum;

elseif (v_porcordinario >= 90 and v_porcordinario <= 100) then

   UPDATE alumno_indice SET iac = 'ALTO' where id_alumno = id_alum;
end if;

end$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_actualizar_iao` (IN `id_alum` INT)   begin

 declare v_eval int;
 declare v_evalordinario int;
 declare v_porc float;
 declare v_porcordinario float;


 select count(e.id) NoEvaluaciones
 into v_eval
 from
 evaluacion e
 where e.id_alumno = id_alum;

 select count(id)
 into v_evalordinario
 from
 evaluacion
 where
 id_alumno = id_alum
 and id_tipo_evaluacion = 1;

 select 100/v_eval into v_porc;

 select v_porc * v_evalordinario into v_porcordinario;



if(v_porcordinario >= 0 and v_porcordinario < 80) then

   UPDATE alumno_indice SET iao = 'BAJO' where id_alumno = id_alum;

elseif (v_porcordinario >= 80 and v_porcordinario < 90) then

   UPDATE alumno_indice SET iao = 'REGULAR' where id_alumno = id_alum;

elseif (v_porcordinario >= 90 and v_porcordinario <= 100) then

   UPDATE alumno_indice SET iao = 'ALTO' where id_alumno = id_alum;
end if;

end$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_actualizar_ide` (IN `id_alum` INT)   begin

 declare v_iac varchar(10);
 declare v_iao varchar(10);
 declare v_ipe varchar(10);

 select iac
 into v_iac
 from
 alumno_indice
 where id_alumno = id_alum;

 select iao
 into v_iao
 from
 alumno_indice
 where id_alumno = id_alum;

 select ipe
 into v_ipe
 from
 alumno_indice
 where id_alumno = id_alum;


if(v_iac = 'BAJO' and v_iao = 'BAJO' and v_ipe = 'BAJO') then

   UPDATE alumno_indice SET ide = 'BAJO' where id_alumno = id_alum;

elseif(v_iac = 'BAJO' and v_iao = 'BAJO' and v_ipe = 'REGULAR') then

   UPDATE alumno_indice SET ide = 'BAJO' where id_alumno = id_alum;

elseif(v_iac = 'BAJO' and v_iao = 'BAJO' and v_ipe = 'ALTO') then

   UPDATE alumno_indice SET ide = 'BAJO' where id_alumno = id_alum;

elseif(v_iac = 'BAJO' and v_iao = 'REGULAR' and v_ipe = 'BAJO') then

   UPDATE alumno_indice SET ide = 'BAJO' where id_alumno = id_alum;

elseif(v_iac = 'BAJO' and v_iao = 'REGULAR' and v_ipe = 'REGULAR') then

   UPDATE alumno_indice SET ide = 'BAJO' where id_alumno = id_alum;

elseif(v_iac = 'BAJO' and v_iao = 'REGULAR' and v_ipe = 'ALTO') then

   UPDATE alumno_indice SET ide = 'BAJO' where id_alumno = id_alum;

elseif(v_iac = 'BAJO' and v_iao = 'ALTO' and v_ipe = 'BAJO') then

   UPDATE alumno_indice SET ide = 'BAJO' where id_alumno = id_alum;

elseif(v_iac = 'REGULAR' and v_iao = 'BAJO' and v_ipe = 'BAJO') then

   UPDATE alumno_indice SET ide = 'BAJO' where id_alumno = id_alum;

elseif(v_iac = 'REGULAR' and v_iao = 'BAJO' and v_ipe = 'REGULAR') then

   UPDATE alumno_indice SET ide = 'BAJO' where id_alumno = id_alum;

elseif(v_iac = 'REGULAR' and v_iao = 'REGULAR' and v_ipe = 'BAJO') then

   UPDATE alumno_indice SET ide = 'BAJO' where id_alumno = id_alum;

elseif(v_iac = 'ALTO' and v_iao = 'BAJO' and v_ipe = 'BAJO') then

   UPDATE alumno_indice SET ide = 'BAJO' where id_alumno = id_alum;

elseif(v_iac = 'REGULAR' and v_iao = 'BAJO' and v_ipe = 'ALTO') then

   UPDATE alumno_indice SET ide = 'REGULAR' where id_alumno = id_alum;

elseif(v_iac = 'BAJO' and v_iao = 'ALTO' and v_ipe = 'REGULAR') then

   UPDATE alumno_indice SET ide = 'REGULAR' where id_alumno = id_alum;

elseif(v_iac = 'BAJO' and v_iao = 'ALTO' and v_ipe = 'ALTO') then

   UPDATE alumno_indice SET ide = 'REGULAR' where id_alumno = id_alum;

elseif(v_iac = 'REGULAR' and v_iao = 'REGULAR' and v_ipe = 'REGULAR') then

   UPDATE alumno_indice SET ide = 'REGULAR' where id_alumno = id_alum;

elseif(v_iac = 'REGULAR' and v_iao = 'REGULAR' and v_ipe = 'ALTO') then

   UPDATE alumno_indice SET ide = 'REGULAR' where id_alumno = id_alum;

elseif(v_iac = 'REGULAR' and v_iao = 'ALTO' and v_ipe = 'BAJO') then

   UPDATE alumno_indice SET ide = 'REGULAR' where id_alumno = id_alum;

elseif(v_iac = 'ALTO' and v_iao = 'BAJO' and v_ipe = 'REGULAR') then

   UPDATE alumno_indice SET ide = 'REGULAR' where id_alumno = id_alum;

elseif(v_iac = 'ALTO' and v_iao = 'BAJO' and v_ipe = 'ALTO') then

   UPDATE alumno_indice SET ide = 'REGULAR' where id_alumno = id_alum;

elseif(v_iac = 'ALTO' and v_iao = 'REGULAR' and v_ipe = 'BAJO') then

   UPDATE alumno_indice SET ide = 'REGULAR' where id_alumno = id_alum;

elseif(v_iac = 'ALTO' and v_iao = 'REGULAR' and v_ipe = 'REGULAR') then

   UPDATE alumno_indice SET ide = 'REGULAR' where id_alumno = id_alum;

elseif(v_iac = 'ALTO' and v_iao = 'ALTO' and v_ipe = 'BAJO') then

   UPDATE alumno_indice SET ide = 'REGULAR' where id_alumno = id_alum;

elseif(v_iac = 'REGULAR' and v_iao = 'ALTO' and v_ipe = 'REGULAR') then

   UPDATE alumno_indice SET ide = 'REGULAR' where id_alumno = id_alum;

elseif(v_iac = 'REGULAR' and v_iao = 'ALTO' and v_ipe = 'ALTO') then

   UPDATE alumno_indice SET ide = 'ALTO' where id_alumno = id_alum;

elseif(v_iac = 'ALTO' and v_iao = 'REGULAR' and v_ipe = 'ALTO') then

   UPDATE alumno_indice SET ide = 'ALTO' where id_alumno = id_alum;

elseif(v_iac = 'ALTO' and v_iao = 'ALTO' and v_ipe = 'REGULAR') then

   UPDATE alumno_indice SET ide = 'ALTO' where id_alumno = id_alum;

elseif(v_iac = 'ALTO' and v_iao = 'ALTO' and v_ipe = 'ALTO') then

   UPDATE alumno_indice SET ide = 'ALTO' where id_alumno = id_alum;

end if;

end$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_actualizar_ipe` (IN `id_alum` INT)   begin

 declare v_promedio int;

 select avg(calificacion) calificacion
 into v_promedio
 from evaluacion where id_alumno = id_alum;


if(v_promedio >= 0 and v_promedio < 80) then

   UPDATE alumno_indice SET ipe = 'BAJO' where id_alumno = id_alum;

elseif (v_promedio >= 80 and v_promedio < 90) then

   UPDATE alumno_indice SET ipe = 'REGULAR' where id_alumno = id_alum;

elseif (v_promedio >= 90 and v_promedio <= 100) then

   UPDATE alumno_indice SET ipe = 'ALTO' where id_alumno = id_alum;
end if;


end$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_actualizar_ire` (IN `id_alum` INT)   begin

 declare
  v_ide int;
 declare
  v_ise int;

  select
    ise,
    ide
  into v_ise, v_ide
  from
    alumno_indice
  where
    id_alumno = id_alum;


if(v_ise = 'REZAGO' and v_ide = 'BAJO') then

   UPDATE alumno_indice SET ire = 'RIESGO ALTO' where id_alumno = id_alum;

elseif (v_ise = 'REZAGO' and v_ide = 'REGULAR') then

   UPDATE alumno_indice SET ire = 'RIESGO ALTO' where id_alumno = id_alum;

elseif (v_ise = 'REZAGO' and v_ide = 'ALTO') then

   UPDATE alumno_indice SET ire = 'RIESGO MODERADO' where id_alumno = id_alum;

elseif (v_ise = 'IRREGULAR' and v_ide = 'BAJO') then

   UPDATE alumno_indice SET ire = 'RIESGO ALTO' where id_alumno = id_alum;

elseif (v_ise = 'IRREGULAR' and v_ide = 'REGULAR') then

   UPDATE alumno_indice SET ire = 'RIESGO MODERADO' where id_alumno = id_alum;

elseif (v_ise = 'IRREGULAR' and v_ide = 'ALTO') then

   UPDATE alumno_indice SET ire = 'RIESGO MODERADO' where id_alumno = id_alum;

elseif (v_ise = 'ÓPTIMO' and v_ide = 'BAJO') then

   UPDATE alumno_indice SET ire = 'RIESGO MODERADO' where id_alumno = id_alum;

elseif (v_ise = 'ÓPTIMO' and v_ide = 'REGULAR') then

   UPDATE alumno_indice SET ire = 'SIN RIESGO' where id_alumno = id_alum;

elseif (v_ise = 'ÓPTIMA' and v_ide = 'ALTO') then

   UPDATE alumno_indice SET ire = 'SIN RIESGO' where id_alumno = id_alum;
end if;

end$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_actualizar_ise` (IN `id_alum` INT)   begin

 declare
  v_creditos_alum int;
 declare
  v_grupo int;
 declare
  v_creditos_t int;


select
sum(n_creditos)
into v_creditos_alum
from
materia
where
id in(
select
 e.id_materia
-- (select avg(calificacion) from evaluacion where id_materia = e.id_materia) CAL,
-- m.n_creditos
from
alumno a,
evaluacion e,
materia m
-- semestre s
WHERE
a.id = id_alum
AND a.id = e.id_alumno
AND e.calificacion > 70
AND e.id_materia = m.id
GROUP BY e.id_materia, m.n_creditos);


select
g.id
into v_grupo
from
alumno a,
grupo g,
semestre s
where
a.id = id_alum
and a.id_grupo = g.id
and g.semestre = s.id;


select
100/sum(m.n_creditos) * v_creditos_alum
into v_creditos_t
from
grupo g,
materia m,
semestre s
where
m.id_grupo = v_grupo
and s.id = g.semestre
and g.id = m.id_grupo;



if(v_creditos_t >= 0 and v_creditos_t < 85) then

   UPDATE alumno_indice SET ise = 'REZAGO' where id_alumno = id_alum;

elseif (v_creditos_t >= 85 and v_creditos_t < 100) then

   UPDATE alumnos_indice SET ise = 'IRREGULAR' where id_alumno = id_alum;

elseif (v_creditos_t >= 100) then

   UPDATE alumno_indice SET ise = 'ÓPTIMO' where id_alumno = id_alum;
end if;

end$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_calificacion_alum` (IN `id_alum` INT)   begin

 select avg(calificacion) calificacion
 from evaluacion where id_alumno = id_alum;

end$$

DELIMITER ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `alumno`
--

CREATE TABLE `alumno` (
  `id` int(10) NOT NULL,
  `nombres` varchar(50) NOT NULL,
  `apellido_p` varchar(50) NOT NULL,
  `apellido_m` varchar(50) NOT NULL,
  `genero` char(1) NOT NULL,
  `status` varchar(20) DEFAULT NULL,
  `id_grupo` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `alumno`
--

INSERT INTO `alumno` (`id`, `nombres`, `apellido_p`, `apellido_m`, `genero`, `status`, `id_grupo`) VALUES
(987654321, 'JAck', 'Man', 'Son', 'F', 'Activo', 3102),
(1245155216, 'DAga', 'GA', 'LA', 'M', 'Activo', 3102),
(1593264782, 'Malcom', 'Asmo', 'MEdio', 'M', 'Activo', 3801),
(2017123089, 'Alonsoa', 'Guadarrama', 'Ruiza', 'M', 'Activo', 3101),
(2017123092, 'Diana', 'Avila', 'Jimenez', 'F', 'Activo', 3801),
(2019123009, 'Alejandro', 'Ocampo', 'Madero', 'M', 'Activo', 3801),
(2023123083, 'Carlop', 'Corinto', 'Perf', 'M', 'Activo', 3102);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `alumno_indice`
--

CREATE TABLE `alumno_indice` (
  `id_alumno_indice` int(11) NOT NULL,
  `id_alumno` int(10) DEFAULT NULL,
  `iao` varchar(35) DEFAULT NULL,
  `iac` varchar(35) DEFAULT NULL,
  `ipe` varchar(35) DEFAULT NULL,
  `ide` varchar(35) DEFAULT NULL,
  `ise` varchar(35) DEFAULT NULL,
  `ire` varchar(35) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `alumno_indice`
--

INSERT INTO `alumno_indice` (`id_alumno_indice`, `id_alumno`, `iao`, `iac`, `ipe`, `ide`, `ise`, `ire`) VALUES
(3, 987654321, 'BAJO', 'ALTO', 'REGULAR', 'REGULAR', 'REZAGO', 'RIESGO ALTO'),
(4, 2023123083, 'ALTO', 'ALTO', 'ALTO', 'ALTO', 'REZAGO', 'RIESGO ALTO');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `docente`
--

CREATE TABLE `docente` (
  `id` int(10) NOT NULL,
  `nombres` varchar(50) NOT NULL,
  `apellido_p` varchar(50) DEFAULT NULL,
  `apellido_m` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `docente`
--

INSERT INTO `docente` (`id`, `nombres`, `apellido_p`, `apellido_m`) VALUES
(1284373821, 'Chespiritoooo', 'Cegobianohj', 'Ruizah'),
(1284390284, 'Enrique', 'Peñapp', 'Nieto'),
(1392749212, 'Joaquin', 'Guzman', 'Loera'),
(1394628402, 'Enrrique', 'Salinas', 'DeGortari'),
(1473826428, 'Vicente', 'Fox', 'Chapucero'),
(1492848201, 'Felipe', 'Calderon', 'Inojozo'),
(2017123081, 'Daniel', 'Ramirez', 'Avilas');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `evaluacion`
--

CREATE TABLE `evaluacion` (
  `id` int(11) NOT NULL,
  `parcial` int(11) NOT NULL,
  `fecha` date NOT NULL,
  `calificacion` int(100) DEFAULT NULL,
  `id_tipo_evaluacion` int(11) NOT NULL,
  `id_materia` int(11) NOT NULL,
  `id_alumno` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `evaluacion`
--

INSERT INTO `evaluacion` (`id`, `parcial`, `fecha`, `calificacion`, `id_tipo_evaluacion`, `id_materia`, `id_alumno`) VALUES
(29, 2, '2022-02-17', 100, 1, 50, 2017123089),
(93, 1, '2023-03-22', 95, 1, 56, 987654321),
(96, 2, '2023-03-22', 89, 2, 56, 987654321),
(112, 1, '2023-03-29', 80, 1, 50, 1593264782),
(114, 2, '2023-03-29', 75, 1, 50, 1593264782),
(115, 1, '2023-03-29', 100, 1, 50, 2019123009),
(118, 1, '2023-04-10', 95, 2, 55, 987654321),
(119, 2, '2023-04-10', 89, 2, 55, 987654321),
(120, 1, '2023-04-10', 70, 1, 55, 1245155216),
(121, 1, '2023-04-10', 89, 2, 54, 987654321),
(122, 1, '2023-04-10', 70, 1, 53, 987654321),
(123, 1, '2023-06-04', 60, 1, 50, 2017123092),
(124, 2, '2023-06-04', 95, 1, 50, 2017123092),
(125, 2, '2023-06-04', 99, 1, 50, 2019123009),
(126, 1, '2023-06-04', 85, 1, 52, 987654321),
(127, 2, '2023-06-09', 95, 1, 52, 987654321),
(128, 1, '2023-11-29', 80, 1, 52, 2023123083),
(129, 2, '2023-11-29', 100, 1, 52, 2023123083);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `grupo`
--

CREATE TABLE `grupo` (
  `id` int(11) NOT NULL,
  `num_g` int(25) NOT NULL,
  `semestre` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `grupo`
--

INSERT INTO `grupo` (`id`, `num_g`, `semestre`) VALUES
(3101, 1, 1),
(3102, 2, 1),
(3111, 3, 1),
(3201, 4, 2),
(3202, 5, 2),
(3211, 6, 2),
(3301, 7, 3),
(3302, 8, 3),
(3311, 9, 3),
(3401, 10, 4),
(3402, 11, 4),
(3411, 12, 4),
(3501, 13, 5),
(3502, 14, 5),
(3511, 15, 5),
(3601, 16, 6),
(3602, 17, 6),
(3611, 18, 6),
(3701, 19, 7),
(3702, 20, 7),
(3711, 21, 7),
(3801, 22, 8),
(3802, 23, 8),
(3811, 24, 8);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `iac`
--

CREATE TABLE `iac` (
  `id_IAC` int(11) NOT NULL,
  `nivel_IAC` varchar(35) NOT NULL,
  `categoria_IAC` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `iac`
--

INSERT INTO `iac` (`id_IAC`, `nivel_IAC`, `categoria_IAC`) VALUES
(1, '>=0,<85', 'BAJO'),
(2, '>=85,<100', 'REGULAR'),
(3, '>=100', 'ALTO');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `iao`
--

CREATE TABLE `iao` (
  `id_IAO` int(10) NOT NULL,
  `nivel_IAO` varchar(35) NOT NULL,
  `categoria_IAO` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `iao`
--

INSERT INTO `iao` (`id_IAO`, `nivel_IAO`, `categoria_IAO`) VALUES
(1, '>=0,<=80', 'BAJO'),
(2, '>=80,<90', 'REGULAR'),
(3, '>=100', 'ALTO');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ide`
--

CREATE TABLE `ide` (
  `id` int(11) NOT NULL,
  `id_IDE` int(3) NOT NULL,
  `categoria_IDE` varchar(25) NOT NULL,
  `categoria_IAO` int(11) NOT NULL,
  `categoria_IAC` int(11) NOT NULL,
  `categoria_IPE` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `ide`
--

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

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ipe`
--

CREATE TABLE `ipe` (
  `id_IPE` int(11) NOT NULL,
  `nivel_IPE` varchar(35) NOT NULL,
  `categoria_IPE` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `ipe`
--

INSERT INTO `ipe` (`id_IPE`, `nivel_IPE`, `categoria_IPE`) VALUES
(1, '>=0,<80', 'BAJO'),
(2, '>=80,<90', 'REGULAR'),
(3, '>=90,<=100', 'ALTO');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ire`
--

CREATE TABLE `ire` (
  `id` int(11) NOT NULL,
  `id_IRE` int(3) NOT NULL,
  `categoria_IRE` varchar(25) NOT NULL,
  `categoria_IDE` int(11) NOT NULL,
  `categoria_ISE` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `ire`
--

INSERT INTO `ire` (`id`, `id_IRE`, `categoria_IRE`, `categoria_IDE`, `categoria_ISE`) VALUES
(1, 1, 'RIESGO ALTO', 1, 1),
(2, 1, 'RIESGO ALTO', 12, 1),
(3, 1, 'RIESGO ALTO', 1, 2),
(4, 2, 'RIESGO MODERADO', 24, 1),
(5, 2, 'RIESGO MODERADO', 12, 2),
(6, 2, 'RIESGO MODERADO', 24, 2),
(7, 2, 'RIESGO MODERADO', 1, 3),
(8, 3, 'SIN RIESGO', 12, 3),
(9, 3, 'SIN RIESGO', 24, 3);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ise`
--

CREATE TABLE `ise` (
  `id_ISE` int(11) NOT NULL,
  `nivel_ISE` varchar(35) NOT NULL,
  `categoria_ISE` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `ise`
--

INSERT INTO `ise` (`id_ISE`, `nivel_ISE`, `categoria_ISE`) VALUES
(1, '>=0,<85', 'REZAGO'),
(2, '>=85,<100', 'IRREGULAR'),
(3, '>=100', 'ÓPTIMO');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `materia`
--

CREATE TABLE `materia` (
  `id` int(11) NOT NULL,
  `clave` varchar(50) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `n_creditos` int(11) NOT NULL,
  `id_grupo` int(11) NOT NULL,
  `id_docente` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `materia`
--

INSERT INTO `materia` (`id`, `clave`, `nombre`, `n_creditos`, `id_grupo`, `id_docente`) VALUES
(1, '', 'CALCULO DIFERENCIAL', 5, 3101, 1284373821),
(2, '', 'MATEMATICAS DISCRETAS', 5, 3101, 1284390284),
(3, '', 'TALLER DE ETICA', 4, 3101, 1492848201),
(4, '', 'MATEMATICAS DISCRETAS', 5, 3101, 1284390284),
(5, '', 'TALLER DE ADMINISTRACION', 4, 3101, 1392749212),
(6, '', 'FUNDAMENTOS DE INVESTIGACION', 4, 3101, 1394628402),
(7, '', 'CALCULO INTEGRAL', 5, 3201, 1394628402),
(8, '', 'PROGRAMACION ORIENTADA A OBJETOS', 5, 3201, 1492848201),
(9, '', 'CONTABILIDAD FINANCIERA', 4, 3201, 1473826428),
(10, '', 'QUIMICA', 4, 3201, 1284390284),
(11, '', 'ALGEBRA LINEAL', 5, 3201, 1392749212),
(12, '', 'PROBABILIDAD Y ESTADISTICA', 5, 3201, 1284373821),
(13, '', 'CALCULO VECTORIAL', 5, 3301, 1284373821),
(14, '', 'ESTRUCTURA DE DATOS', 5, 3301, 1284390284),
(15, '', 'CULTURA EMPRESARIAL', 4, 3301, 1284390284),
(16, '', 'INVESTIGACIÓN DE OPERACIONES', 4, 3301, 1394628402),
(17, '', 'SISTEMAS OPERATIVOS', 4, 3301, 1394628402),
(18, '', 'FÍSICA GENERAL', 5, 3301, 1392749212),
(19, '', 'ECUACIONES DIFERENCIALES', 5, 3401, 1473826428),
(20, '', 'MÉTODOS NUMÉRICOS', 4, 3401, 1492848201),
(21, '', 'TÓPICOS AVANZADOS DE PROGRAMACIÓN', 5, 3401, 1394628402),
(22, '', 'FUNDAMENTOS DE BASE DE DATOS', 5, 3401, 1392749212),
(23, '', 'TALLER DE SISTEMAS OPERATIVOS', 4, 3401, 1473826428),
(24, '', 'PRINCIPIOS ELÉCTRICOS Y APLICACIONES DIGITALES', 5, 3401, 1492848201),
(25, '', 'DESARROLLO SUSTENTABLE', 5, 3501, 1394628402),
(26, '', 'FUNDAMENTOS DE TELECOMUNICACIONES', 4, 3501, 1473826428),
(27, '', 'TALLER DE BASE DE DATOS', 4, 3501, 1394628402),
(28, '', 'SIMULACION', 5, 3501, 1492848201),
(29, '', 'FUNDAMENTOS DE INGENIERIA DE SOFTWARE', 4, 3501, 1394628402),
(30, '', 'ARQUITECTURA DE COMPUTADORAS', 5, 3501, 1473826428),
(31, '', 'INGENIERÍA DE REQUERIMIENTOS', 4, 3501, 1394628402),
(32, '', 'LENGUAJES Y AUTÓMATAS l', 5, 3601, 1473826428),
(33, '', 'REDES DE COMPUTADORAS', 5, 3601, 1394628402),
(34, '', 'ADMINISTRACIÓN DE BASES DE DATOS', 5, 3601, 1392749212),
(35, '', 'GRAFICACIÓN', 4, 3601, 1284390284),
(36, '', 'INGENIERÍA DE SOFTWARE', 5, 3601, 1392749212),
(37, '', 'LENGUAJES DE INTERFAZ', 4, 3601, 1284373821),
(38, '', 'ARQUITECTURA Y DISEÑO DE SOFTWARE', 4, 3601, 1392749212),
(39, '', 'LENGUAJES Y AUTÓMATAS ll', 5, 3701, 1284390284),
(40, '', 'CONMUTACIÓN Y ENRUTAMIENTO DE REDES', 5, 3701, 1392749212),
(41, '', 'TALLER DE INVESTIGACIÓN l', 4, 3701, 1284390284),
(42, '', 'GESTIÓN DE PROYECTOS DE SOFTWARE', 5, 3701, 1284373821),
(43, '', 'SISTEMAS PROGRAMABLES', 5, 3701, 1392749212),
(44, '', 'PROCESO PERSONAL PARA EL DESARROLLO', 4, 3701, 1284390284),
(45, '', 'MODELO DE DESARROLLO INTEGRAL CMMI', 4, 3701, 1284373821),
(46, '', 'PROGRAMACIÓN LÓGICA Y FUNCIONAL', 4, 3801, 1284373821),
(47, '', 'TALLER DE INVESTIGACIÓN ll', 4, 3801, 1284390284),
(48, '', 'PROGRAMACIÓN WEB', 5, 3801, 1284373821),
(49, '', 'INTELIGENCIA ARTIFICIAL', 4, 3801, 1284390284),
(50, '', 'VERIFICACIÓN Y VALIDACION', 5, 3801, 2017123081),
(51, '', 'PROGRAMACIÓN EN MOVILES', 5, 3801, 1392749212),
(52, '42', 'CALCULO DIFERENCIAL', 5, 3102, 2017123081),
(53, '43', 'FUNDAMENTOS DE PROGRAMACION', 5, 3102, 2017123081),
(54, '44', 'TALLER DE ETICA', 4, 3102, 2017123081),
(55, '45', 'MATEMATICAS DISCRETAS', 5, 3102, 2017123081),
(56, '', 'FUNDAMENTOS DE INVESTIGACION', 4, 3102, 2017123081),
(58, '50', 'CALCULO INTEGRAL', 5, 3202, 2017123081);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `periodos`
--

CREATE TABLE `periodos` (
  `id_periodos` int(11) NOT NULL,
  `periodo` varchar(35) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `periodos`
--

INSERT INTO `periodos` (`id_periodos`, `periodo`) VALUES
(1, 'SEP2021-MAR2022'),
(2, 'MAR2022-SEP2023'),
(3, 'SEP2023-MAR2024'),
(4, 'MAR2024-SEP2024');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `semestre`
--

CREATE TABLE `semestre` (
  `id` int(11) NOT NULL,
  `nombre` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `semestre`
--

INSERT INTO `semestre` (`id`, `nombre`) VALUES
(1, 'primer semestre'),
(2, 'segundo semestre'),
(3, 'tercero semestre'),
(4, 'cuarto semestre'),
(5, 'quinto semestre'),
(6, 'sexto semestre'),
(7, 'septimo semestre'),
(8, 'octavo semestre');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tipo_evaluacion`
--

CREATE TABLE `tipo_evaluacion` (
  `id` int(11) NOT NULL,
  `nombre` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `tipo_evaluacion`
--

INSERT INTO `tipo_evaluacion` (`id`, `nombre`) VALUES
(1, 'Curso normal'),
(2, 'Segunda oportunidad'),
(3, 'Recurse'),
(4, 'Especial');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tipo_usuario`
--

CREATE TABLE `tipo_usuario` (
  `id` tinyint(1) UNSIGNED NOT NULL,
  `usuario` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `tipo_usuario`
--

INSERT INTO `tipo_usuario` (`id`, `usuario`) VALUES
(1, 'Administrador'),
(2, 'docente');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuario`
--

CREATE TABLE `usuario` (
  `id` int(10) UNSIGNED NOT NULL,
  `usuario` varchar(20) NOT NULL,
  `nombres` varchar(20) NOT NULL,
  `apellido_p` varchar(20) NOT NULL,
  `apellido_m` varchar(20) NOT NULL,
  `password` char(120) NOT NULL,
  `tipo_usuario` tinyint(1) UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `usuario`
--

INSERT INTO `usuario` (`id`, `usuario`, `nombres`, `apellido_p`, `apellido_m`, `password`, `tipo_usuario`) VALUES
(22, '2017123062', 'Alberto', 'Estrada', 'Garcia', 'pbkdf2:sha256:260000$qVvqPAm1NwwP7Len$c5ad32952ce9b239f22a9e93f5a4ee5b39989e2bcc9b2888c21d0885939a9e29', 2),
(23, '2017123082', 'Daniel', 'Ramirez', 'Avila', 'pbkdf2:sha256:260000$R0xgR6pbQC4IHj6P$31b2858c5ada39e477ec7e26d2f6721c6159ccfabf27e278a7bc8129486863a2', 1),
(24, '2017123081', 'Dan', 'Ram', 'Avi', 'pbkdf2:sha256:260000$kTTQOmKOlLFGBId8$d283e7ee640c68ee8979e86bc3e7c6b7277142d42e718251aedd90fed1a8d52d', 2);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `alumno`
--
ALTER TABLE `alumno`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_grupo` (`id_grupo`);

--
-- Indices de la tabla `alumno_indice`
--
ALTER TABLE `alumno_indice`
  ADD PRIMARY KEY (`id_alumno_indice`);

--
-- Indices de la tabla `docente`
--
ALTER TABLE `docente`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `evaluacion`
--
ALTER TABLE `evaluacion`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_tipo_evaluacion` (`id_tipo_evaluacion`),
  ADD KEY `id_alumno` (`id_alumno`),
  ADD KEY `id_materia` (`id_materia`);

--
-- Indices de la tabla `grupo`
--
ALTER TABLE `grupo`
  ADD PRIMARY KEY (`id`),
  ADD KEY `semestre` (`semestre`);

--
-- Indices de la tabla `iac`
--
ALTER TABLE `iac`
  ADD PRIMARY KEY (`id_IAC`);

--
-- Indices de la tabla `iao`
--
ALTER TABLE `iao`
  ADD PRIMARY KEY (`id_IAO`);

--
-- Indices de la tabla `ide`
--
ALTER TABLE `ide`
  ADD PRIMARY KEY (`id`),
  ADD KEY `categoria_IAO` (`categoria_IAO`),
  ADD KEY `categoria_IAC` (`categoria_IAC`),
  ADD KEY `categoria_IPE` (`categoria_IPE`);

--
-- Indices de la tabla `ipe`
--
ALTER TABLE `ipe`
  ADD PRIMARY KEY (`id_IPE`);

--
-- Indices de la tabla `ire`
--
ALTER TABLE `ire`
  ADD PRIMARY KEY (`id`),
  ADD KEY `categoria_IDE` (`categoria_IDE`),
  ADD KEY `categoria_ISE` (`categoria_ISE`);

--
-- Indices de la tabla `ise`
--
ALTER TABLE `ise`
  ADD PRIMARY KEY (`id_ISE`);

--
-- Indices de la tabla `materia`
--
ALTER TABLE `materia`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_grupo` (`id_grupo`),
  ADD KEY `id_docente` (`id_docente`);

--
-- Indices de la tabla `periodos`
--
ALTER TABLE `periodos`
  ADD PRIMARY KEY (`id_periodos`);

--
-- Indices de la tabla `semestre`
--
ALTER TABLE `semestre`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `tipo_evaluacion`
--
ALTER TABLE `tipo_evaluacion`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `tipo_usuario`
--
ALTER TABLE `tipo_usuario`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `usuario`
--
ALTER TABLE `usuario`
  ADD PRIMARY KEY (`id`),
  ADD KEY `tipo_usuario` (`tipo_usuario`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `alumno_indice`
--
ALTER TABLE `alumno_indice`
  MODIFY `id_alumno_indice` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `evaluacion`
--
ALTER TABLE `evaluacion`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=130;

--
-- AUTO_INCREMENT de la tabla `materia`
--
ALTER TABLE `materia`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=59;

--
-- AUTO_INCREMENT de la tabla `semestre`
--
ALTER TABLE `semestre`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT de la tabla `tipo_evaluacion`
--
ALTER TABLE `tipo_evaluacion`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `tipo_usuario`
--
ALTER TABLE `tipo_usuario`
  MODIFY `id` tinyint(1) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `usuario`
--
ALTER TABLE `usuario`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=31;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `alumno`
--
ALTER TABLE `alumno`
  ADD CONSTRAINT `alumno_ibfk_1` FOREIGN KEY (`id_grupo`) REFERENCES `grupo` (`id`);

--
-- Filtros para la tabla `evaluacion`
--
ALTER TABLE `evaluacion`
  ADD CONSTRAINT `evaluacion_ibfk_1` FOREIGN KEY (`id_tipo_evaluacion`) REFERENCES `tipo_evaluacion` (`id`),
  ADD CONSTRAINT `evaluacion_ibfk_2` FOREIGN KEY (`id_alumno`) REFERENCES `alumno` (`id`),
  ADD CONSTRAINT `evaluacion_ibfk_3` FOREIGN KEY (`id_materia`) REFERENCES `materia` (`id`);

--
-- Filtros para la tabla `grupo`
--
ALTER TABLE `grupo`
  ADD CONSTRAINT `grupo_ibfk_1` FOREIGN KEY (`semestre`) REFERENCES `semestre` (`id`);

--
-- Filtros para la tabla `ide`
--
ALTER TABLE `ide`
  ADD CONSTRAINT `ide_ibfk_1` FOREIGN KEY (`categoria_IAO`) REFERENCES `iao` (`id_IAO`),
  ADD CONSTRAINT `ide_ibfk_2` FOREIGN KEY (`categoria_IAC`) REFERENCES `iac` (`id_IAC`),
  ADD CONSTRAINT `ide_ibfk_3` FOREIGN KEY (`categoria_IPE`) REFERENCES `ipe` (`id_IPE`);

--
-- Filtros para la tabla `materia`
--
ALTER TABLE `materia`
  ADD CONSTRAINT `materia_ibfk_1` FOREIGN KEY (`id_grupo`) REFERENCES `grupo` (`id`),
  ADD CONSTRAINT `materia_ibfk_2` FOREIGN KEY (`id_docente`) REFERENCES `docente` (`id`);

--
-- Filtros para la tabla `usuario`
--
ALTER TABLE `usuario`
  ADD CONSTRAINT `usuario_ibfk_1` FOREIGN KEY (`tipo_usuario`) REFERENCES `tipo_usuario` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
