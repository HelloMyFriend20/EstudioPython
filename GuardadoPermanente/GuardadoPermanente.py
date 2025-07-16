import pickle

class Persona:
    def __init__(self, nombre, genero, edad):
        self.nombre = input()
        self.genero = input()
        while True:
            try:
                self.edad = int(input())
                break
            except ValueError:
                print("Digite una edad valida")

        print(f'Se ha creado una persona nueva con el nombre: {self.nombre}')

    def __str__(self): #Convierte a cadena de texto la información de un objeto.
        return f'{self.nombre}, {self.genero}, {self.edad}'
        #Tambien se podría
        #return "{} {} {}".format(self.nombre, self.genero, self.edad)

class ListaPersonas:
    personas = []
    def __init__(self):
        with open("FicheroExterno.txt", "ab+") as listaDePersonas: #Nueva manera de usar el método open()
            listaDePersonas.seek(0)
            while True:
                try:
                    self.personas = pickle.load(listaDePersonas)
                except EOFError:
                    break

        print("Se cargaron {} personas del fichero externo".format(len(self.personas)))

    def agregarPersonas(self, p):
        self.personas.append(p) #Esto agregará los datos de "p" a la lista personas
        self.guardarCambios() #Esto llama a la función que guarda los datos en el archivo de texto.

    def mostrarPersonas(self):
        for p in self.personas:
            print(p)

    def guardarCambios(self):
        with open("FicheroExterno.txt","wb") as listaDePersonas:
            pickle.dump(self.personas, listaDePersonas)

    def mostrarInformacion(self): #Mostrará la información del fichero
        print(f'La información del fichero externo es la siguiente: ')
        for p in self.personas:
            print(p)

miLista = ListaPersonas()
p = Persona("","",0)
miLista.agregarPersonas(p)

miLista.mostrarPersonas()
miLista.mostrarInformacion() #Muestra la información guardada en el fichero externo.