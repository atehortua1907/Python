class Coche:
    
    #Atributos o propiedades con valores por defecto
    color = "Rojo"
    marca = "Ferrari"
    modelo = "Aventura"
    velocidad = 300

    soyAtributoPublico = "Soy un atributo publico"
    __soyAtributoPrivado = "Soy un atributo privado" #al tener como prefijo un __ es privado


    #Getters y Setters
    def setColor(self, color):
        self.color = color
    
    def getColor(self):
        return self.color
    
    def setMarca(self, marca):
        self.marca = marca
    
    def getMarca(self):
        return self.marca
    
    def SetModel(self, modelo):
        self.modelo = modelo
    
    def getModel(self):
        return self.modelo

    def setVelocidad(self, velocidad):
        self.velocidad = velocidad
    
    def getVelocidad(self):
        return self.velocidad

    
    #Constructor
    def __init__(self, color, marca, modelo, velocidad):
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad

    #Métodos, son acciones que hace el objeto (Coche) (funciones)    
    def acelerar(self):
        self.velocidad += 1
    
    def frenar(self):
        self.velocidad -= 1
    
    def getInfoCoche(self):

        info = f"--------- Información del coche {self.getMarca()}---------"
        info += f"\n Color: {self.getColor()}"
        info += f"\n Marca: {self.getMarca()}"
        info += f"\n Modelo: {self.getModel()}"
        info += f"\n Velocidad: {self.getVelocidad()}"

        return info
