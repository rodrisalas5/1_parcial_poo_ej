'''
Crear una clase padre Colegio:

    Crear metodos para esta clase de:
        Constructor con: nombre, año, direccion
        seters y gettes
        get_clase (que clase es) 
        Crear una clase padre Club:

    Crear metodos para esta clase de:
        Constructor con: nombre, año, direccion
        seters y gettes
        get_clase (que clase es)

    Crear una clase Organizacion que herede de Colegio y Club:

    Crear un menu con las funciones de
        Crear Colegio, club o organizacion y guardar en una lista
        Listar
'''


class Colegio:
    def __init__(self, nombre, ano, direccion):
            self.nombre = nombre
            self.ano = ano
            self.direccion = direccion

    def get_nombre(self):
        print(f"Nombre: {self.nombre}")

    def get_ano(self):
        print(f"Ano: {self.ano}")
    
    def get_direccion(self):
        print(f"Direccion: {self.direccion}")

    def set_nombre(self, nombre_nuevo):
        self.nombre = nombre_nuevo
    
    def set_ano(self, ano_nuevo):
        self.ano = ano_nuevo

    def set_direccion(self, direccion_nuevo):
        self.direccion = direccion_nuevo

    def get_type(self):
        print("Soy una clase del tipo", type(self).__name__)

class Club:
    def __init__(self, nombre, ano, direccion):
            self.nombre = nombre
            self.ano = ano
            self.direccion = direccion

    def get_nombre(self):
        print(f"Nombre: {self.nombre}")

    def get_ano(self):
        print(f"Ano: {self.ano}")
    
    def get_direccion(self):
        print(f"Direccion: {self.direccion}")

    def set_nombre(self, nombre_nuevo):
        self.nombre = nombre_nuevo
    
    def set_ano(self, ano_nuevo):
        self.ano = ano_nuevo

    def set_direccion(self, direccion_nuevo):
        self.direccion = direccion_nuevo

    def get_type(self):
        print("Soy una clase del tipo", type(self).__name__)

class Organizacion(Colegio, Club):
    def __init__(self, nombre, ano, direccion):
        super().__init__(nombre, ano, direccion)

lista = []

def crear():
    nombre = input("Ingrese un nombre: ")
    ano = int(input("ingrese un ano: "))
    direccion = input("Ingrese la direccion: ")
    opcion = int(input("1. Colegio, 2. Club, 3. Organizacion: "))
    if opcion == 1:
        lista.append(Colegio(nombre, ano, direccion))
    elif opcion == 2:
        lista.append(Club(nombre, ano, direccion))
    else:
        lista.append(Organizacion(nombre, ano, direccion))

def listar():
    for i in lista:
        i.get_type()

while True:
    opcion = input("""MENU:
    \t1 Crear Colegio, club o organizacion y guardar en una lista
    \t2 Listar
    \t3 Salir
    \nOpcion: """)
    if opcion == "1":
        crear()
    elif opcion == "2":
        listar()
    elif opcion == "4":
        break
    else:
        print("Opcion incorrecta, reintentar.")

