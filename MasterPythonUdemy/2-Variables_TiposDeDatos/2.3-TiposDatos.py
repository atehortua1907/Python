print("Principales tipos en python:")

nada = None
cadena = "Hola esto es una cadena"
entero = 99
flotante = 4.7
booleano = True
tuplaNoCambia = ("los datos aquí", "no se pueden cambiar", "porque es tupla", 22)
diccionario = {"nombre": "David", "apellido": "Atehortua"}
rango = range(9)
dato_byte = b"tipodatobyte"
listaTipos = [nada, cadena, entero, flotante, booleano, 
            tuplaNoCambia, diccionario, dato_byte]

print(type(listaTipos))
#Esto es un ciclo for que se ve despues, se usa aquí para imprimir los tipos de forma iterativa
for tipo in listaTipos:
    print(type(tipo))