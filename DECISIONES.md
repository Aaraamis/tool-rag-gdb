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
| 2026-11-17 | Delegar la primera lectura en qwen3.5:9b local (Ollama) con selección de bloques; el agente revisa | Medido contra la referencia del primer lote; aprobado por Aramis |
| 2026-11-17 | Laya queda para la fase 2 (D4): no extrae y sin ajuste está cerca del azar | Evaluación del repositorio y de sus límites declarados |
| 2026-11-17 | Emisor IDU por «Al responder cite este número» en la primera página | Muestra de los 72 PDF con radicado numérico; aprobado por Aramis |
| 2026-11-17 | Frecuencia de un requisito = radicados IDU distintos; la interventoría se informa aparte | ESPECIFICACION RF8 y checklist |
| 2026-11-17 | Taxonomía de 11 temas propuesta en `config/temas.csv`, pendiente de validación de Aramis | Lectura de los 306 grupos iniciales |
| 2026-11-17 | El paquete `IDU-351-2020` es el alistamiento oficial de 2020 entregado por el IDU para los contratos 348 y 351; aplica a la entrega de construcción del 348 | Confirmación de Aramis; 649 archivos del origen y la copia coinciden por hash |
| 2026-11-17 | La similitud de embeddings solo ordena candidatos de enlace normativo; cada enlace se confirma manualmente | La primera medición RF7 produjo falsos positivos incluso por encima de 0,70 |
| 2026-11-17 | Código y entregables finales viajan por Git; los intermedios ignorados se trasladan en un paquete privado con SHA-256 | La siguiente sesión se ejecutará fuera de meraxes-f |
| 2026-11-18 | El contrato de cada documento extraído se registra a mano en `config/contratos-documentos.csv` como contrato de obra, con su evidencia; C.1443 → 348, MAB-1/2-1463 → 1385, MV2 → 1384. Sin señal queda «sin determinar» (9 documentos) | Asuntos, citas y respuestas que citan el mismo radicado; pedido por Aramis |
| 2026-11-18 | 1558 es la interventoría del contrato 1533 y se añade a `contratos.csv`; 1309 no es un contrato del alcance (`BASE-IDU-1309-2018.dwg` se trata como archivo de ejemplo o referencia) | Confirmación de Aramis; el corpus escribe siempre 1558 (`Contrato No 1558`, `MAB-1-1558-…`) |
| 2026-11-18 | Las decisiones por grupo (enlaces normativos, redacción) se trasladan al grupo actual que reúne la mayoría de sus observaciones, mediante `config/grupos-registro.csv`; un grupo dividido vuelve a quedar pendiente | `clave_grupo` es un hash de los miembros y cambia al reconsolidar con más documentos |
| 2026-11-18 | Propuesta editorial: 294 grupos redactados como 93 requisitos genéricos, con 7 reasignaciones de tema; pendiente de validación | `docs/revision-editorial.md` |
| 2026-11-18 | Las prácticas observadas sin respaldo escrito van en una sección aparte del checklist | Criterio de aceptación 6 de la especificación |
| 2026-11-18 | Completar todos los PDF pendientes, no solo el piloto | Pedido por Aramis; se ejecuta en meraxes-f, donde están los PDF y Ollama |

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
- Extracción del lote completa (8 de 8): V1 con 54 observaciones, V2 con 41,
  junio de 2024 con 16, octubre con 22, diciembre con 17 y enero de 2025 con 21
  (171 en total). Los dos traslados MV2 quedan registrados sin observaciones
  porque no traen su texto.
- La V2 (julio de 2023) y enero de 2025 son rondas de seguimiento: repiten los
  enunciados anteriores con su estado nuevo. Enero repite las observaciones 1,
  2, 9 y 10 del radicado `STEST 202434601243021` con la «VALIDACIÓN No. 3»
  (1 atendida, 2 parcial, 9 parcial, 10 parcial). La consolidación (RF8) debe
  unir los enunciados repetidos por texto y radicado, y quedarse con el estado
  más reciente.
