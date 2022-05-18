# Utilizando la clase cola y sus metodos.
# Eliminar el i-esimo elemento despues del frente  de la cola.

import claseCola as co

cola_1 = co.Cola()

cola_1.encolar(3)
cola_1.encolar(4)
cola_1.encolar(5)
cola_1.encolar(6)
cola_1.encolar(7)
cola_1.encolar(8)

cola_1.ver_cola()

while True:
    try:
        numero = int(input("Ingrese el i-esimo elemento de la cola a eliminar(no puede ser el primero): "))
    except:
        print("Error, reintentar.")
    if (numero <= 1 or numero > cola_1.tamano_cola()): #No puede ser el frente por requisito
        print("No puede ser el primero o el mismo tamano de la cola")
    else:
        break

for i in range(cola_1.tamano_cola()):
    if i == numero-1:
        print(f"Se elimino el emento {cola_1.desencolar()}")
    else:
        cola_1.mover_cabeza_al_final()

cola_1.ver_cola()