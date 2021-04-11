"""
    # FOR 
     for variable in elemento_iterable (lista, rango, etc):
         BLOQUE DE INSTRUCCIONES
"""
resultado = 0

for  item in range(0, 5):
    print(f"Iteración número: {item}")
    resultado += item

print(f"El resulta de la suma es: {resultado}")

"""
    Iteración número: 0
    Iteración número: 1
    Iteración número: 2
    Iteración número: 3
    Iteración número: 4
    El resulta de la suma es: 10
"""

print("\n")
print("################# Tabla de multiplicar #################")

numero_usuario = int(input("De que número quieres la tabla?: "))

if numero_usuario < 1:
    numero_usuario = 1

print(f"### Tabla de multiplicar del número : {numero_usuario}")

for item in range(1,11):

    if numero_usuario == 45:
        print(f"El numero {numero_usuario} es prohibido!")
        break #Cortamos el ciclo

    print(f"{numero_usuario} X {item} = {numero_usuario * item}")
    
else: #Python permite colocar un else que se ejecuta cuando un ciclo ha terminado
    print(f"Tabla de multiplicar del {numero_usuario} finalizada!")

"""
    ################# Tabla de multiplicar #################
    De que número quieres la tabla?: 3
    ### Tabla de multiplicar del número : 3
    3 X 1 = 3
    3 X 2 = 6
    3 X 3 = 9
    3 X 4 = 12
    3 X 5 = 15
    3 X 6 = 18
    3 X 7 = 21
    3 X 8 = 24
    3 X 9 = 27
    3 X 10 = 30
    Tabla de multiplicar del 3 finalizada!
"""

"""
    ################# Tabla de multiplicar #################
    De que número quieres la tabla?: 45
    ### Tabla de multiplicar del número : 45
    El numero 45 es prohibido!
"""



