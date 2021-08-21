from .entities.Docentes import Docentes


class Modelo_docente():
    @classmethod
    def agregar_docente(self, db, id, nombres, apellido_p, apellido_m):
        try:
            cursor = db.connection.cursor()
            query = """INSERT INTO docente(id, nombres, apellido_p, apellido_m)
            VALUES({0},'{1}','{2}','{3}')""".format(id, nombres, apellido_p, apellido_m)
            cursor.execute(query)
            db.connection.commit()
        except Exception as e:
            raise Exception(e)

    @classmethod
    def obtener_docentes(self, db):
        try:
            cursor = db.connection.cursor()
            query = """SELECT id, nombres, apellido_p, apellido_m FROM docente"""
            cursor.execute(query)
            data = cursor.fetchall()
            docentes = []
            for d in data:
                docente = Docentes(d[0], d[1], d[2], d[3])
                docentes.append(docente)
            return docentes
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def editar_docente(self, db, id, nombres, apellido_p, apellido_m):
        try:
            cursor = db.connection.cursor()
            query = """ UPDATE docente SET id = '{0}', nombres = '{1}', apellido_p = '{2}', apellido_m = '{3}'
            WHERE id = '{4}'""".format(id, nombres, apellido_p, apellido_m, id)
            cursor.execute(query)
            db.connection.commit()
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def eliminar_docente(self, db, id):
        try:
            cursor = db.connection.cursor()
            query = "DELETE FROM docente WHERE id = '{0}'".format(id)
            cursor.execute(query)
            db.connection.commit()
        except Exception as ex:
            raise Exception(ex)
