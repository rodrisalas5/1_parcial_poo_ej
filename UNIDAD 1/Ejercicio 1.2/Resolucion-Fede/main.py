#SOLO LA PARTE DE FECHA ASCENDENTE

import gestor as gp

gestor = gp.Gestor()

while True:
    opcion = input ("""
    --- MENU PRINCIPAL ---
    1. Crear un empleado
    2. Ver empleados segun DNI
    3. Ver empleados segun fecha de ingreso
    4. Eliminar ultimo empleado creado
    5. Listar personas
    6. Salir
    Opcion: """)
    if opcion == "1":
        gestor.crear_empleado()
    elif opcion == "2":
        while True:
            try: 
                orden = int(input("Indique 1 para imprimir ascendentemente o 2 para imprimir descendentemente: "))
                if orden == 1:
                    gestor.listar_por_DNI_ascendente()
                    break
                elif orden == 2:
                    gestor.listar_por_DNI_descendente()
                    break
                else:
                    print("Reintentar, recuerde que puede ser opcion 1 u opcion 2.")
            except:
                    print("Reintentar, recuerde que debe ingresar solo numeros.")
    elif opcion == "3":
        while True:
            try: 
                orden = int(input("Indique 1 para imprimir ascendentemente o 2 para imprimir descendentemente: "))
                if orden == 1:
                    gestor.listar_fecha_ascendente()
                    break
                elif orden == 2:
                    gestor.listar_fecha_descendente()
                    break
                else:
                    print("Reintentar, recuerde que puede ser opcion 1 u opcion 2.")
            except:
                    print("Reintentar, recuerde que debe ingresar solo numeros.")
    elif opcion == "4":
        gestor.eliminar()
    elif opcion == "5":
        gestor.listar()
    elif opcion == "6":
        break
    else:
        print("Error, valor no valido.")