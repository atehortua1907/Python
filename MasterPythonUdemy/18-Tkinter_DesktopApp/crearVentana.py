from tkinter import *

class CrearVentanaTkinter:

    def __init__(self, title, icon, size, resizable):
        self.title = title
        self.icon = icon
        self.size = size
        self.resizable = resizable

    def cargar(self):

        #Crear la ventana raíz
        self.ventana = Tk()

        #Titulo de la ventana
        self.ventana.title(self.title)

        # Icono de la ventana
        self.ventana.iconbitmap(self.icon)

        #Cambio en el tamaño de ventana
        self.ventana.geometry(self.size)

        # Bloquear el tamaño de la ventana
        #Parametros que indican (ancho, alto) aquí puede modificar el tamaño del ancho pero no del alto
        if self.resizable:
            ventana.resizable(1,1) 
        else:
            self.ventana.resizable(0,0)

    #Mostrar texto en el programa
    def addTexto(self, text):
        texto = Label(self.ventana, text=text)
        texto.pack()

    def mostrar(self):
        #Arrancar y mostrar la ventana hasta que se cierre
        self.ventana.mainloop()
