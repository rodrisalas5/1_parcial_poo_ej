class Pila: #Dinamica
    def __init__(self):
        print("Se crea una pila vacia")
        self.items = []

    def apilar(self, x):
        self.items.append(x)

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

    def get_tamanio(self):
        return len(self.items)

    #ordenada
    def ver_pila(self):
        for i in reversed(self.items):
            print(i)
        # for i in range(len(self.items)-1, -1, -1):
        #     print(i)

    def contar_letra(self):
        contador = 0
        letra_a_contar = input("Ingrese la letra a buscar: ")
        for i in  self.items:
            if i == letra_a_contar:
                contador = contador + 1
        return print(f"La letra {letra_a_contar} esta {contador} veces en la pila")
