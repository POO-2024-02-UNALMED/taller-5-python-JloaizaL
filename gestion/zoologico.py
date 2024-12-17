from gestion.zona import Zona

class Zoologico:
    def __init__(self, nombre=None, ubicacion=None):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.zonas = []

    def agregarZonas(self, zona: Zona):
        self.zonas.append(zona)

    def cantidadTotalAnimales(self) -> int:
        return sum(zona.cantidad_animales() for zona in self.zonas)

    def getNombre(self):
        return self.nombre

    def setNombre(self, nombre):
        self.nombre = nombre

    def getUbicacion(self):
        return self.ubicacion

    def setUbicacion(self, ubicacion):
        self.ubicacion = ubicacion

    def getZonas(self):
        return self.zonas

    def setZonas(self, zonas):
        self.zonas = zonas
