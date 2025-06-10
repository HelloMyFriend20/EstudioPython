#Permiten almacenar incluso listas, tuplas u otros diccionarios
#Se almacenan en clave valor

midiccionario = {"Alemania":"Berlin","Francia":"Paris","Reino Unido":"Londres","España":"Madrid"}
print(f'Imprimimos el diccionario: {midiccionario}')
print(f'Buscamos en el diccionario con la clave "Francia": {midiccionario["Francia"]}')

#Como agregar mas elementos a un diccionario ya construido
midiccionario["Italia"]="Lisboa" #Valor erroneo
print(midiccionario)
#Como modificamos este valor erroneo?
midiccionario["Italia"]="Roma" #Sobrescribimos en la clave "Italia"
print(midiccionario)

#Como eliminar un elemento del diccionario
del midiccionario["Reino Unido"]
print(f'Diccionario borrando la clave y valor de "Reino Unido" con "del": {midiccionario}')


#Diccionario con varios tipos de datos:
midiccionario2 = {"Alemania":"Berlin", 23:"Jordan", "Mosqueteros":23}
print(f'Diccionario con varios tipos de datos: {midiccionario2}')

#Usando tuplas
mitupla = "España","Francia","Reino Unido"
midiccionario3={mitupla[0]:"Madrid", mitupla[1]:"Paris", mitupla[2]:"Londres"}
print(f'Para acceder a un valor usando de la tupla con el diccionario: {midiccionario3[mitupla[1]]}')
print(f'Igual usando la clave: {midiccionario["Francia"]}')

#Una clave con varios valores:
midiccionario4 = {23:"Jordan", "Nombre":"Michael", "Equipo":"Chicago","Anillos":{"temporadas":(1991,1992,1993,1996,1997,1998)}}
print(f'{midiccionario4["Anillos"]}') #Un subdiccionario

#Metodos interesantes. Metodo keys, values y len:
print(f'Claves diccionario usando el metodo keys(): {midiccionario.keys()}')
print(f'Valores diccionario usando el metodo values(): {midiccionario.values()} ')
print(f'Longitud diccionario usando el metodo len(): {len(midiccionario)}')
