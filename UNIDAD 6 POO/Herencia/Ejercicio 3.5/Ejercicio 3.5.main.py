""""
Crear una clase Persona unicamente con metodos estaticos.

Los metodos a crear son:
    1. Calcular edad, parametro ano de nacimiento
    2. Calcular peso promedio, parametro estatura y genero
    3. Calcular imc, parametro peso y altura 
"""
import clasePersona as cp

while True:
    opcion = input("""\nMENU:\n
    \t1 Calcular edad
    \t2 Calcular peso
    \t3 Calcular IMC
    \t4 Salir
    \nOpcion: """)
    if opcion == "1":
        while True:
            try:
                ano_nacimiento = int(input("Ingrese el ano de nacimiento: "))
                break
            except:
                print("Error, reitentar")
        print(cp.Persona.edad(ano_nacimiento))
    elif opcion == "2":
        while True:
            try:
                estatura = int(input("Ingrese la estatura: "))
                genero = input("Ingrese el genero: ")
                break
            except:
                print("Error, reitentar")
        print(cp.Persona.peso(estatura, genero))
    elif opcion == "3":
        while True:
            try:
                estatura = int(input("Ingrese la estatura: "))
                peso = int(input("Ingrese el peso: "))
                break
            except:
                print("Error, reitentar")
        print(cp.Persona.calcular_imc(peso, estatura))
    elif opcion == "4":
        break
    else:
        print("Opcion incorrecta, reintentar.")
