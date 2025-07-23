#Veremos los CheckButtons
from tkinter import *

root = Tk()
root.title("Ejemplo")

playa = IntVar()
montana = IntVar()
rural = IntVar()

def opcionViaje():
    opcionEscogida = ""
    if playa.get() == 1:
        opcionEscogida+="playa\n"
    if montana.get() == 1:
        opcionEscogida+="montaña\n"
    if rural.get() == 1:
        opcionEscogida+="rural\n"

    textoFinal.config(text = opcionEscogida)

foto = PhotoImage(file="avion.png")
Label(root, image=foto).pack()

frame = Frame(root)
frame.pack()

Label(frame, text="Elige destinos: ", width=50).pack()

Checkbutton(frame, text="playa", variable=playa, onvalue=1, offvalue=0, command=opcionViaje).pack()
Checkbutton(frame, text="montaña", variable=montana, onvalue=1, offvalue=0, command=opcionViaje).pack()
Checkbutton(frame, text="rural", variable=rural, onvalue=1, offvalue=0, command=opcionViaje).pack()

textoFinal = Label(frame)
textoFinal.pack()

root.mainloop()