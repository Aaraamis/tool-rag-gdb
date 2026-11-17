# Revisión del primer piloto

Fecha: 2026-11-17. Salidas en meraxes-f:
`~/repos/tool-rag-gdb/datos/02_convertidos/`.

| PDF | Páginas | Conversión | Hallazgo inicial |
|---|---:|---|---|
| Revisión alistamiento 351 | 14 | JSON y MD generados | Texto escaso en el perfil inicial; revisar OCR y tablas página por página |
| GUIC06, guía de entrega digital v2 | 41 | JSON y MD generados | Guía extensa; revisar estructura y tablas |
| C.1443, revisión BDG V1 | 21 | JSON y MD generados | Contiene observaciones y tablas; revisar que no falten filas |
| MAB traslado STMSV 20213560227311 | 2 | JSON y MD generados | Menciona ocho folios anexos ausentes en este PDF; no extraer observaciones de ese traslado |

## Revisión realizada

Se comprobó la existencia de JSON y Markdown, y el recuento de 78 páginas.
En las 64 páginas con capa de texto suficiente (los otros 14 folios pertenecen
al PDF 351), Docling no dejó páginas vacías y conservó al menos el 80 % de los
identificadores numéricos extraíbles de cada página. Esta comparación detecta
omisiones grandes de texto, pero no valida significado, orden ni geometría.

Se cotejaron visualmente páginas representativas del PDF y sus datos de Docling:

| Documento y página PDF | Hallazgo | Consecuencia |
|---|---|---|
| Revisión 351, pp. 1, 6, 9 y 12 | Son separadores con solo un título; el bajo número de caracteres no indica pérdida de observaciones en esas páginas. | El umbral de OCR es solo una señal de revisión. |
| Revisión 351, p. 5 | El título y algunos identificadores de la captura se leen, pero el mapa de polígonos no queda representado en Markdown. | Para entender la observación «Polígonos sin dividir compartiendo PK» hay que abrir el PDF. |
| Revisión 351, p. 10 | Docling detecta la tabla de 34 filas y 3 columnas, pero la captura y los rótulos del mapa producen identificadores con ruido OCR. | No confiar en los identificadores de esta página sin cotejo visual. |
| GU-IC-06, p. 11 | Conserva texto y la tabla de coordenadas de 10 filas; el esquema de carpetas de la BDG aparece como imagen y pierde su jerarquía visual en Markdown. | Citar el PDF al interpretar la estructura de carpetas. |
| C.1443/CE4437/23/7.7, pp. 5 y 13 | Las tablas y ejemplos de observaciones están en el JSON/Markdown. El texto en rojo (observaciones del interventor resaltadas para dar énfasis, según Aramis) se conserva como texto, pero el Markdown no registra el color. | El rojo no filtra observaciones; basta con leer la columna de observaciones y citar la página. |
| Traslado MAB-2-1463-0012-21, p. 1 | El texto coincide con el PDF. Remite a ocho folios anexos que no forman parte de este archivo de dos páginas. | Es contexto, no fuente directa de las observaciones anexas. |

**Resultado:** el piloto sirve para continuar con documentos de texto y tablas,
con verificación de citas por página. Los PDF con mapas o capturas necesitan
revisión visual al extraer observaciones; el texto en rojo es énfasis del
interventor y no la requiere. No se declara todavía
cumplido el criterio final de 20 PDF variados ni la revisión visual completa de
las 78 páginas; la inspección visual fue dirigida a las páginas indicadas.
