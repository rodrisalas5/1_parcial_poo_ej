"""
Crear una clase abstracta Animal con 4 metodos. (Hablar, Mover, Dormir, Comer) y dos 
clases Gato y Perro que hereden la clase Animal.
Luego crear un menu para crear animales y guardarlos en una lista.
"""
from abc import ABC
from abc import abstractmethod

class Animal (ABC):
    @abstractmethod #Hace que el metodo sea obligatorio
    def hablar (self):
        pass

    @abstractmethod
    def mover (self):
        pass

    @abstractmethod
    def dormir (self):
        pass

    @abstractmethod
    def comer (self):
        pass

class Gato (Animal):
    def hablar (self):
        print("Soy un gato que habla")

    def mover (self):
        print("Soy un gato moviendose")

    def dormir (self):
        print("Soy un gato durmiendo")

    def comer (self):
        print("Soy un gato comiendo")

class Perro (Animal): 
    def hablar (self):
        print("Soy un perro que habla")

    def mover (self):
        print("Soy un perro moviendose")

    def dormir (self):
        print("Soy un perro durmiendo")

    def comer (self):
        print("Soy un perro comiendo")