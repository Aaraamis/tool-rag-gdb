# tool-rag-gdb — Especificación (v0.3, iterativa)

> Guía de trabajo, no camisa de fuerza. Lo que cambie al implementar se anota en **Decisiones** y se sigue.

## Método de entrega

La fase 1 se construye en hitos verificables. El primero cubre traslado verificado,
inventario, perfil técnico y conversión piloto. Tras revisar resultados reales se
ajustan las decisiones de clasificación, extracción y consolidación. Los criterios
de la sección 8 son metas de cierre de fase 1, no puertas del primer piloto.

El entregable concreto es la revisión de la GDB del contrato IDU 348 en etapa de
construcción (récord). La etapa de diseños ya fue aprobada. La normativa aplicable
es el paquete de alistamiento de 2020 que el IDU entregó para los contratos 348 y
351; el nombre de un archivo o plantilla con el número 351 no limita por sí solo su
aplicación al 348.

Lucía apoya la gestión del repositorio; ninguna función del pipeline depende de ella.
Citadel es una guía opcional para mantener calidad sin añadir capas innecesarias.

## 1. Propósito

Consolidar las observaciones, guías, reglamentos y comunicados del IDU sobre la
**geodatabase (GDB)**, recogidos de varios proyectos entre 2019 y 2026, en un
conjunto corto de documentos que sirvan para **prevenir esas observaciones en la
entrega de construcción (récord) del contrato 348**.

Objetivo secundario: dejar un corpus limpio, convertido y con datos de referencia verificados, para una **prueba controlada de RAG local** (fase 2) antes del RAG grande de [tool-talia].

## 2. Usuario y uso

- Usuario único: Aramis.
- Uso: consulta y preparación del próximo proyecto. Entregables en Markdown.
- Plazo: el entregable de la fase 1 tiene que estar listo antes del inicio del próximo proyecto (≈ 1 mes).

## 3. Entradas

| Entrada | Ubicación | Notas |
|---|---|---|
| PDF descargados por tool-batea | Copia local en meraxes-f (origen: Drive, `Gmail - Recolector de adjuntos/IDU`) | ≈ 490 archivos, ya filtrados a mano (se borraron los de accidentalidad) |
| Hoja `Recolector_de_adjuntos` | `.ods` / Google Sheet de Batea, pestaña `Inventario` | Por adjunto: fecha, remitente, asunto, id de correo, nombre, md5, sha256, enlace, estado |
| `contratos.csv` | Completo (2026-11-15) | `contrato, tipo, contrato_obra, proyecto`. Contratos IDU en alcance: 348, 351, 1383, 1384, 1385, 1443 (interventoría de 348), 1531, 1533, 1712 |
| Alistamiento IDU 2020 | Copia verificada de `IDU-351-2020` | Paquete oficial entregado por el IDU para 348 y 351; sus documentos y plantillas se registran por ruta y SHA-256 |

El ZIP recibido en meleys contiene 490 PDF y todos tienen SHA-256 en la hoja.
La hoja marca 508 PDF como `DESCARGADO`: 18 no están en el ZIP. Su motivo
permanece **sin confirmar** hasta revisar el origen o la depuración manual.
De esos 18, 13 llevan «Accidente de Trabajo» en el nombre, cuatro son campañas
de residuos y uno es un catálogo de pavimentos; la lista exacta saldrá en el
manifiesto.

## 4. Salidas (fase 1)

En `datos/04_entregables/`:

1. **`checklist-gdb.md`**: requisitos de la normativa **vigente**, enlazados con su
   fuente oficial, el número de radicados IDU distintos que los observaron y 1–2
   ejemplos con referencia (radicado o archivo y página). Las exigencias recurrentes
   no encontradas en una fuente escrita se separan y se identifican como prácticas
   observadas. Es el entregable principal.
2. **`matriz-observaciones.md`**: todas las observaciones extraídas, agrupadas por tema, con fecha, contrato y referencia.
3. **`normativa-vigente.md`**: inventario confirmado del paquete oficial y catálogo
   de requisitos por fuente y sección. Para esta entrega, «vigente» significa
   aplicable según el alistamiento IDU 2020 para 348 y 351; no significa la versión
   más reciente publicada después de ese paquete.
4. **`informe-corpus.md`**: cuántos documentos entraron, cuántos se descartaron y por qué, cuántos necesitaron OCR y qué quedó pendiente.

