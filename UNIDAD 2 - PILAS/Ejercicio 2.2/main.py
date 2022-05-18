"""Utilizando la clase Pila y sus metodos
*  Permitir que el usuario cargue valores en una Pila
*  Determinar el número de ocurrencias de un determinado elemento en una pila."""

import clasePila as cp

pila_1 = cp.Pila()

while True:
    x = input("Ingrese lo que desea ingresar a la pila, si ingresa BASTA se corta el ingreso: ")
    if x == "BASTA":
        break
    else:
        pila_1.apilar(x)

contador = 0

ocurrencia_a_contar = input("Ingrese la palabra a buscar: ")

for i in range(pila_1.get_tamano()):
    if pila_1.desapilar() == ocurrencia_a_contar:
        contador += 1

print(f"La letra {ocurrencia_a_contar} esta {contador} veces en la pila")