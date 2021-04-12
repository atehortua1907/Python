peliculas = ['Batman', 'Spiderman', 'El señor de los anillos', 'Titanic', 'Masacre en texas', 'Saw', 'El lobo de wall street']
numeros = [4, 6, 77, 1, 55, 0, 3]

#Ordenar
print(numeros)
numeros.sort()
print(numeros)

print(peliculas)

#Eliminar elementos por indices
peliculas.pop(2)

#Eliminar por nombre
peliculas.remove('Spiderman')
print(peliculas)

#Colocar los elmentos de atras para adelante
print(numeros)
numeros.reverse()
print(numeros)

#Buscar dentro de una lista
print('Titanic' in peliculas)

#Contar elementos
print(len(peliculas))

#Contar cuantas veces esta un elemento
print(peliculas.count('Batman'))

#Conseguir un indice
print(peliculas.index('Saw'))

#Unir listas
peliculas.extend(numeros)
print(peliculas)

"""
Impresiones archivo: 
[4, 6, 77, 1, 55, 0, 3]
[0, 1, 3, 4, 6, 55, 77]
['Batman', 'Spiderman', 'El señor de los anillos', 'Titanic', 'Masacre en texas', 'Saw', 'El lobo de wall street']
['Batman', 'Titanic', 'Masacre en texas', 'Saw', 'El lobo de wall street']
[0, 1, 3, 4, 6, 55, 77]
[77, 55, 6, 4, 3, 1, 0]
True
5
1
3
['Batman', 'Titanic', 'Masacre en texas', 'Saw', 'El lobo de wall street', 77, 55, 6, 4, 3, 1, 0]
"""