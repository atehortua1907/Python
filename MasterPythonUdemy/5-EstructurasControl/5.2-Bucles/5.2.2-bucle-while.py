"""
    #BUCLE WHILE 
    Estructura de control que itrera o repite la ejecución de una
    serie de instrucciones tantas veces como sea necesario,
    hasta que deje de cumplirse la condición

    contador = inicializar contador

    while condición:
        bloque de instrucciones
        actualización de contador
"""

contador = 0

#Imprimir numeros del 0 al 100
while contador <= 100:
    print(f"# {contador}")
    contador += 1

print("---------------------------")

#Imprimir los números del 1 al 100 en una sola linea separados por coma (,)
contador = 1
muestrame = str(0)

while contador <= 100:
    muestrame = f"{muestrame} ,{contador}"
    contador += 1

print(muestrame)

print("\n")
print("################# Tabla de multiplicar #################")

numero_usuario = int(input("De que número quieres la tabla?: "))

if numero_usuario < 1:
    numero_usuario = 1

print(f"### Tabla de multiplicar del número : {numero_usuario}")

contador = 1
while contador <= 10:
    print(f"{numero_usuario} X {contador} = {numero_usuario * contador}")
    contador += 1
else: #Python permite colocar un else que se ejecuta cuando un ciclo ha terminado
    print(f"Tabla de multiplicar del {numero_usuario} finalizada!")

"""
    ################# Tabla de multiplicar #################
    De que número quieres la tabla?: 4
    ### Tabla de multiplicar del número : 4
    4 X 1 = 4
    4 X 2 = 8
    4 X 3 = 12
    4 X 4 = 16
    4 X 5 = 20
    4 X 6 = 24
    4 X 7 = 28
    4 X 8 = 32
    4 X 9 = 36
    4 X 10 = 40
    Tabla de multiplicar del 4 finalizada!
"""
    
