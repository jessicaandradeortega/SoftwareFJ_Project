from abc import ABC, abstractmethod
from core.entidad import EntidadBase

class Servicio(EntidadBase, ABC):
    """
    Clase abstracta para representar servicios generales.
    """

    def __init__(self, id, nombre, costo_base):
        super().__init__(id)
        self._nombre = nombre
        self._costo_base = costo_base

    @abstractmethod
    def calcular_costo(self, *args, **kwargs):
        pass

    @abstractmethod
    def mostrar_info(self):
        pass
