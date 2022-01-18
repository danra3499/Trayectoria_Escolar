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
            for a in data:
                alum = Alumno(a[0], a[1], a[2],
                              a[3], a[4], a[5], a[6])
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
        except Exception as ex:
            raise Exception(ex)
    
   

    @classmethod
    def editar_alumno(self, db, id, nombres, apellido_p, apellido_m, genero, status ,id_grupo):
        try:
            cursor = db.connection.cursor()
            query = """ UPDATE alumno SET id = '{0}', nombres = '{1}', apellido_p = '{2}', apellido_m = '{3}', genero = '{4}', status = '{5}', id_grupo = '{6}'
            WHERE id = '{7}'""".format(id, nombres, apellido_p, apellido_m, genero, status, id_grupo, id)
            cursor.execute(query)
            db.connection.commit()
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def eliminar_alumno(self, db, id):
        try:
            cursor = db.connection.cursor()
            query = "DELETE FROM alumno WHERE id = '{0}'".format(id)
            cursor.execute(query)
            db.connection.commit()
        except Exception as ex:
            raise Exception(ex)