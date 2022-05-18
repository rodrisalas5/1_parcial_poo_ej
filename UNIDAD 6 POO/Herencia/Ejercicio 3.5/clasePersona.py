class Persona:
    @staticmethod
    def calcular_imc (peso, estatura):
        return peso/(estatura**2)

    @staticmethod
    def peso (estatura, genero):
        if genero == "F":
            return estatura-20
        else:
            return estatura-10

    @staticmethod
    def edad (ano_nacimiento):
        return (2022-ano_nacimiento)