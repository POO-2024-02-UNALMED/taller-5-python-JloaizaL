import sys
sys.path.append("C:/Users/Hogar/Documents/GitHub/taller-5-python-JloaizaL")
from .animal import Animal

class Ave(Animal):
    halcones = 0
    aguilas = 0

    def __init__(self, nombre=None, edad=None, habitat=None, genero=None, colorPlumas=None):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPlumas = colorPlumas
        Animal.aves += 1

    # Getters y Setters
    def getColorPlumas(self):
        return self._colorPlumas

    def setColorPlumas(self, colorPlumas):
        self._colorPlumas = colorPlumas

    @staticmethod
    def crearHalcon(nombre, edad, genero):
        Ave.halcones += 1
        return Ave(nombre, edad, "cielo", genero, "gris")

    @staticmethod
    def crearAguila(nombre, edad, genero):
        Ave.aguilas += 1
        return Ave(nombre, edad, "montañas", genero, "blanco")
