"""
    Las variables globales estan fuera de las funciones y pueden ser accedidas en todo el archivo
    Las variables locales son las que se definen dentro de las funciones y solo pueden ser accedidas en el interior de las mismas,
    al menos que se hagan globales con la palabra reservada 'global'
"""

#Variable Global
variableGlobal = "Esto es una variable global"

def holaMundo():
    variableLocal = "Esto es una variable local"
    print(variableGlobal)
    print("\n")
    print(variableLocal)
    global variableLocalHechaGlobal
    variableLocalHechaGlobal = "Esto es una variable Local hecha global"
    print("\n")
    print(f"{variableLocalHechaGlobal} impresa desde el interior de una función")



#Produce error
#print(variableLocal)
"""
    Error:
    D:\Repositories\Python\MasterPythonUdemy\7-Funciones>"7.7-VariablesGlobales&Locales.py"
    Traceback (most recent call last):
    File "D:\Repositories\Python\MasterPythonUdemy\7-Funciones\7.7-VariablesGlobales&Locales.py", line 15, in <module>
        print(variableLocal)
    NameError: name 'variableLocal' is not defined
"""

#Produce error porque la función que declara la variable aun no se ha invocado
#print(f"{variableLocalHechaGlobal} impresa desde el exterior de la función 'holaMundo'")
"""
    Traceback (most recent call last):
    File "D:\Repositories\Python\MasterPythonUdemy\7-Funciones\7.7-VariablesGlobales&Locales.py", line 33, in <module>
        print(f"{variableLocalHechaGlobal} impresa desde el exterior de la función 'holaMundo'")
    NameError: name 'variableLocalHechaGlobal' is not defined
"""
holaMundo()
print(f"{variableLocalHechaGlobal} impresa desde el exterior de la función 'holaMundo'")
