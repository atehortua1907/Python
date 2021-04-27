"""
    Hacer un programa que tenga una lista de 
    8 numeros enteros y haga lo siguiente:
    - Recorrer la lista y mostrarla
    - Hacer funcion que recorra listas de numeros y devuelva un string
    - Ordenarla y mostrarla
    - Mostrar su longitud
    - Busca algun elemento (que el usuario pida por teclado)
"""

listNum = [8,3,5,1,7,2,6,4]
print("Esta es la lista: ")
for num in listNum:
    print(num)

def getStringList(lista):
    stringNum = ""
    for num in lista:
        stringNum = f"{num},{stringNum}"
    return stringNum

print("\nLista de números en string: ")
print(getStringList(listNum))

print("\nLista de números ordenada: ")
listNum.sort()
print(listNum)

print(f"La lista tiene una longitud de: {len(listNum)}")

searchElement = int(input("Ingresa un número a buscar: "))

if searchElement in listNum:
    print(f"El número {searchElement} se encuentra en la lista ")
else:
    print(f"El número {searchElement} no esta en la lista")
