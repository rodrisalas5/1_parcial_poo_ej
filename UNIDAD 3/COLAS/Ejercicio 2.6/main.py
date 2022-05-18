# Utilizando la clase cola y sus metodos.
# Eliminar el i-esimo elemento despues del frente  de la cola.

import clasePila as cp
import claseCola as co

cola_1 = co.Cola()
pila_1 = cp.Pila()

cola_1.encolar("a")
cola_1.encolar("b")
cola_1.encolar("c")
cola_1.encolar("d")
cola_1.encolar("e")
cola_1.encolar("f")

cola_1.ver_cola()

for i in range(cola_1.tamano_cola()):
    pila_1.apilar(cola_1.desencolar())
for i in range(pila_1.get_tamanio()):
    cola_1.encolar(pila_1.desapilar())

cola_1.ver_cola()