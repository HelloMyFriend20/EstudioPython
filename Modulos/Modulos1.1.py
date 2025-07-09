#Importamos el módulo, ya sea el otro archivo con las funciones
#Se podría hacer asi:
#import Modulos1
#Modulos1.suma(7,5)

#O también asi:
from Modulos1 import * #Con el * importamos todo del modulo anterior.
sumar(7,5)

#Modulos1.restar(90, 12)

from Modulo_Vehiculo import * #Esto hara que imprima todo lo que esta en Modulo_Vehiculo

#Creamos una instancia
miCoche = Vehiculos("Ferrari","SF90")
miCoche.estado()

#Para que los modulos funcionen tienen que estar en una misma carpeta, tanto el modulo que importamos como el modulo que vamos a usar.
#Para solucionar esto podemos usar los paquetes.
#Que veremos en el siguiente video.