"""
  Proyecto Python y MySql
  -Abrir asistente
  -Login o registro
  -Si elegimos registro, creará un usuario en la bd
  -Crear nota, mostrar notas, borrarlas  
"""
from Usuarios import acciones

print(
  """
    Acciones disponibles:
      - Registro
      - Login
  """
)

hazEl = acciones.Acciones()
accion = input("¿Que quieres hacer?")

if accion == "Registro":
  hazEl.registro()
elif accion == "Login":
  hazEl.login()



