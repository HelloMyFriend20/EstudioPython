contrasena = input(f'Ingrese su contraseña: ').lower()
intentos = 5
for x in range(intentos):
    comprobar_contrasena = input().lower()
    if comprobar_contrasena == contrasena:
        print(f'Su contraseña {contrasena} es correcta')
        break
    else:
        print(f'Su contraseña es incorrecta, vuelva a intentar')

print("BLOQUEO DEL SISTEMA")
