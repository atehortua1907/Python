"""
    Operadores Logicos:
    and     Y
    or      O
    not     NO
    !       Negación
"""

edad_minima = 18
edad_maxima = 65
edad_oficial = int(input("Digite su edad"))

#Operador logico 'and'
if edad_oficial >= 18 and edad_oficial <= 65:
    print("Esta en edad de trabajar")
else:
    print("No esta en edad de trabajar")
