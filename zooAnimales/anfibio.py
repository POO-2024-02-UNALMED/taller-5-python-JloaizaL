import sys
sys.path.append("C:/Users/Hogar/Documents/GitHub/taller-5-python-JloaizaL")

from zooAnimales.animal import Animal

class Anfibio(Animal):
    ranas = 0
    salamandras = 0

    def __init__(self, nombre="", edad=0, habitat="", genero="", colorPiel="", venenoso=False):
        super().__init__(nombre, edad, habitat, genero)
        self.colorPiel = colorPiel
        self.venenoso = venenoso
        Animal.anfibios += 1

    @staticmethod
    def crearRana(nombre, edad, genero):
        Anfibio.ranas += 1
        return Anfibio(nombre, edad, "charcos", genero, "verde", False)

    @staticmethod
    def crearSalamandra(nombre, edad, genero):
        Anfibio.salamandras += 1
        return Anfibio(nombre, edad, "bosques", genero, "amarillo", True)

    def movimiento(self):
        return "saltar"
