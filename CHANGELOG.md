# Historial de cambios

El proyecto usa SemVer. `VERSION` es la fuente de verdad; `pyproject.toml` debe coincidir.
La versión 0.1.0 es la versión inicial declarada y todavía no tiene una publicación verificada.

## [Unreleased]

### Added

- `rag-gdb matriz` genera `matriz-observaciones.md` (504 observaciones por tema, con fecha,
  contrato y referencia; el contrato sale de `config/contratos-documentos.csv`, revisado
  por documento con evidencia: 453 de 504 observaciones tienen contrato) y
  `rag-gdb informe` genera `informe-corpus.md` con el estado de cada PDF del manifiesto.

- `config/grupos-registro.csv` y `rag-gdb registrar-grupos` conservan los miembros de los
  294 grupos revisados; el checklist traslada enlaces normativos y revisiones al grupo
  actual que reúne la mayoría de sus observaciones, de modo que sobreviven a reconsolidar.
- `config/requisitos-redaccion.csv` redacta el checklist como 93 requisitos genéricos y
  verificables que agrupan los 294 grupos, con 7 reasignaciones de tema; checklist y matriz
  la aplican y `docs/revision-editorial.md` resume criterios y puntos para validar.
- `contratos.csv` incluye 1558, interventoría del contrato 1533.

### Fixed

- El perfil técnico retira rutas obsoletas cuando cambia la extracción de nombres del corpus.
- Las rutas relativas del manifiesto, la validación de extracciones y el hash de
  directorios normativos usan `/` también en Windows, de modo que los resultados
  coinciden con los generados en Linux.

### Changed

- La especificación incorpora lo aprendido en el piloto: objetivo de construcción
  del contrato 348, autoridad del alistamiento IDU 2020 compartido con el 351,
  unidad y frecuencia de observaciones, alcance de RF7 y uso acotado de embeddings
  locales en la fase 1.
- `jsonschema` y `numpy` pasan a dependencias del paquete (ya las instalaba Docling).
- La revisión piloto distingue contenido textual conservado de información visual que requiere consultar el PDF.
- El trabajo fuera de meraxes usa un paquete privado con SHA-256 para los datos
  derivados ignorados; código y entregables finales continúan por Git.

### Added

- Catálogo normativo (RF7): `rag-gdb normativa` verifica por SHA-256 el paquete
  oficial de alistamiento 2020 y extrae requisitos de GU-IC-06, FO-IC-05,
  `Productos_BDG` y `Productos_DWG` para generar `normativa-vigente.md`.
- `rag-gdb enlazar-normativa` ordena con `bge-m3` candidatos auditables entre
  los grupos consolidados y el catálogo oficial, sin aceptar coincidencias de
  forma automática.
- `rag-gdb revisar-enlaces-normativa` obtiene una segunda opinión local y
  reanudable; `config/normativa-enlaces.csv` conserva la revisión humana y el
  checklist publica solo enlaces confirmados. La revisión cubre los 294 grupos:
  261 con respaldo normativo y 33 como prácticas observadas.
- Consolidación (RF8): `rag-gdb consolidar` agrupa observaciones repetidas con
  embeddings locales (bge-m3), con revisión de pares dudosos en
  `config/consolidacion-pares.csv`, frecuencia por radicado IDU y tema según
  `config/temas.csv` y `config/temas-asignacion.csv`. `rag-gdb checklist` genera el
  borrador de `checklist-gdb.md`.
- `rag-gdb proponer`: primera pasada local con Ollama que propone candidatos de
  observación; la cita es el bloque literal del PDF. Prompt en
  `prompts/proponer-observaciones.md`, salida reanudable en `datos/03_candidatos/`.
- Emisor IDU por la primera página («Al responder cite este número») cuando el
  nombre no trae código; la ANI y los formularios de radicación quedan por revisar.
- Extracción de observaciones (RF6): esquema JSON, `rag-gdb validar` (esquema,
  hash, página y cita literal contra el PDF), `rag-gdb paginas` y prompt de
  extracción. Piloto con el primer lote (171 observaciones en los seis oficios C.1443 del primer lote, más dos traslados sin observaciones).
- Clasificación preliminar conservadora por código inicial, tipo y señales GDB,
  con cola explícita de documentos por revisar.
- Registro de decisiones manuales de clasificación por SHA-256 y primer lote
  reanudable de ocho documentos de interventoría.
- Inventario por SHA-256, perfil técnico por página y conversión piloto reanudable.
- Auditoría de la especificación y muestra de cuatro PDF verificada en meraxes-f.
- Política mínima de versión, comprobación local y pruebas en CI.
