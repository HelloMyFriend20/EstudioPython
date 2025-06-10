#Son listas inmutables, no se pueden modificar
#No permiten busquedas (no index) pero si comprobar si un elemento se encuentra en la tupla
#Utilidades: Mas rapidas, usan menos espacio (mas optimizadas)
#Sintaxis: nombreTupla=(elem1,elem2,elem3,...)

mitupla = ("Juan",13,1,1995)
print(type(mitupla))
print(mitupla[1])

#Se pueden convertir tuplas en listas y viceversa
#Para convertir tuplas a listas
milista=list(mitupla)
print(f'Convirtiendo tupla a lista usando el metodo list() : {type(milista)}')

#Convertir lista a tupla
nueva_lista = [1,2,3,4]
nueva_tupla = tuple(nueva_lista)
print(f'Convirtiendo lista a tupla usando el metodo tuple(): {type(nueva_tupla)}')

#Podemos ver si hay un elemento en la tupla usando in:
print(f'Imprimira true o false usando "in": {"Juan" in nueva_tupla}')

#Para ver cuantos elementos se encuentran en una tupla:
print(f'Contara cuantas veces se repite el item 3 usando el metodo count(): {nueva_tupla.count(3)}')

#Para ver la longitud de una tupla:
print(f'Imprime cuantos items tiene la tupla con el metodo len(): {len(nueva_tupla)}')


#Tuplas unitarias (con un unico objeto)
tupla_unitaria = "Carlos", #Las tuplas sin parentesis son llamadas empaquetado de tupla
print(f'"Carlos", es una tupla unitaria: {type(tupla_unitaria)}')

#Desempaquetado de tupla (funciona tambien en listas)
nombre, dia, mes, ano = milista
print("A continuacion se reemplazaran los items de la tupla en orden por las variables creadas: ")
print(nombre,dia,mes,ano)