import sys
sys.path.append("C:/Users/Hogar/Documents/GitHub/taller-5-python-JloaizaL")
from .animal import Animal

class Mamifero(Animal):
    caballos = 0
    leones = 0

    def __init__(self, nombre=None, edad=None, habitat=None, genero=None, pelaje=None, patas=None):
        super().__init__(nombre, edad, habitat, genero)
        self._pelaje = pelaje
        self._patas = patas
        Animal.mamiferos += 1

    # Getters y Setters
    def getPelaje(self):
        return self._pelaje

    def setPelaje(self, pelaje):
        self._pelaje = pelaje

    def getPatas(self):
        return self._patas

    def setPatas(self, patas):
        self._patas = patas

    @staticmethod
    def crearCaballo(nombre, edad, genero):
        Mamifero.caballos += 1
        return Mamifero(nombre, edad, "pradera", genero, True, 4)

    @staticmethod
    def crearLeon(nombre, edad, genero):
        Mamifero.leones += 1
        return Mamifero(nombre, edad, "selva", genero, True, 4)
