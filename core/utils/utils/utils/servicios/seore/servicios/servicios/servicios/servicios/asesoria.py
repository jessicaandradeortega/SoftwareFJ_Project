from servicios.servicio import Servicio

class AsesoriaEspecializada(Servicio):
    def __init__(self, id, nombre, costo_base, especialidad):
        super().__init__(id, nombre, costo_base)
        self.especialidad = especialidad

    def calcular_costo(self, horas=1, tarifa_extra=0):
        return (self._costo_base * horas) + tarifa_extra

    def mostrar_info(self):
        return f"Asesoría: {self._nombre}, Especialidad: {self.especialidad}"
