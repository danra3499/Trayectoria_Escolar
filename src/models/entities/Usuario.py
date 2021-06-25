from werkzeug.security import check_password_hash
from flask_login import UserMixin


class Usuario(UserMixin):
    def __init__(self, id, usuario, nombres, apellidos, password, tipo_usuario):
        self.id = id
        self.usuario = usuario
        self.nombres = nombres
        self.apellidos = apellidos
        self.password = password
        self.tipo_usuario = tipo_usuario

    @classmethod
    def check_password(self, encrypted, password):
        return check_password_hash(encrypted, password)
