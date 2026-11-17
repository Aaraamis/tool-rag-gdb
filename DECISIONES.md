# Decisiones

| Fecha | Decisión | Evidencia |
|---|---|---|
| 2026-11-17 | Ejecutar fase 1 por hitos; primero inventario y conversión piloto | Acuerdo con Aramis |
| 2026-11-17 | Los criterios de 20 PDF, 10 documentos y 90 % son metas de cierre | Acuerdo con Aramis |
| 2026-11-17 | Copiar y verificar el ZIP en meraxes-f, sin borrar el origen | Evita pérdida antes de la revisión |
| 2026-11-17 | Mantener 18 PDF del inventario como ausentes con motivo pendiente | 508 descargados en ODS frente a 490 PDF en ZIP |
| 2026-11-17 | Usar Lucía para gestión del repo, no como dependencia de ejecución | Acuerdo con Aramis |
| 2026-11-17 | Esquema RF6: una entrada por observación, con página y cita literal verificable | Piloto sobre C.1443 de junio de 2024 |
| 2026-11-17 | Unidad de observación: un enunciado distinto por documento; si se repite en varias filas o planos de una tabla se registra una vez y no se listan los planos. Las observaciones sobre planos sí se capturan | Aprobado por Aramis |
| 2026-11-17 | Se evitan los PDF que son planos (dibujos), no los comunicados que observan planos. La regla de exclusión queda pendiente de definir | Aclarado por Aramis: lo importante son los comunicados y los correos |

## Primer inventario en meraxes-f

- ZIP, ODS y CSV copiados con SHA-256 idéntico en ambos equipos.
- 490 PDF extraídos, 490 coincidencias por hash, cero huérfanos y 18 filas
  `DESCARGADO` sin archivo. El manifiesto conserva las 18 claves.
- Perfil completo: 490 PDF sin errores; 18 con alguna página de texto escaso.
  El umbral de 40 caracteres es provisional y se revisará con el piloto.
- La extracción con `unzip` alteró nombres con tildes. Se repitió con `zipfile`
  de Python y las cuatro rutas de la muestra coincidieron con el manifiesto.
- Docling convirtió los cuatro PDF de `muestras/piloto.txt` sin errores. Los
  JSON conservan 14, 41, 21 y 2 páginas respectivamente.
- El traslado MAB de dos páginas menciona ocho folios anexos que no están en
  ese PDF; se considera contexto y no fuente directa de observaciones.
- La revisión del piloto confirmó que mapas y capturas pueden aportar
  significado que Markdown no conserva. Para esos casos, la extracción de
  observaciones debe cotejar el PDF y citar la página original.
- Aclarado por Aramis: el texto en rojo de las tablas de la interventoría
  (p. ej. C.1443 BDG V1, p. 11) resalta observaciones del propio interventor
  para darles énfasis. No decide qué filas cuentan: toda observación de la
  columna cuenta, con `autor: interventoria`. Ese texto está en la capa de
  texto del PDF, así que su cita se valida como cualquier otra.
- Primeras páginas de MAB-1/2-1463 identifican explícitamente el contrato de
  interventoría 1463 y comunicaciones sobre la obra 1385; las de MV2 identifican
  interventoría 1464 y obra 1384. La regla de emisor se limita a esos códigos.
- La clasificación automática usa solo señales positivas del nombre y del
  texto. Sin señal no se excluye el PDF; queda por revisar. Una mención aislada
  en el texto se marca probable o posible, no confirmada.
- Las correcciones manuales se registran por SHA-256, con página y motivo, en
  `config/clasificacion-manual.csv`; así sobreviven a la reejecución de reglas.
- MV2-025-21 y MV2-026-21 son remisiones de observaciones IDU según su primera
  página. Se clasifican como traslados; su frecuencia corresponde al radicado
  IDU citado, no a una observación nueva de MV2.

## Piloto de extracción (RF6)

- La extracción de `2024-06-24_..._GEODATABASE_V3.pdf` dio 7 observaciones IDU,
  todas con página y cita validadas contra el PDF. El oficio habla de
  «observaciones IDU (DITINI)» sin radicado, por eso `radicado_origen` es nulo.
- **Resuelta con la V1, octubre y diciembre:** dentro de cada seguimiento la
  interventoría añade hallazgos propios (p. ej. carpetas marcadas OK que no se
  entregaron). Se registran como entradas aparte (`autor: interventoria`), una
  por enunciado, con el radicado IDU de la observación de la que derivan.
  Se añadieron también al documento de junio, que no los tenía. Para las tablas
  por plano rige la decisión de la tabla superior.
- **Frecuencia (RF8):** el oficio de diciembre de 2024 repite las observaciones
  1, 2, 9 y 10 del oficio de octubre, mismo radicado `STEST 202434601243021` y
  misma numeración. Son persistencias, no observaciones nuevas: la frecuencia
  se cuenta por (radicado IDU, número), no por documento.
- El oficio de junio de 2024 no cita radicado; otro oficio sugiere
  `202434600421281` (13 de marzo de 2024), sin confirmar. Queda nulo.
- Extracción del lote: 4 de 8 documentos (V1 con 54 observaciones, junio con 16,
  octubre con 22 y diciembre con 17). Pendientes V2, enero de 2025 y los dos
  traslados MV2, que no traen el texto de las observaciones.
- C.1443 BDG V1 (marzo de 2023): 54 observaciones de la interventoría, todas con
  página y cita validadas, incluidas las de planos (tablas 2 a 8). Se registraron
  una vez los enunciados repetidos en las tablas. Se dejó fuera una fila de la
  Tabla 4 («Sección típica alzado: No se incluye») por ser una celda demasiado
  corta para citarla. Esa carta no cita radicado IDU: es revisión propia.
- Las citas de celdas de tabla deben caber en una línea del texto del PDF:
  `pdftotext` intercala las columnas vecinas cuando la celda ocupa varias líneas.
