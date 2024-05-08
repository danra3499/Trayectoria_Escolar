from .entities.Indices import Indices
from .entities.Indices import IndicesIAC
from .entities.Indices import IndicesIPE
from .entities.Indices import IndicesIDE
from .entities.Indices import IndicesISE
from .entities.Indices import IndicesIRE
from .entities.Indices import IndicesAlum

"""---------------------- AGREGAR ALUMNOS A INDICES ----------------------------"""
class Modelo_agregar_alumno():
    @classmethod
    def add_Alum_Ind(self, db, id_alumno):
        try:
            cursor = db.connection.cursor()
            query = """INSERT INTO alumno_indice(id_alumno)
            VALUES({0})""".format(id_alumno)
            cursor.execute(query)
            db.connection.commit()
        except Exception as e:
            raise Exception(e)

"""---------------------------- ACTUALIZAR INDICES ---------------------------------"""

class Modelo_actualizar_indices():
    

    @classmethod
    def actual_IAO(self, db, id_alumno):
        try:
            cursor = db.connection.cursor()

            query = "call sp_actualizar_iao('{0}')".format(id_alumno)
            cursor.execute(query)
            db.connection.commit()
        except  Exception as ex:
            raise Exception(ex)

    @classmethod
    def actual_IAC(self, db, id_alumno):
        try:
            cursor = db.connection.cursor()

            query = "call sp_actualizar_iac('{0}')".format(id_alumno)
            cursor.execute(query)
            db.connection.commit()
        except  Exception as ex:
            raise Exception(ex)

    @classmethod
    def actual_IPE(self, db, id_alumno):
        try:
            cursor = db.connection.cursor()
            query = "call sp_actualizar_ipe('{0}')".format(id_alumno)
            cursor.execute(query)
            db.connection.commit()
        except  Exception as ex:
            raise Exception(ex)

    @classmethod
    def actual_IDE(self, db, id_alumno):
        try:
            cursor = db.connection.cursor()

            query = "call sp_actualizar_ide('{0}')".format(id_alumno)
            cursor.execute(query)
            db.connection.commit()
        except  Exception as ex:
            raise Exception(ex)

    @classmethod
    def actual_ISE(self, db, id_alumno):
        try:
            cursor = db.connection.cursor()

            query = "call sp_actualizar_ise('{0}')".format(id_alumno)
            cursor.execute(query)
            db.connection.commit()
        except  Exception as ex:
            raise Exception(ex)

    @classmethod
    def actual_IRE(self, db, id_alumno):
        try:
            cursor = db.connection.cursor()

            query = "call sp_actualizar_ire('{0}')".format(id_alumno)
            cursor.execute(query)
            db.connection.commit()
        except  Exception as ex:
            raise Exception(ex)


"""------------------------------- ALUMNOS INDICES ---------------------------------"""

class Modelo_indice_alumno():
    @classmethod
    def obtener_indice_alumnos(self, db, id_grupo):
        try:
            cursor = db.connection.cursor()
            query = """SELECT 
                        ai.*,
                        concat(a.nombres,' ', a.apellido_p,' ',a.apellido_m) nombre
                       FROM 
                        alumno_indice ai,
                        grupo g,
                        alumno a
                       WHERE g.id = '{0}'
                       AND g.id = a.id_grupo
                       AND a.id = ai.id_alumno""".format(id_grupo)
            cursor.execute(query)
            data = cursor.fetchall()
            indicesAlum = []
            for indalumn in data:
                indicAlum = IndicesAlum(indalumn[0], indalumn[1], indalumn[2],indalumn[3],indalumn[4],indalumn[5],indalumn[6],indalumn[7],indalumn[8])
                indicesAlum.append(indicAlum)
            return indicesAlum
        except Exception as ex:
            raise Exception(ex)


"""-----------------IAO------------------------------"""
class Modelo_indice():
    @classmethod
    def obtener_indice(self, db):
        try:
            cursor = db.connection.cursor()
            query = """SELECT id_IAO, nivel_IAO, categoria_IAO FROM iao"""
            cursor.execute(query)
            data = cursor.fetchall()
            indices = []
            for i in data:
                indice = Indices(i[0], i[1], i[2])
                indices.append(indice)
            return indices
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def editar_IAO(self, db, id_IAO, nivel_IAO, categoria_IAO):
        try:
            cursor = db.connection.cursor()
            query = """UPDATE iao SET id_IAO = '{0}', nivel_IAO = '{1}', categoria_IAO = '{2}'
                       WHERE id_IAO = '{3}'""".format(id_IAO, nivel_IAO, categoria_IAO, id_IAO)
            cursor.execute(query)
            db.connection.commit()
        except Exception as ex:
            raise Exception(ex)
 
