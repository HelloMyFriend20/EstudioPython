#Veremos la creación de barras de menus, para crear una interfaz graficas operativa.

from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

root = Tk()
root.title("Mi primera pagina web en python que en realidad no es una pagina web si no mas bien una aplicacion de escritorio muchas gracias. ")
root.config(width=600, height=300)

#Creacion de funcion para realizar una ventana emergente.
#Para las ventanas emergentes se debe importar la libreria messagebox
def infoAdicional():
    messagebox.showinfo("Acerca de", "Programa de Martin Ramirez")

def licencia():
    messagebox.showwarning("Licencia", "Estado de su licencia:\n Bajo la licencia de tu madre :)")

def salir():
    #valor = messagebox.askquestion("Salir", "¿Desea salir del programa?")
    #if valor == "yes":
        #root.destroy()

    valor = messagebox.askokcancel("Salir", "¿Quiere salir del programa?")
    if valor == True:
        root.destroy()

def abrirDocumento():
    fichero = filedialog.askopenfilename(title="Abrir: ")
    print(fichero)

def cerrarDocumento():
    valor = messagebox.askretrycancel("Fatal Error", "Documento Bloqueado")
    if valor == False:
        root.destroy()


barramenu = Menu(root)
root.config(menu = barramenu)

archivoMenu = Menu(barramenu, tearoff=0) #Elimina el separador inicial del menu.
archivoMenu.add_command(label="Nuevo")
archivoMenu.add_command(label="Abrir", command=abrirDocumento)
archivoMenu.add_command(label="Guardar")
archivoMenu.add_command(label="Guardar como")
archivoMenu.add_command(label="Cerrar archivo", command=cerrarDocumento)
archivoMenu.add_separator()
archivoMenu.add_command(label="Salir", command=salir)

archivoEdicion = Menu(barramenu, tearoff=0)
archivoEdicion.add_command(label="Copiar")
archivoEdicion.add_command(label="Cortar")
archivoEdicion.add_command(label="Pegar")

archivoHerramientas = Menu(barramenu, tearoff=0)
archivoHerramientas.add_command(label="Plugins")
archivoHerramientas.add_command(label="Configuración")

archivoAyuda = Menu(barramenu, tearoff=0)
archivoAyuda.add_command(label="Licencia", command=licencia)
archivoAyuda.add_command(label="Acerca de", command=infoAdicional)

barramenu.add_cascade(label="Archivo", menu=archivoMenu)
barramenu.add_cascade(label="Edición", menu=archivoEdicion)
barramenu.add_cascade(label="Herramientas", menu=archivoHerramientas)
barramenu.add_cascade(label="Ayuda", menu=archivoAyuda)


root.mainloop()