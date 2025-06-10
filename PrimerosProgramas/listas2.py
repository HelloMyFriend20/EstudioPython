milista = ["Maria",5,True,78.35]
milista.extend(["Sandra","Ana","Lucia"])

#Para remover objetos
milista.remove("Ana")
print(milista)

#Para remover el ultimo elemento de una lista
milista.pop()
print(milista)

#Ahora crearemos otra lista
milista2 = ["Martin","Fernando"]
#Para unir 2 listas podemos hacer lo siguiente:
lista_definitiva = milista + milista2
print(f'Imprimira la union de las 2 listas: {lista_definitiva}')

#Al multiplicar una lista funcionara como un repetidor:
print(f'Imprime mi lista 3 veces: {milista2 * 3}')