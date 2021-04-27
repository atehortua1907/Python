"""
    El programa tiene que pedir la nota de 15 alumnos y 
    sacar por pantalla cuantos han aprobado y cuantos han suspendido
"""

count = 1
perdieron = 0
while count <= 15:
    nota = int(input(f"Digite la nota del alumno {count}: "))
    if nota < 3:
        perdieron += 1
    count += 1

print(f"\nLos alumnos que perdieron la materia fueron: {perdieron}\n")
print(f"Los alumnos que aprobaron la materia fueron: {15 - perdieron}\n")