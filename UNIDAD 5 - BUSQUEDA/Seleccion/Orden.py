def seleccion(lista):
  for i in range(0,len(lista)-1):
    minimo = i
    print(f"minimo i: {lista[minimo]}")
    for j in range(i+1,len(lista)):
      if(lista[minimo] > lista[j]):
        minimo = j
        print(f"minimo j: {lista[minimo]}")
      print(lista)
    lista[i],lista[minimo] = lista[minimo],lista[i]


#lista = [1,2,3,4,5,6,7,8]
lista = [8,7,6,5,4,3,2,1]
seleccion(lista)
print(lista)