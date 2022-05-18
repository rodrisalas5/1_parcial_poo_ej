"""
Crear una clase persona con atributos dni, nombre, apellido encapsulados de tal forma de poder acceder y moficiar 
los atributos unicamente desde los metodos set y get utilizando decorador property
"""

class Persona:
    def __init__(self, dni, nombre, apellido):
        self.__dni = dni
        self.__nombre = nombre
        self.__apellido = apellido

    @property
    def nombre (self):
        return self.__nombre
    
    @nombre.setter
    def nombre (self, nombre):
        self.__nombre = nombre

    @property
    def dni (self):
        return self.__dni

    @dni.setter
    def dni (self, dni):
        self.__dni = dni

    @property
    def apellido (self):
        return self.__apellido

    @apellido.setter
    def apellido (self, apellido):
        self.__apellido = apellido

persona = Persona(333, "rodrigo", "salas")
persona.nombre = "Ramiro"
print(persona.nombre)