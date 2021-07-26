from .entities.Grupo import Grupo


class Modelo_grupo():
    @classmethod
    def obtener_grupos(self, db):
        try:
            cursor = db.connection.cursor()
            query = "SELECT id, semestre FROM grupo"
            cursor.execute(query)
            data = cursor.fetchall()
            grupos = []
            for grupo in data:
                g = Grupo(grupo[0], grupo[1])
                grupos.append(g)
            return grupos
        except Exception as e:
            raise Exception(e)
