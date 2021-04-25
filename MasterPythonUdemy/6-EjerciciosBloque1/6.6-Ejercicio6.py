"""
    Mostrar todas las tablas de multiplicar del 1 al 10.
    Mostrando el titulo de la tabla y luego las multiplicaciones del 1 al 10
"""

for tabla in range(1, 11):
    print(f"\n######## Tabla de multiplicar del {tabla} ########")
    for num in range(1, 11):
        print(f"{tabla} X {num} = {tabla * num}")
