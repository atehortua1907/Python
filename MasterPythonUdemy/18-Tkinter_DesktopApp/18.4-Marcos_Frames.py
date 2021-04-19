from tkinter import *

ventana = Tk()
ventana.title("Marcos | Master en Python")
ventana.geometry("700x700")

#********** Marco Superior **********#
marco_padre = Frame(ventana, width=250, height=250)
marco_padre.config(
    bg="lightblue"
)
marco_padre.pack(side=TOP, fill=X, expand=YES, anchor=N)

marco = Frame(marco_padre, width=250, height=250)
marco.config(
    bg="yellow",
    bd=5,
    relief=SOLID
)
marco.pack(side=LEFT, anchor=SW)
marco.pack_propagate(False) #Para que quede estatico y no lo afecten las demas modificaciones

texto = Label(marco, text="MARCO 1")
#Una forma para centrar el texto
texto.config(
    bg="yellow",
    fg="black",
    font=("Arial", 20),
    anchor = CENTER,
    height=10,
    width=10
)
texto.pack()

marco = Frame(marco_padre, width=250, height=250)
marco.config(
    bg="blue",
    bd=5,
    relief=SOLID
)
marco.pack(side=RIGHT, anchor=SE)
marco.pack_propagate(False) #Para que quede estatico y no lo afecten las demas modificaciones

texto = Label(marco, text="MARCO 2")
#Otra forma para centrar el texto
texto.config(
    bg="blue",
    fg="white",
    font=("Arial", 20),
    anchor = CENTER
)
texto.pack(fill=Y, expand=YES)


#********** Marco Ingerior **********#
marco_padre = Frame(ventana, width=250, height=250)
marco_padre.config(
    bg="lightblue"
)
marco_padre.pack(side=BOTTOM, fill=X, expand=YES, anchor=S)

marco = Frame(marco_padre, width=250, height=250)
marco.config(
    bg="red",
    bd=5,
    relief=SOLID
)
marco.pack(side=LEFT)

marco = Frame(marco_padre, width=250, height=250)
marco.config(
    bg="green",
    bd=5,
    relief=SOLID
)
marco.pack(side=RIGHT)


ventana.mainloop()