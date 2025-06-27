#El pass puede ser usado con:
#while True:
#    pass

class miClase:
    pass #Para implementar mas tarde.

def funcion():
    pass

#Else
#Se puede utilizar con bucles

#Programa para saber si hay una arroba o no en el correo.
email = input("Introduce tu email: ")

for i in email:
    if i == "@":
        arroba = True
        break

else:
    arroba = False
print(arroba)