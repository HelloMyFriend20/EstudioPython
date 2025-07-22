#Realizacion de una calculadora.

from tkinter import *

raiz = Tk()

miFrame = Frame(raiz)
miFrame.pack()

operacion = ""
reset_pantalla = False
resultado = 0

# ----- PANTALLA -----
numeroPantalla = StringVar()
pantalla = Entry(miFrame, textvariable=numeroPantalla)
pantalla.grid(row=1, column=1, padx=10, pady=10, columnspan=4) #columspan = hace que la pantalla ocupe 4 columnas.
pantalla.config(background="black", fg="#03f943", justify="right")

# ------ FUNCIONES ------
def numeroPulsado(num):
    global operacion
    global reset_pantalla

    if reset_pantalla != "":
        numeroPantalla.set(num)
        reset_pantalla = False
    else:
        numeroPantalla.set(numeroPantalla.get() + num)

def suma(num):
    global operacion
    global resultado
    global reset_pantalla

    resultado+=int(num)
    operacion = "suma"
    reset_pantalla = True

    numeroPantalla.set(resultado)

num1 = 0
contador_resta = 0
def resta(num):
    global operacion
    global resultado
    global num1
    global contador_resta
    global reset_pantalla

    if contador_resta == 0:
        num1 = int(num)
        resultado=num1
    else:
        if contador_resta == 1:
            resultado=num1-int(num)
        else:
            resultado=int(resultado)-int(num)
        numeroPantalla.set(resultado)
        resultado=numeroPantalla.get()

    contador_resta+=1
    operacion = "resta"
    reset_pantalla = True

contador_mult = 0
def multiplicar(num):
    global operacion
    global resultado
    global num1
    global contador_mult
    global reset_pantalla

    if contador_mult == 0:
        num1 = int(num)
        resultado=num1
    else:
        if contador_mult == 1:
            resultado=num1*int(num)
        else:
            resultado=int(resultado)*int(num)
        numeroPantalla.set(resultado)
        resultado=numeroPantalla.get()

    contador_mult+=1
    operacion="multiplicacion"
    reset_pantalla = True

contador_division = 0
def divide(num):
    global operacion
    global resultado
    global num1
    global contador_division
    global reset_pantalla

    if contador_division == 0:
        num1 = int(num)
        resultado = num1
    else:
        if contador_division == 1:
            resultado=num1/float(num)
        else:
            resultado=float(resultado)/float(num)
        numeroPantalla.set(resultado)
        resultado=numeroPantalla.get()

    contador_division+=1
    operacion="division"
    reset_pantalla=True


def resultado_final():
    global resultado
    global operacion
    global contador_resta
    global contador_mult
    global contador_division

    if operacion == "suma":
        numeroPantalla.set(int(resultado)+int(numeroPantalla.get()))
        resultado = 0
    elif operacion == "resta":
        numeroPantalla.set(int(resultado)-int(numeroPantalla.get()))
        resultado = 0
        contador_resta=0
    elif operacion == "multiplicacion":
        numeroPantalla.set(int(resultado)*int(numeroPantalla.get()))
        resultado = 0
        contador_mult=0
    elif operacion == "division":
        numeroPantalla.set(float(resultado)/int(numeroPantalla.get()))
        resultado = 0
        contador_division = 0

# ----- FILA 1 -----
boton7 = Button(miFrame, text="7", width=3, command=lambda:numeroPulsado("7"))
boton7.grid(row=2, column=1)
boton8 = Button(miFrame, text="8", width=3, command=lambda:numeroPulsado("8"))
boton8.grid(row=2, column=2)
boton9 = Button(miFrame, text="9", width=3, command=lambda:numeroPulsado("9"))
boton9.grid(row=2, column=3)
botonDiv= Button(miFrame, text="%", width=3, command=lambda:divide(numeroPantalla.get()))
botonDiv.grid(row=2, column=4)

# ----- FILA 2 -----
boton4 = Button(miFrame, text="4", width=3, command=lambda:numeroPulsado("4"))
boton4.grid(row=3, column=1)
boton5 = Button(miFrame, text="5", width=3, command=lambda:numeroPulsado("5"))
boton5.grid(row=3, column=2)
boton6 = Button(miFrame, text="6", width=3, command=lambda:numeroPulsado("6"))
boton6.grid(row=3, column=3)
botonMult= Button(miFrame, text="X", width=3, command=lambda:multiplicar(numeroPantalla.get()))
botonMult.grid(row=3, column=4)

# ----- FILA 3 -----
boton1 = Button(miFrame, text="1", width=3, command=lambda:numeroPulsado("1"))
boton1.grid(row=4, column=1)
boton2 = Button(miFrame, text="2", width=3, command=lambda:numeroPulsado("2"))
boton2.grid(row=4, column=2)
boton3 = Button(miFrame, text="3", width=3, command=lambda:numeroPulsado("3"))
boton3.grid(row=4, column=3)
botonRest= Button(miFrame, text="-", width=3, command=lambda:resta(numeroPantalla.get()))
botonRest.grid(row=4, column=4)

# ----- FILA 4 -----
boton0 = Button(miFrame, text="0", width=3, command=lambda:numeroPulsado("0"))
boton0.grid(row=5, column=1)
botonDecimal = Button(miFrame, text=",", width=3, command=lambda:numeroPulsado(","))
botonDecimal.grid(row=5, column=2)
botonTotal= Button(miFrame, text="=", width=3, command=lambda:resultado_final())
botonTotal.grid(row=5, column=3)
botonSuma = Button(miFrame, text="+", width=3, command=lambda:suma(numeroPantalla.get()))
botonSuma.grid(row=5, column=4)

# ----- FILA 5 -----
botonDel = Button(miFrame, text="DEL", width=8)
botonDel.grid(row=6, column=1, columnspan=2)
botonDel1 = Button(miFrame, text="<-" , width=8)
botonDel1.grid(row=6, column=3, columnspan=2)

raiz.mainloop()