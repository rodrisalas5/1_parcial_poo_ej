#Dada una lista de objetos de una clase, modificar el algoritmo de burbuja para que ordene 
#por el determinado atributo de estas

class Persona:
    def __init__(self, dni, nombre, apellido):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido

    def set_dni(self, dni_nuevo):
        self.dni = dni_nuevo

    def get_dni(self):
        return self.dni

lista_personas = []
persona_1 = Persona(dni = "200", nombre = "Rodrigo", apellido = "Salas")
persona_2 = Persona(dni = "100", nombre = "Ramiro", apellido = "Salas")
persona_3 = Persona(dni = "300", nombre = "Ricardo", apellido = "Salas")
lista_personas.append(persona_1)
lista_personas.append(persona_2)
lista_personas.append(persona_3)

def imprimir_lista(lista):
    for i in lista:
        print(i.get_dni(), end = ",")
    print("")

def orden_largo(lista, atributo):
    if atributo == "dni":
        i = 0 
        control = True
        while(i <= len(lista)-2 and control):
            control = False
            for j in range(0, len(lista)-i-1):
                if (lista[j].get_dni() > lista[j+1].get_dni()):
                    lista[j], lista[j+1] = lista[j+1], lista[j]
                    control = True
                    imprimir_lista(lista)
            i += 1


orden_largo(lista_personas, atributo = "dni")