"""----------------IAC--------------------------------"""
class Modelo_indiceIAC():
    @classmethod
    def obtener_indiceIAC(self, db):
        try:
            cursor = db.connection.cursor()
            query = """SELECT id_IAC, nivel_IAC, categoria_IAC FROM iac"""
            cursor.execute(query)
            data = cursor.fetchall()
            indicesIAC = []
            for p in data:
                indiceIAC = IndicesIAC(p[0], p[1], p[2])
                indicesIAC.append(indiceIAC)
            return indicesIAC
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def editar_IAC(self, db, id_IAC, nivel_IAC, categoria_IAC):
        try:
            cursor = db.connection.cursor()
            query = """UPDATE iac SET id_IAC = '{0}', nivel_IAC = '{1}', categoria_IAC = '{2}'
                       WHERE id_IAC = '{3}'""".format(id_IAC, nivel_IAC, categoria_IAC, id_IAC)
            cursor.execute(query)
            db.connection.commit()
        except Exception as ex:
            raise Exception(ex)
            
"""-----------------------IPE----------------------------------------------"""

class Modelo_indiceIPE():
    @classmethod
    def obtener_indiceIPE(self, db):
        try:
            cursor = db.connection.cursor()
            query = """SELECT id_IPE, nivel_IPE, categoria_IPE FROM ipe"""
            cursor.execute(query)
            data = cursor.fetchall()
            indicesIPE = []
            for ipe in data:
                indiceIPE = IndicesIPE(ipe[0], ipe[1], ipe[2])
                indicesIPE.append(indiceIPE)
            return indicesIPE
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def editar_IPE(self, db, id_IPE, nivel_IPE, categoria_IPE):
        try:
            cursor = db.connection.cursor()
            query = """ UPDATE ipe SET id_IPE = '{0}', nivel_IPE = '{1}', categoria_IPE = '{2}'
                        WHERE id_IPE = '{3}'""".format(id_IPE, nivel_IPE, categoria_IPE, id_IPE)
            cursor.execute(query)
            db.connection.commit()
        except Exception as ex:
            raise Exception(ex)


"""-------------------------------------ISE-------------------------------------------"""


class Modelo_indiceISE():
    @classmethod
    def obtener_indiceISE(self, db):
        try:
            cursor = db.connection.cursor()
            query = """SELECT id_ISE, nivel_ISE, categoria_ISE FROM ise"""
            cursor.execute(query)
            data = cursor.fetchall()
            indicesISE = []
            for ise in data:
                indiceISE = IndicesISE(ise[0], ise[1], ise[2])
                indicesISE.append(indiceISE)
            return indicesISE
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def editar_ISE(self, db, id_ISE, nivel_ISE, categoria_ISE):
        try:
            cursor = db.connection.cursor()
            query = """UPDATE ise SET id_ISE = '{0}', nivel_ISE = '{1}', categoria_ISE = '{2}'
                       WHERE id_ISE = '{3}'""".format(id_ISE, nivel_ISE, categoria_ISE, id_ISE)
            cursor.execute(query)
            db.connection.commit()
        except Exception as ex:
            raise Exception(ex)


"""------------------------------IDE------------------------------------------"""

class Modelo_indiceIDE():
    @classmethod
    def obtener_indiceIDE(self, db):
        try:
            cursor = db.connection.cursor()
            query = """SELECT  ide.id_IDE,ide.categoria_IDE, iao.categoria_IAO , iac.categoria_IAC, ipe.categoria_IPE 
                       from (((ide 
                       INNER JOIN iao  ON ide.categoria_IAO = iao.id_IAO)
                       INNER JOIN iac  ON ide.categoria_IAC = iac.id_IAC)
                       INNER JOIN ipe  ON ide.categoria_IPE = ipe.id_IPE)  ORDER BY id asc"""
            cursor.execute(query)
            data = cursor.fetchall()
            indicesIDE = []
            for ide in data:
                indiceIDE = IndicesIDE(None, ide[0], ide[1], ide[2], ide[3], ide[4])
                indicesIDE.append(indiceIDE)
            return indicesIDE
        except Exception as ex:
            raise Exception(ex)




"""----------------------------------------------------------------------------"""

        
class Modelo_indiceIRE():
    @classmethod
    def obtener_indiceIRE(self, db):
        try:
            cursor = db.connection.cursor()
            query = """SELECT  A.id_IRE, A.categoria_IRE, B.categoria_IDE, C.categoria_ISE from ((ire A
                       INNER JOIN ide B ON A.categoria_IDE = B.id)
                       INNER JOIN ise C ON A.categoria_ISE = C.id_ISE) order by id_IRE asc"""
            cursor.execute(query)
            data = cursor.fetchall()
            indicesIRE = []
            for ire in data:
                indiceIRE = IndicesIRE(None,ire[0], ire[1], ire[2], ire[3])
                indicesIRE.append(indiceIRE)
            return indicesIRE
        except Exception as ex:
            raise Exception(ex)

