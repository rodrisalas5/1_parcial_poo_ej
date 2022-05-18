#Dada una cola de números cargados aleatoriamente, 
#eliminar de ella todos los que no sean primos.

import claseCola as cl

cola = cl.Cola()
cola_aux = cl.Cola()

while True:
    try:
        #Pide el 0 por que no cumple ser primo por regla.
        valor_a_agregar = int(input("Ingrese un numero o el numero cero para dejar de ingresar: "))
        if valor_a_agregar != 0:
            cola.encolar(valor_a_agregar)
        else:
            break
    except:
        print("Reintentar, no ha agregado un numero natural.")

print("")
cola.ver_cola()
print("")

i = 1 #Deben arrancar en 1 ya que no pueden ser divididos por 0
n = 1

for i in cola.items: #Recorro la cola, i es cada elemento
    contador_divisores = 0 #Va a determinar la cantidad de divisores de cada numero
    #Este bucle divide cada elemento por todos los divisores posibles e incluso hasta por si mismo
    for n in range(1, i+1): #i+1 Para que se divida por su mismo numero
        print(f"Numero {i} divido por {n} da resto {i % n}") #Muestra la operacion que va realizando el bucle
        if i % n == 0: #Si el modulo es 0 entonces es divisible
            contador_divisores = contador_divisores + 1
    if contador_divisores == 2: #Por definicion, los primos solo tienen dos divisores
        print(f"{i} es primo")
        cola_aux.encolar(i) #En una lista auxiliar agrego el numero
    else:
        print(f"No se agrego el numero {i} a la cola de numeros primos")

print("\nSe han eliminado los numeros no primos")
cola = cola_aux #Igualo la cola, a la cola de numeros primos. Antes de esta linea la cola original no se habia modificado
print("La cola de numeros primos es: \n")
cola.ver_cola()