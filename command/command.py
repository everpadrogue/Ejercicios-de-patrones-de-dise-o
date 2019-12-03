

from abc import ABC, abstractmethod

class Celular(ABC):
    @abstractmethod
    def action(self):
        pass

class VisualizarRedessociales(Celular):
    def __init__(self, Celular):
        self.celular = Celular

    def action(self):
        self.celular.Ver_Redes_sociales()


class ReproducirMusica(Celular):
    def __init__(self, Celular):
        self.celular = Celular

    def action(self):
        self.celular.escuchar_music()


class VisualizarVideos(Celular):
    def __init__(self, Celular):
        self.celular = Celular

    def action(self):
        self.celular.ver_videos()

      
class Vizualizaciondearchivos(Celular):
    def __init__(self, Celular):
        self.celular = Celular

    def action(self):
        self.celular.enviar_archivos()

class ActionMenu:
    def Ver_Redes_sociales(self):
        pass
        
    def escuchar_music(self):
        pass
        
    def ver_videos(self):
        pass

    def enviar_archivos(self):
        pass

class Action:
    def __init__(self):
        self._actions = []

    def executar_tareas(self, Celular):
        self._actions.append(Celular)
        Celular.action()


class main():
    menu = ActionMenu()
    celular_Ver_Redes_sociales = VisualizarRedessociales(menu)
    celular_escuchar_music = ReproducirMusica(menu)
    celular_ver_videos = VisualizarVideos(menu)
    celular_enviar_archivos = Vizualizaciondearchivos(menu)

    act = Action()
    act.executar_tareas(celular_Ver_Redes_sociales)
    act.executar_tareas(celular_escuchar_music)
    act.executar_tareas(celular_ver_videos)
    act.executar_tareas(celular_enviar_archivos)
