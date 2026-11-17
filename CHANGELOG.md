# Historial de cambios

El proyecto usa SemVer. `VERSION` es la fuente de verdad; `pyproject.toml` debe coincidir.
La versión 0.1.0 es la versión inicial declarada y todavía no tiene una publicación verificada.

## [Unreleased]

### Fixed

- El perfil técnico retira rutas obsoletas cuando cambia la extracción de nombres del corpus.

### Changed

- `jsonschema` y `numpy` pasan a dependencias del paquete (ya las instalaba Docling).
- La revisión piloto distingue contenido textual conservado de información visual que requiere consultar el PDF.

### Added

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
