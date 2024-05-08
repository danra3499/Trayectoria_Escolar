class IndicesAlum():
    def __init__(self, id_alumno_indice, id_alumno, iao, iac, ipe, ide, ise, ire, nombre):
        self.id_alumno = id_alumno
        self.iao = iao
        self.iac = iac
        self.ipe = ipe
        self.ide = ide
        self.ise = ise
        self.ire = ire
        self.nombre = nombre
class Indices():
    def __init__(self, id_IAO, nivel_IAO, categoria_IAO):
        self.id_IAO = id_IAO
        self.nivel_IAO = nivel_IAO
        self.categoria_IAO = categoria_IAO

class IndicesIAC():
    def __init__(self, id_IAC, nivel_IAC, categoria_IAC):
        self.id_IAC = id_IAC
        self.nivel_IAC = nivel_IAC
        self.categoria_IAC = categoria_IAC    
    
class IndicesIPE():
    def __init__(self, id_IPE, nivel_IPE, categoria_IPE):
        self.id_IPE = id_IPE
        self.nivel_IPE = nivel_IPE
        self.categoria_IPE = categoria_IPE   

class IndicesIDE():
    def __init__(self, id,id_IDE, categoria_IDE, categoria_IAO, categoria_IAC, categoria_IPE):
        self.id = id
        self.id_IDE = id_IDE
        self.categoria_IDE = categoria_IDE
        self.categoria_IAO = categoria_IAO
        self.categoria_IAC = categoria_IAC
        self.categoria_IPE = categoria_IPE

class IndicesISE():
    def __init__(self, id_ISE, nivel_ISE, categoria_ISE):
        self.id_ISE = id_ISE
        self.nivel_ISE = nivel_ISE
        self.categoria_ISE = categoria_ISE   

class IndicesIRE():
    def __init__(self, id, id_IRE, categoria_IRE, categoria_IDE, categoria_ISE):
        self.id = id
        self.id_IRE = id_IRE
        self.categoria_IRE = categoria_IRE
        self.categoria_IDE = categoria_IDE
        self.categoria_ISE = categoria_ISE
