from datetime import date, time, datetime
import clase as cl

listaPersonas = []

class Gestor:
    def crear_empleado(self):
        #Pedimos DNI
        flag_while = True
        while flag_while:
            try:
                flag = True
                dni = int(input("Ingrese el DNI de la persona: "))
                for persona in listaPersonas:
                    if dni == persona.get_dni():
                        flag = False
                if flag == True and dni > 99 and dni < 1000:
                    flag_while = False
                elif flag == False:
                    print("DNI ya registrado.")
                    return #Retorno por que a mi criterio se confundio y desea agregar a alguien existente
                else:
                    print("El DNI no cumple los requerimientos, reintentar.")
            except:
                print("El DNI no cumple los requerimientos, reintentar.")
        while True:
            nombre = input("Ingrese el nombre: ").capitalize()
            if nombre.isalpha():
                break
            else:
                print("Reintentar, el nombre debe ser solamente alfabetico")
        while True:
            apellido = input("Ingrese el apellido: ").capitalize()
            if apellido.isalpha():
                break
            else:
                print("Reintentar, el apellido debe ser solamente alfabetico")
        while True:
            funcion = input("Ingrese el funcion: ").capitalize()
            if funcion.isalpha():
                break
            else:
                print("Reintentar, la funcion debe ser solamente alfabetico")
        while True:
            try: 
                fecha_ingresada = datetime.strptime(input("Ingrese el ano de ingreso del empleado dd/mm/yyyy: "),
                                                    '%d/%m/%Y')
                break
            except:
                print("Reintentar, fecha mal ingresada.")
        listaPersonas.append(cl.Empleado(dni, nombre, apellido, funcion, fecha_ingresada))
        return print("\nPersona agregado existosamente!!!")

    def eliminar(self):
        for i in range(len(listaPersonas)):
            if i == (len(listaPersonas)-1):
                listaPersonas.pop(len(listaPersonas)-1)
        print("Ultimo empleado eliminado con exito!!!")

    def listar(self):
        for persona in listaPersonas:
            persona.presentarse()

    def listar_por_DNI_ascendente(self):
        listaDNI = []
        for persona in listaPersonas:
            listaDNI.append(persona.dni)
        listaDNI.sort()
        for i in range(len(listaDNI)):
            for persona in listaPersonas:
                if listaDNI[i] == persona.dni:
                    persona.presentarse()

    def listar_por_DNI_descendente(self):
        listaDNI = []
        for persona in listaPersonas:
            listaDNI.append(persona.dni)
        listaDNI.sort(reverse = True)
        for i in range(len(listaDNI)):
            for persona in listaPersonas:
                if listaDNI[i] == persona.dni:
                    persona.presentarse()

    def listar_fecha_ascendente(self):
        lista_aux_ordenada = []
        objeto_menor = listaPersonas[0]#suponemos que es el menor para arrancar
        
        while(len(listaPersonas) > 0): #Hasta que se vacie
            for persona in listaPersonas:
                if (persona.get_fecha() < objeto_menor.get_fecha()):
                    objeto_menor = persona
            lista_aux_ordenada.append(objeto_menor) #agrego el menor
            listaPersonas.remove(objeto_menor)

        listaPersonas = lista_aux_ordenada
        self.presentarse()

    def listar_fecha_descendente(self):
        listaFechas= []
        for persona in listaPersonas:
            listaFechas.append(persona.ano_ingreso)
        listaFechas.sort(reverse = True)
        for i in range(len(listaFechas)):
            for persona in listaPersonas:
                if listaFechas[i] == persona.ano_ingreso:
                    persona.presentarse_con_fecha()
