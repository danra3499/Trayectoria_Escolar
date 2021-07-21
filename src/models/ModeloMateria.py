class Modelo_materia():
    @classmethod
    def agregar(self, db, nombre, n_creditos, semestre):
        try:
            cursor = db.connection.cursor()
            query = """INSERT INTO materia(nombre, n_creditos, id_semestre)
            VALUES('{0}','{1}','{2}')""".format(nombre, n_creditos, semestre)
            cursor.execute(query)
            db.connection.commit()
        except Exception as e:
            raise Exception(e)
