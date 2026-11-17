# tool-rag-gdb

Pipeline local para preparar el corpus de geodatabases del IDU. El primer hito
implementa inventario por SHA-256, perfil de texto por página y conversión piloto
reanudable. La [especificación](ESPECIFICACION.md) registra las metas de fase 1.
`VERSION` indica la versión actual; [AGENTS.md](AGENTS.md) define cuándo y cómo
actualizarla. `python3 tools/check_repo.py` comprueba versión y changelog.

## Instalación

En meraxes-f, con Python 3.11 o superior:

```bash
python3 -m venv .venv
.venv/bin/pip install -e '.[conversion,test]'
```

`pdfinfo` y `pdftotext` (Poppler) deben estar en `PATH`. Docling se instala solo
para convertir. Los PDF y resultados viven fuera de Git.
Los entregables finales en `datos/04_entregables/` sí se podrán versionar.
Para retomar el trabajo del repositorio puede usarse `lucia session-start
--dir . --compact`; el pipeline no invoca Lucía.

## Entradas

El ZIP y `Recolector de adjuntos.ods` se copian a meraxes-f en
`~/datos/tool-rag-gdb/entrada/`. Tras verificar el SHA-256 del ZIP en ambos
equipos, se extrae a `~/datos/tool-rag-gdb/pdf/`. Se conserva el ZIP original.
La ruta de los PDF se pasa a la CLI; la estructura interna `IDU/` del ZIP se
mantiene. Nunca se modifica un PDF original.
Usar `python3 -m zipfile -e archivo.zip carpeta` para extraer: `unzip` alteró
nombres con tildes en la prueba inicial de meraxes-f.

## Primer hito

```bash
.venv/bin/rag-gdb inventariar --pdf-dir ~/datos/tool-rag-gdb/pdf \
  --ods ~/datos/tool-rag-gdb/entrada/'Recolector de adjuntos.ods'
.venv/bin/rag-gdb perfilar
```

El manifiesto está en `datos/01_inventario/manifiesto.json`. `perfiles.json`
registra páginas con menos de 40 caracteres como candidatas a OCR; esta regla
es una señal para revisión, no un diagnóstico definitivo. Para convertir una
muestra, crear un TXT con rutas relativas tal como aparecen en el manifiesto:

Se puede pasar `--reglas reglas.json` a `inventariar` con, por ejemplo,
`{"remitentes": ["ejemplo@dominio"], "asuntos": ["accidentalidad"]}`.
El manifiesto conserva los archivos excluidos y su motivo. Las reglas deben
revisarse antes de cualquier uso de IA.

```bash
.venv/bin/rag-gdb convertir --seleccion muestras/piloto.txt
```

La salida se guarda en `datos/02_convertidos/`, junto con `estado.json`. Una
ejecución posterior omite archivos completados con el mismo hash y salidas
existentes. Los errores se registran por PDF y se reintentan al repetir el
comando. `pytest -q` ejecuta las pruebas del primer hito.

## Revisión piloto

Elegir PDF escaneados, con tablas, guías largas y comunicados con observaciones.
Comparar cada original con su Markdown y anotar pérdidas con página en
`datos/04_entregables/revision-piloto.md`. La revisión define ajustes antes de
ampliar el corpus. No se publica un checklist normativo en este hito.
