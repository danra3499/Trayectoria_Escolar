from .entities.Periodos import Periodos

class Modelo_periodo():
    @classmethod
    def obtener_periodos(self, db):
        try: 
            cursor = db.connection.cursor()
            query = "SELECT id_periodos, periodo FROM periodos"
            cursor.execute(query)
            data = cursor.fetchall()
            periodos = []
            for periodo in data:
                p = Periodos(periodo[0], periodo[1])
                periodos.append(p)
            return periodos
        except Exception as e:
            raise Exception(e)