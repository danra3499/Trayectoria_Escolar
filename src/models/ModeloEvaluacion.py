from datetime import date
from src.models.entities.Evaluacion import Evaluacion


class Modelo_evaluacion():

    @classmethod
    def evaluar(self, db, parcial, fecha, calificacion, tipo_evaluacion, id_materia, id_alumno):
        try:
            cursor = db.connection.cursor()
            query = """INSERT INTO evaluacion(parcial, fecha, calificacion, id_tipo_evaluacion, id_materia, id_alumno) VALUES ('{0}','{1}','{2}','{3}','{4}','{5}')""".format(
                parcial, fecha, calificacion, tipo_evaluacion, id_materia, id_alumno)
            cursor.execute(query)
            db.connection.commit()
        except Exception as e:
            raise Exception(e)
