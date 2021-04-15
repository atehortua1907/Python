
def obtenerNombreEdad():
    nombre = input("Introduce el nombre: ")
    edad = int(input("Introduce la edad: "))

    if edad < 5 or edad > 110:
        raise ValueError("Lanzando excepcion edad no es real")
    elif not nombre:
        raise ValueError("Lanzando excepcion nombre no valido")

#Capturo excepción y la imprimo
try:
    obtenerNombreEdad()
except Exception as e:
    print(e)

"""
    Impresiones archivo 
    Introduce el nombre: Loco
    Introduce la edad: 150
    Lanzando excepcion edad no es real
"""