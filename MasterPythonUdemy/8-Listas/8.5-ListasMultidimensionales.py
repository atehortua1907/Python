print("############ Listado de contactos ############")

contactos = [
    [
        'Antonio',
        'antonio@antonio.com'
    ],
    [
        'Luis',
        'luis@luis.com'
    ],
    [
        'Salvador',
        'salvador@salvador.com'
    ]
]

#Para acceder al email de salvador
emailSalvador = contactos[2][1]
print(emailSalvador)

for contacto in contactos:
    for index, datos in enumerate(contacto):
        if index == 0:
            print(f"Nombre: {datos}")
        else:
            print(f"Email: {datos}")
    print("\n")


"""
    Impresiones archivo:
    ############ Listado de contactos ############
    salvador@salvador.com
    Nombre: Antonio
    Email: antonio@antonio.com


    Nombre: Luis
    Email: luis@luis.com


    Nombre: Salvador
    Email: salvador@salvador.com
"""