#Funcionamiento
#En lugar de "return" habria un "yield"
#Yield construye un objeto iterable con el primer valor

#Con un generador buscamos construir un objeto generador iterable
#En el cual esta almacenado el primer valor que se nos va a devolver
#Para mas tarde entrar en modo de suspension

#Al volver a llamar al generador se extraera el siguiente valor y volvera a quedar en suspension.

#Sintaxis
#def function():
#    yield ejemplo

#Programa que cree una funcion que genere numeros pares
def generaPares(limite):
    num = 1
    lista = []
    while num < limite:
        lista.append(num*2)
        num+=1
    return lista

print(generaPares(int(input())))

#Mismo programa con un generador:
def generaPares(limite):
    num = 1
    while num < limite:
        yield num*2
        num+=1

resultado = generaPares(int(input()))
#for i in resultado:
#    print(i)

#Uso del metodo next()
print(next(resultado)) #Imprime el primer resultado
print("Aqui podria ir mas codigo...")
print(next(resultado)) #Imprime el siguiente (next) resultado
print("Aqui podria ir mas codigo...")
print(next(resultado)) #Imprime el numero 6