"""
    Hacer un programa que muestre todos los numeros impares 
    entre dos numeros que diga el usuario
"""

num1 = int(input("Digite el número inicial: "))
num2 = int(input("Digite el número final: "))

for num in range(num1, num2 + 1):
    if num % 2 == 0:
        continue
    print(num)