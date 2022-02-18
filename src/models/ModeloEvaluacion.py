from datetime import date
from src.models.entities.Evaluacion import Evaluacion


class Modelo_evaluacion():

    @classmethod
    def capturar_evaluaciones(self, db, parcial, fecha, calificacion, tipo_evaluacion, id_materia, id_alumno):
        try:
            cursor = db.connection.cursor()
            query = """INSERT INTO evaluacion(parcial, fecha, calificacion, id_tipo_evaluacion, id_materia, id_alumno) 
                       VALUES ('{0}','{1}','{2}','{3}','{4}','{5}')""".format(
                parcial, fecha, calificacion, tipo_evaluacion, id_materia, id_alumno)
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
            calificacion_vista= []
            for c in data:
                evaluacion = Evaluacion(None, None, None , c[0], None, c[1], c[2]) 
                calificacion_vista.append(evaluacion)
            return calificacion_vista
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
            promedio_alumno= []
            for calu in data:
                alumn = Evaluacion(None, None, calu[0], calu[1], None, None, calu[2]) 
                promedio_alumno.append(alumn)
            return promedio_alumno
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def obtener_calificacion_por_alumnos(self, db, id_alumno):
        try:
            cursor = db.connection.cursor()
            query = "SELECT parcial,calificacion FROM evaluacion WHERE id_alumno='{0}' order by id_alumno".format(id_alumno)
            cursor.execute(query)
            data = cursor.fetchall()
            calificacion_por_alumno= []
            for alumc in data:
                alumcal = Evaluacion(None, alumc[0], None, alumc[1], None, None, None) 
                calificacion_por_alumno.append(alumcal)
            return calificacion_por_alumno
        except Exception as ex:
            raise Exception(ex)
