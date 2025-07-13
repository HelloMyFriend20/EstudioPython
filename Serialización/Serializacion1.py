#Veremos como serializar colecciones y objetos.

#La serialización consiste en guardar en ficheros externos colecciones, diccionarios u objetos codificados en código binario
#Esto sirve para distribuir cosas por internet de maneras más sencillas.

#Se requiere de la biblioteca pickle.
#Metodo dump(): Realiza un volcado de datos al fichero binario externo
#Metodo load(): Realiza una carga de los datos del fichero binario externo.

#Importamos la libreria
import pickle
lista_nombres = ["Pedro","Ana","Maria","Isabel"]

#Crearemos un fichero externo con acceso de escritura binaria.
fichero_binario = open("Lista Nombres","wb")#Para escritura binaria seria "wb".

#Con el método dump realizamos un volcado de los datos guardados en la lista_nombres
pickle.dump(lista_nombres, fichero_binario)#Requiere 2 argumentos, la información que queremos volcar, y la ubicación donde realizaremos el volcado.

fichero_binario.close() #Todo queda guardado en el fichero.

del (fichero_binario) #Borramos el fichero de la memoria.


#Para leer la informacion guardada en el fichero:
nuevo_fichero = open("lista Nombres", "rb") #Lectura binaria.

lista = pickle.load(nuevo_fichero) #Cargamos la informacion en la variable

print(lista)

nuevo_fichero.close()
del (nuevo_fichero)