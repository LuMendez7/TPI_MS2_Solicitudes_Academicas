from app.repositorio_solicitudes import RepositorioSolicitudes


def test_repositorio_inicialmente_vacio():
    repositorio = RepositorioSolicitudes()

    assert repositorio.listar() == []


def test_agregar_solicitud():
    repositorio = RepositorioSolicitudes()

    solicitud = {
        "id": 1,
        "titulo": "Solicitud de certificado",
        "estado": "PENDIENTE",
    }

    repositorio.agregar(solicitud)

    assert len(repositorio.listar()) == 1


def test_buscar_solicitud_existente():
    repositorio = RepositorioSolicitudes()

    solicitud = {
        "id": 1,
        "titulo": "Solicitud de certificado",
    }

    repositorio.agregar(solicitud)

    resultado = repositorio.buscar_por_id(1)

    assert resultado == solicitud


def test_buscar_solicitud_inexistente():
    repositorio = RepositorioSolicitudes()

    resultado = repositorio.buscar_por_id(999)

    assert resultado is None


def test_generar_identificadores_consecutivos():
    repositorio = RepositorioSolicitudes()

    primer_id = repositorio.generar_id()
    segundo_id = repositorio.generar_id()

    assert primer_id == 1
    assert segundo_id == 2


def test_repositorios_independientes():
    repositorio_a = RepositorioSolicitudes()
    repositorio_b = RepositorioSolicitudes()

    repositorio_a.agregar({"id": 1, "titulo": "Solicitud A"})

    assert len(repositorio_a.listar()) == 1
    assert len(repositorio_b.listar()) == 0


def test_listar_devuelve_una_copia():
    repositorio = RepositorioSolicitudes()
    repositorio.agregar({"id": 1, "titulo": "Solicitud A"})

    listado = repositorio.listar()
    listado.clear()

    assert len(repositorio.listar()) == 1
