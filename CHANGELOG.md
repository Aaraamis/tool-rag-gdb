# Historial de cambios

El proyecto usa SemVer. `VERSION` es la fuente de verdad; `pyproject.toml` debe coincidir.
La versión 0.1.0 es la versión inicial declarada y todavía no tiene una publicación verificada.

## [Unreleased]

### Fixed

- El perfil técnico retira rutas obsoletas cuando cambia la extracción de nombres del corpus.

### Changed

- La revisión piloto distingue contenido textual conservado de información visual que requiere consultar el PDF.

### Added

- Clasificación preliminar conservadora por código inicial, tipo y señales GDB,
  con cola explícita de documentos por revisar.
- Registro de decisiones manuales de clasificación por SHA-256 y primer lote
  reanudable de ocho documentos de interventoría.
- Inventario por SHA-256, perfil técnico por página y conversión piloto reanudable.
- Auditoría de la especificación y muestra de cuatro PDF verificada en meraxes-f.
- Política mínima de versión, comprobación local y pruebas en CI.
