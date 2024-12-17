import sys
sys.path.append("C:/Users/Hogar/Documents/GitHub/taller-5-python-JloaizaL")
from .animal import Animal

class Reptil(Animal):
    iguanas = 0
    serpientes = 0

    def __init__(self, nombre=None, edad=None, habitat=None, genero=None, colorEscamas=None, largoCola=None):
        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas = colorEscamas
        self._largoCola = largoCola
        Animal.reptiles += 1

    # Getters y Setters
    def getColorEscamas(self):
        return self._colorEscamas

    def setColorEscamas(self, colorEscamas):
        self._colorEscamas = colorEscamas

    def getLargoCola(self):
        return self._largoCola

    def setLargoCola(self, largoCola):
        self._largoCola = largoCola

    @staticmethod
    def crearIguana(nombre, edad, genero):
        Reptil.iguanas += 1
        return Reptil(nombre, edad, "selvas", genero, "verde", 5)

    @staticmethod
    def crearSerpiente(nombre, edad, genero):
        Reptil.serpientes += 1
        return Reptil(nombre, edad, "desiertos", genero, "marron", 3)
