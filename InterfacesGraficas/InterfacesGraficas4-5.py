#Veremos el widget Entry, utilizado para introducir texto,

from tkinter import *

root = Tk()
root.config(bg="gray")

miFrame = Frame(root, width=1200, height=600)
miFrame.pack()
miFrame.config(bg="gray")

#Línea de código correspondiente a la función codigoBoton
minombre = StringVar() #Asi le decimos que se trata de una cadena de caracteres.

#Creamos una variable llamando a la clase entry
cuadroNombre = Entry(miFrame, textvariable=minombre) #Asocioamos cuadroNombre a la variable minombre, que a su vez se asocia a la función
#cuadroTexto.pack()
#cuadroTexto.place(x=100, y=100)
#Metodo grid() construye una grilla o tabla con tantas filas y columnas como queramos.
#Y ubicar nuestros elementos
cuadroNombre.grid(row=0, column=1) #row = 0, columna = 0
cuadroNombre.config(fg="red", justify="left") #fg = color frontal

#Crearemos 3 cuadros de texto mas
cuadroApellido = Entry(miFrame)
cuadroApellido.grid(row=1, column=1)

cuadroPassword = Entry(miFrame)
cuadroPassword.grid(row=2, column=1)
cuadroPassword.config(show="*") #Mostrara "*" en vez de las letras que coloquemos

cuadroDireccion = Entry(miFrame)
cuadroDireccion.grid(row=3, column=1)

#Actualizado de la clase 5.
textoComentario = Text(miFrame, width=30, height=5)
textoComentario.grid(row=4, column=1)

scrollbar = Scrollbar(miFrame, command=textoComentario.yview) #Asi construimos un scrollbar para textoComentario.
scrollbar.grid(row=4, column=2, sticky="nsew") #nsew hace que se adapte la barra al tamaño del texto.

textoComentario.config(yscrollcommand=scrollbar.set) #Hace que la barra vaya a donde el usuario se pare sobre el texto.


#LABELS
labelNombre = Label(miFrame, text="Nombre: ")
#nombreLabel.place(x=40, y=100)
labelNombre.grid(row=0, column=0, sticky="w", pady=10, padx=2)

labelApellido = Label(miFrame, text="Apellido: ")
labelApellido.grid(row=1, column=0, sticky="w", pady=10, padx=2)

labelPassword = Label(miFrame, text="Password: ")
labelPassword.grid(row=2, column=0, sticky="w", pady=10, padx=2)

labelDireccion = Label(miFrame, text="Dirección: ")
labelDireccion.grid(row=3, column=0, sticky="w", pady=10, padx=2)


#Actualizado de la clase 5.
comentarioLabel = Label(miFrame, text="Comentarios: ")
comentarioLabel.grid(row=4, column=0, sticky="w", pady=10, padx=2)

#Intefaces graficas 5

#Veremos los widgets Text y Button
#El text servirá para ingresar texto largo.
#El button son botones para poder interactuar con la interfaz.

def codigoBoton():
    minombre.set("Juan") #Usamos set para establecer información a una variable
    #Con get() podemos obtener información de una variable.

#Botones
botonEnvio = Button(root, text="Enviar", command=codigoBoton) #Llamamos a la función codigoBoton para el botón
botonEnvio.pack()

root.mainloop()
