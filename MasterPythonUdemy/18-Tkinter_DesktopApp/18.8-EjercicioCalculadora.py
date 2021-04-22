"""
    CALCULADORA:
    -Dos campos de texto
    -4 botones para las operaciones
    -Mostrar el resultado en una alerta
"""

from tkinter import *
from tkinter import messagebox as MessageBox

def operaciones(operacion):

    numero1 = int(num1.get())
    numero2 = int(num2.get())
    result = 0

    if operacion == "suma":
        result = numero1 + numero2
    
    if operacion == "resta":
        result = numero1 - numero2
    
    if operacion == "multiplicacion":
        result = numero1 * numero2
    
    if operacion == "division":
        result = numero1 / numero2
    
    message = f"""
            La {operacion} entre el numero {numero1}
            y el {numero2} es {result}
        """

    MessageBox.showinfo("Resultado", message)  



ventana = Tk()

ventana.title("Formularios en Tkinter | Ejercicio Calculadora")

#Texto encabezado para
encabezado = Label(ventana, text="Calculadora")
encabezado.config(
    fg="white",
    bg="darkgray",
    font=("Open Sans", 18),
    padx = 10,
    pady = 10
)
encabezado.grid(row=0, column=0, columnspan=12, sticky=N)

#Label para el campo Número 1
label = Label(ventana, text="Número 1:")
label.grid(row=1, column=0, sticky=W, padx=5, pady=5)

#Campo de texto
num1 = Entry(ventana)
num1.grid(row=1, column=1, sticky=W, padx=5, pady=5)
num1.config(justify="right", state="normal")


#Label para el campo Número 2
label = Label(ventana, text="Número 2:")
label.grid(row=2, column=0, sticky=W, padx=5, pady=5)

#Campo de texto
num2 = Entry(ventana)
num2.grid(row=2, column=1, sticky=W, padx=5, pady=5)
num2.config(justify="left", state="normal")

Button(ventana, text="Sumar", command=lambda: operaciones("suma")).grid(row=3, column=0, sticky=W)
Button(ventana, text="Restar", command=lambda: operaciones("resta")).grid(row=3, column=1, sticky=W)
Button(ventana, text="Multiplicar", command=lambda: operaciones("multiplicacion")).grid(row=3, column=2, sticky=W)
Button(ventana, text="Dividir", command=lambda: operaciones("division")).grid(row=3, column=3, sticky=W)

ventana.mainloop()