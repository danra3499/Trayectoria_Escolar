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
                                     None, None, data[2], None)
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
            print(data)
            usuario = TipoUsuario(data[2], data[3])
            logged = Usuario(data[0], data[1], None, None, None, usuario)
            return logged

        except Exception as e:
            raise Exception(e)
