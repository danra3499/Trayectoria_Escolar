from .entities.Alumno import Alumno


class Modelo_alumno():
    @classmethod
    def add(self, db, id, nombres, apellido_p, apellido_m, genero, status, grupo):
        try:
            cursor = db.connection.cursor()
            query = """INSERT INTO alumno(id, nombres, apellido_p, apellido_m, genero, status, id_grupo)
            VALUES({0},'{1}','{2}','{3}','{4}','{5}','{6}')""".format(id, nombres, apellido_p, apellido_m, genero, status, grupo)
            cursor.execute(query)
            db.connection.commit()
        except Exception as e:
            raise Exception(e)

    @classmethod
    def obtener_alumnos(self, db):
        try:
            cursor = db.connection.cursor()
            query = """SELECT * FROM alumno"""
            cursor.execute(query)
            data = cursor.fetchall()
            alumnos = []
            for alumno in data:
                alum = Alumno(alumno[0], alumno[1], alumno[2],
                              alumno[3], alumno[4], alumno[5], alumno[6])
                alumnos.append(alum)
            return alumnos
        except Exception as e:
            raise Exception(e)

    @classmethod
    def obtener_alumno_id(self, db, id):
        try:
            cursor = db.connection.cursor()
            query = "SELECT id, nombre, apellido_p, apellido_m FROM alumno WHERE id = {0}".format(
                id)
            cursor.execute(query)
        except Exception as e:
            raise Exception(e)

 
