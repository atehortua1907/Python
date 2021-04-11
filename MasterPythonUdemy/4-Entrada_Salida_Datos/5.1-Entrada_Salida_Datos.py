#Entrada de datos en consola
nombre = input("Cuál es tú nombre?: ")
edad = input("¿Cual es tú edad?: ")

"""
  Todas las entradas son cadenas, 
  hay que convertir los datos según la necesidad  
"""
#Salida de datos 'print()'
print(f"Bienvenido {nombre}!")
print(f"Cumpliras {int(edad) + 1} años el próximo año")