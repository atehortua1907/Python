pais = input("Digite un pais")

#Operador logico or
if pais == "Mexico" or pais == "España" or pais == "Colombia":
    print(f"{pais} es un país de habla hispana!!")
else:
    print(f"{pais} no es unpaís de habla hispana :(")

#Operador logico !
if not(pais == "Mexico" or pais == "España" or pais == "Colombia"):
    print(f"{pais} no es unpaís de habla hispana :(")
else:
    print(f"{pais} es un país de habla hispana!!")

#Operador logico and y operador de comparación !=
if pais != "Mexico" and pais != "España" and pais != "Colombia"):
    print(f"{pais} no es unpaís de habla hispana :(")
else:
    print(f"{pais} es un país de habla hispana!!")

