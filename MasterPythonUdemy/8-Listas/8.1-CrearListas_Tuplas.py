"""
    LISTAS (arrays)
    Son colecciones o conjunto de datos/valores, bajo un unico nombre
    Para acceder a esos valores podemos usar un indice númerico.
"""

pelicula = "Batman"

#Definir lista
peliculas = ["Barman", "Spiderman", "El señor de los anillos"]

#Definir tupla
cantantes = ('2pac', 'Drake', 'Jennifer Lopez')

print(peliculas)
print(cantantes)

#Convertir tupla a lista
print(list(cantantes))

#Convertir un iterable 'range()' en lista
years = list(range(2020, 2050))

#Las listas pueden tener diferentes tipos de datos
listDiferentTypes = ["David", 30, 34.5, True, b"9"]

for item in listDiferentTypes:
    print(type(item))

"""
Impresiones archivo: 
['Barman', 'Spiderman', 'El señor de los anillos']
('2pac', 'Drake', 'Jennifer Lopez')
['2pac', 'Drake', 'Jennifer Lopez']
<class 'str'>
<class 'int'>
<class 'float'>
<class 'bool'>
<class 'bytes'>
"""