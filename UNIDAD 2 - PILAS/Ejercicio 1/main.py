import clasePila as cp

pila_1 = cp.Pila() #Creo una pila nueva
print(pila_1.pila_vacia())

# pila_1.apilar(2)
# pila_1.apilar(3)
# pila_1.apilar(4)
# print("Veamos la pila")
# pila_1.ver_pila_original()
# print("Voy a desapilar")
# pila_1.desapilar()
# print("Veamos la pila")
# pila_1.ver_pila_original()

pila_1.apilar("a")
pila_1.apilar("b")
pila_1.apilar("a")
pila_1.apilar("c")
pila_1.apilar("a")
pila_1.apilar("b")
pila_1.apilar("c")
print("Veamos la pila")
pila_1.ver_pila_original()

pila_1.contar_letra()
