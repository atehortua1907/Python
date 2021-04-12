""" 
    Crear un script que tenga 4 variables, una lista, un string,
    entero y booleano y que imprima un mensaje
    segun el tipo de dato de cada variable, Usar funciones

"""

listaTipoVariables = [["Variable", "tipo", "lista"], "Variable tipo String", 4, False]

def imprimirValorVariable(variable):
    print(f"El valor de la variable es = '{variable}'")

def imprimirTipoVariable(variable):
    print(f"El tipo de la variable es = '{type(variable)}'")

print("\n")
for index, variable in enumerate(listaTipoVariables):
    print(f"******* Elemento número {index + 1} *******")
    imprimirValorVariable(variable)
    imprimirTipoVariable(variable)
    print("\n")

"""
    Impresión archivo:
    
    ******* Elemento número 1 *******
    El valor de la variable es = '['Variable', 'tipo', 'lista']'
    El tipo de la variable es = '<class 'list'>'


    ******* Elemento número 2 *******
    El valor de la variable es = 'Variable tipo String'
    El tipo de la variable es = '<class 'str'>'


    ******* Elemento número 3 *******
    El valor de la variable es = '4'
    El tipo de la variable es = '<class 'int'>'


    ******* Elemento número 4 *******
    El valor de la variable es = 'False'
    El tipo de la variable es = '<class 'bool'>'
"""