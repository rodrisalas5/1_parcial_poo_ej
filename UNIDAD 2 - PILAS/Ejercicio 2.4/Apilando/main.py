"""
Ejercicio 2.4
Utilizando la clase Pila y sus métodos
*  Permitir que el usuario cargue una palabra y cargar letra a letra en una Pila
*  Con métodos de la pila visualizarla en forma inversa.
"""
import clasePila as pi
pila = pi.Pila()

palabra = input("Por favor ingrese una palabra: ")

for i in palabra:
    pila.apilar(i)

pila.ver_pila()

letra_a_reemplazar = input("Ingrese la letra que quiere reemplazar: ")
letra_que_reemplaza = input("Ingrese la letra que la reemplazara: ")

pila_aux = pi.Pila()

for i in range(pila.get_tamanio()):
    elemento = pila.desapilar()
    if elemento == letra_a_reemplazar:
        pila_aux.apilar(letra_que_reemplaza)
    else:
        pila_aux.apilar(elemento)

print("Pila al con elemento reemplazado y desordenada")
pila_aux.ver_pila()

#volvemos a apilar la pila inicial
for i in range(pila_aux.get_tamanio()):
    pila.apilar(pila_aux.desapilar())

print("Pila al con elemento reemplazado y ordenada")
pila.ver_pila()