def burbuja(lista):
    for i in range(0, len(lista)-1):
        # print(f"i = {i}")
        for j in range(0, len(lista)-i-1): #Para que no tome uno que ya itero
            # print(f"j = {j}")
            if (lista[j] > lista[j+1]):
                # print(f"Entre al if por que {(lista[j])} > {lista[j+1]}")
                # print(f"entonces hago {lista[j], lista[j+1]} = {lista[j+1], lista[j]}")
                lista[j], lista[j+1] = lista[j+1], lista[j]
                #print(lista)

lista = [8, 7, 6, 5, 4, 3, 2, 1]
burbuja(lista)
print(lista)

#No es eficiente, recorre todo aunque este ordenada por ende entrea al bucle
#Se van comparando de a uno, uno con el de la derecha

def burbuja_mejorada(lista):
    i = 0 
    control = True
    while(i <= len(lista)-2 and control): #El menor o igual compara hasta el ultimo
        control = False #No entra al proximo si esta ordenado
        for j in range(0, len(lista)-i-1):
            if (lista[j] > lista[j+1]):
                lista[j], lista[j+1] = lista[j+1], lista[j]
                control = True
        i += 1

lista = [8, 7, 6, 5, 4, 3, 2, 1]
burbuja_mejorada(lista)
print(lista)