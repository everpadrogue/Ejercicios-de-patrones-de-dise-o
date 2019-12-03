from __future__ import annotations
from abc import ABC, abstractmethod, abstractproperty
from typing import Any


class Builder(ABC):

    @abstractproperty
    def casa(self) -> None:
        pass
    @abstractmethod
    def tabicon(self) -> None:
        pass
    @abstractmethod
    def cemento(self) -> None:
        pass
    @abstractmethod
    def material_herramientas(self) -> None:
        pass

#######################################################
class HerramientasConcret(Builder):

    def __init__(self) -> None:

        self.constructor()

    def constructor(self) -> None:
        self._casa = Departamento()

    @property
    def casa(self) -> Departamento:

        casa = self._casa
        self.constructor()
        return casa

    def tabicon(self) -> None:
        self._casa.add("Tabicon")

    def cemento(self) -> None:
        self._casa.add("cemento")

    def material_herramientas(self) -> None:
        self._casa.add("material de herramientas")


class Departamento():

    def __init__(self) -> None:
        self.herramientas = []

    def add(self, part: Any) -> None:
        self.herramientas.append(part)

    def material(self) -> None:
        print(f"Product herramientas: {', '.join(self.herramientas)}", end="")


class EmpresaArquitectura:


    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, builder: Builder) -> None:

        self._builder = builder


    def plano(self) -> None:
        self.builder.tabicon()

    def cemiento(self) -> None:
        self.builder.tabicon()
        self.builder.cemento()
        

######################################################
if __name__ == "__main__":

    empresa_construccion = EmpresaArquitectura()
    builder = HerramientasConcret()
    empresa_construccion.builder = builder
