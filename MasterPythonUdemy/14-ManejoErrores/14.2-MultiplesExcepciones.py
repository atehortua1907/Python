try:
    numero = int(input("Numero para elevarlo al cuadrado "))
    calculoMalo = 4/0
    print("El cuadrado es: "+numero**2)    
except TypeError:
    print("Debes convertir tus cadenas a enteros en el código.")
except ValueError:
    print("Introduce un número correcto")
except Exception as e:
    print(type(e))
    print("Ha ocurrido un error general, el nombre de la excepcion es ", type(e).__name__)

"""
    Impresiones archivo
    Numero para elevarlo al cuadrado 4
    <class 'ZeroDivisionError'>
    Ha ocurrido un error general, el nombre de la excepcion es  ZeroDivisionError
"""
