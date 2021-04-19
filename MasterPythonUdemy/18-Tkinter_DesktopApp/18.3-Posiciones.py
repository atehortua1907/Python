from tkinter import *

ventana = Tk()
# ventana.geometry("500x700")

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
texto.pack(side=TOP)

texto = Label(ventana, text="televisor")
texto.config(
    height=3, #Son como 3 textos del mismo tamaño
    bg="red",
    font=("Arial", 18),
    padx=10,
    pady=20,
    cursor="star" #esto cambia el estilo del cursor
)
texto.pack(side=TOP, fill=X, expand=YES)

texto = Label(ventana, text="básico")
texto.config(
    height=3, #Son como 3 textos del mismo tamaño
    bg="green",
    font=("Arial", 18),
    padx=10,
    pady=20,
    cursor="clock" #esto cambia el estilo del cursor
)
texto.pack(side=LEFT, fill=X, expand=YES)

texto = Label(ventana, text="ventilador")
texto.config(
    height=3, #Son como 3 textos del mismo tamaño
    bg="blue",
    font=("Arial", 18),
    padx=10,
    pady=20,
    cursor="star" #esto cambia el estilo del cursor
)
texto.pack(side=LEFT, fill=X, expand=YES)

texto = Label(ventana, text="celular")
texto.config(
    height=3, #Son como 3 textos del mismo tamaño
    bg="orange",
    font=("Arial", 18),
    padx=10,
    pady=20,
    cursor="heart" #esto cambia el estilo del cursor
)
texto.pack(side=LEFT, fill=X, expand=YES)

ventana.mainloop()