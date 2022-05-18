"""
Crear una clase persona con atributos dni, nombre, apellido encapsulados de tal forma de poder acceder y moficiar 
los atributos unicamente desde los metodos set y get
"""

class Persona:
    def __init__(self, dni, nombre, apellido):
        self.__dni = dni
        self.__nombre = nombre
        self.__apellido = apellido

    def get_nombre (self):
        return self.__nombre

    def get_dni (self):
        return self.__dni

    def get_apellido (self):
        return self.__apellido

    def set_nombre (self, nombre):
        self.__nombre = nombre

    def set_dni (self, dni):
        self.__dni = dni

    def set_apellido (self, apellido):
        self.__apellido = apellido