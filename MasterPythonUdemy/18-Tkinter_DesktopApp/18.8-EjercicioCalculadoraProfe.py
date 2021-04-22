"""
    CALCULADORA:
    -Dos campos de texto
    -4 botones para las operaciones
    -Mostrar el resultado en una alerta
"""

from tkinter import *
from tkinter import messagebox as MessageBox

ventana = Tk()
ventana.title("Formularios en Tkinter | Ejercicio Calculadora")
ventana.geometry("400x400")
ventana.config(bd=25)

numero1 = StringVar()
numero2 = StringVar()

marco = Frame(ventana, width=300, height=200)
marco.config(
    bd=5,
    padx=15,
    pady=15,
    relief=SOLID
)
marco.pack(side=TOP, anchor=CENTER)
marco.pack_propagate(False)

#Label para el campo Número 1
label = Label(marco, text="Primer número:").pack()
Entry(marco, textvariable=numero1, justify="center").pack()

label = Label(marco, text="Segundo número:").pack()
Entry(marco, textvariable=numero2, justify="center").pack()

Button(marco, text="Sumar", command=lambda: operaciones("suma")).pack(side="left", fill=X, expand=YES)
Button(marco, text="Restar", command=lambda: operaciones("resta")).pack(side="left", fill=X, expand=YES)
Button(marco, text="Multiplicar", command=lambda: operaciones("multiplicacion")).pack(side="left", fill=X, expand=YES)
Button(marco, text="Dividir", command=lambda: operaciones("division")).pack(side="left", fill=X, expand=YES)


def tryParseInt(num):
    try:
        int(num)
        return True
    except:
        return False

def operaciones(operacion):

    if not tryParseInt(numero1.get()) or not tryParseInt(numero2.get()):
        numero1.set("")
        numero2.set("")
        MessageBox.showerror("Error", "Debe ingresar números")
        return

    num1 = int(numero1.get())
    num2 = int(numero2.get())
    result = 0

    if operacion == "suma":
        result = num1 + num2
    
    if operacion == "resta":
        result = num1 - num2
    
    if operacion == "multiplicacion":
        result = num1 * num2
    
    if operacion == "division":
        result = num1 / num2
    
    message = f"""
            La {operacion} entre el numero {num1}
            y el {num2} es {result}
        """
    numero1.set("")
    numero2.set("")
    MessageBox.showinfo("Resultado", message)  

ventana.mainloop()