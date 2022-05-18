def cuenta_regresiva(numero):
    numero -= 1
    if numero > 0:
        print(numero)
        cuenta_regresiva(numero)
    else:
        print("BOOOOM")
    print("Fin de la funcion", numero)

cuenta_regresiva(5)        