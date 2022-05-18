"""
Crear una clase Persona con metodos estaticos, de clase y de instancia.

    -Tiene que tener un atributo de clase : Nacionalidad.

Los metodos a crear son:

    -Constructor con atributos DNI, nombre, apellido
    -Metodos de clase: set y get nacionalidad
    -Metodos de instancia: setters y getters, crear con @property
    -Metodos estaticos.
"""

class Persona:

    nacionalidad = "Argentino"

    def __init__(self, dni, nombre, apellido):
        self.__dni = dni
        self.__nombre = nombre
        self.__apellido = apellido

    @classmethod
    def set_nacionalidad(cls,x):
        cls.nacionalidad = x

    @classmethod
    def get_nacionalidad (cls):
        return cls.nacionalidad

    @staticmethod
    def calcular_imc (peso, estatura):
        return peso/(estatura**2)

    @staticmethod
    def peso (estatura, genero):
        if genero == "F":
            return estatura-20
        else:
            return estatura-10

    @staticmethod
    def edad (ano_nacimiento):
        return (2022-ano_nacimiento)

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