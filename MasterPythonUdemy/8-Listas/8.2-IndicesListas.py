peliculas = ["Batman", "Spiderman", "El señor de los anillos", "Titanic", "Masacre en texas"]
print(peliculas[2])
print(peliculas[-1]) #Item en cuenta regresiva -1 es el último
print(peliculas[1:3]) #Items entre el 1 y el 3 Sin incluir el indice final (3)
print(peliculas[2:]) #Items a partir del indice 2
peliculas[1] = "Spiderman 2"
print(peliculas[1])

"""
Impresiones archivo: 
    El señor de los anillos
    Masacre en texas
    ['Spiderman', 'El señor de los anillos']
    ['El señor de los anillos', 'Titanic', 'Masacre en texas']
    Spiderman 2
"""