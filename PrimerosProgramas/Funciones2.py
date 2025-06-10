def suma(): #Creacion funcion
    num1 = int(input()) #Declaramos variables
    num2 = int(input())
    print(num1+num2) #Imprime variables

suma() #Llamado a la funcion


def suma2(numero1, numero2): #Declaramos 2 argumentos en la zona de parametros
    caracol = numero1 + numero2
    print(caracol)

suma2 (int(input()),int(input())) #Damos los valores para la zona de parametros


#Funciones con return
def suma3(x,y):
    resultado = x + y
    return f'Aqui imprimiera un resultado: {resultado}'

print(suma3(5,4))

almacenar_resultado = suma3(5,8)
print(almacenar_resultado)