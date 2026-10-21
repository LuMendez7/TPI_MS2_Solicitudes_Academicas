
import pytest

from app import sistema


@pytest.fixture(autouse=True)
def limpiar_datos():
    """Restablece el sistema antes y después de cada prueba."""
    sistema.solicitudes.clear()
    sistema.contador = 1

    yield

    sistema.solicitudes.clear()
    sistema.contador = 1


def registrar_solicitud():
    return sistema.procesar(
        1,
        titulo="Certificado de alumno regular",
        tipo="CERTIFICADO",
        prioridad="ALTA",
        responsable="Secretaria Academica",
    )


def test_registrar_solicitud():
    # Arrange: preparar los datos
    titulo = "Certificado de alumno regular"

    # Act: registrar la solicitud
    resultado = sistema.procesar(
        1,
        titulo=titulo,
        tipo="CERTIFICADO",
        prioridad="ALTA",
        responsable="Secretaria Academica",
    )

    # Assert: verificar el resultado
    assert resultado == "Solicitud registrada"
    assert len(sistema.solicitudes) == 1
    assert sistema.solicitudes[0]["titulo"] == titulo
    assert sistema.solicitudes[0]["estado"] == "PENDIENTE"


def test_rechazar_titulo_vacio():
    resultado = sistema.procesar(
        1,
        titulo="",
        tipo="CERTIFICADO",
        prioridad="ALTA",
    )

    assert resultado == "Titulo obligatorio"
    assert len(sistema.solicitudes) == 0


def test_rechazar_tipo_vacio():
    resultado = sistema.procesar(
        1,
        titulo="Solicitud de certificado",
        tipo="",
        prioridad="ALTA",
    )

    assert resultado == "Tipo obligatorio"


def test_rechazar_prioridad_vacia():
    resultado = sistema.procesar(
        1,
        titulo="Solicitud de certificado",
        tipo="CERTIFICADO",
        prioridad="",
    )

    assert resultado == "Prioridad obligatoria"


def test_rechazar_prioridad_invalida():
    resultado = sistema.procesar(
        1,
        titulo="Solicitud de certificado",
        tipo="CERTIFICADO",
        prioridad="URGENTE",
    )

    assert resultado == "Prioridad invalida"
    assert len(sistema.solicitudes) == 0


def test_asignar_responsable():
    registrar_solicitud()

    resultado = sistema.procesar(
        2,
        numero=1,
        responsable="Direccion Academica",
    )

    assert resultado == "Responsable asignado"
    assert sistema.solicitudes[0]["responsable"] == "Direccion Academica"


def test_asignar_responsable_inexistente():
    resultado = sistema.procesar(
        2,
        numero=999,
        responsable="Direccion Academica",
    )

    assert resultado == "Solicitud no encontrada"


def test_cambiar_estado():
    registrar_solicitud()

    resultado = sistema.procesar(
        3,
        numero=1,
        estado="EN_PROCESO",
    )

    assert resultado == "Estado actualizado"
    assert sistema.solicitudes[0]["estado"] == "EN_PROCESO"


def test_rechazar_estado_invalido():
    registrar_solicitud()

    resultado = sistema.procesar(
        3,
        numero=1,
        estado="CANCELADA",
    )

    assert resultado == "Estado invalido"
    assert sistema.solicitudes[0]["estado"] == "PENDIENTE"


def test_consultar_solicitud():
    registrar_solicitud()

    resultado = sistema.procesar(4, numero=1)

    assert "Certificado de alumno regular" in resultado
    assert "'id': 1" in resultado


def test_consultar_solicitud_inexistente():
    resultado = sistema.procesar(4, numero=999)

    assert resultado == "Solicitud no encontrada"


def test_generar_reporte():
    registrar_solicitud()

    resultado = sistema.procesar(5)

    assert resultado == (
        "Pendientes: 1 | En proceso: 0 | Resueltas: 0"
    )


def test_listar_solicitudes():
    registrar_solicitud()

    resultado = sistema.procesar(6)

    assert "Certificado de alumno regular" in resultado


def test_opcion_invalida():
    resultado = sistema.procesar(99)

    assert resultado == "Opcion invalida"


def test_identificadores_consecutivos():
    registrar_solicitud()
    registrar_solicitud()

    assert sistema.solicitudes[0]["id"] == 1
    assert sistema.solicitudes[1]["id"] == 2
