class Modelo_evaluacion():

    @classmethod
    def evaluar(db, parcial, fecha, id_materia, id_alumno, nota):
        try:
            cursor = db.connection.cursor()
            query = """INSERT INTO evaluacion(parcial, fecha, id_materia, id_alumno, nota)
                        VALUES({0},{1},{2},{3},{4})""".format(parcial, fecha, id_materia, id_alumno, nota)
            cursor.execute(query)
            db.connection.commit()
        except Exception as e:
            raise Exception(e)
