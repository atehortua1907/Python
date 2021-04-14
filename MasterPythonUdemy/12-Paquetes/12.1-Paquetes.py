"""
    Paquetes: son una agrupacion de modulos
    Para crear un paquete: 
        1.Crear carpeta con el nombre del paquete 
        2.Crar un archivo llamado __init__.py
        3.Crear los diferentes modulos del paquete
"""

print("PROBANDO PAQUETES: ")

from miPaquete import pruebas
from miPaquete import herramientas

#from miPaquete import pruebas, herramientas #O podemos importar los paquetes en una sola linea

pruebas.probando()
herramientas.nombreCompleto("Jeison David", "Atehortua Alvarez")

"""
    Impresiones archivo
    PROBANDO PAQUETES:
    Esto es una prueba de un modulo dentro de un paquete
    Jeison David Atehortua Alvarez
"""