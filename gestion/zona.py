from zooAnimales.animal import Animal

class Zona:
    def __init__(self, nombre=None, zoo=None):
        self.nombre = nombre
        self.zoo = zoo
        self.animales = []

    def agregarAnimales(self, animal: Animal):
        self.animales.append(animal)

    def cantidadAnimales(self) -> int:
        return len(self.animales)

    def getNombre(self):
        return self.nombre

    def setNombre(self, nombre):
        self.nombre = nombre

    def getZoo(self):
        return self.zoo

    def setZoo(self, zoo):
        self.zoo = zoo

    def getAnimales(self):
        return self.animales

    def setAnimales(self, animales):
        self.animales = animales
