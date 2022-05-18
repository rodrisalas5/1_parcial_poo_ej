import ClaseCola as cl

cola = cl.Cola()
cola_aux = cl.Cola()

class Gestor:
    def agregar_numero(self):
        flag = True
        while flag:
            try:
                valor_a_agregar = int(input("Ingrese un numero o el numero cero para dejar de ingresar: "))
                if valor_a_agregar != 0:
                    cola.encolar(valor_a_agregar)
                else:
                    flag = False
            except:
                print("Reintentar, no ha agregado un numero entero.")
    
    def agregar_prioridad(self):
        flag = True
        while flag:
            try:
                valor_a_agregar = int(input("Ingrese un numero a ingresar con prioridad: "))
                flag = False
            except:
                print("Reintentar, no ha agregado un numero entero.")

        while True:
            prioridad = int(input("""
            Prioridad = 0 se agrega al frente de la cola
            Prioridad = 1 se agrega al segundo en la cola
            Prioridad = 2 se agrega tercero en la cola
            Ingrese la prioridad: """))
            if prioridad == 0 or prioridad == 1 or prioridad == 2:
                break
            else:
                print("Incorrecto, reintentar.")
        cola.agregar_con_prioridad(prioridad, valor_a_agregar)

    def ver_cola(self):
        cola.ver_cola()