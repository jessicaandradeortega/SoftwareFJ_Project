from abc import ABC, abstractmethod
from datetime import datetime

class EntidadBase(ABC):
    """
    Clase abstracta base para representar entidades generales del sistema.
    """

    def __init__(self, id):
        if not id:
            raise ValueError("El ID no puede estar vacío")
        self._id = id
        self._fecha_creacion = datetime.now()

    @property
    def id(self):
        return self._id

    @property
    def fecha_creacion(self):
        return self._fecha_creacion

    @abstractmethod
    def mostrar_info(self):
        pass
