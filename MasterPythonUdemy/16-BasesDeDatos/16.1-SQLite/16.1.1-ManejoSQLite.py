#SQLite nos almacena una base de datos en un archivo
import sqlite3

#Abrir conexion
conexion = sqlite3.connect('pruebas.db')

#Crear cursor
cursor = conexion.cursor()

#Crear tabla
cursor.execute("""
CREATE TABLE IF NOT EXISTS productos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo varchar(255),
    descripcion text, 
    precio int(255)
);
""")

#Guardar cambios
conexion.commit()

#Insertar datos (id null porque es incremental)
cursor.execute("INSERT INTO productos VALUES(null, 'Primer producto', 'Descripción', 550)")
conexion.commit()

#Lectura de datos
def getProductos(where = ""):
    cursor.execute(f"SELECT * FROM productos {where}")
    productos = cursor.fetchall() #Traer todos los registros
    print(productos) # [(1, 'Primer producto', 'Descripción', 550)]

    print(f"\n Todos los productos {where}: \n")
    for producto in productos:
        print("ID: ", producto[0])
        print("Titulo: ", producto[1])
        print("Descripción: ", producto[2])
        print("Precio: ", producto[3])
        print("\n")

getProductos()

cursor.execute("SELECT titulo FROM productos")
producto = cursor.fetchone() #Traer el primer registro
print(producto)

"""
    Impresion archivo:
    [(1, 'Primer producto', 'Descripción', 550), (2, 'Primer producto', 'Descripción', 550)]

    Todos los productos:

    Titulo:  Primer producto
    Descripción:  Descripción
    Precio:  550


    Titulo:  Primer producto
    Descripción:  Descripción
    Precio:  550


    ('Primer producto',)
"""
#Borrar registros
cursor.execute("DELETE FROM productos")
conexion.commit()

#Insertar muchos registros de una sola vez
productos = [
    ("Ordenador portatil", "Buen PC", 700),
    ("Telefono movil", "Buen Telefono", 140),
    ("Placa Base", "Buena Table", 80),
    ("Tablet 15", "Buena tablet", 300),
]
cursor.executemany("INSERT INTO productos VALUES (null,?,?,?)", productos)
conexion.commit()
getProductos()

#Listar con condicional where
getProductos("WHERE precio >= 300")

#Update con condición
cursor.execute("UPDATE productos SET precio = 678 WHERE precio=80")
getProductos("WHERE precio == 678")

#Cerrar conexion
conexion.close()

"""
    Impresion archivo
    [(16, 'Ordenador portatil', 'Buen PC', 700), (17, 'Telefono movil', 'Buen Telefono', 140), (18, 'Placa Base', 'Buena Table', 80), (19, 'Tablet 15', 'Buena tablet', 300), (20, 'Primer producto', 'Descripción', 550)]

    Todos los productos :

    ID:  16
    Titulo:  Ordenador portatil
    Descripción:  Buen PC
    Precio:  700


    ID:  17
    Titulo:  Telefono movil
    Descripción:  Buen Telefono
    Precio:  140


    ID:  18
    Titulo:  Placa Base
    Descripción:  Buena Table
    Precio:  80


    ID:  19
    Titulo:  Tablet 15
    Descripción:  Buena tablet
    Precio:  300


    ID:  20
    Titulo:  Primer producto
    Descripción:  Descripción
    Precio:  550


    ('Ordenador portatil',)
    [(21, 'Ordenador portatil', 'Buen PC', 700), (22, 'Telefono movil', 'Buen Telefono', 140), (23, 'Placa Base', 'Buena Table', 80), (24, 'Tablet 15', 'Buena tablet', 300)]

    Todos los productos :

    ID:  21
    Titulo:  Ordenador portatil
    Descripción:  Buen PC
    Precio:  700


    ID:  22
    Titulo:  Telefono movil
    Descripción:  Buen Telefono
    Precio:  140


    ID:  23
    Titulo:  Placa Base
    Descripción:  Buena Table
    Precio:  80


    ID:  24
    Titulo:  Tablet 15
    Descripción:  Buena tablet
    Precio:  300


    [(21, 'Ordenador portatil', 'Buen PC', 700), (24, 'Tablet 15', 'Buena tablet', 300)]

    Todos los productos WHERE precio >= 300:

    ID:  21
    Titulo:  Ordenador portatil
    Descripción:  Buen PC
    Precio:  700


    ID:  24
    Titulo:  Tablet 15
    Descripción:  Buena tablet
    Precio:  300


    [(23, 'Placa Base', 'Buena Table', 678)]

    Todos los productos WHERE precio == 678:

    ID:  23
    Titulo:  Placa Base
    Descripción:  Buena Table
    Precio:  678
"""