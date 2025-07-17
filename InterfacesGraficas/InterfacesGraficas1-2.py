#Las interfaces gráficas son ventanas con las cuales los usuarios interactúan
#Son intermediaros entre el programa que se está ejecutando y sus usuarios

#Se componen de ventanas las cuales tienen dentro un frame.
#Los frames a su vez tienen dentro widgets

from tkinter import *

raiz = Tk()
raiz.title("Programa en Python") #Coloca un titulo en la ventana
raiz.resizable(True,True) #El primero es width, el segundo height, con 0,0 no lo dejamos redimensionar
#También podemos colocar 1,1 si se redimensiona.
raiz.iconbitmap("icono.ico") #Cambio el icono de la ventana con una imagen que tengamos previamente guardada.
raiz.geometry("1024x600") #La ventana abre según la medida que le demos.
raiz.config(bg="black")

#Creacion de un frame
miFrame = Frame() #Le declaramos a la variable miFrame que sea un Frame xd
miFrame.pack(side="top", anchor="n") #Empaquetamos el frame, el top ancla el frame a la parte superior
#El anchor acompaña al side según "n" = norte, south, west, east. Usando puntos cardinales
#Igualmente se puede usar: left, right, bottom
miFrame.pack(fill="y",expand=True) #Redimensiona verticalmente.
#Se puede utilizar "y" para vertical "x" para horizontal y el "both" para ambos.
miFrame.config(bg="gray") #Le declaramos un color al frame
miFrame.config(width="800",height="600") #Cambiamos las medidas
miFrame.config(relief="groove") #Esto da un borde
miFrame.config(bd=35) #Da el tamaño a un borde
miFrame.config(cursor="pirate") #Cambia el cursor.

#El mainloop() siempre debe estar al final
raiz.mainloop() #Con estas instrucciones creamos la ventana.

#Para que no nos abra la consola tenemos que guardar nuestro archivo con extension .pyw
#La "w" de windows