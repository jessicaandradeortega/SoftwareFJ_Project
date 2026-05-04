from servicios.servicio import Servicio

class ReservaSala(Servicio):
    def __init__(self, id, nombre, costo_base, capacidad):
        super().__init__(id, nombre, costo_base)
        self.capacidad = capacidad

    def calcular_costo(self, horas=1, impuesto=0):
        return (self._costo_base * horas) + impuesto

    def mostrar_info(self):
        return f"Reserva Sala: {self._nombre}, Capacidad: {self.capacidad}"
