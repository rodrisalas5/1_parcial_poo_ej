# El programa debe:
    # Contar con:
    # Contar con una Clase  con los atributos (dni (int - único), nombre (string), apellido (string))
    # Contar con una Clase Hija  que use el constructor de la clase padre con los atributos:
        # funcion (string)
        # año_ingreso (string 'yyyy')
# Se deben crear los siguientes métodos para la clase padre Persona (que heredará la clase hija):
    # Set y Get dni.
# Se deben crear los siguientes métodos para la clase hija.
    # Set y Get funcion.
# Se debe contar y crear funciones para un menu que tenga las siguiente opciones,
    # Crear un empleado y guardarlo en una lista_empleados
    # Recorrer la lista de empleados segun DNI, mayor a menor o menor a mayor
    # Recorrer la lista de empleados segun fecha_ingreso, mayor a menor o menor a mayor
    # Eliminar el ultimo empleado agregado
# IMPORTANTE:
    # Se deben crear metodos y clases a criterio
    # Gestionar posibles errores
    # Estructurar el programa a criterio propio

import Gestor as gp

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
