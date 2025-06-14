#Crea un programa que pida tres números por teclado. El programa imprime en consola
#la media aritmética de los números introducidos.

entrada = input("Ingrese 3 numeros separados por espacio: ").split()
a,b,c = int(entrada[0]), int(entrada[1]), int(entrada[2])

def mediaAritmetica():
    resultado = (a + b + c)/3
    return f'La media aritmetica es: {resultado}'

print(mediaAritmetica())
