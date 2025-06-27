#Varias excepciones en un mismo try:

def divide():
    try:
        op1 = float(input("Ingrese el primer numero: "))
        op2 = float(input("Ingrese el segundo numero: "))

        print(f'La division de {int(op1)} entre {int(op2)} es {op1/op2}')
    except ValueError:
        print("El valor introducido es erroneo")
    except ZeroDivisionError:
        print("No se puede dividir entre 0")
    finally: #Es una instruccion que hace que una linea siempre se ejecuta.
        print("Calculo finalizado") #Esta linea siempre se ejecutara.

divide()

#En caso de hacer un except vacio es como hacer una excepcion general.