## 5. Requisitos funcionales

- **RF1. Inventario**: cruzar los archivos en disco con la hoja de Batea por `sha256`. Señalar los archivos sin fila en la hoja (huérfanos) y las filas sin archivo (ausentes).
- **RF2. Ruido**: excluir por reglas configurables (remitente, patrón de asunto, archivo ausente) antes de usar IA.
- **RF3. Perfil técnico**: número de páginas, texto por página y si necesita OCR.
- **RF4. Conversión**: cada PDF se convierte a JSON de Docling + Markdown y se omite en reanudaciones si su hash y ambas salidas siguen vigentes. Los originales no se tocan nunca.
- **RF5. Clasificación**: tipo de documento y si trata o no de la GDB. Primero reglas; los casos ambiguos los decide el agente.
  En la primera pasada, una señal positiva en el nombre confirma relevancia;
  una mención en el PDF produce `probable` o `posible` y se revisa. La ausencia
  de términos no equivale a `no`, especialmente en documentos escaneados.
- **RF6. Extracción**: de cada documento relevante, sacar las observaciones a JSON validado contra un esquema, con la página de origen.
  Si una observación depende de mapas o capturas, se coteja la página del PDF;
  el Markdown por sí solo no basta como evidencia. El texto en rojo de las
  tablas de la interventoría es énfasis de sus propias observaciones, no un filtro.
  La unidad es un enunciado distinto por documento: si se repite en varias filas o
  planos de una tabla se registra una sola vez. Las observaciones sobre planos sí se
  extraen. IDU e interventoría pueden originar observaciones; obra y diseños aportan
  contexto sobre su respuesta.
- **RF7. Normativa**: verificar por SHA-256 el registro de documentos del
  alistamiento, identificar código, versión y aplicabilidad a construcción, extraer
  un catálogo estructurado de requisitos oficiales y enlazarlo con los grupos del
  checklist. Las fuentes principales son GU-IC-06, FO-IC-05, `Productos_BDG` y
  `Productos_DWG`; las demás guías y plantillas se registran aunque no todas generen
  requisitos. La propuesta automática y los enlaces dudosos requieren confirmación
  manual. En el piloto quedaron revisados los 294 grupos: 261 con respaldo
  normativo y 33 como prácticas observadas sin regla escrita localizada.
- **RF7b. Emisor**: cada documento se marca como IDU, interventoría, obra o diseños.
  Solo IDU e interventoría generan observaciones. La primera página y señales como
  «Al responder cite este número» prevalecen sobre nombres ambiguos; traslados y
  copias conservan el radicado IDU de origen cuando pueda verificarse.
- **RF8. Consolidación**: la frecuencia se cuenta por radicado IDU distinto, no por
  archivo ni por traslado. Cuando una serie trae número de observación, la identidad
  es `(radicado IDU, número)` y los seguimientos conservan el estado más reciente.
  La frecuencia de interventoría se informa aparte. El agente propone una taxonomía
  de temas, Aramis la valida, y luego se asigna un tema a cada grupo y se generan los
  entregables.
  Implementado con `rag-gdb consolidar` (embeddings locales y revisión de pares
  dudosos) y `rag-gdb checklist`. La taxonomía propuesta está en
  `config/temas.csv`, pendiente de validación y redacción editorial.
- **RF9. Reanudable**: cada etapa registra su estado por documento. Si se agota el cupo de la suscripción, el proceso sigue después desde donde quedó, sin repetir trabajo.

## 6. Restricciones

- **Máquina**: la extracción principal y el acceso a originales ocurren en
  **meraxes-f** (Fedora, RTX 5070 12 GB). La revisión editorial puede continuar
  en otro equipo con un paquete privado de datos derivados verificado por SHA-256.
- **IA**: el agente **orquesta y decide**. No se usa API con pago por token. La
  primera lectura mecánica se delega en `qwen3.5:9b` local vía Ollama
  (`rag-gdb proponer`), pero el agente revisa los candidatos y la cita literal del
  PDF sigue siendo la evidencia. El volumen se ajusta al cupo disponible: lotes
  pequeños y reanudación.
