from tkinter import *
from tkinter import ttk #Para tablas en tkinter

#Definir Ventana
ventana = Tk()
ventana.geometry("500x500")
ventana.title("Proyecto Tkinter | Master en Python")
ventana.resizable(0,0)

#Pantallas
def home():
    #Mostrar pantalla    
    home_label.config(
        fg="white",
        bg="black",
        font=("Arial", 30),
        padx=210,
        pady=20
    )
    home_label.grid(row=0, column=0)
    products_table.grid(row=1)

    #Listar Productos
    for product in products:
        if len(product) == 3:
            product.append("added")
            products_table.insert('', 0, text=product[0], values=(product[1]))

    #Ocultar pantallas
    add_label.grid_remove()
    add_frame.grid_remove()
    info_label.grid_remove()
    data_label.grid_remove()

def add():
    #Encabezado
    add_label.config(
        fg="white",
        bg="black",
        font=("Arial", 30),
        padx=110,
        pady=20
    )
    add_label.grid(row=0, column=0, columnspan=10)
    
    #Campos del formulario
    add_frame.grid(row=1)
    add_name_label.grid(row=1, column=0, padx = 5, pady = 5, sticky=E)
    add_name_entry.grid(row=1, column=1, padx = 5, pady = 5, sticky=W)

    add_price_label.grid(row=2, column=0, padx = 5, pady = 5, sticky=E)
    add_price_entry.grid(row=2, column=1, padx = 5, pady = 5, sticky=W)

    add_description_label.grid(row=3, column=0, padx = 5, pady = 5, sticky=NE)
    add_description_entry.grid(row=3, column=1, padx = 5, pady = 5, sticky=W)
    add_description_entry.config(
        width=30,
        height=5,
        font = ("Consolas", 12),
        padx = 15,
        pady = 15
    )

    boton.grid(row=5, column=1, padx = 5, pady = 10, sticky=W)
    boton.config(
        bg="green", fg="white",padx = 15, pady = 5
    )

    #Ocultar pantallas
    home_label.grid_remove()
    info_label.grid_remove()
    data_label.grid_remove()
    products_table.grid_remove()

def info():    
    info_label.config(
        fg="white",
        bg="black",
        font=("Arial", 30),
        padx=150,
        pady=20
    )
    info_label.grid(row=0, column=0)
    
    data_label.grid(row=1,column=0)

    #Ocultar pantallas
    add_frame.grid_remove()
    home_label.grid_remove()
    add_label.grid_remove()
    products_table.grid_remove()

def add_product():
    products.append([
        name_data.get(),
        price_data.get(),
        add_description_entry.get("1.0", "end-1c"),
    ])
    name_data.set("")
    price_data.set("")
    add_description_entry.delete("1.0", END)

    home()


#Variables importantes
products = []
name_data = StringVar()
price_data = StringVar()
description_data = StringVar()

#Definir campos de pantalla INICIO
home_label = Label(ventana, text="Inicio")

style = ttk.Style()
style.configure("mystyle.Treeview", padding=35)
products_table = ttk.Treeview(height=12, columns=2, style="mystyle.Treeview")
products_table.grid(row=1, column=0,columnspan=2)
products_table.heading("#0", text='Producto', anchor=W)
products_table.heading("#1", text='Precio', anchor=W)


#********** Pantalla AÑADIR **********#

add_label = Label(ventana, text="Añadir Producto")

#Campos formulario
add_frame = Frame(ventana)
add_name_label = Label(add_frame, text="Nombre: ")
add_name_entry = Entry(add_frame, textvariable=name_data)

add_price_label = Label(add_frame, text="Precio: ")
add_price_entry = Entry(add_frame, textvariable=price_data)

add_description_label = Label(add_frame, text="Descripción: ")
add_description_entry = Text(add_frame)

boton = Button(add_frame, text="Guardar", command=add_product)

#Definir campos de pantalla INFORMACIÓN
info_label = Label(ventana, text="Información")
data_label = Label(ventana, text="Creado por David Atehortua - 2021")

# Cargar pantalla inicio
home()

#Menú superior
menu_superior = Menu(ventana)
menu_superior.add_command(label="Inicio", command=home)
menu_superior.add_command(label="Añadir", command=add)
menu_superior.add_command(label="Información", command=info)
menu_superior.add_command(label="Salir", command=ventana.quit)

#Cargar Menú
ventana.config(menu=menu_superior)

#Salir


#Cargar ventana
ventana.mainloop()