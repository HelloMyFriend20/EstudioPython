#Métodos de cadenas
#Veremos los mas importantes para manipular cadenas:

#upper(): convierte el texto a mayúsculas
#lower(): Convierte el texto en minúsculas
#Capitalize(): Convierte la primera letra en Mayúscula
#count(): Cuenta cuantas veces aparece una letra o cadena dentro de una frase
#find(): Representa la posición en la cual aparece un caracter en un texto
#isdigit(): Devuelve True o False dependiendo de si el caracter es numerico o no.
#isalum(): Comprueba si es alfanumérico, si hay solo letras
#split(): Separa caracteres por espacio predeterminadamente o un caracter que nosotros le demos.
#strip(): Borra los espacios sobrantes al inicio y al final.
#replace(): Cambia palabra o letra por otra
#rfind(): Representa el indice de un caracter contando desde atras.

#Practica:
nombre_usuario = input("Introduzca su nombre: ")
print(f'El nombre en mayuscula usando upper(): {nombre_usuario.upper()}')
print(f'El nombre en minuscula usando lowe(): {nombre_usuario.lower()}')
print(f'Eñ nombre con la primera en mayuscula, usando capitalize(): {nombre_usuario.capitalize()}')
print(" ")

edad = input("Introduce tu edad: ")
print(f'Usando isdigit() devolvera True o False si es un numero o no\nCon la variable edad: {edad.isdigit()}\ncon la variable nombre_usuario: {nombre_usuario.isdigit()}')

#usos del isdigit:
while edad.isdigit() == False:
    edad = input("Ingresa un valor numerico: ")

if int(edad) < 18:
    print("No puede pasar")
else:
    print("Puedes pasar")