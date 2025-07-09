class Vehiculos():
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
        print(f'Marca: {self.marca}\nModelo: {self.modelo}\nEn Marcha {self.enmarcha}\nAcelerando: {self.acelera}\nFrenando: {self.frena}')

#Herencia 2
#Veremos sobrescritura de metodos, herencia simple y multiple.

#Haremos una cadena o jerarquía de herencia
class furgoneta(Vehiculos):
    def carga(self, cargar):
        self.cargado = cargar
        if self.cargado: #Aqui decimos "Si self.cargado es verdadero"
            return "La furgoneta esta cargada"
        else:
            return "La furgoneta no esta cargada"

#Sintaxis para heredar:
class Moto(Vehiculos): #Escribimos el nombre de la clase que hereda moto
    #Crearemos un comportamiento nuevo para una moto:
    hcaballito = ""
    def caballito(self):
        self.hcaballito = "Voy haciendo el caballito" #Ahora tiene los comportamientos del constructor y los de la nueva funcion.

    #Sobrescribimos el metodo estado:
    def estado(self):
        print(f'Marca: {self.marca}\nModelo: {self.modelo}\nEn Marcha {self.enmarcha}\nAcelerando: {self.acelera}\nFrenando: {self.frena}\n{self.hcaballito}')

#Creamos nueva clase
class VehiculosElectricos():
    def __init__(self):
        self.autonomia = 100

    def cargarEnergia(self):
        self.cargando = True

miMoto = Moto("Honda", "CBR")
#Podria ser también: miMoto = Moto(input(), input())
miMoto.caballito()#Llamamos el método, de lo contrario no se mostrará en la impression
miMoto.estado() #Imprime el método de la clase padre.
#Después de sobrescribir imprime hcaballito.
print("-----------SIGUIENTE CLASE------------")

miFurgoneta = furgoneta("Renault","Kangoo")
miFurgoneta.arrancar()
miFurgoneta.estado()
print(miFurgoneta.carga(True))

#Lo siguiente daria un error
#miMoto.carga()
#Ya que carga es un método que no pertenece a la clase moto.

class BicicletaElectrica(VehiculosElectricos,Vehiculos): #Se da prioridad a la primera clase llamada.
    #Se herendan metodos y condiciones de las 2 clases
    pass

miBici = BicicletaElectrica()