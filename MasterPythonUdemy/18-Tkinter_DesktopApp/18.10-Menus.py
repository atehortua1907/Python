from tkinter import *

ventana = Tk()
ventana.geometry("600x600")

#Menu principal
mi_menu = Menu(ventana)
ventana.config(menu=mi_menu)

#Submenu
archivo = Menu(mi_menu, tearoff=0)
archivo.add_command(label="Nuevo Archivo")
archivo.add_command(label="Nueva Ventana")
archivo.add_separator()
archivo.add_command(label="Abrir Archivo")
archivo.add_command(label="Abrir Carpeta")
archivo.add_command(label="Salir", command=ventana.quit)

#Añadiendo submenu
mi_menu.add_cascade(label="Archivo",menu=archivo)
mi_menu.add_command(label="Editar")
mi_menu.add_command(label="Seleccion")
ventana.mainloop()