#Obtener los numeros de una N sucesion de Fibonacci
#Fibonacci suma los dos ultimos numeros

    #SIN RECURSIVIDAD
def fibonacci(n):
    n_0 = 0
    n_1 = 1
    suma = n_0 + n_1
    while (suma < n):
        suma = n_0 + n_1
        n_0 = n_1
        n_1 = suma
        if suma < n:
            print(suma)

# fibonacci(90)

    #CON RECURSIVIDAD
def fibonnaci_recursiva(numero):
    if numero == 0:
        return 0
    elif numero == 1:
        return 1
    else:
        return fibonnaci_recursiva(numero - 1) + fibonnaci_recursiva (numero - 2)

for i in range(90):
    if fibonnaci_recursiva(i) < 90:
        print(fibonnaci_recursiva(i))
