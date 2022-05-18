#Una lista de palabras, que ordene por el largo

def orden_largo(lista):
    i = 0 
    control = True
    while(i <= len(lista)-2 and control):
        control = False
        for j in range(0, len(lista)-i-1):
            if (len(lista[j]) > len(lista[j+1])):
                lista[j], lista[j+1] = lista[j+1], lista[j]
                control = True
        i += 1

lista = ["hola", "que", "tal", "Rodrigo", "rojo", "violeta", "transparente"]
orden_largo(lista)
print(lista)