import sys
sys.path.append("C:/Users/Hogar/Documents/GitHub/taller-5-python-JloaizaL")
from .animal import Animal

class Anfibio(Animal):
    ranas = 0
    salamandras = 0

    def __init__(self, nombre=None, edad=None, habitat=None, genero=None, colorPiel=None, venenoso=False):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPiel = colorPiel
        self._venenoso = venenoso
        Animal.anfibios += 1

    # Getters y Setters
    def getColorPiel(self):
        return self._colorPiel

    def setColorPiel(self, colorPiel):
        self._colorPiel = colorPiel

    def isVenenoso(self):
        return self._venenoso

    def setVenenoso(self, venenoso):
        self._venenoso = venenoso

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
