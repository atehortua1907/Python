import random

"""
Búsqueda binaria lo único que hace es tratar de encontrar
un resultado en una lista ordenada de tal manera que podamos razonar.
Si tenemos un elemento mayor que otro, podemos simplemente la mitad
de la lista cada vez.
"""

def binary_search(data, target, lowIndex, highIndex):
    if lowIndex > highIndex:
        return False

    mid = (lowIndex + highIndex) // 2 #División de enteros //

    if target == data[mid]:
        return True
    elif target < data[mid]:
        return binary_search(data, target, lowIndex, mid - 1)
    else:
        return binary_search(data, target, mid + 1, highIndex)


if __name__ == '__main__':
    data = [random.randint(0,100) for i in range(10)] #List Comprehension

data.sort() #Ordena la lista

print(data)

target = int(input('What number would you like to find?'))
found = binary_search(data, target, 0, len(data) - 1)

print(found)