#Bucle for usando el tipo de dato Range, recorriendo strings y notaciones especiales con print.
for i in 'Juan','Carlos',3:
    print(i, end=" ")
print("\n")

#Imprimir la palabra hola en cuestion de los caracteres de un string:
for a in "martin":
    print(f'Hola {a}')

#Imprimir cada caracter de una variable tipo string.
variable = "fernando"
for b in variable:
    print(b)

#Comprobar correo
email = False #Se crea variable de tipo boleana
for x in "martinramirez@correo.com":
    if(x == "@"): #X recorrera caracter por caracter hasta que x sera igual a "@"
        email = True #Al ser x igual a "@" email cambiara a True.
if email: #Como email ya es verdadero, no hace falta un email == True:
    print("Email correcto")
else:
    print("Email incorrecto")

#Comprobar correo con variable creada
email = False
correo = input("Introduce tu direccion de correo electronico: ")
for i in correo:
    if (i == "@"):
        email = True
if email:
    print("Email correcto")
else:
    print("Email incorrecto")
