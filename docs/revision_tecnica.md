# REVISIÓN TÉCNICA DEL CÓDIGO (CODE REVIEW)

**Proyecto:** Sistema de Gestión de Solicitudes Académicas  
**Materia:** Metodología de Sistemas II  
**Modalidad:** Individual  
**Versión revisada:** Rama `refactorizacion`

## 1. Objetivo

El objetivo de esta revisión técnica es evaluar la calidad del código del Sistema de Gestión de Solicitudes Académicas después de aplicar las refactorizaciones.

Se busca comprobar que las modificaciones mejoraron la organización, la legibilidad y el mantenimiento del sistema, sin alterar su funcionamiento esperado.

## 2. Componentes revisados

Se consideran los siguientes archivos:

- `app/sistema.py`: operaciones principales y menú del sistema.
- `app/datos_solicitud.py`: agrupación de los datos de una solicitud.
- `app/repositorio_solicitudes.py`: administración de las solicitudes y sus identificadores.
- `tests/test_sistema.py`: pruebas del comportamiento del sistema.
- `tests/test_repositorio_solicitudes.py`: pruebas del repositorio.

## 3. Lista de verificación (Checklist)

| Criterio | Estado | Observación |
|---|---|---|
| El código utiliza nombres comprensibles | Cumple parcialmente | Se identifican nombres claros, aunque todavía pueden mejorarse algunas variables. |
| Las responsabilidades están separadas | Cumple parcialmente | Se creó un repositorio, pero `sistema.py` todavía reúne distintas operaciones. |
| Se aplicó Extract Method | Cumple | Se extrajeron responsabilidades para facilitar la lectura y el mantenimiento. |
| Se aplicó Introduce Parameter Object | Cumple | Se incorporó `DatosSolicitud` para agrupar los datos de registro. |
| Se aplicó Move Method o traslado de responsabilidad | Cumple | La búsqueda y otras operaciones del almacenamiento se trasladaron al repositorio. |
| Se redujo el uso de variables globales | Cumple parcialmente | Se eliminó el contador redundante, aunque continúa existiendo una lista global de solicitudes. |
| Se incorporaron pruebas automatizadas | Cumple | Se cuenta con 23 pruebas verificadas durante el desarrollo. |
| Se conserva el comportamiento esperado | Cumple según las pruebas ejecutadas | Las pruebas automatizadas informadas finalizaron correctamente. |
| Se utiliza Git para registrar los cambios | Cumple | Se realizaron commits durante las etapas de refactorización. |
| Se documentaron las decisiones técnicas | En proceso | Se está completando la revisión técnica y el informe integrador. |

## 4. Observaciones de la revisión

**Observación 1. Concentración de responsabilidades**

El archivo `sistema.py` todavía contiene la función `procesar()`, encargada de resolver varias operaciones mediante condiciones.

Esto puede dificultar la incorporación de nuevas funcionalidades.

**Recomendación:** continuar separando las operaciones en funciones específicas, siempre que la modificación resulte necesaria y pueda verificarse con pruebas.

**Observación 2. Estado global compartido**

El sistema conserva una lista global llamada `solicitudes`.

Aunque el repositorio permite organizar el acceso a los datos, la existencia de estado global puede dificultar el aislamiento de las pruebas y el mantenimiento futuro.

**Recomendación:** evaluar una instancia compartida de repositorio o una estructura que permita inyectar esta dependencia.

**Observación 3. Cobertura de pruebas**

Las pruebas automatizadas verifican diferentes comportamientos del sistema. Sin embargo, aprobar las pruebas no significa que todos los caminos posibles del programa estén cubiertos.

**Recomendación:** revisar los sectores sin cobertura y priorizar los casos relevantes para el funcionamiento del sistema.

## 5. Evaluación general

La revisión permite reconocer avances en la calidad interna del proyecto.

La incorporación de `DatosSolicitud`, la creación de `RepositorioSolicitudes` y la eliminación del contador global redundante contribuyen a una distribución más clara de las responsabilidades.

También se dispone de pruebas automatizadas que permiten detectar regresiones durante el proceso de refactorización.

No obstante, todavía existen oportunidades de mejora relacionadas con la función `procesar()`, el uso de la lista global y la cobertura de pruebas.

## 6. Resultado de la revisión

**Estado:** revisión preliminar realizada, con observaciones pendientes de seguimiento.

La aceptación técnica definitiva se realizará después de comprobar el estado actualizado del proyecto, registrar las evidencias y decidir qué observaciones requieren corrección dentro del alcance del TPI.

## 7. Reflexión sobre el proceso individual

Al tratarse de un trabajo individual, la revisión técnica se realiza mediante una autoevaluación estructurada con criterios de calidad.

Este procedimiento permite detectar problemas y registrar decisiones, aunque no reemplaza completamente una revisión independiente realizada por otra persona.

Por ese motivo, se complementa con pruebas automatizadas y evidencia del historial de Git.

## 8. Seguimiento de observaciones y decisiones técnicas

A partir de la revisión técnica realizada, se analizaron las principales observaciones detectadas en la versión refactorizada del Sistema de Gestión de Solicitudes Académicas.

### Observación 1. Concentración de operaciones en procesar()

**Estado:** mejora pendiente.

La función `procesar()` todavía contiene distintas alternativas de ejecución según la operación solicitada.

Aunque se realizaron refactorizaciones para separar responsabilidades, esta función conserva parte de la lógica de coordinación.

**Decisión:** mantener su funcionamiento actual dentro del alcance del TPI y proponer como mejora futura la extracción de operaciones específicas.

### Observación 2. Uso de una lista global

**Estado:** mejora pendiente.

El sistema utiliza una lista global denominada `solicitudes` para almacenar los registros durante la ejecución.

La incorporación de `RepositorioSolicitudes` permitió organizar las operaciones de almacenamiento y búsqueda. Sin embargo, todavía existe una dependencia del estado global.

**Decisión:** conservar la implementación actual y considerar, como mejora futura, una instancia compartida del repositorio que permita reducir el acoplamiento.

### Observación 3. Cobertura de pruebas

**Estado:** verificación realizada, con oportunidades de mejora.

Durante la última ejecución documentada se obtuvieron los siguientes resultados:

- Pruebas automatizadas aprobadas: 23.
- Cobertura total: 68 %.
- Cobertura de `datos_solicitud.py`: 100 %.
- Cobertura de `repositorio_solicitudes.py`: 100 %.
- Cobertura de `sistema.py`: 60 %.

Estos resultados permiten comprobar que los casos evaluados funcionan correctamente, aunque no garantizan la ausencia de errores en los caminos que todavía no fueron cubiertos.

**Decisión:** conservar los resultados como evidencia y proponer la ampliación de las pruebas como mejora futura.

### Conclusión del seguimiento

La revisión técnica permitió reconocer mejoras concretas en la estructura del código y registrar aspectos que todavía pueden perfeccionarse.

Las observaciones pendientes no se consideran resueltas. Se documentan como oportunidades de evolución del sistema, diferenciándolas de las refactorizaciones efectivamente implementadas y verificadas.