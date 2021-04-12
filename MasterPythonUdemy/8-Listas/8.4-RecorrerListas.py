peliculas = ['Batman', 'Spiderman', 'El señor de los anillos', 'Titanic', 'Masacre en texas', 'Saw', 'El lobo de wall street']

for index, pelicula in enumerate(peliculas):
    print(f"Pelicula {index + 1} {pelicula}")

"""
    Pelicula 1 Batman
    Pelicula 2 Spiderman
    Pelicula 3 El señor de los anillos
    Pelicula 4 Titanic
    Pelicula 5 Masacre en texas
    Pelicula 6 Saw
    Pelicula 7 El lobo de wall street
"""

nueva_pelicula = ""
while nueva_pelicula != "parar":
    nueva_pelicula = input("Introduce una nueva pelicula: ")
    if nueva_pelicula != "parar":
        peliculas.append(nueva_pelicula)

print("****** LISTADO DE PELICULAS *****")
for pelicula in peliculas:
    print(f"Pelicula {peliculas.index(pelicula)+1} {pelicula}")
