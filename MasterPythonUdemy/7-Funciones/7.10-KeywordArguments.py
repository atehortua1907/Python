"""
    Es posible invocar una función enviando los parametros en un orden distinto
    a lo definido, siempre y cuando se indique el keywordArgument
    Esto puede ser útil cuando una función tiene muchos parametros y acordarse o tener
    en cuenta el orden no es necesario
"""

def obtenerNombreCompletoYPais(nombre, apellidos, pais):
    return f"{nombre} {apellidos} {pais}"

#Aquí enviamos los parametros en un orden distinto al definido
nombre_Completo = obtenerNombreCompletoYPais(pais="Colombia", apellidos="Atehortua", nombre="David")

print("El nombre completo y su pais es: ", nombre_Completo) #El nombre completo y su pais es:  David Atehortua Colombia