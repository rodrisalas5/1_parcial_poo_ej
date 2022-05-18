#Crear un metodo de pila que elimine los numeros impares que estan encolados

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

    def eliminar_impar(self):
        for i in range(len(self.items)):
            if self.items[i]%2 != 0:
                self.items.pop(i)        

#Crear un metodo de pila que elimine los numeros impares que estan encolados
