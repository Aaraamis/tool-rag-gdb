# tool-rag-gdb — Especificación (v0.2, iterativa)

> Guía de trabajo, no camisa de fuerza. Lo que cambie al implementar se anota en **Decisiones** y se sigue.

## Método de entrega

La fase 1 se construye en hitos verificables. El primero cubre traslado verificado,
inventario, perfil técnico y conversión piloto. Tras revisar resultados reales se
ajustan las decisiones de clasificación, extracción y consolidación. Los criterios
de la sección 8 son metas de cierre de fase 1, no puertas del primer piloto.

Lucía apoya la gestión del repositorio; ninguna función del pipeline depende de ella.
Citadel es una guía opcional para mantener calidad sin añadir capas innecesarias.

## 1. Propósito

Consolidar las observaciones, guías, reglamentos y comunicados del IDU sobre la **geodatabase (GDB)**, recogidos de varios proyectos entre 2019 y 2026, en un conjunto corto de documentos que sirvan para **prevenir esas observaciones en el próximo proyecto**.

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

El ZIP recibido en meleys contiene 490 PDF y todos tienen SHA-256 en la hoja.
La hoja marca 508 PDF como `DESCARGADO`: 18 no están en el ZIP. Su motivo
permanece **sin confirmar** hasta revisar el origen o la depuración manual.
De esos 18, 13 llevan «Accidente de Trabajo» en el nombre, cuatro son campañas
de residuos y uno es un catálogo de pavimentos; la lista exacta saldrá en el
manifiesto.

## 4. Salidas (fase 1)

En `datos/04_entregables/`:

1. **`checklist-gdb.md`**: requisitos de la normativa **vigente**, cada uno con el número de veces que el IDU lo observó y 1–2 ejemplos con su referencia (radicado o archivo y página). Es el entregable principal.
2. **`matriz-observaciones.md`**: todas las observaciones extraídas, agrupadas por tema, con fecha, contrato y referencia.
3. **`normativa-vigente.md`**: guías e instructivos (código, versión, fecha), con la versión vigente marcada y las reemplazadas señaladas.
4. **`informe-corpus.md`**: cuántos documentos entraron, cuántos se descartaron y por qué, cuántos necesitaron OCR y qué quedó pendiente.

## 5. Requisitos funcionales

- **RF1. Inventario**: cruzar los archivos en disco con la hoja de Batea por `sha256`. Señalar los archivos sin fila en la hoja (huérfanos) y las filas sin archivo (ausentes).
- **RF2. Ruido**: excluir por reglas configurables (remitente, patrón de asunto, archivo ausente) antes de usar IA.
- **RF3. Perfil técnico**: número de páginas, texto por página y si necesita OCR.
- **RF4. Conversión**: cada PDF se convierte a JSON de Docling + Markdown y se omite en reanudaciones si su hash y ambas salidas siguen vigentes. Los originales no se tocan nunca.
- **RF5. Clasificación**: tipo de documento y si trata o no de la GDB. Primero reglas; los casos ambiguos los decide el agente.
- **RF6. Extracción**: de cada documento relevante, sacar las observaciones a JSON validado contra un esquema, con la página de origen.
  Si una observación depende de mapas, capturas o marcas por color, se coteja
  la página del PDF; el Markdown por sí solo no basta como evidencia.
- **RF7. Normativa**: identificar código y versión de cada guía o instructivo y marcar cuál es la vigente. La propuesta es automática y la confirmación es manual.
- **RF7b. Emisor**: cada documento se marca como IDU, interventoría, obra o diseños. Solo los del IDU y la interventoría generan observaciones; los de obra y diseños son contexto (cómo se respondió).
- **RF8. Consolidación**: la frecuencia de cada observación se cuenta por radicado IDU de origen, para no contar dos veces un traslado. el agente propone una taxonomía de temas, Aramis la valida, y luego se asigna un tema a cada observación y se generan los entregables.
- **RF9. Reanudable**: cada etapa registra su estado por documento. Si se agota el cupo de la suscripción, el proceso sigue después desde donde quedó, sin repetir trabajo.

