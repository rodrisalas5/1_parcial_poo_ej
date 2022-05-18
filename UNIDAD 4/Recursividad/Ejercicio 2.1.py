#Calcular el producto con recursividad

def multiplicar(numero, multiplo, resultado):
    if multiplo == 0:
        return resultado
    else:
        resultado += numero
        return multiplicar(numero, multiplo-1, resultado)

numero = int(input("Ingrese el numero que quiere multiplicar: "))
multiplo = int(input("Ingrese el numero a multiplicar: "))


print(f"{numero} x {multiplo} es {multiplicar(numero, multiplo, resultado = 0)}")


# def multiplicar(numero, multiplo):
#     if (multiplo == 0):
#         return 0
#     else:
#         return numero + multiplicar(numero, multiplo-1)

# print(multiplicar(3,5))