
class RepositorioSolicitudes:
    def __init__(self, solicitudes=None):
        if solicitudes is None:
            solicitudes = []

        self.solicitudes = solicitudes

        self.siguiente_id = max(
            (solicitud["id"] for solicitud in self.solicitudes),
            default=0
        ) + 1

    def buscar_por_id(self, numero):
        for solicitud in self.solicitudes:
            if solicitud["id"] == numero:
                return solicitud

        return None

    def agregar(self, solicitud):
        self.solicitudes.append(solicitud)

    def generar_id(self):
        identificador = self.siguiente_id
        self.siguiente_id += 1
        return identificador

    def listar(self):
        return self.solicitudes.copy()
