#Comprobar correo usando or
contador = 0
correo= input("Ingresa tu direccion de correo electronico: ")

for i in correo:
    if (i == "@" or i == "."): #Si la primera condicion se cumple contador valdra 1
        contador = contador + 1 #Si la segunda condicion se cumple contador valdra 2

if contador == 2:
    print("Correo correcto")
else: #Si contador es menor que 2 es pq alguna condicion no se cumple.
    print("Correo incorrecto")
print(" ")

#Uso tipo de dato Range
for x in range(5):
    print("Hola",x)