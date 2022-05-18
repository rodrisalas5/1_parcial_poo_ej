"""Reemplazar un elemento de la pila por una palabra deseada.
Tiene que quedar ordenada como antes"""

import clasePila as cp

pila_1 = cp.Pila()

while True:
    x = input("Ingrese lo que desea ingresar a la pila, si ingresa BASTA se corta el ingreso: ")
    if x == "BASTA":
        break
    else:
        pila_1.apilar(x)

print("\n")
print("Pila al inicio:")
pila_1.ver_pila()
print("\n")

ocurrencia_a_reemplazar = input("Ingrese la palabra a reemplazar: ")
ocurrencia_que_reemplaza = input("Ingrese la palabra que reemplazara: ")

pila_aux = cp.Pila()

for i in range(pila_1.get_tamano()):
    elemento = pila_1.desapilar()
    if elemento == ocurrencia_a_reemplazar:
        pila_aux.apilar(ocurrencia_que_reemplaza)
    else:
        pila_aux.apilar(elemento)


for i in range(pila_aux.get_tamano()):
    pila_1.apilar(pila_aux.desapilar())

print("\n")
print("Asi quedo la pila 1 reemplazada:")
pila_1.ver_pila()



