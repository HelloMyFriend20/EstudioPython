#Veremos como manejar un puntero dentro de un fichero de texto.

from io import open
#Podemos importar también del archivo anterior.
#from ArchivosExternos import ArchivosExternos1

archivo_texto = open("archivo.txt","r")
print(archivo_texto.read()) #read() realiza una lectura hasta donde le indiquemos
#Si se deja por defecto, es decir vació, leerá el texto dejando el puntero al final.

#En python podemos desplazar el puntero del archivo.
#Con el primer print el cursor quedaría al final del texto
#Al hacer otro print no imprime nada, ya que el cursor se encuentra al final del texto.
print(archivo_texto.read())

#¿Como modificamos la posición del puntero?
#Metodo seek() posiciona el puntero en el lugar que especificamos
archivo_texto.seek(0)
print(archivo_texto.read(11))

archivo_texto.seek(11) #Colocará el puntero en el carácter 11 del texto.
print(archivo_texto.read())

#Otra manera:
archivo_texto.seek(len(archivo_texto.read())/2) #Imprime la mitad de lo que seria el archivo de texto.
print(archivo_texto.read())

#Podemos usar tambien readline() para leer linea por linea
archivo_texto.seek(len(archivo_texto.readline())/2)
print(archivo_texto.read())
print("----- FIN ------")
archivo_texto.close()

archivo_texto = open("archivo.txt","r+") #Lectura y escritura.

archivo_texto.write("Nuevo comienzo del texto al") #Sobrescribe desde la primera línea lo que había anteriormente.

archivo_texto.seek(0)
print(archivo_texto.read())

archivo_texto.seek(0)
print(archivo_texto.readlines()) #Imprime por lineas representados por sus saltos de lineas.
print(" ")


#Como agregar una linea en mitad del documento
archivo_texto.seek(0)
lista_texto = archivo_texto.readlines()
lista_texto[1] = "Modificamos la linea secundaria del texto\n"

archivo_texto.seek(0)
archivo_texto.writelines(lista_texto)

archivo_texto.seek(0)
print(archivo_texto.read())

archivo_texto.close()


