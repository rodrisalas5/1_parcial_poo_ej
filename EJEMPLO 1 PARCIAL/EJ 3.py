"""Utilizando unicamente la clase Cola y sus metodos dados 
(si es necesario tmb se puede utilizar la clase PILA).
    Crear una funcion me devuelva la cantidad de datos tipo int de una cola.
    Importante: La cola al finalizar la funcion tiene que quedar igual."""

#clase PILA
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

#clase COLA
class Cola:
    def __init__(self):
        self.items=[]

    def encolar(self, x):
        self.items.append(x)

    def desencolar(self):
        try:
            return self.items.pop(0)
        except:
            raise ValueError("La cola está vacía")
    
    def es_vacia(self):
        return self.items == []
    
    def ver_cola(self): 
        for i in range(len(self.items)-1, -1, -1):
            if i == len(self.items)-1:
                print("Final", end =" ")
            print(self.items[i], end =" ")
            if i == 0:
                print("Frente", end =" ")

def contar_int(cola_1):
    contador = 0
    cola_aux = Cola()
    while cola_1.es_vacia() == False:
        dato = cola_1.desencolar()
        if type(dato) == type(123):
            contador += 1
        cola_aux.encolar(dato)

    while cola_aux.es_vacia() == False:
        cola_1.encolar(cola_aux.desencolar())

    print(f"Hay {contador} datos enteros")

cola_1 = Cola()
cola_1.encolar(2)
cola_1.encolar(3)
cola_1.encolar(4)
cola_1.encolar("string")
cola_1.encolar(6)
cola_1.encolar("string")
cola_1.encolar(8)
contar_int(cola_1)
cola_1.ver_cola()