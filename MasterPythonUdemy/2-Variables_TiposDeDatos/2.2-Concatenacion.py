nombre = "Gohan"
appellidos = "Atehortua Gallego"
edad = "2 años"

#Concatenacion 1
print(nombre + " " + appellidos + " " + edad)

#Concatenacion 2
print(f"{nombre} {appellidos} {edad}")

#Concatenacion 3
print("Hola mi nombre es {} {} y mi edad es {}".format(nombre, appellidos, edad))

#pasarle a la función print los datos y ella los concatena en su interior
print(nombre, appellidos, edad)