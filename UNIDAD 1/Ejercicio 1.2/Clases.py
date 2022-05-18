class Persona:
    def __init__(self, dni, nombre, apellido):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido

    def set_dni(self, numero_dni):
        self.dni = numero_dni

    def get_dni(self):
        return self.dni
    
    def presentarse(self):
        print(f"\t\t{self.nombre} - {self.apellido} - DNI = {self.dni}")



class Empleado (Persona):
    def __init__(self, dni, nombre, apellido, funcion, ano_ingreso):
        super().__init__(dni, nombre, apellido)
        self.funcion = funcion
        self.ano_ingreso = ano_ingreso

    def set_funcion(self, numero_funcion):
        self.funcion = numero_funcion

    def get_funcion(self):
        return self.funcion

    def presentarse_con_fecha(self):
        print(f"\t\t{self.nombre} - {self.apellido} - Ano de ingreso = {self.ano_ingreso}")
