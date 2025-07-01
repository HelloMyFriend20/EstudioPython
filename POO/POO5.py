#Clase Coche actualizada desde POO 3 y 4.
#Veremos metodos encapsulados (línea 31)
class Coche():
    def __init__(self): #Metodo constructor
        self.__largoChasis = 250 #Encapsulamos una variable
        self.__anchoChasis = 120
        self.__ruedas = 4
        self.__enmarcha = False

    def arrancar(self, arrancamos):
        self.__enmarcha = arrancamos

        if self.__enmarcha:
            chequeo = self.__chequeo_interno() #Guardamos el metodo en una variable

        if self.__enmarcha and chequeo:
            return "El coche esta en marcha"
        elif self.__enmarcha and chequeo == False:
            return "Problema del chequeo"
        else:
            return "El coche esta parado"

    def estado(self):
        print(f'El coche tiene: {self.__ruedas} ruedas. Un ancho de {self.__anchoChasis} y un largo de {self.__largoChasis}')

    #Nuevo metodo de manera encapsulada:
    def __chequeo_interno(self): #De momento este metodo no esta encapsulado "def chequeo_interno(self):"
        print("Realizando chequeo interno")

        self.gasolina = "ok" #Creamos nuevas variables
        self.aceite = "ok"
        self.puertas = "cerradas"

        if self.gasolina == "ok" and self.aceite == "ok" and self.puertas == "cerradas":
            return True
        else:
            return False

miCoche = Coche()
print(miCoche.arrancar(True))
miCoche.estado()

print("-----A continuación creamos el segundo objeto-----")
miCoche2 = Coche()
print(miCoche2.arrancar(False))
miCoche2.estado()

#Que utilidades tiene un método encapsulado
#No permite que se acceda a variables del metodo de manera externa al metodo
#Estas se podran editar unicamente con el metodo
#Segun nuestras necesidades podemos encapsular un metodo o no