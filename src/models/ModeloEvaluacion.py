from datetime import date
from src.models.entities.Evaluacion import Evaluacion


class Modelo_evaluacion():

    @classmethod
    def evaluar(self, db, parcial, fecha, calificacion, tipo_evaluacion, id_materia, id_alumno):
        try:
            cursor = db.connection.cursor()
            query = """INSERT INTO evaluacion(parcial, fecha, calificacion, id_tipo_evaluacion, id_materia, id_alumno) 
                       VALUES ('{0}','{1}','{2}','{3}','{4}','{5}')""".format(
                parcial, fecha, calificacion, tipo_evaluacion, id_materia, id_alumno)
            cursor.execute(query)
            db.connection.commit()
        except Exception as e:
            raise Exception(e)

    #@classmethod
    #def evaluar_materia(self, db, id_evaluar):
     #   try:
      #      cursor = db.connection.cursor()
       #     query = """SELECT nombre, id_grupo , CONCAT(nombre)as nombre_materia from Materia
        #      INNER JOIN evaluar
         #     ON materia.id = materia.id_materia
          #    WHERE id_evaluar = '{0}'""".format(
           #     id_evaluar)
            #cursor.execute(query)
            #data = cursor.fetchall()
            #evaluar = []
            #for m in data:
             #   materia = Materia(None, m[0], None, m[1], m[2])
              #  materias.append(materia)
            #return materias
        #except Exception as ex:
         #   raise Exception(ex)