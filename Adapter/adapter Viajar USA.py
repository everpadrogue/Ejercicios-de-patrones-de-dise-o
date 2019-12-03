
from abc import ABC, abstractmethod

class AplicacionViaje(ABC):
    @abstractmethod
    def attak(self):
        pass
class ViajeNacional(AplicacionViaje):
        pass

class Mexicano:
    def pasaporte(self):
        print("metodo pasaporte")
    def visa(self):
        print("metodo visa")


        
class VisaAdapter(ViajeNacional):
    def __init__(self):
        self._mexicano = Mexicano()
        
    def visa(self):
        print("metodo visa")

