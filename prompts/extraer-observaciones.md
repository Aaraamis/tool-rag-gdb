# Extraer observaciones de un documento

Tarea: leer un documento del corpus GDB y registrar sus observaciones en
`datos/03_extraido/<ruta del PDF sin .pdf>.json`, conforme a
`src/rag_gdb/observaciones.schema.json`. Sirve cualquier agente que lea
archivos, ejecute comandos y escriba JSON.

## Pasos

1. Elegir un PDF de `datos/01_inventario/clasificacion.csv` con `gdb` en `si` o
   `probable` y emisor `idu` o `interventoria`. Si ya existe su JSON de salida
   con el mismo `sha256`, omitirlo.
2. Partir de los candidatos de `datos/03_candidatos/` si existen
   (`rag-gdb proponer`): su cita ya es literal. Contrastarlos con el texto con
   marcas de página, `rag-gdb paginas "<ruta del manifiesto>"`, para quitar
   ruido (respuestas del contratista, encabezados) y añadir lo que falte. El
   Markdown de `datos/02_convertidos/` sirve de apoyo, pero no trae páginas.
3. Registrar cada observación: una entrada por enunciado distinto, no por
   respuesta ni por fila. Si el mismo enunciado se repite en varias filas o
   planos de una tabla, se registra una vez y no se listan los planos. Las
   observaciones sobre planos sí se registran. No se leen los PDF que son planos
   (dibujos) y no documentos: importan los comunicados y los correos. `cita` es un fragmento **literal** del enunciado, de una sola
   página y de al menos 25 caracteres; `pagina` es la del PDF.
4. Si el sentido depende de un mapa o una captura, abrir la página del PDF,
   poner `requiere_cotejo_visual: true` y describir en `resumen` lo que se ve.
   La cita de esas entradas no se comprueba contra el texto. El texto en rojo
   de las tablas es énfasis del interventor sobre sus propias observaciones:
   se extrae como cualquier otro, con `autor: interventoria`.
5. `autor` es quien levanta la observación. `radicado_origen` es el radicado IDU
   que la originó, o `null` si el documento no lo dice; no lo deduzcas de
   otros documentos. Un traslado sin sus anexos no aporta observaciones.
6. `estado_en_documento` es el que declara el propio documento, no el que
   se deduzca. Sin declaración, `sin_estado`.
7. Anotar en `notas` los criterios aplicados y las dudas abiertas.
8. Ejecutar `rag-gdb validar` y corregir hasta que no haya errores. El
   comando comprueba el esquema, el hash, la página y la cita.

No asignar `tema`: la taxonomía se define después, con Aramis.
