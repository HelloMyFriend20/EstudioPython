#Crea un programa que pida dos números por teclado. El programa tendrá una función
#llamada “DevuelveMax” encargada de devolver el número más alto de los dos introducidos.

entrada = input("Ingresa 2 numeros separados por un espacio: ").split()
a,b = int(entrada[0]), int(entrada[1])

def DevuelveMax(a,b):
    if a == b:
        return f'El numero {a} es igual que {b}' #Return hace que se agregue el resultado a la funcion
    elif a < b:
        return f'El numero {b} es el mayor'
    else:
        return f'El numero {a} es el mayor'

print(DevuelveMax(a,b)) #Al imprimir la funcion regresara el valor retornado.


