from tkinter import *

ventana = Tk()
ventana.geometry("800x500")

encabezado = Label(ventana, text="Formularios 2")
encabezado.config(
    padx = 15,
    pady = 15,
    fg = 'white',
    bg = 'green',
    font = ("Consolas", 20)
)
encabezado.grid(row=0, column=0, columnspan=5, sticky=W)

# Botones check

def mostrarProfesion():
    texto = ""
    if web.get():
        texto = 'Desarrollo Web'
    
    if movil.get() and web.get():
        texto += ' y'
    
    if movil.get():
        texto += ' Desarrollo movil'

    mostrar.config(
        text = texto,
        bg = "green", 
        fg="white"
    )

web = BooleanVar()
movil = BooleanVar()

Label(ventana, text="¿A que te dedicas?").grid(row=1, column=0)
Checkbutton(
    ventana,
    text="Desarrollo web",
    variable=web,
    onvalue=True,
    offvalue=False,
    command=mostrarProfesion
).grid(row=2, column=0)

Checkbutton(
    ventana,
    text="Desarrollo movil",
    variable=movil,
    onvalue=True,
    offvalue=False,
    command=mostrarProfesion
).grid(row=3, column=0)

mostrar = Label(ventana)
mostrar.grid(row=4, column=0)

# Radio buttons
def marcar():
    marcado.config(text=opcion.get())

opcion = StringVar()
opcion.set(None)

Label(ventana, text="¿Cuál es tu Genero?").grid(row=5)
Radiobutton(
    ventana,
    text="Masculino",
    value="Masculino",
    variable=opcion,
    command=marcar
).grid(row=6)

Radiobutton(
    ventana,
    text="Femenino",
    value="Femenino",
    variable=opcion,
    command=marcar
).grid(row=7)

marcado = Label(ventana)
marcado.grid(row=8)


# Menu opciones, combobox
opcion = StringVar()
opcion.set('Seleccione una opción...')
Label(ventana, text="Selecciona una opción").grid(row=5, column=1)
select = OptionMenu(ventana, opcion, "Opcion 1", "Opcion 2", "Opcion 3")
select.grid(row=6, column=1)


ventana.mainloop()