from io import open
import pathlib
import shutil
import os
import os.path


rutaOrigen = f"{pathlib.Path().absolute()}/fichero_texto.txt"
rutaDestino = f"{pathlib.Path().absolute()}/fichero_copiado.txt"
rutaAbsolutaNivelArriba = f"{pathlib.Path().absolute()}/../0-Intro_Documentacion/fichero_copiado2.txt"
rutaMovido = f"{pathlib.Path().absolute()}/../0-Intro_Documentacion/"
rutaOrigenRenombrado = f"{pathlib.Path().absolute()}/fichero_Movido_Renombrado.txt"

#Copiar Archivos
shutil.copy(rutaOrigen, rutaDestino)
shutil.copy(rutaDestino, rutaAbsolutaNivelArriba)

#Mover o renombrar
shutil.move(rutaOrigen, rutaMovido)
shutil.move(rutaOrigen, rutaOrigenRenombrado)

#Eliminar archivo
os.remove(rutaOrigenRenombrado)

#Comprobar si un archivo existe
if os.path.exists(rutaOrigen):
    print("El archivo existe")
else:
    print("El archivo no existe")