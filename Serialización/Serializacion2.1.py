import pickle

ficheroApertura = open("losCoches","rb") #Lectura de bites
misCoches = pickle.load(ficheroApertura)

ficheroApertura.close()
del ficheroApertura

for x in misCoches: #Aqui veremos los 3 objetos y su espacio en memoria
    #print(x) Asi veremos la información en memoria
    print(x.estado()) #Asi veremos el método estado

#ESTE CODIGO NO FUNCIONA
#Aunque se intente leer el archivo de losCoches no podra debido a la falta de la clase y los metodos.

#Se puede leer el archivo si se copia la clase y sus metodos.