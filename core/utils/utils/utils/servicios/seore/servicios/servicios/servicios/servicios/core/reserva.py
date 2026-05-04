from utils.excepciones import ReservaError

class Reserva:
    """
    Clase que integra cliente, servicio y duración.
    """

    def __init__(self, cliente, servicio, duracion):
        if duracion <= 0:
            raise ReservaError("Duración inválida")

        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "Pendiente"

    def confirmar(self):
        self.estado = "Confirmada"

    def cancelar(self):
        self.estado = "Cancelada"

    def procesar(self):
        try:
            costo = self.servicio.calcular_costo(self.duracion)
            self.confirmar()
            return costo
        except Exception as e:
            raise ReservaError("Error al procesar reserva") from e
