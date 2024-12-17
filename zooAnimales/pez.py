import sys
sys.path.append("C:/Users/Hogar/Documents/GitHub/taller-5-python-JloaizaL")
from .animal import Animal

class Pez(Animal):
    salmones = 0
    bacalaos = 0

    def __init__(self, nombre=None, edad=None, habitat=None, genero=None, colorEscamas=None, cantidadAletas=None):
        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas = colorEscamas
        self._cantidadAletas = cantidadAletas
        Animal.peces += 1

    # Getters y Setters
    def getColorEscamas(self):
        return self._colorEscamas

    def setColorEscamas(self, colorEscamas):
        self._colorEscamas = colorEscamas

    def getCantidadAletas(self):
        return self._cantidadAletas

    def setCantidadAletas(self, cantidadAletas):
        self._cantidadAletas = cantidadAletas

    @staticmethod
    def crearSalmon(nombre, edad, genero):
        Pez.salmones += 1
        return Pez(nombre, edad, "océanos", genero, "rosado", 2)

    @staticmethod
    def crearBacalao(nombre, edad, genero):
        Pez.bacalaos += 1
        return Pez(nombre, edad, "mares", genero, "blanco", 3)
