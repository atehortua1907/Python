from io import open
import pathlib

#pathlib.Path().absolute() ruta absoluta... es donde se esta ejecutando el scrip
ruta = f"{pathlib.Path().absolute()}/fichero_texto.txt"
print(ruta)
archivo = open(ruta, "a+") #Abre un archivo y si no exite lo crea

#Escribir en el archivo
archivo.write("*********  Soy un texto metido desde python *********\n")

#Cerrar el archivo
archivo.close()

#Abrir archivo
archivo_abierto = open(ruta, "r")

#Leer el contenido
contenidoArchivo = archivo_abierto.read()
print(contenidoArchivo)
archivo_abierto.close()

#Abrir archivo
archivo_abierto = open(ruta, "r")

#Leer contenido y guardar en una lista
listaContenidoArchivo = archivo_abierto.readlines()

for frase in listaContenidoArchivo:
    print(f"---{frase}")
"""
Impresion archivo
*********  Soy un texto metido desde python *********
*********  Soy un texto metido desde python *********
*********  Soy un texto metido desde python *********
*********  Soy un texto metido desde python *********

---*********  Soy un texto metido desde python *********

---*********  Soy un texto metido desde python *********

---*********  Soy un texto metido desde python *********

---*********  Soy un texto metido desde python *********
"""