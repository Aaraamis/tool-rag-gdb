# Traspaso para la próxima sesión

El código y su historial se trasladan por Git. El archivo de transferencia
conserva solamente los datos de trabajo que `.gitignore` excluye de GitHub.

## Cuando Aramis entregue la ruta del comprimido

1. Clonar o actualizar `tool-rag-gdb` desde GitHub y leer `AGENTS.md`.
2. Localizar junto al comprimido el archivo con sufijo `.sha256` y verificarlo:

   ```bash
   cd "$(dirname RUTA_DEL_COMPRIMIDO)"
   sha256sum -c "$(basename RUTA_DEL_COMPRIMIDO).sha256"
   ```

3. Extraer el paquete en la raíz del clon. El archivo contiene el directorio
   `datos/`, por lo que no debe extraerse dentro de otro `datos/`:

   ```bash
   cd /RUTA/DEL/CLON/tool-rag-gdb
   tar -xzf RUTA_DEL_COMPRIMIDO
   ```

4. Crear un entorno nuevo e instalar el proyecto:

   ```bash
   python3 -m venv .venv
   .venv/bin/pip install -e '.[test]'
   python3 tools/check_repo.py
   PYTHONPATH=src .venv/bin/python -m pytest -q
   PYTHONPATH=src .venv/bin/python -m rag_gdb.cli checklist
   ```

5. Confirmar que el checklist informa 294 grupos revisados, 261 con enlace
   normativo y 93 requisitos redactados. Las pruebas reportan 51 casos
   aprobados (45 en el estado empaquetado del 2026-11-17).

## Contenido no versionado

- `datos/01_inventario`: manifiesto, perfiles y clasificación.
- `datos/02_convertidos`: 23 archivos de conversión y su estado.
- `datos/03_candidatos`: candidatos y estado reanudable.
- `datos/03_extraido`: 45 JSON de observaciones validadas.
- `datos/04_consolidado`: 294 grupos, catálogo, candidatos, decisiones de
  revisión y embeddings.

Los entregables finales de `datos/04_entregables` deben llegar por GitHub una
vez que Aramis actualice el repositorio; no forman parte del paquete privado.

## Estado y continuación

- RF7 está revisado para los 294 grupos: 261 con respaldo normativo y 33 como
  prácticas observadas sin regla escrita localizada.
- Se aceptaron 307 relaciones normativas: 216 directas y 91 parciales.
- Sesión del 2026-11-18 (fuera de meraxes-f): `matriz-observaciones.md` e
  `informe-corpus.md` generados; contrato por documento en
  `config/contratos-documentos.csv` (9 sin determinar); redacción editorial en
  93 requisitos (`config/requisitos-redaccion.csv`, pendiente de validación);
  `config/grupos-registro.csv` conserva las decisiones al reconsolidar. Estado
  de los criterios: `docs/aceptacion-fase1.md`.
- Siguiente trabajo, en meraxes-f con los PDF y Ollama: procesar los 445
  pendientes (`proponer`, depurar, `validar`, `consolidar`), añadir el contrato
  de los documentos nuevos, revisar normativa y redacción de los grupos nuevos,
  ejecutar `registrar-grupos` y regenerar `checklist`, `matriz` e `informe`.
  Cerrar los criterios 2 y 3 con los originales.

## Datos ausentes

El paquete no incluye los PDF originales ni el alistamiento original
`IDU-351-2020`. No son necesarios para la siguiente etapa editorial. Para
corregir citas, revisar evidencia visual o repetir la verificación SHA-256 de la
normativa, Aramis deberá proporcionar nuevamente una ruta a esos originales.

No regenerar `normativa-vigente.md` sin el alistamiento original. No preparar una
versión ni crear tags hasta cerrar los entregables restantes y recibir aceptación
de Aramis.
