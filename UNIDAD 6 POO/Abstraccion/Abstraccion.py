from abc import ABC
from abc import abstractmethod

class Mando_abs(ABC):
  @abstractmethod
  def siguiente_canal(self):
      pass

  @abstractmethod
  def canal_anterior(self):
      pass

  @abstractmethod
  def subir_volumen(self):
      pass

  @abstractmethod
  def bajar_volumen(self):
      pass

class MandoSamsung(Mando_abs):
    def __init__(self, nombre, marca):
        self.nombre = nombre
        self.marca = marca

    def siguiente_canal(self):
        print("Samsung->Siguiente")

    def canal_anterior(self):
        print("Samsung->Anterior")

    def subir_volumen(self):
        print("Samsung->Subir")

    def bajar_volumen(self):
        print("Samsung->Bajar")

    def get_anio(self):
        print("Digo el ano.")

mando_samsung = MandoSamsung("control","Sansung")
mando_samsung.get_anio()