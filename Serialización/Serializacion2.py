import pickle

class Vehiculo():
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.enmarcha = False
        self.acelera = False
        self.frena = False

    def arrancar(self):
        self.enmarcha = True

    def acelerar(self):
        self.acelera = True

    def frenar(self):
        self.frena = True

    def estado(self):
        print(f'Marca: {self.marca}\nModelo: {self.modelo}\nEn Marcha: {self.enmarcha}\nAcelerando: {self.acelerar()}\nFrenando: {self.acelera}')

coche1 = Vehiculo("Ferrari", "812 Superfast")
coche2 = Vehiculo("Lamborghini", "Gallardo")
coche3 = Vehiculo("Mercedes", "AMG Black Series")
coches = [coche1, coche2, coche3]

fichero = open("losCoches","wb") #Escritura de bites
pickle.dump(coches, fichero)

fichero.close()
del fichero

ficheroApertura = open("losCoches","rb") #Lectura de bites
misCoches = pickle.load(ficheroApertura)

ficheroApertura.close()
del ficheroApertura

for x in misCoches: #Aqui veremos los 3 objetos y su espacio en memoria
    #print(x) Asi veremos la información en memoria
    print(x.estado()) #Asi veremos el método estado