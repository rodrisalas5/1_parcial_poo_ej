class Pila: #Dinamica
    def __init__(self):
        #print("Se crea una pila vacia")
        self.items = []

    def apilar(self, x):
        self.items.append(x)
        print(f"Agrega el elemnto {x} a la pila")

    def desapilar(self):
        # print("Devuelve el elemento tope y lo elimina de la pila. Si la pila esta vacia levanta error.")
        try:
            return self.items.pop()
        except:
            print("La pila esta vacia")

    def ver_pila_original(self):
        for i in (self.items):
            print(i)

    def pila_vacia(self):
        if (len(self.items) == 0):
            return True
        else:
            return False

    def get_tamano(self):
        return len(self.items)

    def get_cima(self):
        return self.items[-1]

    #ordenada
    def ver_pila_reversed(self):
        for i in reversed(self.items):
            print(i)
        # for i in range(len(self.items)-1, -1, -1):
        #     print(i)