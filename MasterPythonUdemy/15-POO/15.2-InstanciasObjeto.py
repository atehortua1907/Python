from claseCoche import Coche

carro1 = Coche("Amarillo", "Renault", "Sandero", 400)
carro2 = Coche("Verde", "Seat", "Panda", 240)
carro3 = Coche("Azul", "Citroen", "Xara", 100)
print(carro1.getInfoCoche(), "\n",carro2.getInfoCoche(), "\n", carro3.getInfoCoche())

#Detectar tipado
if type(carro1) == Coche:
    print(f"{carro1.getMarca()} es un objeto tipo {type(carro1).__name__}")

"""
    Impresiones archivo
    --------- Información del coche Renault---------
    Color: Amarillo
    Marca: Renault
    Modelo: Sandero
    Velocidad: 400
    --------- Información del coche Seat---------
    Color: Verde
    Marca: Seat
    Modelo: Panda
    Velocidad: 240
    --------- Información del coche Citroen---------
    Color: Azul
    Marca: Citroen
    Modelo: Xara
    Velocidad: 100

    Renault es un objeto tipo Coche
"""

import Herencia

persona = Herencia.Persona()
persona.setNombre("David")
persona.setApellidos("Atehortua")
persona.setAltura(177)
persona.setEdad(34)
print(f"La persona es {persona.getNombre()}")
print(persona.hablar(),persona.caminar())

informatico = Herencia.Informatico()
informatico.setNombre("Gohan")
informatico.setApellidos("Atehortua")
print(f"El informatico es {informatico.getNombre()} {informatico.getApellidos()}")
print(f"Sabe los siguientes lenguajes: {informatico.getLenguajes()}")
print(f"metodo de la clase padre: {informatico.caminar()}")

tecnicoRedes = Herencia.TecnicoRedes()
tecnicoRedes.setNombre("Manolo")
print("TecnicoRedes Objeto que hereda de informatico", tecnicoRedes.getNombre(), tecnicoRedes.auditoria(), tecnicoRedes.getLenguajes())

"""
    Impresiones archivo
    La persona es David
    Estoy hablando Estoy caminando
    Estoy hablando Estoy caminando
    El informatico es Gohan Atehortua
    Sabe los siguientes lenguajes: HTML, CSS, JavaScript, PHP
    metodo de la clase padre: Estoy caminando
    TecnicoRedes Objeto que hereda de informatico Manolo Estoy auditando una red HTML, CSS, JavaScript, PHP
"""
