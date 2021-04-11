nombre = "David"
ciudad = "Itagui"
continente = "Sur-America"
edad = 55
mayoria_edad = 18

if edad >= mayoria_edad:
    print(f"{nombre} No es mayor de edad")

    if continente != "Sur-America":
        print(f"{nombre} No es Suramericano")
    else:
        print(f"Es suramericano y de la ciudad {ciudad}")
else:
    print(f"{nombre} No es mayor de edad")