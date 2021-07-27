from .entities.Materia import Materia


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

    @classmethod
    def obtener_materias_por_semestre(self, db, semestre):
        try:
            cursor = db.connection.cursor()
            query = """SELECT nombre, n_creditos FROM materia
            WHERE id_semestre = {0}""".format(semestre)
            cursor.execute(query)
            data = cursor.fetchall()
            materias_por_semestre = []
            for materia in data:
                materias = Materia(None, materia[0], materia[1], None)
                materias_por_semestre.append(materias)
            return materias_por_semestre
        except Exception as e:
            raise Exception(e)

    @classmethod
    def obtener_nombre_materia(self, db, semestre):
        try:
            cursor = db.connection.cursor()
            query = """SELECT nombre FROM materia
            WHERE id_semestre = {0}""".format(semestre)
            cursor.execute(query)
            data = cursor.fetchall()
            materias = []
            for materia in data:
                m = Materia(None, materia[0], None, None)
                materias.append(m)
            return materias
        except Exception as e:
            raise Exception(e)
