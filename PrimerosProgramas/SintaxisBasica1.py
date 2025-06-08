#Veremos Tipos, operadores y variales
print(f'Lo que sobra de una division {10%3}')
print(f'Potencia {5**3}')
print(f'Division entera {9//2}')

# En python el tipo de variable se define por le tipo de dato
numero = 5
print(type(numero))

nombre = "Martin"
print(type(nombre))

decimal = 11.1
print(type(decimal))

#Mensajes con triple comilla
Mensaje = """Esto es un mensaje
con 3 saltos
de linea"""
print(Mensaje)

#Condicionales

num1, num2 = 5,7 # =Operador de asignacion, ==Es de comparacion
if num1 > num2:
    print(f'El numero {num1} es mayor que el numero {num2}')
elif num1 < num2:
    print(f'El numero {num2} es mayor que el numero {num1}')
else:
    print(f'El numero {num1} es igual que el numero {num2}')