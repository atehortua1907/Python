#Capturar excepciones y manejar errores en código
#Susceptibe a fallos/errores

try:
    nombre = input("¿Cual es tú nombre?: ")

    if nombre:
        nombre_usuario = "El nombre es " + nombre

    print(nombre_usuario)
except:
    print("Ha ocurrido un error, mete bien el nombre pendejo")
else:
    print("puedo meter un else si no hay error... todo anda bien, sin errores")
finally:
    print("Fin de la iteración, aquí llegamos haya o no errores")