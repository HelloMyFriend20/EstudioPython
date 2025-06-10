#Las listas nos permiten almacenar en la memoria del ordenador varios valores
#Son estructuras muy utilizadas
#sintaxis de una lista: nombreLista = [elem1,elem2,elem3,...]

#Ejercicios
milista = ['Maria','Pepe','Martha','Antonio']
print(milista[2]) #Imprime Martha
print(milista[-2]) #Imprime Martha, Empieza a contar desde el final (No comienza contando en 0)

#Porcion de lista
#Se accede a un trozo de la lista
print(f'[0:3] Imprime del primer item al tercero: {milista[0:3]}') #Se puede realizar esto mismo sin el 0,
print(f'[:3] Empieza a imprimir desde el item 0: {milista[:3]}') #Python reconoce automaticamente que el inicio es 0
print(f'[2:] Imprime los 2 ultmos elementos: {milista[2:]}') #Al precindir del segundo indice le decimos que acceda a los 2 ultimos elementos

#Agregar items a la lista
milista.append('Juan')
print(f'Lista con un item agregado usando append: {milista}')

#Agregar items a la lista con una posicion o indice
milista.insert(2,'Martin')
print(f'Lista con un item agregado en la posicion 2: {milista}')

#Agregar varios items a la lista
milista.extend(["Sandra","Ana","Lucía","Maria"])
print(f'Lista con elementos extendidos: {milista[:]}')

#Muestra la posicion de un atributo en la lista
#Mostrara la primera vez que se ve ese atributo, en orden de 0 a N.
print(f'Imprime el indice de "Antonio" {milista.index("Antonio")}')

#Busqueda en lista usando el elemento "in"
print(f'Imprime True o False en caso de hallar o no el atributo: {("Pepe" in milista)}')
print(f'Imprimira False: {("Pedrito" in milista)}')
print(f'Esto es una lista: {type(milista)} Gracias')