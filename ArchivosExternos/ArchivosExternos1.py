#Usaremos el módulo estandar io (Se recomienda mirar documentación)

#El principal objetivo es la persistencia de datos, es decir la posibilidad de guardar los datos de nuestra aplicación python para que no se pierda
#A la hora de almacenar datos podemos guardarlo en archivos externos o guardar la información en base de datos
#Al guardar en archivos externos tenemos: Archivos binarios, de texto plano y muchas subcategorias.

#Fases para guardar información en archivos externos
#Creacion -> Apertura -> Manipulación -> Cierre

from io import open
#Open se usa para abrir un archivo externo

archivo_texto = open("archivo.txt","w") #La w es de escritura (write), al no existir "archivo.txt" el método open() lo creara.
#Open pedirá 2 cosas
#El archivo por abrir
#El modo en que abriremos el archivo (lectura, escritura, append (para agregar información al archivo))

frase = "Estupendo dia para estudiar python\n el Jueves"
archivo_texto.write(frase) #Esto agregará lo que contiene frase al archivo.txt

archivo_texto.close() #Después de manipular el archivo hay que cerrarlo.
#Al decir cerrar nos referimos a cerrar el archivo en memoria que hemos ejecutado desde python.

archivo_texto = open("archivo.txt","r")
texto = archivo_texto.read() #Leera lo hay dentro del archivo y lo almacené en la variable
archivo_texto.close()
print(texto) #Nos mostrará lo que hay en el archivo de texto guardado en la variable.

#También existe el metodo realines()
#El cual hara que se guarde el texto del archivo en una variable en forma de lista
archivo_texto = open("archivo.txt","r")
lineas_texto = archivo_texto.readlines()
archivo_texto.close()

print(lineas_texto[0]) #Podemos acceder a un item específico de la lista con un índice.

#Vamos a agregar una tercera linea de texto
archivo_texto = open("archivo.txt","a") #Abrimos el archivo en modo append.
archivo_texto.write("\nSiempre es una buena ocasión para estudiar python. ")
archivo_texto.close()




