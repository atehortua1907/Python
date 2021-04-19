from tkinter import *

ventana = Tk()
ventana.geometry("500x500")

texto = Label(ventana, text="Bienvenido a mi programa")

#Configuraciones de texto
texto.config(
    fg="white",
    bg="#000000",
    padx=50,
    pady=20,
    font=("Consolas", 30)
)

texto.pack()

texto = Label(ventana, text="Soy David Atehortua")
texto.config(
    height=3, #Son como 3 textos del mismo tamaño
    bg="orange",
    font=("Arial", 18),
    padx=10,
    pady=20,
    cursor="spider" #esto cambia el estilo del cursor
)
texto.pack(anchor=E)

texto = Label(ventana, text="Soy David Atehortua")
texto.config(
    height=3, #Son como 3 textos del mismo tamaño
    bg="red",
    font=("Arial", 18),
    padx=10,
    pady=20,
    cursor="star" #esto cambia el estilo del cursor
)
texto.pack(anchor=W)

ventana.mainloop()

