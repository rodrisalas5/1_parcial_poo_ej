#Dada una lista de letrar, modificar el algoritmo de seleccion para que ordene por orden alfabetico.

def seleccion(lista):
  for i in range(0,len(lista)-1): #Como ya lo ubique entonces no recorro todo de nuevo
    minimo = i #Para determinar el minimo de la lista, toma el primiro como el minimo
    for j in range(i+1,len(lista)): #El i ya lo toma como minimo, no lo tiene en cuenta
        #El i+1 por que no me voy a comparar el mismo minimo
        if(lista[minimo] > lista[j]):
            minimo = j  
    lista[i],lista[minimo] = lista[minimo],lista[i]

lista = ["c", "f", "a", "j", "b",]
seleccion(lista)
print(lista)