- **Independiente del agente**: la lógica vive en scripts Python, prompts en archivos y esquemas JSON. Cualquier agente capaz de leer archivos, ejecutar comandos y escribir JSON debe poder hacer el trabajo.
- **Minimalismo**: archivos planos (CSV, JSON, JSONL, MD). Sin base de datos, sin frameworks de RAG y sin interfaz en la fase 1.

## 7. Fuera de alcance (fase 1)

- Comprimidos (`zip`, `rar`, `7z`) y enlaces de Drive que Batea dejó `PENDIENTE` (ver Decisiones D1, D2).
- La pasada extra de Batea con términos nuevos (D3).
- Índice de recuperación, reranker, Laya y respuestas RAG son de la fase 2. En la
  fase 1 se permiten embeddings locales únicamente como herramienta de
  consolidación, clasificación temática y propuesta de enlaces normativos; no
  constituyen todavía un índice de consulta.
- Recuperación visual (ColPali), GraphRAG e interfaz de chat.

## 8. Criterios de aceptación (fase 1)

1. `informe-corpus.md` da cuenta del 100 % de los archivos en disco: procesado, descartado (con motivo) o pendiente.
2. En una muestra de **20 PDF variados** (escaneados, con tablas, guías largas), la
   conversión revisada contra el PDF no pierde observaciones. Mapas, capturas y otras
   evidencias visuales que no sobrevivan a Markdown quedan señaladas para cotejo.
3. En **10 documentos de observaciones** revisados a mano, la extracción recupera al menos el 90 % de las observaciones numeradas, y cada una apunta a la página correcta.
4. Todos los JSON de `03_extraido/` pasan `validar`.
5. Cada requisito del checklist cita al menos una observación real con su referencia.
6. Cada requisito enlaza una fuente y sección del catálogo normativo, o aparece en
   una sección separada como práctica observada sin respaldo escrito localizado.

## 9. Fase 2: prueba de RAG (resumen, se detalla después)

Índice híbrido local (BM25 + embeddings + reranker) sobre `02_convertidos/`, con metadatos de vigencia, y modelo local en la 5070. Se evalúa contra las observaciones de la fase 1, que hacen de **respuestas conocidas**: recall@k, fidelidad y si evita citar normativa derogada. Laya actúa como router (pregunta puntual → RAG; pregunta global → resultado del map-reduce) y como apoyo en la clasificación.

## 10. Decisiones abiertas y resueltas

Definiciones operativas del primer hito: *archivo* es una entrada PDF física;
*registro* es una fila de `Inventario`; *documento* es una pieza lógica que
puede tener duplicados físicos. La unidad de observación, el radicado de origen y
la frecuencia se rigen por RF6 y RF8.

| # | Tema | Propuesta inicial |
|---|---|---|
| D1 | 65 comprimidos pendientes. Algunos parecen clave, por ejemplo `Rta CE8495 - Revisión entrega GDB preconstrucción.zip` y anexos de comunicados | Descargar a mano solo los de asunto con revisión, observación o anexo y extraerles los PDF. Las `.gdb.zip` quedan fuera |
| D2 | 386 enlaces de Drive/Docs pendientes | Fuera de la v1. Revisar una muestra de 20 para estimar cuánto valor tienen |
| D3 | Términos que Batea no buscó | Pasada de conteo después de la v1 |
| D4 | Laya en clasificación | Solo en la fase 2, como experimento comparado contra las reglas y el agente. Evaluado 2026-11-17: clasifica y puntúa pero no extrae; sin ajuste está cerca del azar. Se ajustaría con las observaciones ya etiquetadas |
| D5 | ~~Significado de `C.1443`~~ | **Resuelto 2026-11-15**: el prefijo `C.` identifica los comunicados de la interventoría; 1443 es la interventoría del contrato 348 (TM grupo 4) |
| D6 | ~~Contratos 1385 y 1533~~ | **Resuelto 2026-11-15**: entran al alcance |
| D7 | ~~Emisor por código~~ | **Resuelto 2026-11-15**: `STEST/STMST` = IDU; `C.` = interventoría; `E-IDU-` = obra; `MI-DIS-IDU-` = memorando interno diseños → obra |
| D8 | ~~Normativa aplicable al contrato 348~~ | **Resuelto 2026-11-17**: el paquete de alistamiento 2020 `IDU-351-2020` fue entregado por el IDU para los contratos 348 y 351; es la autoridad para la entrega de construcción del 348 |
