from tkinter import *
from tkinter import messagebox as MessageBox



ventana = Tk()
ventana.config(bd=70)

def sacarAlerta():
    MessageBox.showinfo("Alerta", "Hola Soy Gohan!")

def salir(nombre = ""):
    resultado = MessageBox.askquestion("Salir", "¿Continuar ejecutando la aplicacion?")

    if resultado != "yes":
        MessageBox.showinfo("Despedida", f"Adios {nombre}")
        ventana.destroy()

Button(ventana, text="Mostrar Alerta!!!", command=sacarAlerta).pack()
Button(ventana, text="Salir", command=salir).pack()
Button(ventana, text="salir con parametro", command=lambda: salir("David")).pack()

ventana.mainloop()