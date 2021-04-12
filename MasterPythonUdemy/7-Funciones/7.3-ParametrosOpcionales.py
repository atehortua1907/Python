def getEmpleado(nombre, dni = None):
    print("EMPLEADO")
    print(f"Nombre: {nombre}")

    if dni:
        print(f"DNI: {dni}")

getEmpleado("David")