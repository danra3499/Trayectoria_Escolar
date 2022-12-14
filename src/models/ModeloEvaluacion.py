from datetime import date
from src.models.entities.Evaluacion import Evaluacion
from .entities.Alumno import Alumno
from .entities.Materia import Materia


class Modelo_evaluacion():

    @classmethod
    def capturar_evaluaciones(self, db, id, parcial, fecha, calificacion, tipo_evaluacion, id_materia, id_alumno):
        try:
            cursor = db.connection.cursor()
            query = """INSERT INTO evaluacion(id, parcial, fecha, calificacion, id_tipo_evaluacion, id_materia, id_alumno) 
                       VALUES ('{0}','{1}','{2}','{3}','{4}','{5}', '{6}')""".format(
                id, parcial, fecha, calificacion, tipo_evaluacion, id_materia, id_alumno)
            cursor.execute(query)
            db.connection.commit()
        except Exception as e:
            raise Exception(e)

    @classmethod
    def obtener_calificacion_grupos(self, db, id_materia):
        try:
            cursor = db.connection.cursor()
            query = """SELECT avg(calificacion),id_materia,id_alumno
                       FROM evaluacion WHERE id_materia = '{0}'""".format(id_materia)
            cursor.execute(query)
            data = cursor.fetchall()
            calificacion_grupo= []
            for c in data:
                evaluacion = Evaluacion(None, None, None , c[0], None, c[1], c[2]) 
                calificacion_grupo.append(evaluacion)
            return calificacion_grupo
        except Exception as ex:
            raise Exception(ex)


    @classmethod
    def obtener_promedio_alumnos(self, db, id_materia):
        try:
            cursor = db.connection.cursor()
            query = """SELECT concat(a.nombres,' ',a.apellido_p,' ',a.apellido_m) as nombre,
                       CAST(round(avg(calificacion),2) as dec(10,2)) cal, id_alumno 
                       FROM evaluacion e
                    INNER JOIN alumno a ON e.id_alumno = a.id
                    where id_materia='{0}' group by id_alumno""".format(id_materia)
            cursor.execute(query)
            data = cursor.fetchall()
            calificacion_alumno= []
            for calu in data:
                alumn = Evaluacion(None, None, calu[0], calu[1], None, None, calu[2]) 
                calificacion_alumno.append(alumn)
            return calificacion_alumno
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def obtener_calificacion_por_alumnos(self, db, id_materia, id_alumno):
        try:
            cursor = db.connection.cursor()
            query = "SELECT id_alumno,parcial,calificacion FROM evaluacion WHERE id_materia='{0}' and id_alumno='{1}'".format(id_materia,id_alumno)
            cursor.execute(query)
            data = cursor.fetchall()
            calificacion_por_alumno= []
            for alumc in data:
                alumcal = Evaluacion(alumc[0], alumc[1], None, alumc[2], None, None, None) 
                calificacion_por_alumno.append(alumcal)
            return calificacion_por_alumno
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def calificacion_materia_alumnos(self, db, id_materia):
        try:
            cursor = db.connection.cursor()
            query = """SELECT  concat(a.nombres,' ',a.apellido_p,' ',a.apellido_m) as nombre,
                       Sum(CASE WHEN parcial = '1' THEN calificacion ELSE 0 END) AS P1,
                       Sum(CASE WHEN parcial = '2' THEN calificacion ELSE 0 END) AS P2,
                       Sum(CASE WHEN parcial = '3' THEN calificacion ELSE 0 END) AS P3,
                       cast(round(avg(calificacion),2) as dec(10,0)),id_alumno
                       FROM evaluacion e
                       INNER JOIN alumno a ON e.id_alumno = a.id WHERE id_materia='{0}' group by id_alumno""".format(id_materia)
            cursor.execute(query)
            data = cursor.fetchall()
            califi_mat_alum = []
            for cma in data:
                cmal = Evaluacion(cma[0],cma[1],cma[2],cma[3],None,cma[4],cma[5])
                califi_mat_alum.append(cmal)
            return califi_mat_alum
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def editar_cal(self, db, id, parcial, fecha, calificacion, tipo_evaluacion, id_materia, id_alumno):
        try:
            cursor = db.connection.cursor()
            query = """ UPDATE evaluacion SET id = '{0}', fecha = '{1}', calificacion = '{2}', id_tipo_evaluacion = '{3}', id_materia = '{4}', id_alumno = '{5}'
            WHERE id = '{6}'""".format(id, parcial, fecha, calificacion, tipo_evaluacion, id_materia, id_alumno, id)
            cursor.execute(query)
            db.connection.commit()
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def eliminar_cal(self, db, id):
        try:
            cursor = db.connection.cursor()
            query = "DELETE FROM evaluacion WHERE id = '{0}'".format(id)
            cursor.execute(query)
            db.connection.commit()
        except Exception as ex:
            raise Exception(ex)


