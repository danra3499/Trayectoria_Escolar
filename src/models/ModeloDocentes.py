from .entities.Docentes import Docentes


class Modelo_docente():
    @classmethod
    def add(self, db, id, nombres, apellido_p, apellido_m):
        try:
            cursor = db.connection.cursor()
            query = """INSERT INTO docente(id, nombres, apellido_p, apellido_m)
            VALUES({0},'{1}','{2}','{3}')""".format(id, nombres, apellido_p, apellido_m)
            cursor.execute(query)
            db.connection.commit()
        except Exception as e:
            raise Exception(e)