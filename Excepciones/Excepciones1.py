#Captura de varias excepciones y la clausuka finally (excepciones2)
def suma(num1,num2):
    return num1 + num2
def resta(num1,num2):
    return num1 - num2
def multiplica(num1,num2):
    return num1 * num2
def divide(num1,num2): #No se puede dividir entre 0
    try: #Intente realizar esta instruccion
        return num1 / num2
    except ZeroDivisionError: #En caso de no cumplir la primera instruccion saltara al except
        return "No se puede dividir entre 0"

while True:
    try:
        op1 = int(input("Ingrese el primer numero: "))
        op2 = int(input("Ingrese el segundo numero: "))
        break
    except ValueError:
        print("Formato invalido")

print("1. Suma")
print("2. Resta")
print("3. Multiplica")
print("4. Divide")
operacion = input("Introduzca la operacion a realizar: ")


if operacion.lower() == "suma":
    print(suma(op1,op2))
elif operacion.lower() == "resta":
    print(resta(op1,op2))
elif operacion.lower == "multiplica":
    print(multiplica(op1,op2))
elif operacion.lower() == "divide":
    print(divide(op1,op2))
else:
    print("Operacion no contemplada")

print("Operacion ejectuada. Continuacion de ejecucion del programa")