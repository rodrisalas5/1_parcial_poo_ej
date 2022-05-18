"""
Crear una clase abstracta informal y otra formal Auto con 2 metodos.
    adelante
    atras
    informal que no la obligo a usarla
    formar la obligo a que la use
"""
#FORMAL
from abc import ABC
from abc import abstractmethod

class Auto(ABC):
  @abstractmethod
  def adelante(self):
      print("Adelante")
  @abstractmethod
  def atras(self):
      print("Atras")

#INFORMAL
class Auto:
    def adelante(self):
        pass
    def atras(self):
        pass