#TUPLAS

a = 1,2,3 #Tuple sin parentesis
print(a)
print(type(a))

a = (1,2,3) #Tuple con parentesis (recomendado)
print(a)
print(type(a))
dir(a) #solo hay dos metodos públicos
#count e index
a.count(1) #devuelve el número de veces que se repite el valor enviado por parametro
a.index(1) #devuelve la posición del elemento enviado por parametro
a[0] = 1 #esto no se puede modificar, caracteristica de las tuplas

#SETS O CONJUNTOS

b = set([1,2,3]) #con el keyword set
c = {3,4,5}  #con llaves, puede ser confuso
print(type(b))
print(type(c))

b[1] #esto no es posible, no podemos acceder a un indice, en conjuntos no existe
b.add(3) #no lo agrega, ya que no se pueden elementos repetidos
b.add(20) #este si lo agrega, ya que no existe previamente

#**** Operaciones con sets ****
b.intersection(c) #elementos iguales entre b y c
b.union(c) #todos los elementos de b y c, sin repetirse
b.difference(c) #lo que hay en b que no este en c
b.remove(20) #para quitar elementos

dir(b) #ver los metodos