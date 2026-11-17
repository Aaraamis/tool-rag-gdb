# Revisión del primer piloto

Fecha: 2026-11-17. Salidas en meraxes-f:
`~/repos/tool-rag-gdb/datos/02_convertidos/`.

| PDF | Páginas | Conversión | Hallazgo inicial |
|---|---:|---|---|
| Revisión alistamiento 351 | 14 | JSON y MD generados | Texto escaso en el perfil inicial; revisar OCR y tablas página por página |
| GUIC06, guía de entrega digital v2 | 41 | JSON y MD generados | Guía extensa; revisar estructura y tablas |
| C.1443, revisión BDG V1 | 21 | JSON y MD generados | Contiene observaciones y tablas; revisar que no falten filas |
| MAB traslado STMSV 20213560227311 | 2 | JSON y MD generados | Menciona ocho folios anexos ausentes en este PDF; no extraer observaciones de ese traslado |

Las cuatro salidas pasaron comprobación automática de existencia y recuento de
páginas. Queda pendiente la comparación visual completa de cada PDF con el
Markdown y el registro de pérdidas con página. Esa revisión decide si se
ajusta OCR, conversión o selección antes de ampliar el corpus.
