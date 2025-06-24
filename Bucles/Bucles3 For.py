#Bucle for con tipo RANGE y notaciones especiales con print.

for a in range(5):
    print(f'Valor de la variable: {a}')
print(" ")

contador = 0
for x in range(0,11,2): #De 0 a 10, de 2 en 2
    contador = contador + 1
    print(f'para x de 2 en 2: "{x}" {contador}')
print(" ")

#Comprobacion de correo usando metodo len()
valido = False
email = input("Ingresa tu correo: ")
for i in range(len(email)):
    if email[i]=="@":
        valido = True

if valido:
    print("Email correcto")
else:
    print("Email incorrecto")
