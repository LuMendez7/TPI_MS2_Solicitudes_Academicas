
# Diagnóstico de calidad del sistema

## Versión analizada

Versión inicial: v1.0-base

Archivo principal: app/sistema.py

## Calidad externa

El sistema permite registrar, consultar y administrar
solicitudes académicas mediante una interfaz de consola.

Se realizaron pruebas manuales de registro, consulta
y generación de reportes.

## Calidad interna

Se identificaron ocho debilidades técnicas:

| ID | Problema | Prioridad |
|---|---|---|
| DT-01 | Múltiples responsabilidades | Alta |
| DT-02 | Condicionales anidados | Alta |
| DT-03 | Números mágicos | Media |
| DT-04 | Cadenas mágicas | Media |
| DT-05 | Variables globales | Alta |
| DT-06 | Duplicación de código | Alta |
| DT-07 | Exceso de parámetros | Media |
| DT-08 | Manejo insuficiente de errores | Alta |

## Estrategia de mejora

- Aplicar SRP y separación de responsabilidades.
- Reducir condicionales anidados.
- Incorporar constantes o enumeraciones.
- Encapsular el almacenamiento.
- Eliminar duplicaciones.
- Simplificar parámetros.
- Mejorar el manejo de errores.
- Verificar los cambios mediante pruebas.

## Estado

Diagnóstico documentado.
Refactorización pendiente.
