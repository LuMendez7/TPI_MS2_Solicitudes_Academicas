
# Sistema de Gestión de Solicitudes Académicas

## Trabajo Práctico Integrador
Metodología de Sistemas II

Tecnicatura Universitaria en Programación - UTN

**Alumno:** Luciano Mendez

## Descripción

Sistema desarrollado en Python para registrar, consultar,
clasificar y administrar solicitudes académicas.

El proyecto tiene como objetivo analizar y mejorar la
calidad interna del software mediante la aplicación
de principios SOLID, Clean Code, refactoring seguro
y revisión técnica profesional.

## Funcionalidades

- Registrar solicitudes académicas.
- Clasificar solicitudes por tipo y prioridad.
- Asignar responsables.
- Modificar estados.
- Consultar solicitudes.
- Listar solicitudes registradas.
- Generar reportes.

## Tecnologías

- Python
- Git y GitHub
- pytest
- Black
- Ruff
- Visual Studio Code

## Ejecución de la versión inicial

Desde la carpeta principal del proyecto:

```powershell
python app/sistema.py
```

## Versiones del proyecto

### Versión inicial
Prototipo funcional que será utilizado para identificar
problemas de calidad interna y deuda técnica.

### Versión refactorizada
Versión mejorada del Sistema de Gestión de Solicitudes Académicas, desarrollada mediante cuatro refactorizaciones principales y mejoras adicionales en la organización del código. Se incorporaron las clases `DatosSolicitud` y `RepositorioSolicitudes`, se redujo la duplicación de código y se reorganizaron responsabilidades. Los cambios fueron verificados mediante pruebas automatizadas con pytest.

## Objetivos de calidad

- Identificar al menos ocho problemas técnicos.
- Aplicar SOLID y Clean Code.
- Documentar al menos cuatro refactorizaciones.
- Ejecutar pruebas antes y después de los cambios.
- Realizar un code review profesional.
- Documentar las mejoras y sus evidencias.

**Estado del proyecto:** refactorización y revisión técnica completadas.

Se realizaron cuatro refactorizaciones principales, se incorporaron pruebas automatizadas y se documentaron los resultados del proceso de mejora.

**Resultados de las pruebas:** 23 pruebas aprobadas mediante pytest.

**Cobertura total del código:** 68 % mediante pytest-cov.

**Control de versiones:** historial de commits y etiquetas de Git correspondientes a las etapas de diagnóstico, refactoring, pruebas y documentación.

**Aspectos pendientes de mejora:** ampliar la cobertura de pruebas y continuar separando las responsabilidades concentradas en `sistema.py`.
