#Continue, pass y else.
#Continue: Salta a la siguiente interaccion de bucle.
#Pass: Devolver Null
#Else: Igual que el usado en los condicionales

for letra in "python":
    if letra == "h":
        continue #Hara que salte la "h" y volvera a comenzar el bucle en la siguiente letra

    print(f'viendo la letra: {letra}')

#Contador de letras saltandonos el espacio.
nombre = "Martin Ramirez"
contador = 0
for i in nombre:
    if i == " ":
        continue
    contador += 1
print(contador)
