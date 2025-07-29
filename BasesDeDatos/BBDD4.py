#Clausula UNIQUE y operaciones CRUD.

import sqlite3

miConexion = sqlite3.connect("NuevoEjemplo")
miCursor = miConexion.cursor()

miCursor.execute('''
    CREATE TABLE PRODUCTOS (
    ID_ARTICULO INTEGER PRIMARY KEY AUTOINCREMENT,
    NOMBRE_ARTICULO VARCHAR(50) UNIQUE,
    PRECIO INTEGER,
    SECCION VARCHAR(20));
''')

productos = [
    ("Pelota", 20, "Juguetería"),
    ("Pantalón", 15, "Confección"),
    ("Destornillador", 25, "Ferretería"),
    ("Jarrón", 45, "Cerámica"),
    ("Pantalones", 35, "Confección")
]

miCursor.executemany("INSERT INTO PRODUCTOS VALUES (NULL,?,?,?)", productos)

miCursor.execute("SELECT * FROM PRODUCTOS WHERE SECCION= 'Confección'")
impresion = miCursor.fetchall()
for x in impresion:
    print(x)
print(" ")

miCursor.execute("UPDATE PRODUCTOS SET PRECIO=35 WHERE NOMBRE_ARTICULO='Pelota'")
miCursor.execute("SELECT * FROM PRODUCTOS")
ejemplo = miCursor.fetchall()
for x in ejemplo:
    print(x)
print(" ")

miCursor.execute("DELETE FROM PRODUCTOS WHERE ID_ARTICULO=5")
miCursor.execute("SELECT * FROM PRODUCTOS")
xd = miCursor.fetchall()
for i in xd:
    print(i)

miConexion.commit()
miConexion.close()