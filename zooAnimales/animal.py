class Animal:
    totalAnimales = 0
    mamiferos = 0
    aves = 0
    reptiles = 0
    peces = 0
    anfibios = 0

    def __init__(self, nombre=None, edad=None, habitat=None, genero=None):
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        Animal.totalAnimales += 1

    # Getters y Setters para nombre
    def getNombre(self):
        return self._nombre

    def setNombre(self, nombre):
        self._nombre = nombre

    # Getters y Setters para edad
    def getEdad(self):
        return self._edad

    def setEdad(self, edad):
        self._edad = edad

    # Getters y Setters para habitat
    def getHabitat(self):
        return self._habitat

    def setHabitat(self, habitat):
        self._habitat = habitat

    # Getters y Setters para genero
    def getGenero(self):
        return self._genero

    def setGenero(self, genero):
        self._genero = genero

    def movimiento(self) -> str:
        return "desplazarse"

    @staticmethod
    def totalPorTipo():
        return (f"Mamiferos: {Animal.mamiferos}\n"
                f"Aves: {Animal.aves}\n"
                f"Reptiles: {Animal.reptiles}\n"
                f"Peces: {Animal.peces}\n"
                f"Anfibios: {Animal.anfibios}")

    def __str__(self):
        return (f"Mi nombre es {self._nombre}, tengo una edad de {self._edad}, "
                f"habito en {self._habitat} y mi genero es {self._genero}")
