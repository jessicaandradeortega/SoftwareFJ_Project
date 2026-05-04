from core.entidad import EntidadBase
from utils.excepciones import ClienteError

class Cliente(EntidadBase):
    """
    Clase para representar clientes del sistema.
    """

    def __init__(self, id, nombre, documento):
        super().__init__(id)

        if not nombre or not nombre.strip():
            raise ClienteError("Nombre inválido")

        if not documento or not documento.strip():
            raise ClienteError("Documento inválido")

        self._nombre = nombre
        self._documento = documento

    @property
    def nombre(self):
        return self._nombre

    @property
    def documento(self):
        return self._documento

    def mostrar_info(self):
        return f"Cliente: {self.nombre} - Documento: {self.documento}"
