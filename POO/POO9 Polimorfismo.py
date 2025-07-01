#Viene del griego poli (muchas) morfismo (formas)
#Muchas formas
#Al cambiar de forma cambia de comportamiento.

class Coche():
    def desplazamiento(self):
        print("Me desplazo utilizando 4 ruedas")

class Moto():
    def desplazamiento(self):
        print("Me desplazo utilizando 2 ruedas")

class Camion():
    def desplazamiento(self):
        print("Me desplazo utilizando 6 ruedas")

#Para crear instancias y utilizar el metodo desplazamiento hay que crearlas una por una
#Esto sería sin polimorfismo

#miVehiculo = Moto()
#miVehiculo.desplazamiento()

#miVehiculo2 = Coche()
#miVehiculo2.desplazamiento()

#miVehiculo3 = Camión()
#miVehiculo3.desplazamiento()



def desplazamientoVehiculo(vehiculo): #Aquí ocurre el polimorfismo
#Le pasamos a Vehículo el parametro de miVehiculo, asi llama al método desplazamiento de la clase camión
    vehiculo.desplazamiento()

miVehiculo = Camion()
desplazamientoVehiculo(miVehiculo)

#En otros lenguajes es mas complejo utilizado el polimorfismo