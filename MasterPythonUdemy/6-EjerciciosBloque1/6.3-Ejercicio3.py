"""
    Escribir un programa que muestre los cuadrados de 
    los 60 primeros numeros naturales
    Resolver con for y con while
"""

#Con while

print("########### Con while ###########")
contador = 1
while contador <= 60:
    print(f" el cuadrado de {contador} es {contador**2}")
    contador += 1

#Con for
print("########### Con for ###########")
for num in range(1,61):
    print(f" el cuadrado de {num} es {num**2}")
