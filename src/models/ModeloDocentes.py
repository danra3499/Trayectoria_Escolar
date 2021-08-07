from .entities.Docentes import Docentes


class Modelo_docente():
    @classmethod
    def add(self, db, id, Profesión, Nombre, Telefono, Email, Materias_impartidas, Horas):
        try:
            cursor = db.connection.cursor()
            query = """INSERT INTO docentes(id, Profesión, Nombre, Telefono, Email, Materias_impartidas, Horas,)
            VALUES({0},'{1}','{2}','{3}','{4}','{5}','{6}','{7}')""".format(id, Profesión, Nombre, Telefono, Email, Materias_impartidas, Horas)
            cursor.execute(query)
            db.connection.commit()
        except Exception as e:
            raise Exception(e)