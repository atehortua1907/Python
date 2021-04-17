import Notas.nota as modelo

class Acciones:

    def crear(self, usuario):
        print(f"Ok {usuario[1]}!! Vamos a crear una nota nueva...")
        titulo = input("Introduce el titulo de tu nota: ")
        descripcion = input("Introduce el contenido de tu nota:")

        nota = modelo.Nota(usuario[0], titulo, descripcion)
        guardar = nota.guardar()

        if guardar[0] >= 1:
            print(f"\nPerfecto has guardado la nota: {nota.titulo}")
        else:
            print(f"\n {usuario[1]} no se logró guardar la nota")

    
    def mostrar(self, usuario):
        print(f"\nVale {usuario[1]}!! Aquí tienes tus notas: ")

        nota = modelo.Nota(usuario[0])
        notas = nota.listar()
        for nota in notas:
            print("\n******************")
            print(nota[2])
            print(nota[3])
            print("******************")

    def borrar(self, usuario):
        print(f"\ok {usuario[1]}!! Vamos a borrar notas")

        titulo = input("Introduce el titulo de la nota a borrar: ")
        nota = modelo.Nota(usuario[0], titulo)
        eliminar = nota.eliminar()

        if eliminar[0] > 0:
            print(f"Hemos borrado la nota: {nota.titulo}")
        else:
            print("No hemos borrado tu nota")

