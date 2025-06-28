#Como construir una clase
class Coche():
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

    def arrancar(self):
        pass

#La clase contiene atributos y metodos
#Creamos un objeto:
miCoche = Coche() #Instanciamos una clase (crear objeto)

#Como establecemos el comportamiento de miCoche
print(f'El largo del coche es: {Coche.largoChasis}') #Imprime la propiedad largo chasis
print(f'El coche tiene {Coche.ruedas} ruedas.')