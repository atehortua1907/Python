import mysql.connector

#Conexión

database = mysql.connector.connect(
    host = 'localhost',
    database = 'master_python_Udemy',
    user = 'root',
    passwd = ""
)

cursor = database.cursor(buffered=True)

cursor.execute("CREATE DATABASE IF NOT EXISTS master_python_Udemy")

cursor.execute("SHOW DATABASES")

for bd  in cursor:
    print(bd)

"""
    Impresión archivo:
    ('information_schema',)
    ('master_python_udemy',) --> nuestra base de datos recien creada
    ('mysql',)
    ('performance_schema',)
    ('sys',)
"""

#Crear tablas
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS vehiculos(
        id int(10) auto_increment not null,
        marca varchar(40) not null,
        modelo varchar(40) not null,
        precio float(10,2) not null,
        CONSTRAINT pf_vehiculo PRIMARY KEY(id)
    )
    """
)

cursor.execute("SHOW TABLES")

for table in cursor:
    print(table) # ('vehiculos',)

#Inserta datos en tablas
#cursor.execute("INSERT INTO vehiculos VALUES(null, 'opel', 'astra', 435.4)")
#database.commit()

#Insertar masivamente
coches = [
    ('Seat', 'Ibiza', 5000),
    ('Renaul', 'Clio', 15000),
    ('Citroen', 'Saxo', 2000),
    ('Mercedes', 'Clase C', 35000),
]

#cursor.executemany("INSERT INTO vehiculos VALUES(null, %s, %s, %s)", coches)
#database.commit()

#Leer datos
def getVehiculosFromDatabase(where = ""):

    cursor.execute(f"SELECT * FROM vehiculos {where}")
    result = cursor.fetchall() #Traer
    print(f"------- TODOS MIS COCHES {where}-------")
    for coche in result:
        print(coche)

#SELECT Y WHERE 
getVehiculosFromDatabase("WHERE precio <= 5000 AND marca = 'seat'")

"""
    Impresiones
    ------- TODOS MIS COCHES WHERE precio <= 5000 AND marca = 'seat'-------
    (4, 'Seat', 'Ibiza', 5000.0)
    (9, 'Seat', 'Ibiza', 5000.0)
    (14, 'Seat', 'Ibiza', 5000.0)
"""

#Traer el primer elemento
cursor.execute("SELECT * FROM vehiculos")
print(cursor.fetchone()) #(1, 'opel', 'astra', 435.4)

#Borrar registros
cursor.execute("DELETE FROM vehiculos WHERE marca = 'Renaul'")
database.commit()
print(cursor.rowcount, " registros borrados!") #3  registros borrados!

#Actualizar registros
cursor.execute("UPDATE vehiculos SET modelo = 'Leon' WHERE marca = 'seat'")
database.commit()
print(cursor.rowcount, " registros actualizados!") #3  registros actualizados!

