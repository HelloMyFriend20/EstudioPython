import sqlite3

miConexion = sqlite3.connect("GestionProductos")
miCursor = miConexion.cursor()

#Crearemos una tabla productos
#La triple comilla es util para una instrucción larga y dividirla en varios renglones.
miCursor.execute('''
    CREATE TABLE PRODUCTOS (
    CODIGO_ARTICULO VARCHAR(4) PRIMARY KEY,
    NOMBRE_ARTICULO VARCHAR(50) UNIQUE,
    PRECIO INTEGER,
    SECCION VARCHAR(20));
''')

#Insertamos los datos a la tabla productos
productos = [
    ("AR01", "Pelota", 20, "Juguetería"),
    ("AR02", "Pantalón", 15, "Confección"),
    ("AR03", "Destornillador", 25, "Ferretería"),
    ("AR04", "Jarrón", 45, "Cerámica"),
]

#Para que ingrese los datos de productos
miCursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?,?)", productos)

#Si repetimos una primary key dara un error de tipo UNIQUE.
miCursor.execute("INSERT INTO PRODUCTOS VALUES ('AR05', 'Tren', 15, 'Juguetería')")

miCursor.execute("SELECT * FROM PRODUCTOS")
test = miCursor.fetchall()
for ejemplo in test:
    print(ejemplo)

miConexion.commit()
miConexion.close()