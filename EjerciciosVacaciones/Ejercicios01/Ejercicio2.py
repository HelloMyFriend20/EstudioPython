#Crea un programa que pida por teclado “Nombre”, “Dirección” y “Tfno”. Esos tres datos
#deberán ser almacenados en una lista y mostrar en consola el mensaje: “Los datos
#personales son: nombre apellido teléfono” (Se mostrarán los datos introducidos por teclado)

nombre = input("Ingrese su nombre: ")
direccion = input("Ingrese su direccion: ")
telefono = int(input("Ingrese su numero de telefono: "))

nueva_lista = [f'Aqui va su nombre: {nombre}, direccion: {direccion}, telefono: {telefono}']
print(nueva_lista)

#Opcion 2 usando metodo append

lista_nueva = []

nombre2 = input("Ingrese su nombre: ")
lista_nueva.append(nombre2)

direccion = input("Ingrese su direccion: ")
lista_nueva.append(direccion)

while True:
    try:
        telefono = int(input("Ingrese su telefono: "))
        break
    except ValueError:
        print("Error: Por favor, coloca un numero de telefono valido")