- **Hallazgo de clasificación:** 72 PDF tienen nombre de radicado numérico
  (p. ej. `2021-06-18_20213560877971.pdf` y su anexo `120213560877971_00002.pdf`).
  Son oficios y memorandos del IDU con las observaciones de origen, y la
  clasificación los deja con emisor `por_revisar`. Son la fuente primaria de
  los radicados que citan los traslados MV2 y los oficios de la interventoría.
  Pendiente: clasificarlos como IDU y extraerlos.
- C.1443 BDG V1 (marzo de 2023): 54 observaciones de la interventoría, todas con
  página y cita validadas, incluidas las de planos (tablas 2 a 8). Se registraron
  una vez los enunciados repetidos en las tablas. Se dejó fuera una fila de la
  Tabla 4 («Sección típica alzado: No se incluye») por ser una celda demasiado
  corta para citarla. Esa carta no cita radicado IDU: es revisión propia.
- Las citas de celdas de tabla deben caber en una línea del texto del PDF:
  `pdftotext` intercala las columnas vecinas cuando la celda ocupa varias líneas.

## Delegación en modelos locales

- Laya (NandhaKishorM/laya, Apache-2.0) es un motor de decisión: elige, puntúa
  y responde sí/no con probabilidades calibradas y una ruta `auto`/`review`. No
  extrae ni resume. Su README declara que los checkpoints base quedan cerca del
  azar sin ajuste; el ajuste pide unas 35 filas etiquetadas por pregunta.
- qwen3.5:9b (Ollama, Q4_K_M, ~11 GB de VRAM cargado) falla al copiar citas
  literales (53 % inventadas). Eligiendo bloques numerados por página recuperó
  14/16, 22/22, 34/41 y 52/54 de la referencia del primer lote (junio y octubre
  de 2024, V2 y V1), con precisión aproximada de 60 a 86 %, en 15 a 61 s por
  documento. La recuperación está algo inflada porque un bloque puede cubrir
  varias entradas; la precisión está subestimada porque parte de lo «extra»
  son hallazgos válidos no registrados. gemma3:4b tuvo 25 % de precisión.
- Regla de emisor: de los 72 PDF con radicado numérico, 65 llevan «Al
  responder cite este número» (oficios y memorandos del IDU: STMSV, STEST,
  DTE, DTINI, STRF…); 2 son de la ANI («Radicado ANI») y 5 son formularios de
  radicación web o de atención al ciudadano. Con la regla, 87 documentos pasan
  a emisor IDU, 12 de ellos con otro nombre: `R-IDU…` es el sello de recibido
  del contratista sobre una carta del IDU, y los anexos MAB contienen el oficio.
- `rag-gdb proponer` real (segmentación por viñetas, rótulos y frases; bloques
  de 124 a 277 caracteres de media; deduplicación por texto en cada documento):
  sobre el primer lote recupera 150 de 171 observaciones de referencia (88 %),
  con 281 candidatos de los que 162 coinciden con la referencia (58 %), en 3 min.
  La primera versión, con párrafos completos y cita recortada a 300 caracteres,
  solo llegaba al 49 %: el modelo elegía bien, pero la cita no contenía la
  observación.
- Primera pasada sobre los oficios y memorandos del IDU con señal GDB
  (`muestras/idu-radicados-1.txt`): 67 documentos, 387 candidatos en 7 min, todos
  válidos. Los 30 sin candidatos son cartas de remisión de una página o
  memorandos de aprobación («se ajusta a los requerimientos»); estos últimos
  sirven para fechar el cierre de observaciones. Las dos copias de GUIC06 se
  sacaron de la selección: son normativa (RF7), no observaciones.
- Depuración de los 387 candidatos de oficios IDU (2026-11-17): quedan 333
  observaciones en 37 documentos, todas con `autor: idu`, número tomado del
  inicio de la cita y radicado de origen leído del encabezado de la página
  donde aparece (la copia `R-IDU…` hereda así el radicado del memorando DTE que
  contiene). Se descartaron 54: fórmulas de cierre y avisos sobre mesas de
  trabajo (37), pies de firma y encabezados (9), fragmentos (5) y ejemplos del
  mismo enunciado (3). Los resúmenes son los del modelo local, revisados por
  muestreo. Total extraído: 504 observaciones en 45 documentos.
