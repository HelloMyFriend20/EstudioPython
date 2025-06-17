#Hay varios tipos de bucles, determinados e indeterminados.
#Repetir lineas de codigo varias veces.

#El bucle determinado en python es el bucle FOR
#Sintaxis: FOR variable IN elemento a recorrer:
                #cuerpo del bucle

#El elemento a recorrer puede ser una lista, tupla, cadena de texto o mas elementos.

a,b,c = "","",""
for i in [a,b,c]: #Recorre en proporcion al numero de items en la lista
    print("Hi PyCharm")

contador = 0
for estaciones in ("primavera","verano","invierno","otoño"):
    contador = contador + 1
    print(f'Estacion {estaciones}. contador: {contador}')
