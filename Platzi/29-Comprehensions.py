#Comprehensions son constructos que nos permiten generar secuencias a
#partir de otras secuencias

#List comprehension
lista_de_numeros = list(range(100))
print(lista_de_numeros)

pares = [numero for numero in lista_de_numeros if numero % 2 == 0]
print(pares)

#Dictionary comprehension
student_uid = [1,2,3]
students = ['Juan', 'Jose', 'Larsen']

#Aquí no hay condición, las condiciones son opcionales:
students_with_uid = {uid: student for uid, student in zip(student_uid, students)} 
#Convertimos a un diccionario las dos listas:
print(students_with_uid)

#Set comprehension
import random
random_numbers = []
for i in range(10):
    random_numbers.append(random.randint(1,3))

print(random_numbers) #Aquí vamos a ver los números repetidos

#Un conjunto(set) no permite repetidos, por defecto los elimina
non_repeated= {number for number in random_numbers}
print(non_repeated)

