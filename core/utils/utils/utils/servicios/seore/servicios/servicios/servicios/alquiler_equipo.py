from servicios.servicio import Servicio

class AlquilerEquipo(Servicio):
    def __init__(self, id, nombre, costo_base, tipo_equipo):
        super().__init__(id, nombre, costo_base)
        self.tipo_equipo = tipo_equipo

    def calcular_costo(self, dias=1, descuento=0):
        return (self._costo_base * dias) - descuento

    def mostrar_info(self):
        return f"Alquiler Equipo: {self._nombre}, Tipo: {self.tipo_equipo}"
