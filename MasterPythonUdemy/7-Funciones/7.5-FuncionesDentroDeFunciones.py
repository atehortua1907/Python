def getNombre(nombre):
    return f"El nombre es {nombre}"

def getApellidos(apellidos):
    return f"Los appellidos son {apellidos}"


print(getNombre("David"))
print(getApellidos("Atehortua"))

def getNombreCompleto(nombre, appellidos):
    return f"{getNombre(nombre)} y {getApellidos(appellidos)}"

print(getNombreCompleto("David", "Atehortua"))