## 6. Restricciones

- **Máquina**: todo corre en **meraxes-f** (Fedora, RTX 5070 12 GB).
- **IA**: el agente (hoy Claude Code con suscripción Pro) **orquesta y hace el trabajo de lectura**. No se usa API con pago por token. El volumen se ajusta al cupo de la suscripción: lotes pequeños y reanudación.
- **Independiente del agente**: la lógica vive en scripts Python, prompts en archivos y esquemas JSON. Cualquier agente capaz de leer archivos, ejecutar comandos y escribir JSON debe poder hacer el trabajo.
- **Minimalismo**: archivos planos (CSV, JSON, JSONL, MD). Sin base de datos, sin frameworks de RAG y sin interfaz en la fase 1.

## 7. Fuera de alcance (fase 1)

- Comprimidos (`zip`, `rar`, `7z`) y enlaces de Drive que Batea dejó `PENDIENTE` (ver Decisiones D1, D2).
- La pasada extra de Batea con términos nuevos (D3).
- Índice vectorial, embeddings, Laya y modelo local: son de la fase 2.
- Recuperación visual (ColPali), GraphRAG e interfaz de chat.

## 8. Criterios de aceptación (fase 1)

1. `informe-corpus.md` da cuenta del 100 % de los archivos en disco: procesado, descartado (con motivo) o pendiente.
2. En una muestra de **20 PDF variados** (escaneados, con tablas, guías largas), la conversión revisada a ojo no pierde observaciones.
3. En **10 documentos de observaciones** revisados a mano, la extracción recupera al menos el 90 % de las observaciones numeradas, y cada una apunta a la página correcta.
4. Todos los JSON de `03_extraido/` pasan `validar`.
5. Cada requisito del checklist cita al menos una observación real con su referencia.

## 9. Fase 2: prueba de RAG (resumen, se detalla después)

Índice híbrido local (BM25 + embeddings + reranker) sobre `02_convertidos/`, con metadatos de vigencia, y modelo local en la 5070. Se evalúa contra las observaciones de la fase 1, que hacen de **respuestas conocidas**: recall@k, fidelidad y si evita citar normativa derogada. Laya actúa como router (pregunta puntual → RAG; pregunta global → resultado del map-reduce) y como apoyo en la clasificación.

## 10. Decisiones abiertas

Definiciones operativas del primer hito: *archivo* es una entrada PDF física;
*registro* es una fila de `Inventario`; *documento* es una pieza lógica que
puede tener duplicados físicos. La identidad del radicado de origen y la unidad
exacta de una observación se fijarán con la muestra de extracción, antes de
calcular frecuencias.

| # | Tema | Propuesta inicial |
|---|---|---|
| D1 | 65 comprimidos pendientes. Algunos parecen clave, por ejemplo `Rta CE8495 - Revisión entrega GDB preconstrucción.zip` y anexos de comunicados | Descargar a mano solo los de asunto con revisión, observación o anexo y extraerles los PDF. Las `.gdb.zip` quedan fuera |
| D2 | 386 enlaces de Drive/Docs pendientes | Fuera de la v1. Revisar una muestra de 20 para estimar cuánto valor tienen |
| D3 | Términos que Batea no buscó | Pasada de conteo después de la v1 |
| D4 | Laya en clasificación | Solo en la fase 2, como experimento comparado contra las reglas y el agente |
| D5 | ~~Significado de `C.1443`~~ | **Resuelto 2026-11-15**: el prefijo `C.` identifica los comunicados de la interventoría; 1443 es la interventoría del contrato 348 (TM grupo 4) |
| D6 | ~~Contratos 1385 y 1533~~ | **Resuelto 2026-11-15**: entran al alcance |
| D7 | ~~Emisor por código~~ | **Resuelto 2026-11-15**: `STEST/STMST` = IDU; `C.` = interventoría; `E-IDU-` = obra; `MI-DIS-IDU-` = memorando interno diseños → obra |
