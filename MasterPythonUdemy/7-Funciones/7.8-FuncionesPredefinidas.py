nombre = "David"

#Función print()
print(nombre)

#Función type()
print(type(nombre))

#Función 'isinstance(var, tipe)' para detectar el tipado, devuelve booleano
if isinstance(nombre, int):
    print(f"la variable nombre es entero")

#Función para limpriar espacios de un string 'str.strip()'
frase = "     frase con espacios al ppio y al final    "
print(frase.strip())

#Palabra reservada para eliminar variables 'del'
year = 2022
print(year)
del year
#print(year) #produce un error porque ya no existe esta variable

#Función que devuelve un entero con el numero de caracteres
print(f"El numero de caracteres de la variable frase es {len(frase)}")

#Podemos entonces comprobar si esta vacio o no
if len(frase) == 0:
    print("vacio")

#Encontrar caracteres en un string, devuelve la posición en la que empieza la palabra y si no la encuentra devuelve -1
print(frase.find("espacios"))

#Reemplazar palabras en un string
nueva_frase = frase.replace("espacios", "vacios")
print(nueva_frase)

#Mayusculas y minusculas
print(frase.lower()) #minusculas
print(frase.upper()) #mayusculas

"""
    Impresion del archivo:
    David
    <class 'str'>
    frase con espacios al ppio y al final
    2022
    El numero de caracteres de la variable frase es 46
    15
        frase con vacios al ppio y al final
        frase con espacios al ppio y al final
        FRASE CON ESPACIOS AL PPIO Y AL FINAL
"""