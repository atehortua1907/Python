"""
def muestraNombres(nombre, edad):
    print(f"Tu nombre es: {nombre}")

    if edad > 18:
        print("Y eres mayor de edad")


nombre = input("Introduce tu nombre ")
edad = int(input("Digita tú edad "))

muestraNombres(nombre, edad)
"""

print("########## EJEMPLO 2 ##########")

def tabla(numero):
    print(f"Tala de multiplicar del número: {numero}")

    for num in range(1,11):
        print(f"{numero} X {num} = {numero * num}")

for num in range(1,11):
    print("\n")
    tabla(num)


