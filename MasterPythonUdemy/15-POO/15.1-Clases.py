class Coche:

    #Atributos o propiedades con valores por defecto
    color = "Rojo"
    marca = "Ferrari"
    modelo = "Aventura"
    velocidad = 300


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

    #Métodos, son acciones que hace el objeto (Coche) (funciones)    
    def acelerar(self):
        self.velocidad += 1
    
    def frenar(self):
        self.velocidad -= 1

# fin definicion clase

# Crear objeto / Instanciar la clase
coche = Coche()
coche.setMarca("Volvo")

print("########## Coche 1 ##########")
print(coche.getMarca(), coche.getModel())
print(f"Velocidad actual: {coche.getVelocidad()}")

coche.acelerar()
coche.acelerar()
coche.acelerar()

print(f"Velocidad actual despues de acelerar: {coche.getVelocidad()}")

coche.frenar()
print(f"Velocidad actual despues de frenar: {coche.getVelocidad()}")


print("########## Coche 2 ##########")
cocheDos = Coche()

cocheDos.setMarca("Renault")
coche.setColor("Fucsia")

print(cocheDos.getMarca(), cocheDos.getColor())


"""
    ########## Coche 1 ##########
    Volvo Aventura
    Velocidad actual: 300
    Velocidad actual despues de acelerar: 303
    Velocidad actual despues de frenar: 302
    ########## Coche 2 ##########
    Renault Rojo
"""