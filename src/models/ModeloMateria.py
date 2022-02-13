from .entities.Materia import Materia
from .entities.Alumno import Alumno


class Modelo_materia():
    @classmethod
    def agregar_materia(self, db, id, clave, nombre, n_creditos, id_grupo, id_docente):
        try:
            cursor = db.connection.cursor()
            query = """INSERT INTO materia(id, clave, nombre, n_creditos, id_grupo, id_docente)
            VALUES('{0}','{1}','{2}','{3}','{4}','{5}')""".format(id, clave, nombre, n_creditos, id_grupo, id_docente)
            cursor.execute(query)
            db.connection.commit()
        except Exception as e:
            raise Exception(e)

    @classmethod
    def obtener_materias(self, db):
        try:
            cursor = db.connection.cursor()
            query = """SELECT id, clave, nombre, n_creditos, id_grupo, id_docente FROM materia"""
            cursor.execute(query)
            data = cursor.fetchall()
            vista_materias = []
            for m in data:
                materias = Materia(m[0], m[1], m[2], m[3], m[4], m[5])
                vista_materias.append(materias)
            return vista_materias
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def obtener_materias_id(self, db, id_materia):
        try:
            cursor = db.connection.cursor()
            query = """SELECT id, clave, nombre, n_creditos, id_grupo, id_docente 
                       FROM materia WHERE id ='{0}'""".format(id_materia)
            cursor.execute(query)
            data = cursor.fetchall()
            vista_materias = []
            for m in data:
                materias = Materia(m[0], m[1], m[2], m[3], m[4], m[5])
                vista_materias.append(materias)
            return vista_materias
        except Exception as ex:
            raise Exception(ex) 

    @classmethod
    def obtener_materias_por_semestre(self, db, id_semestre):
        try:
            cursor = db.connection.cursor()
            query = """SELECT materia.nombre, materia.n_creditos 
            FROM materia 
            JOIN grupo ON materia.id_grupo = grupo.id 
            JOIN semestre ON grupo.semestre = semestre.id 
            WHERE grupo.num_g = {0}""".format(
                id_semestre)
            cursor.execute(query)
            data = cursor.fetchall()
            materias_por_semestre = []
            for materia in data:
                materias = Materia(None, None, materia[0], materia[1], None, None)
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
            query = "SELECT id, nombre, id_grupo FROM materia WHERE id_docente = {0}".format(
                id_docente)
            cursor.execute(query)
            data = cursor.fetchall()
            materias = []
            for m in data:
                materia = Materia(m[0], None, m[1], None, m[2], None)
                materias.append(materia)
            return materias
        except Exception as e:
            raise Exception(e)

    @classmethod
    def alumnos_materia_id(self, db, id_materia):
        """Funcion para consultar a los alumnos que cursan una materia"""
        try:
            cursor = db.connection.cursor()
            query = """SELECT alumno.id, alumno.nombres, alumno.apellido_p, alumno.apellido_m,alumno.status, alumno.id_grupo 
                    FROM materia JOIN grupo ON materia.id_grupo = grupo.id 
                    JOIN alumno ON alumno.id_grupo = grupo.id 
                    WHERE materia.id = '{0}'""".format(
                id_materia)
            cursor.execute(query)
            data = cursor.fetchall()
            alumnos = []
            for a in data:
                alumno = Alumno(a[0], a[1], a[2], a[3], None, a[4], a[5])
                alumnos.append(alumno)
            return alumnos
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def jalar_materia_alumno(self,db,id_materia, id_alumno):
        try:
            cursor = db.connection.cursor()
            query = """SELECT alumno.id as id_alumno, materia.nombre, materia.id as id_materia, grupo.id as id_grupo
                       FROM materia 
                       JOIN grupo ON materia.id_grupo = grupo.id
                       JOIN alumno ON alumno.id_grupo = grupo.id 
                       WHERE materia.id='{0}' and alumno.id='{0}';""".format(id_materia,id_alumno)
            cursor.execute(quey)
            data = cursor.fetchall()
            materias = []
            for am in data:
                materia = Materia(am[0], None, am[1], None, am[2], None)
                materias.append(materia)
            return materias
        except Exception as ex:
            raise Exception(ex)           


    @classmethod
    def materia_grupo(self, db, id_grupo):
        try:
            cursor = db.connection.cursor()
            query = """SELECT nombre,n_creditos, id_grupo , CONCAT(nombres,' ',apellido_p,' ',apellido_m)as nombre_docente from docente
              INNER JOIN materia
              ON docente.id = materia.id_docente
              WHERE id_grupo = '{0}'""".format(
                id_grupo)
            cursor.execute(query)
            data = cursor.fetchall()
            materias = []
            for m in data:
                materia = Materia(None, None, m[0], m[1], m[2], m[3])
                materias.append(materia)
            return materias
        except Exception as ex:
            raise Exception(ex)

  
    
    @classmethod
    def editar_materia(self, db, id, clave, nombre, n_creditos, id_grupo, id_docente):
        try:
            cursor = db.connection.cursor()
            query = """ UPDATE materia SET id = '{0}', clave = '{1}', nombre = '{2}', n_creditos = '{3}', id_grupo = '{4}', id_docente = '{5}'
            WHERE id = '{6}'""".format(id, clave, nombre, n_creditos, id_grupo, id_docente, id)
            cursor.execute(query)
            db.connection.commit()
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def eliminar_materia(self, db, id):
        try:
            cursor = db.connection.cursor()
            query = "DELETE FROM materia WHERE id = '{0}'".format(id)
            cursor.execute(query)
            db.connection.commit()
        except Exception as ex:
            raise Exception(ex)