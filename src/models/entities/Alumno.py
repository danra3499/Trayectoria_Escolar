class Alumno():
    def __init__(self, id, nombres, apellido_p, apellido_m, genero, status, semestre, grupo):
        self.id = id
        self.nombres = nombres
        self.apellido_p = apellido_p
        self.apellido_m = apellido_m
        self.genero = genero
        self.status = status
        self.semestre = semestre
        self.grupo = grupo

    def nombre_completo(self):
        return f'{self.apellido_p} {self.apellido_m} {self.nombres}'
