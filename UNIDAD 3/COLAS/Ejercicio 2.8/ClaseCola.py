class Cola:
    """ Representa a una cola, con operaciones de encolar y desencolar.
        El primero en ser encolado es también el primero en ser desencolado.
    """

    def __init__(self):
        """ Crea una cola vacía. """
        # La cola vacía se representa por una lista vacía
        self.items=[]

    def encolar(self, x):
        """ Agrega el elemento x como último de la cola. """
        self.items.append(x)

    def desencolar(self):
        """Elimina el primer elemento de la cola y devuelve su
            valor. Si la cola está vacía, levanta ValueError."""
        try:
            return self.items.pop(0)
        except:
            raise ValueError("La cola está vacía")
    
    def es_vacia(self):
        """ Devuelve True si la cola esta vacía, False si no."""
        return self.items == []
    
    def ver_cola(self): 
        for i in range(len(self.items)-1, -1, -1):
            if i == len(self.items)-1:
                print("Final", end =" ")
            print(self.items[i], end =" ")
            if i == 0:
                print("Frente", end =" ")
        print("")
    
    def recorrer_cola(self): 
        for i in range(len(self.items)-1, -1, -1):
            print(f"Elemento {self.items[i]}")

    def tamano_cola(self):
        return len(self.items)
    
    def obtener_cabezera(self):
        return print(f"\nEl frente es: {self.items[0]}")

    def obtener_final(self):
        return print(f"\nEl final es: {self.items[-1]}")

    def mover_cabeza_al_final(self):
        try:
            self.items.append(self.items.pop(0))
        except:
            raise ValueError("La cola está vacía")
        
    def agregar_con_prioridad(self, prioridad, x):
        if prioridad == 0:
            #Se agrega al frente de la cola
            self.items.insert(0, x)
        elif prioridad == 1:
            self.items.insert(1,x)
        else:
            self.items.insert((len(self.items)/2)-1, x)