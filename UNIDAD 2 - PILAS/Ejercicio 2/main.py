import clasePila as cp

lista_letras = ["a", "b", "a", "d", "a", "c"]

pila_1 = cp.Pila()
pila_aux = cp.Pila()

lista_vocales = ["a", "e", "i", "o", "u"]

for i in lista_letras:
    pila_1.apilar(i)
    pila_aux.apilar(i)

contador_vocales = 0

for j in range(pila_aux.get_tamanio()):
    if pila_aux.desapilar() in lista_vocales:
        contador_vocales += 1

print(f"La cantidad de vocales es de {contador_vocales}")