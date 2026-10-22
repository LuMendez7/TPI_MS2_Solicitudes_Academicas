
class RepositorioSolicitudes:
    def __init__(self, solicitudes):
        self.solicitudes = solicitudes

    def buscar_por_id(self, numero):
        for solicitud in self.solicitudes:
            if solicitud["id"] == numero:
                return solicitud

        return None
