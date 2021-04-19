from tkinter import *
from PIL import Image, ImageTk

ventana = Tk()
ventana.geometry("700x500")

Label(ventana, text="Hola soy Gokú").pack(anchor=W)
imagen = Image.open('./Imagenes/M51.jpg')
render = ImageTk.PhotoImage(imagen)
Label(ventana, image=render).pack()
ventana.mainloop()