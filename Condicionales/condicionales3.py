#Python usa concatenacion de operadores de comparacion para realizar un condicional.
#Usamos tambien operadores logicos
#and, or e in

edad = -90
if 0 < edad < 100: #ESO ESTA EPICO
    print("Edad es correcta")
else:
    print("Edad incorrecta")

#Programa que evalua el salario
salario_presidente = int(input("Introduce el salario del presidente: "))
print ("Salario presidente: " + str(salario_presidente))

salario_director = int(input("Introduce el salario del director: "))
print(f'Salario director: {salario_director}')

salario_jefe_area = int(input("Introduce salario jefe area: "))
print(f'Salario jefe area: {salario_jefe_area}')

salario_administrativo = int(input("Introduce salario administrativo: "))
print(f'Salario administrativo; {salario_administrativo}')

if salario_administrativo < salario_jefe_area < salario_director < salario_presidente:
    print(f'Todo funciona correctamente')
else:
    print(f'Fallo en el sistema')
