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

5. Confirmar que el checklist informa 294 grupos revisados y 261 con enlace
   normativo. En el estado empaquetado las pruebas reportan 45 casos aprobados.

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
- Siguiente trabajo: validar taxonomía y redacción del checklist, generar
  `matriz-observaciones.md` e `informe-corpus.md`, y revisar los criterios de
  aceptación de la fase 1.

## Datos ausentes

El paquete no incluye los PDF originales ni el alistamiento original
`IDU-351-2020`. No son necesarios para la siguiente etapa editorial. Para
corregir citas, revisar evidencia visual o repetir la verificación SHA-256 de la
normativa, Aramis deberá proporcionar nuevamente una ruta a esos originales.

No regenerar `normativa-vigente.md` sin el alistamiento original. No preparar una
versión ni crear tags hasta cerrar los entregables restantes y recibir aceptación
de Aramis.
