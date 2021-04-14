import datetime

print(datetime.date.today())

fecha_completa = datetime.datetime.now()
print(fecha_completa)
print(fecha_completa.year)
print(fecha_completa.month)
print(fecha_completa.day)

fecha_formateada = fecha_completa.strftime("%d/%m/%Y, %H:%M:%S")
print("Mi fecha formateada: ", fecha_formateada)

print("fecha tipo unix: ", datetime.datetime.now().timestamp())

"""
    Impresiones archivo
    2021-04-13
    2021-04-13 21:23:30.843668
    2021
    4
    13
    Mi fecha formateada:  13/04/2021, 21:23:30
    fecha tipo unix:  1618367010.846682
"""