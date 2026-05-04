from centro.entidad import EntidadBase

class Cliente(EntidadBase):
    """
    Clase que representa clientes del sistema Software FJ.
    """

    def __init__(self, id, nombre, documento):
        super().__init__(id)

        if not nombre or not nombre.strip():
            raise ValueError("El nombre no puede estar vacío")

        if not documento or not documento.strip():
            raise ValueError("El documento no puede estar vacío")

        self._nombre = nombre
        self._documento = documento

    @property
    def nombre(self):
        return self._nombre

    @property
    def documento(self):
        return self._documento

    def mostrar_info(self):
        return (
            f"Cliente ID: {self.id}, "
            f"Nombre: {self.nombre}, "
            f"Documento: {self.documento}, "
            f"Fecha creación: {self.fecha_creacion}"
        )
