"""
    SET es un tipo de dato para tener una colección de valores,
    pero no tiene ni indice ni orden
"""

personas = {
    "Victor",
    "Manolo",
    "Francisco"
}

personas.add("Paco")
print(personas)
personas.remove("Manolo")
print(personas)
print(type(personas))

"""
Impresiones archivo:
{'Manolo', 'Victor', 'Paco', 'Francisco'}
{'Victor', 'Paco', 'Francisco'}
<class 'set'>
"""