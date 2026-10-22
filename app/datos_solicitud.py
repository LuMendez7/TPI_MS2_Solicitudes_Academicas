
from dataclasses import dataclass


@dataclass
class DatosSolicitud:
    titulo: str
    tipo: str
    prioridad: str
    responsable: str = ""
