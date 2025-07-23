from tkinter import *

root = Tk()
varOpcion = IntVar()

def imprimir():
    #print (varOpcion.get())
    if varOpcion.get() == 1:
        etiqueta.config(text="YUPIIIIIIIIII")
    else:
        etiqueta.config(text=":(")

Label(root, text="Quisieras ser mi central? UwU").pack()
Radiobutton(root, text="Si", variable=varOpcion, value=1, command=imprimir).pack()
Radiobutton(root, text="No", variable=varOpcion, value=2, command=imprimir).pack()

etiqueta = Label(root)
etiqueta.pack()

root.mainloop()