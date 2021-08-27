from datetime import date


class Evaluacion():
    def __init__(self, id, parcial, fecha, calificacion,  id_tipo_evaluacion, id_materia, id_alumno):
        self.id = id
        self.parcial = parcial
        self.fecha = date.today()
        self.calificacion = calificacion
        self.id_tipo_evaluacion = id_tipo_evaluacion
        self.id_meteria = id_materia
        self.id_alumno = id_alumno

        """
      id INT NOT NULL AUTO_INCREMENT,
      parcial INT NOT NULL,
      fecha DATE NOT NULL,
      calificacion DECIMAL(2,2),
      id_tipo_evaluacion INT NOT NULL,
      id_materia INT NOT NULL,
      id_alumno INT NOT NULL,
      FOREIGN KEY(id_tipo_evaluacion) REFERENCES tipo_evaluacion(id),
      FOREIGN KEY(id_alumno) REFERENCES alumno(id),
      FOREIGN KEY(id_materia) REFERENCES materia(id),
      PRIMARY KEY(id)
    """
