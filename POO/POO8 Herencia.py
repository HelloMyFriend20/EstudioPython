class Persona():
    def __init__(self, nombre, edad, lugar_residencia):
        self.__nombre = nombre
        self.__edad = edad
        self.__lugar_residencia = lugar_residencia

    def descripcion(self):
        print(f'Nombre: {self.__nombre}\nEdad: {self.__edad}\nResidencia: {self.__lugar_residencia}')

class Empleado(Persona):
    def __init__(self, salario, antiguedad, nombre_empleado, edad_empleado, residencia_empleado):
        super(). __init__(nombre_empleado, edad_empleado, residencia_empleado) #Extiende la super clase o clase padre.
        self.__salario = salario
        self.__antiguedad = antiguedad

    def descripcion(self):
        super().descripcion()
        print(f'Salario: {self.__salario}\nAntiguedad: {self.__antiguedad}')

nuevoNombre = Empleado(1900000, "5 años", "Martin", 55, "Colombia")
nuevoNombre.descripcion()

#Principio de sustitución:
#Cuando tenemos herencia un objeto de la subclase siempre sera un objeto de la clase padre.
#En este caso un empleado siempre es una persona.
#Pero una persona no siempre es empleado.

#La función isintance() nos informa si un objeto es instancia de una clase determinada.
#Esta función devolvera True o False
print(isinstance(nuevoNombre, Empleado)) #Devolvera True ya que nuevoNombre pertenece a la clase Empleado
print(isinstance(nuevoNombre,Persona)) #También es True.

#Ejemplo cambiando la línea 20 a nuevoNombre = Persona
#print(isinstance(Manuel, Empleado))
#Imprimira False

