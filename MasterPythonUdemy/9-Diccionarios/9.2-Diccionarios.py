"""
    DICCIONARIO:
    Es un tipo de dato que almacena un conjunto de datos.
    En formato clave - valor
    Es parecido a un array asociativo o un objeto json.
"""

personas = {
    "nombre": "David",
    "apellidos": "Atehortua Alvarez",
    "profesion": "Ingeniero Sistemas"
}

print(personas)
print(personas["apellidos"])
print(type(personas))

"""
Impresión archivo:
{'nombre': 'David', 'apellidos': 'Atehortua Alvarez', 'profesion': 'Ingeniero Sistemas'}
Atehortua Alvarez
<class 'dict'>
"""