"""
Utilizando unicamente la clase Pila y sus metodos dados.
    Crear una funcion me devuelva la cantidad de datos tipo string de una pila.
    Importante: La pila al finalizar la funcion tiene que quedar igual.
"""


class Pila:
    def __init__(self):
      print("Crea una pila vacía.")
      self.items=[]
    
    def apilar(self, x):
      print(f"Agrega el elemento {x} a la pila.")
      self.items.append(x)
    
    def desapilar(self):
      try:
        return self.items.pop()
      except IndexError:
        raise ValueError("La pila está vacía")
    
    def ver_pila(self):
      print("-----PILA-----")
      for i in reversed(self.items):
        print(i)
      print("--------------")
    
    def get_tamanio(self):
      return len(self.items)

def contar_string(pila_1):
    pila_aux = Pila()
    contador = 0
    for i in range(pila_1.get_tamanio()):
        dato = pila_1.desapilar()
        if type(dato) == type("str"):
            contador += 1
        pila_aux.apilar(dato)

    #vuelvo la pila a su formato original
    for i in range(pila_aux.get_tamanio()):
        pila_1.apilar(pila_aux.desapilar())

    print(f"Hay {contador} datos string")




pila_1 = Pila()
pila_1.apilar(2)
pila_1.apilar("Soy un string")
pila_1.apilar("Soy otro string")
pila_1.apilar(5)
pila_1.apilar(6)
pila_1.apilar("Yo tambien soy otro string")
pila_1.ver_pila()
contar_string(pila_1)
pila_1.ver_pila()