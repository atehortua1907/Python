import MiModulo #Importando toda el modulo completo
#Para llamarlo debe usarse el nombre del modulo.[funcion]
print(MiModulo.holaMundo("David"))
print(MiModulo.calculadora(3,5))

from MiModulo import holaMundo #Importando solo una funcion del modulo
print(holaMundo("Gohan")) #No necesita el prefijo del modulo solo se invoca la función

from MiModulo import * #Para incluir todas las funciones en el contexto de este archivo
#No necesita el prefijo del modulo solo se invoca la función
print(holaMundo('Damaris'))
print(calculadora(4,2,True))

"""
    Impresiones archivo
    Hola mundo desde función propia bienvenid@ David!
    Suma = 8
    Resta = -2
    Multiplicación = 15
    División = 0.6

    Hola mundo desde función propia bienvenid@ Gohan!
    Hola mundo desde función propia bienvenid@ Damaris!
    Suma = 6
    Resta = 2
"""
