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
    def obtener_materias_por_semestre(self, db, id_semestre):
        try:
            cursor = db.connection.cursor()
            query = """SELECT materia.nombre, materia.n_creditos 
            FROM materia 
            JOIN grupo ON materia.id_grupo = grupo.id 
            JOIN semestre ON grupo.semestre = semestre.id 
            WHERE semestre.id = {0}""".format(
                id_semestre)
            cursor.execute(query)
            data = cursor.fetchall()
            materias_por_semestre = []
            for materia in data:
                materias = Materia(None, materia[0], materia[1], None, None)
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

    @classmethod
    def materia_docente(self, db, id_docente):
        try:
            cursor = db.connection.cursor()
            query = "SELECT nombre FROM materia WHERE id_docente = {0}".format(
                id_docente)
            cursor.execute(query)
            data = cursor.fetchall()
            materias = []
            for m in data:
                materia = Materia(None, m[0], None, None, None)
                materias.append(materia)
            return materias
        except Exception as e:
            raise Exception(e)
