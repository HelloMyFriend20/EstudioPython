#Haga un programa el cual compruebe si un correo
# tiene "@" o ".", si es asi, que el correo sea correct
# de lo contrario imprimira incorrecto

correo = input("Ingresa tu correo: ")
if "@" in correo and "." in correo:
    print(f'Tu correo es correcto')
else:
    print(f'Soy una mierda')