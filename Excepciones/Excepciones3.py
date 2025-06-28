#Lanzamiento de excepciones
#Instrucciones Raise
#Creacion de excepciones propias (mas adelante en el curso POO)

import math

def EvaluaEdad(edad):
    if edad <= 0:
        raise ZeroDivisionError ("No se permiten edades negativas")
        #Podemos personalizar el mensaje al usuario
        #Podemos usar el error que queramos, siempre y cuando exista
        #Podemos inventarnos un error usando una clase

    if edad < 20:
        return "Eres muy joven"
    elif edad < 40:
        return "Eres joven"
    elif edad < 65:
        return "Eres maduro"
    elif edad < 100:
        return "Cuidate"
    else:
        return "Sos inmortal"

print(EvaluaEdad(int(input())))

#Nuevo concepto
#Importamos clase math
def calculaRaiz(num1):
    if num1 < 0:
        raise ValueError("El numero no puede ser negativo.")
    else:
        return int(math.sqrt(num1))
try:
    print(calculaRaiz(int(input("Introduce un numero: "))))
except ValueError as ErrorDeNumeroNegativo: #Damos un alias a ValueError
    print(ErrorDeNumeroNegativo)

print("Programa terminado")