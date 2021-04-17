import Usuarios.usuario as model
import Notas.acciones as notas

class Acciones:

    def registro(self):
        print("\nOk!! vamor a registrarte en el sistema...")
        nombre = input("¿Cuál es tú nombre?: ")
        apellidos = input("¿Cuales son tús apellidos?: ")
        email = input("Introduce tú email: ")
        password = input("Introduce tú contraseña: ")

        usuario = model.Usuario(nombre, apellidos, email, password)
        registro = usuario.registrar()

        if registro[0] >= 1:
            print(f"\nPerfecto {registro[1].nombre} te has registrado con el email {registro[1].email}")
        else:
            print("\nNo te has registrado correctamente")

    def login(self):
        print("\nVale! Identificate en el sistema...")
        email = input("Introduce tú email: ")
        password = input("Introduce tú contraseña: ")

        usuario = model.Usuario('', '', email, password)
        login = usuario.identificar() 

        try:
            if email == login[3]:
                print(f"Bienvenido {login[1]}, te has registrado correctamente!")
                self.proximasAcciones(login)
        except Exception as e:
            print(f"Login incorrecto, intentalo mas tarde {e}")

    
    def proximasAcciones(self, usuario):

        print(
            """
                Acciones disponibles:
                -Crear nota (crear)
                -Mostrar tus notas (mostrar)
                -Eliminar nota (eliminar)
                -Salir (salir)
            """
        )

        accion = input("¿Que quieres hacer?: ")

        if accion == "crear":
            print("vamor a crear")
            notas.Acciones().crear(usuario)
        elif accion == "mostrar":
            print("vamor a mostrar")
            notas.Acciones().mostrar(usuario)
        elif accion == "eliminar":
            print("vamor a eliminar")
            notas.Acciones().borrar(usuario)
        elif accion == "salir":
            print(f"Ok {usuario[1]}, hasta pronto!")
            exit()
        
        self.proximasAcciones(usuario)