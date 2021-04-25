"""
    ¿Cuanto es el X por ciento de X numero?
    ejemplo 20% de 150
"""

porcentaje = int(input("Digite el porcentaje a calcular: "))
num = int(input("Digite el número: "))

print(f"El {porcentaje}% de {num} es : {porcentaje/100*num}")