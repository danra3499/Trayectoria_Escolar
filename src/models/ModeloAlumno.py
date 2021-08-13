from .entities.Alumno import Alumno


class Modelo_alumno():
    @classmethod
    def add(self, db, id, nombres, apellido_p, apellido_m, genero, status, semestre, grupo):
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
            query = """SELECT id, nombres, apellido_p, apellido_m, genero, status FROM alumno"""
            cursor.execute(query)
            data = cursor.fetchall()
            alumnos = []
            for alumno in data:
                alum = Alumno(alumno[0], alumno[1], alumno[2],
                              alumno[3], alumno[4], alumno[5], None)
                alumnos.append(alum)
            return alumnos
        except Exception as e:
            raise Exception(e)
