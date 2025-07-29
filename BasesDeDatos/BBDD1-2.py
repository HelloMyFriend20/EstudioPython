#Python es capaz de manipular la información de diferentes sistemas gestores de bases de datos.
#No solo relacionales sí nó también bd orientadas a objetos.

import sqlite3 #Importamos la libreria para la base de datos.

miConexion = sqlite3.connect("PythonBD") #Le declaramos una variable a la conexión con la base de datos

#Al ejecutar el programa con la variable "miConexion" habremos creado un archivo con el nombre que indicamos dentro de comillas
#El cual hará referencia a una base de datos

#Para crear una tabla tendremos que crear un cursor:
miCursor = miConexion.cursor() #Asi creamos el cursor o puntero.

#Con esta linea podemos agregar una tabla a la BD
#miCursor.execute("CREATE TABLE PRODUCTOS (NOMBRE_ARTICULO VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(20));")

#Podemos usar listas y tuplas para insertar registros.
#Para insertar lotes de registros es mas comodo de esta manera.
variosProductos = [
    ("Camiseta", 10, "Deportes"),
    ("Jarron", 90, "Ceramica"),
    ("Camion", 20, "Jugueteria")
]

#Se colocan tantos ? como argumentos para llenar la tabla
miCursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?)", variosProductos)

miCursor.execute("INSERT INTO PRODUCTOS VALUES ('BALON', '15', 'Deportes')")

miCursor.execute("SELECT * FROM PRODUCTOS")
#Para ver la información del select haremos lo siguiente:
variosProductos = miCursor.fetchall() #Devuelve una lista con todos los registros de nuestra db
print(variosProductos)

#Con este ciclo veremos cada lista en orden.
for producto in variosProductos:
    print(f'Nombre articulo: {producto[0]}, precio: {producto[1]}, seccion: {producto[2]}')

#Para confirmar los cambios realizados en la tabla:
miConexion.commit()

miConexion.close() #Con este método cerramos la conexión