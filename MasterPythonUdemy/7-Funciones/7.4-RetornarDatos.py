def calculadora(numero1, numero2, soloBasicas = False):

    suma = numero1 + numero2
    resta = numero1 - numero2
    multi = numero1 * numero2
    division = numero1 / numero2

    resultados = f"Suma = {suma}"
    resultados += "\n"
    resultados += f"Resta = {resta}"
    resultados += "\n"

    if soloBasicas == False:
        resultados += f"Multiplicación = {multi}"
        resultados += "\n"
        resultados += f"División = {division}"
        resultados += "\n"
    
    return resultados


print(calculadora(4, 3))

"""
    Suma = 7
    Resta = 1
    Multiplicación = 12
    División = 1.3333333333333333
"""