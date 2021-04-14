import os
import shutil

fichero = "D:\\FicheroNoExiste"
ficheroOrigen = "D:\\FicheroCopy"
destino = "D:\\FicheroSiExiste\FicheroPegado"

#Crear carpeta
if os.path.exists(fichero):
    print("Ya existe el directorio")
else:
    os.mkdir(fichero)


#Borrar carpeta OJO: si la carpeta tiene contenido no la borra, saca error
os.rmdir(fichero)

#Copiar carpeta
shutil.copytree(ficheroOrigen,destino)

#Llevar contenido de un fichero a una lista
contenido = os.listdir(destino)

for fichero in contenido:
    print(f"Fichero: {fichero}")