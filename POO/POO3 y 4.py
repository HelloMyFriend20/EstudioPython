class Coche(): #Construimos la clase Coche()
    largoChasis = 250
    anchoChasis = 120
    ruedas = 4
    enmarcha = False

#Como construir comportamientos a una clase
#Utilizando metodos
    #Un metodo es una funcion perteneciente a una clase
    #Una funcion no pertenece a ninguna clase.

    #def function(self):
        #pass

    #self hace referencia al propio objeto perteneciente a la clase
    #self suele ser similiar a this en C++ o Java
    #pass evita errores cuando la funcion este vacia.

    def arrancar(self,arrancamos): #El metodo arrancar hara lo del metodo estado agregando un parametro
        self.enmarcha = arrancamos
        if self.enmarcha:
            return "El estado del coche es en pausa"
        else:
            return "El estado del coche es en marcha"

    def estado(self):
            return f'el coche tiene {self.ruedas} ruedas. Un ancho de {self.anchoChasis} y un largo de {self.largoChasis}'

#La clase contiene atributos y metodos
#Creamos un objeto:
miCoche = Coche() #Instanciamos una clase (crear objeto)

#Como establecemos el comportamiento de miCoche
print(f'El largo del coche es: {Coche.largoChasis}') #Imprime la propiedad largo chasis
print(f'El coche tiene {Coche.ruedas} ruedas.')

#Sí queremos acceder al comportamiento de arrancar
print(f'Consultamos el estado del coche: {miCoche.estado()} ') #Dara false

#Si llamamos al metodo arrancar el estado del coche cambiará al True:
print(f'Llamamos al metodo arrancar: {miCoche.arrancar(True)}')
print(f'Volvemos a consultar el estado del coche: {miCoche.estado()}')

#Con esto concluimos que nuestra clase coche tiene:
# 4 propiedades y 2 comportamientos


#Poo 4
print(" ")
print("-----A continuación creamos el segundo objeto-----")

miCoche2=Coche()

#Estamos cambiando la propiedad ruedas
miCoche2.ruedas = 2
#Encapsulamiento: Encapsulamos o protegemos una propiedad para que no se pueda modificar fuera de la clase.
#Asi se encapsula:
#   self.__ruedas = 4    De esta manera no permitira hacer cambios externos

print(F'El largo del coche es: {miCoche2.largoChasis}')
print(f'El coche tiene {miCoche2.ruedas} ruedas')
print(miCoche2.arrancar(False))
print(miCoche2.estado())

#Constructor: Metodo especial que le da estado inicial a un objeto perteneciente a una clase.
#Ejemplo:
'''
class Coche():
    def __init__(self):
    
    self.largoChasis = 250
    self.anchoChasis = 120
    self.__ruedas = 4
    self.enmarcha = False 
'''