- Los 30 documentos IDU sin candidatos no se registran como extraídos: se
  verificaron dos (memorandos de aprobación sin observaciones); los demás son
  cartas de remisión de una página o aprobaciones, pendientes de confirmar.
- Para RF8 se evaluó `bge-m3` (Ollama, 1,2 GB, multilingüe) sobre las 504
  observaciones (resumen + cita, 19 s). Con similitud ≥ 0,85 con otra de otro
  documento los pares son el mismo requisito; entre 0,80 y 0,85 casi siempre;
  entre 0,75 y 0,80 son temas relacionados pero distintos. Propuesta: agrupar
  de forma automática desde 0,85, revisar los pares entre 0,78 y 0,85 y tratar
  el resto como distintos. 206 observaciones tienen un par ≥ 0,90 en otro
  documento.
- El último dígito del radicado IDU parece indicar el tipo (1 salida, 2
  entrada, 3 memorando); no se usa como regla porque la ANI usa el mismo formato.

## Consolidación (RF8), borrador editorial

- 504 observaciones de 41 documentos con observaciones quedan en 294 grupos;
  188 los observó el IDU al menos una vez y 106 solo la interventoría. Los más
  repetidos: intervenciones de los planos ausentes en las tablas de reporte
  (16 radicados), fecha de registro de las áreas de intervención distinta entre
  GDB, CAD y FOIC09 (12), revisar integralmente los productos (10) y FOIC09 que
  no concuerda con la base CAD y la GDB (8).
- Agrupación: unión desde 0,85 de similitud con un piso de 0,78 entre todos los
  miembros, para evitar cadenas. Se revisaron 157 pares dudosos en siete rondas
  (`config/consolidacion-pares.csv`). Las pruebas mostraron que un par sobre el
  umbral bloqueado por el piso no se listaba: ahora se revisa también, y un «no»
  entre dos miembros cierra la revisión entre sus grupos.
- Tema: centroide del grupo frente a la descripción de cada tema. qwen3.5:9b dio
  una segunda opinión; coincidieron en 204 de 306 grupos y los 102 desacuerdos
  se decidieron a mano (`config/temas-asignacion.csv`). Criterio: el tema del
  objeto observado, no del archivo nombrado; la fecha de registro y el registro
  de intervenciones van a consistencia entre productos (T09). Caso para validar:
  el grupo que une el registro de intervenciones con los CIV y PK_ID de las
  tablas quedó en T07.
- El checklist usaba como requisito el resumen representativo de cada grupo.
  Desde el 2026-11-18 lo reemplaza la redacción propuesta en
  `config/requisitos-redaccion.csv` (93 requisitos), pendiente de validación de
  Aramis junto con los temas.

## Normativa (RF7), catálogo y revisión completa

- Los 24 documentos del registro coinciden por SHA-256 con el paquete oficial
  de 649 archivos entregado para los contratos 348 y 351.
- El catálogo extrae requisitos de GU-IC-06, FO-IC-05, `Productos_BDG` y
  `Productos_DWG`, incluida la hoja `ElementosConstruccion (Récord)`.
- `bge-m3` propone cinco enlaces por cada grupo consolidado. El tema completo
  mejora la recuperación frente a usar solo su código, pero la aceptación queda
  manual porque una similitud alta no garantiza equivalencia normativa.
- `qwen3.5:9b` revisó los cinco candidatos de los 294 grupos y sugirió 60
  enlaces. La revisión humana cubre ya los 294 grupos: de los 188 observados por
  el IDU, 177 tienen respaldo normativo y 11 quedan como prácticas sin regla
  oficial equivalente; de los 106 exclusivos de la interventoría, 84 tienen
  respaldo y 22 quedan como prácticas observadas. En total se aceptaron 307
  relaciones en 261 grupos (216 directas y 91 parciales); 33 grupos no tienen
  respaldo escrito localizado. Una ausencia de sugerencia del modelo no se
  interpreta por sí sola como ausencia de norma: cada caso fue revisado contra
  el catálogo.
