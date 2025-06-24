#En algunos programas hay necesidad que se use un bucle infinito
#De aqui el uso del while.
import math

#Programa que calcule la raiz cuadrada de un numero
print("Programa de calculo de raiz cuadrada")
numero = int(input("Introduzca un numero: "))
intentos = 0
while numero < 0:
    print("No se puede hallar la raiz de un numero negativo.")
    if intentos == 2:
        print("Has hecho demasiados intentos.")
        break

    numero = int(input("Introduce un numero positivo por favor: "))
    if numero < 0:
        intentos = intentos + 1

if intentos < 2:
    solucion = math.sqrt(numero)
    print(f'La raiz cuadrade de {numero} es {solucion}')