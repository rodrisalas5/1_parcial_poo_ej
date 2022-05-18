#Implementar una funcion que calcule la suma de todos los numeros enteros entre 0 y un numero positivo ingresado


    #SIN RECURSIVIDAD
def suma_numeros(numero):
    suma = 0
    for i in range(numero+1):
        suma += i
    return suma

print(f"La suma de numeros de 0 a 10 es: {suma_numeros(10)}")

    #CON RECURSIVIDAD
def suma_numeros_recursivo(numero):
    if numero == 0:
        return 0
    else:
        return numero + suma_numeros_recursivo(numero-1)

print(f"La suma de numeros de 0 a 10 es: {suma_numeros_recursivo(10)}")