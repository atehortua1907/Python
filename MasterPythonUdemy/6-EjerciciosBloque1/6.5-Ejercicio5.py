"""
    Hacer un programa que muestre todos los numeros entre
    dos numeros que diga el usuario
"""

num1 = int(input("Digite el número inicial: "))
num2 = int(input("Digite el número final: "))

for num in range(num1, num2 + 1):
    print(num)