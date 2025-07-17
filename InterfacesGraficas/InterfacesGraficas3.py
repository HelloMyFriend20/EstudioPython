#Labels: Widgets usados para mostrar texto o imágenes.
#No se puede interactuar con ellos.
#Sintaxis: variable = Label(contenedor, opciones)

from tkinter import *
from PIL import Image, ImageTk #Para usar imágenes de diferentes formatos, importamos desde Pillow

root = Tk()
miFrame = Frame(root, width=800,height=600)
miFrame.pack()

miLabel = Label(miFrame,text="Hace pruebas de texto con un label", fg="red", font=("calibri",(20)))
#Dejamos miFrame como un contenedor padre
miLabel.place(x=200,y=100)
#Nos permite ubicar el texto en cualquier lugar dentro de la interfaz gráfica mediante unas coordenadas x, y

#Para utilizar imágenes podemos usar otras librerias, por defecto solo deja 2 formatos.
#miImagen = PhotoImage(file="BackgroundImage.jpg") Opción por defecto
#Label(miFrame, image=miImagen).place(x=100,y=200)
#Opcion usado Pillow:
miImagen = (Image.open("BackgroundImage.jpg"))
miImagen = miImagen.resize((600,250)) #Declaramos la altura y anchura de la imagen
imagen_tk = ImageTk.PhotoImage(miImagen) #Convertimos la imagen para Tkinter
# Mostrar la imagen en un Label
label_imagen = Label(miFrame, image=imagen_tk)
label_imagen.place(x=100, y=200)
# IMPORTANTE: mantener referencia a la imagen para que no se borre de memoria
label_imagen.image = imagen_tk

root.mainloop()