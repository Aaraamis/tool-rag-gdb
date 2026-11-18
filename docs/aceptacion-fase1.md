# Criterios de aceptación de la fase 1: estado al 2026-11-18

Revisión frente a la sección 8 de `ESPECIFICACION.md`, hecha fuera de meraxes-f
sin los PDF originales. Los criterios 2, 3 y 4 se cierran donde estén los PDF.

| # | Criterio | Estado | Evidencia y pendiente |
|---|---|---|---|
| 1 | `informe-corpus.md` da cuenta del 100 % de los archivos en disco | **Cumple en forma** | Los 490 PDF del manifiesto aparecen una vez: 45 procesados, 0 descartados y 445 pendientes. El criterio solo pide clasificar; Aramis decidió completar todos, así que el cierre real llega cuando los pendientes pasen a procesados o descartados con motivo. |
| 2 | 20 PDF variados sin pérdida de observaciones en la conversión | **Pendiente** | `docs/revision-piloto.md`: 4 PDF del piloto, 78 páginas, más 8 del primer lote; 11 convertidos en total. Falta elegir y revisar 20 variados (escaneados, con tablas, guías largas) contra el PDF. Requiere los originales. |
| 3 | 10 documentos de observaciones revisados a mano: ≥ 90 % recuperado y página correcta | **Pendiente** | La referencia del primer lote (8 documentos, 171 observaciones) mide la pasada local: 88 % de recuperación antes de depurar. Falta el cotejo manual de 10 documentos contra el PDF, con página. Requiere los originales. |
| 4 | Todos los JSON de `03_extraido/` pasan `validar` | **Cumple al traspaso; repetir** | Los 45 JSON se validaron en meraxes-f el 2026-11-17. Aquí no puede repetirse: `validar` lee el texto del PDF. Repetir tras cada nueva extracción. |
| 5 | Cada requisito del checklist cita al menos una observación real con referencia | **Cumple** | Comprobado sobre el borrador: los 93 requisitos tienen al menos un ejemplo con radicado o archivo y página. |
| 6 | Cada requisito enlaza fuente y sección, o aparece aparte como práctica observada | **Cumple** | 80 requisitos con enlace normativo confirmado (directo o parcial) y 13 en la sección separada de prácticas observadas. Corregido el 2026-11-18: antes las prácticas aparecían mezcladas dentro de cada tema. |

## Condiciones de cierre

- Validación de Aramis de la taxonomía y de la redacción
  (`docs/revision-editorial.md`).
- Contrato de 9 documentos sin determinar en `config/contratos-documentos.csv`,
  con la primera página del PDF.
- Procesar en meraxes-f los 445 pendientes: `proponer`, depurar, `validar`,
  `consolidar`, `registrar-grupos` y revisión normativa y editorial de los
  grupos nuevos. Después, regenerar `checklist`, `matriz` e `informe`.
