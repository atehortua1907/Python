#Tkinter
#Modulo para crear interfaces gráficas de usuario

from crearVentana import CrearVentanaTkinter
import os.path

ruta_icono = os.path.abspath('./Imagenes/Logo.ico')

#para cuando se ejecute por visual studio code
if not os.path.isfile(ruta_icono):
    ruta_icono = os.path.abspath('D:/Repositories/Python/MasterPythonUdemy/18-Tkinter_DesktopApp/Imagenes/Logo.ico')


programa = CrearVentanaTkinter("Tkinter con Python", ruta_icono, "750x500",  False )
programa.cargar()
programa.addTexto("Hola Mundo!")
programa.mostrar()

