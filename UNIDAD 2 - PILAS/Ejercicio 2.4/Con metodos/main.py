"""Ejercicio 2.4
Utilizando la clase Pila y sus métodos
*  Permitir que el usuario cargue una palabra y cargar letra a letra en una Pila
*  Con métodos de la pila visualizarla en forma inversa."""
import clasePila as cp

pila = cp.Pila()

while True:
    palabra = input("Ingrese una palabra a agregar letra a letra en la pila: ")
    if palabra.isalpha():
        print("\n")
        break
    else:
        print("ERROR, no ha ingresado una palabra. Reintentar.")

for i in palabra:
    pila.apilar(i)

print("\nPila original")
pila.ver_pila_original()

print("\nPila inversa")
pila.ver_pila_reversed()