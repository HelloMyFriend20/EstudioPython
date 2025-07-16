#Ventajas de F-strings
#Son más legibles y más concisas.
#Tiene soporte pára expresiones complejas, ya que dentro de las {} podemos colocar cualquier calculo, incluso funciones y metodos.
#Podemos usar format para limitar valores numericos.

#Con el uso de la libreria timeit podemos comparar el tiempo de ejecucion de los f-strings con el format.

import timeit

nombre = "Martin"
edad = 30

#Con f-strings
f_strings = timeit.timeit('"Hola {nombre}, tienes {edad} años."',globals = globals(), number = 1000000)

#Usando .format()
uso_format = timeit.timeit('"Hola {} tienes {} años." .format(nombre, edad)', globals = globals(), number = 1000000)

print(f'Tiempo usando F-Strigs: {f_strings:.5f}')
print(f'Tiempo usando .format(): {uso_format:.5f}')