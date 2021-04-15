"""
    HERENCIA: Es la posiblidad de compartir atributos y Métodos
    entre clases y que diferentes clases hereden de otras
"""

class Persona:
    """
        nombre
        apellidos
        altura
        edad
    """

    # __nombre : "nombre"
    # __apellidos
    # __altura
    # __edad

    def getNombre(self):
        return self.__nombre
    
    def setNombre(self, nombre):
        self.__nombre = nombre
    
    def getApellidos(self):
        return self.__apellidos
    
    def setApellidos(self, apellidos):
        self.__apellidos = apellidos
    
    def getAltura(self):
        return self.__altura
    
    def setAltura(self, altura):
        self.__altura = altura
    
    def getEdad(self):
        return self.__edad
    
    def setEdad(self, edad):
        self.__edad = edad

    def hablar(self):
        return "Estoy hablando"
    
    def caminar(self):
        return "Estoy caminando"

    def dormir(self):
        return "Estoy durmiendo"


class Informatico(Persona):
    """
        lenguajes
        experiencia
    """

    # __lenguajes
    # __experiencia

    def __init__(self):
        self.__lenguajes = "HTML, CSS, JavaScript, PHP"
        self.__experiencia = 5
    
    def getLenguajes(self):
        return self.__lenguajes
    
    def aprender(self, lenguajes):
        self.__lenguajes = lenguajes
        return self.__lenguajes

    def programar(self):
        return "Estoy programando"

class TecnicoRedes(Informatico):

    def __init__(self):
        super().__init__() #Para invocar constructor del padre
        self.uditarRedes = 'Experto'
        self.experienciaRedes = 15
    
    def auditoria(self):
        return "Estoy auditando una red"