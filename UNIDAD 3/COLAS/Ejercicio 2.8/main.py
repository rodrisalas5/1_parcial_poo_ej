# Crear un metodo de cola que permita agregar un elemento con cierta prioridad
# P = 0 se agrega al frente de la cola
# P = 1 se agrega al segundo en la cola
# P = 2 se agrega terccero en la cola

import gestor as gp

gestor = gp.Gestor()

while True:
    opcion = input("""MENU:
    \t1 Agregar con prioridad
    \t2 Agregar elementos a la cola
    \t3 Ver cola
    \t4 Salir
    \nOpcion: """)
    if opcion == "1":
        gestor.agregar_prioridad()
    elif opcion == "2":
        gestor.agregar_numero()
    elif opcion == "3":
        gestor.ver_cola()
    elif opcion == "4":
        break
    else:
        print("Opcion incorrecta, reintentar.")
