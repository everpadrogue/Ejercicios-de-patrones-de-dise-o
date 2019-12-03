

from abc import ABC, abstractmethod

class RutinaDiaria(ABC):
    def rutina_diaria(self):
         pass
    
    def levanarse(self):
        pass
       
    def comer(self):
        pass

    def desayunar(self):
        pass
    def trabajar(self):
        pass
    def relajarse(self):
        pass

    def ver_tv(self):
        pass

    def dormir(self):
        pass
    
class Contador(RutinaDiaria):
    
    def levanarse(self):
        print("metodo rutina_diaria")
    def comer(self):
        print("metodo rutina_diaria")

    def desayunar(self):
        print("metodo rutina_diaria")

    def trabajar(self):
        print("metodo rutina_diaria")
    def relajarse(self):
        print("metodo rutina_diaria")

    def ver_tv(self):
        print("metodo rutina_diaria")

    def dormir(self):
        print("metodo rutina_diaria")

class Ingeniero(RutinaDiaria):
    
    
    def levanarse(self):
        print("metodo rutina_diaria")
    def comer(self):
        print("metodo rutina_diaria")

    def desayunar(self):
        print("metodo rutina_diaria")

    def trabajar(self):
        print("metodo rutina_diaria")
    def relajarse(self):
        print("metodo rutina_diaria")

    def ver_tv(self):
        print("metodo rutina_diaria")

    def dormir(self):
        print("metodo rutina_diaria")


class Electricista(RutinaDiaria):
    
   
    
    def levanarse(self):
        print("metodo rutina_diaria")
    def comer(self):
        print("metodo rutina_diaria")

    def desayunar(self):
        print("metodo rutina_diaria")

    def trabajar(self):
        print("metodo rutina_diaria")
   
    def dormir(self):
        print("metodo rutina_diaria")

class profesor(RutinaDiaria):

    
    def levanarse(self):
        print("metodo rutina_diaria")
    def comer(self):
        print("metodo rutina_diaria")

    def desayunar(self):
        print("metodo rutina_diaria")

    def trabajar(self):
        print("metodo rutina_diaria")
    def relajarse(self):
        print("metodo rutina_diaria")

  

    def dormir(self):
        print("metodo rutina_diaria")


class Trabajador:
    def __init__(self):
        self.contador = Contador()
        self.contador.comer()

ejemplo = Trabajador()

