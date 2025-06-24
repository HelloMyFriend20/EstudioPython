#Sintaxis
#while condicion:
    #cuerpo del bucle

#Mientras la conficion sea verdadera el bucle se ejecutara constamente.

i = 1
while i <= 10: #Evalua e imprime la situacion siempre que sea verdadera
    print(f'Ejecucion numero {i}')
    i = i + 1
print(" ")
print("Termino la ejecucion")

#Ejercicio que pregunta la edad
#Si la edad es negativa nos volvera a preguntar la edad

edad = int(input("Introduce tu edad por favor: "))
while edad <= 0:
    print("Has introducido una edad incorrecta. Vuelva a intentarlo")
    edad = int(input("Introduce tu edad por favor: "))

print(f'Gracias, tu tienes {edad} años')

edad2 = int(input("Vuelve a introducir tu edad: "))
while edad2 <= 5 or edad >= 100:
    print("Has introducido una edad incorrecta. Vuelva a intentarlo")
    edad2 = int(input("Vuelve a introducir tu edad: "))
print(f'Gracias, tu tienes {edad2} años')


