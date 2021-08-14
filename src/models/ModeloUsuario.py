from .entities.Usuario import Usuario
from .entities.TipoUsuario import TipoUsuario


class ModeloUsuario():
    @classmethod
    def login(self, db, usuario):
        try:
            cursor = db.connection.cursor()
            query = """SELECT id, usuario, password
						FROM usuario
						WHERE usuario = '{0}'""".format(usuario.usuario)
            cursor.execute(query)
            data = cursor.fetchone()

            if data != None:
                match = Usuario.check_password(data[2], usuario.password)
                if match:
                    logged = Usuario(data[0], data[1],
                                     None, None, None, data[2], None)
                    return logged
                else:
                    return None
            else:
                return None

        except Exception as e:
            raise Exception(e)

    @classmethod
    def get_id(self, db, id):
        try:
            cursor = db.connection.cursor()
            query = """SELECT usuario.id, usuario.usuario, tipo_usuario.id, tipo_usuario.usuario
						FROM usuario INNER JOIN tipo_usuario ON usuario.tipo_usuario = tipo_usuario.id
						WHERE usuario.id = {0}""".format(id)
            cursor.execute(query)
            data = cursor.fetchone()
            usuario = TipoUsuario(data[2], data[3])
            logged = Usuario(data[0], data[1], None, None, None, None, usuario)
            return logged

        except Exception as e:
            raise Exception(e)

    @classmethod
    def agregar_usuario(self, db, usuario, nombres, apellido_p, apellido_m, password, tipo_usuario):
        try:
            cursor = db.connection.cursor()
            query = """INSERT INTO usuario(usuario, nombres, apellido_p, apellido_m, password, tipo_usuario)
            VALUES('{0}', '{1}', '{2}', '{3}', '{4}', '{5}')""".format(
                usuario, nombres, apellido_p, apellido_m, password, tipo_usuario)
            cursor.execute(query)
            db.connection.commit()
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def consultar_usuarios(self, db):
        try:
            cursor = db.connection.cursor()
            query = """SELECT usuario, nombres, apellido_p, apellido_m, tipo_usuario
            FROM usuario"""
            cursor.execute(query)
            data = cursor.fetchall()
            usuarios = []
            for u in data:
                usuario = Usuario(None, u[0], u[1], u[2], u[3], None, u[4])
                usuarios.append(usuario)
            return usuarios
        except Exception as ex:
            raise Exception(ex)
