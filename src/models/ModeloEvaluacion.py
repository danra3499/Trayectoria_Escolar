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