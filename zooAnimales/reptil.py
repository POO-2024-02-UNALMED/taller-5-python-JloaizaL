from zooAnimales.animal import Animal

class Reptil(Animal):
    iguanas = 0
    serpientes = 0

    def __init__(self, nombre=None, edad=None, habitat=None, genero=None, colorEscamas=None, largoCola=None):
        super().__init__(nombre, edad, habitat, genero)
        self.colorEscamas = colorEscamas
        self.largoCola = largoCola
        Animal.reptiles += 1

    @staticmethod
    def crearIguana(nombre, edad, genero):
        Reptil.iguanas += 1
        return Reptil(nombre, edad, "selvas", genero, "verde", 5)

    @staticmethod
    def crearSerpiente(nombre, edad, genero):
        Reptil.serpientes += 1
        return Reptil(nombre, edad, "desiertos", genero, "marron", 3)
