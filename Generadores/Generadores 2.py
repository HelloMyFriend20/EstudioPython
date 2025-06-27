#Con el uso de Yield from.
#Simplifican el codigo de los generadores
#en el caso de usar bucles anidados

#Sintaxis
def ciudades(*ciudades): #El * marca que recibira un numero indeterminado de argumentos en forma de tupla
    for elemento in ciudades:
       #for subElemento in elemento: Con yield from nos ahorramos esta linea de codigo,
            yield from elemento

ciudades_devueltas = ciudades("Madrid","Barcelona","Bilbao","Valencia")

print(next(ciudades_devueltas))
print(next(ciudades_devueltas))