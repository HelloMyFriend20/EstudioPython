import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="PruebaPython"
)

if conexion.is_connected():
    print("Se ha echo una conexion exitosa a la base de datos")
else:
    print("Conexion no exitosa")