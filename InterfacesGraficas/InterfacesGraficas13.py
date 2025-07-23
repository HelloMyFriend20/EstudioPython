#Utilizacion de guardado de archivos y apertura de estos.

from tkinter import *
from tkinter import filedialog

root = Tk()
def abrefichero():
    fichero = filedialog.askopenfilename(title="Abrir", initialdir="D:\Programacion Cursos\Python\CursoPython\InterfacesGraficas", filetypes=(("Ficheros de Excel","*.xlsx"), ("Extensiones de Python","*.py"),("Todos los ficheros", "*.*")))
    print(fichero)

Button(root, text="Abrir Fichero", command=abrefichero).pack()

root.mainloop()