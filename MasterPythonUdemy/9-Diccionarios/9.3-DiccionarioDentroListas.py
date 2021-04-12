contactos = [
    {
        "nombre": "David",
        "apellidos": "Atehortua Alvarez",
        "profesion": "Ingeniero Sistemas"
    },  
    {
        "nombre": "Jessica",
        "apellidos": "Atehortua Alvarez",
        "profesion": "Contadora"
    },
    {
        "nombre": "Gohan",
        "apellidos": "Atehortua Gallego",
        "profesion": "Astrofisico"
    }
]

contactos[2]["nombre"] = "Gohan David"
print(contactos[2]["nombre"])

print("\n")
print("######## LISTA DE CONTACTOS ########")

for contacto in contactos:
    print(f"Nombre Contacto: {contacto['nombre']}")
    print(f"Apellidos Contacto: {contacto['apellidos']}")
    print(f"Profesion Contacto: {contacto['profesion']}")
    print("\n")

"""
Impresiones archivo:
Gohan David


######## LISTA DE CONTACTOS ########
Nombre Contacto: David
Apellidos Contacto: Atehortua Alvarez
Profesion Contacto: Ingeniero Sistemas


Nombre Contacto: Jessica
Apellidos Contacto: Atehortua Alvarez
Profesion Contacto: Contadora


Nombre Contacto: Gohan David
Apellidos Contacto: Atehortua Gallego
Profesion Contacto: Astrofisico
"""