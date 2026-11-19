# Traspaso para la próxima sesión

Última actualización: 2026-11-19. El código, la configuración revisada y los
entregables viajan por Git. Los datos intermedios que `.gitignore` excluye
(`datos/01_inventario` a `datos/04_consolidado`) están en meraxes-f o en el
paquete privado del 2026-11-17. Las sesiones del 2026-11-18 y del 2026-11-19
(en otro PC) no los modificaron: todo lo que produjeron está versionado. La
próxima sesión continúa en meraxes-f: basta `git pull`.

## 1. Arranque

1. Leer `AGENTS.md`. Revisar `git status --short --branch`, `VERSION`,
   `CHANGELOG.md` (sección `Unreleased`) y `DECISIONES.md`.
2. Preparar los datos según el equipo:
   - **meraxes-f:** `git pull` en el clon. Los datos de `datos/` ya están; las
     rutas de PDF y ODS figuran en `datos/01_inventario/manifiesto.json`.
   - **Otro equipo:** cuando Aramis entregue la ruta del comprimido, verificar
     su `.sha256` y extraerlo en la raíz del clon, que ya contiene `datos/`:

     ```bash
     cd "$(dirname RUTA_DEL_COMPRIMIDO)"
     sha256sum -c "$(basename RUTA_DEL_COMPRIMIDO).sha256"
     cd /RUTA/DEL/CLON/tool-rag-gdb
     tar -xzf RUTA_DEL_COMPRIMIDO
     ```

3. Crear o actualizar el entorno y verificar (en Windows,
   `.venv\Scripts\python`):

   ```bash
   python3 -m venv .venv
   .venv/bin/pip install -e '.[test]'           # añadir conversion en meraxes-f
   python3 tools/check_repo.py
   PYTHONPATH=src .venv/bin/python -m pytest -q
   .venv/bin/ruff check --preview src tests tools
   PYTHONPATH=src .venv/bin/python -m rag_gdb.cli checklist
   ```

4. Valores esperados: 52 pruebas aprobadas, Ruff sin avisos y el checklist con
   `{"grupos": 294, "requisitos": 95, "requisitos_redactados": 95,
   "grupos_normativa_revisados": 294, "grupos_con_enlace": 261}`. El comando
   reescribe `datos/04_entregables/checklist-gdb.md`; si solo cambia la fecha,
   descartar el cambio con `git checkout`.

## 2. Estado

| Área | Estado | Dónde |
|---|---|---|
| Corpus | 490 PDF: 45 procesados, 445 pendientes, 0 descartados; 18 necesitan OCR | `datos/04_entregables/informe-corpus.md` |
| Observaciones | 504 en 41 documentos (otros 4 sin observaciones), validadas en meraxes-f el 2026-11-17 | `datos/03_extraido/` |
| Grupos y normativa | 294 grupos, todos revisados; 307 relaciones aceptadas (216 directas, 91 parciales) | `config/normativa-enlaces.csv` |
| Redacción | 95 requisitos (82 con respaldo, 13 prácticas en sección aparte), 7 reasignaciones de tema; Aramis resolvió los 3 puntos del 2026-11-19; **taxonomía y textos aún por validar** | `config/requisitos-redaccion.csv`, `docs/revision-editorial.md` |
| Alcance | Todo lo técnico de la entrega (GDB, CAD, planos, informes, estructura documental); el checklist sirve además de apoyo jurídico-contractual para redactar comunicados | `ESPECIFICACION.md`, `DECISIONES.md` |
| Diccionario de atributos | `Productos_BDG` resumido por feature dataset: 43 clases, 110 tablas, 1066 campos (563 obligatorios y 172 según alcance en construcción) | `docs/diccionario-atributos.md` |
| Contratos | Contrato de obra de los 45 documentos con su evidencia; 9 sin determinar (51 observaciones) | `config/contratos-documentos.csv` |
| Aceptación | Criterios 5 y 6 cumplen; 1 en forma; 4 por repetir; 2 y 3 pendientes | `docs/aceptacion-fase1.md` |
| Versión | `0.1.0`; `Unreleased` acumula las sesiones del 2026-11-18 y 2026-11-19 | `CHANGELOG.md` |

## 3. Siguiente trabajo

Aramis pidió procesar todos los PDF pendientes, no solo los del piloto. Se hace
en meraxes-f, que tiene los PDF, Poppler, Docling y Ollama con
`qwen3.5:9b-q4_K_M` y `bge-m3`. Orden recomendado:

1. **Selección.** Generar listas en `muestras/` con las rutas pendientes del
   manifiesto: primero las 316 marcadas `gdb=si|probable` en
   `clasificacion.csv` y luego las 129 por revisar. Excluir los planos (dibujos):
   lo que importa son comunicados y correos. Procesar por lotes de unas 50 rutas.
2. **Candidatos.** `rag-gdb proponer --seleccion muestras/<lote>.txt`. Los 18
   PDF que necesitan OCR no tienen texto para `pdftotext`; tratarlos aparte con
   `convertir` (Docling) y cotejo visual.
3. **Depuración.** Escribir `datos/03_extraido/` con `prompts/extraer-observaciones.md`
   y el esquema. Seguir las reglas de `DECISIONES.md`: una observación por
   enunciado distinto, radicado de origen tomado del encabezado de la página,
   traslados sin anexo sin observaciones propias y el rojo de la interventoría
   como énfasis. Ejecutar `rag-gdb validar` hasta 0 inválidos.
4. **Contrato.** Añadir a `config/contratos-documentos.csv` una fila por
   documento nuevo (sha256, ruta, contrato de obra, evidencia). Resolver de paso
   los 9 sin determinar con la primera página del PDF. Mapeos confirmados:
   C.1443 → 348, MAB-x-1463 → 1385, MV2 → 1384, MAB-x-1558 → 1533. El 1309 no es
   un contrato del alcance.
5. **Consolidación.** Copiar `datos/04_consolidado/grupos.json` como respaldo y
   ejecutar `rag-gdb consolidar`. Revisar `pares-revisar.csv` y registrar las
   decisiones en `config/consolidacion-pares.csv`.
6. **Normativa y redacción de los grupos nuevos.** `rag-gdb checklist` marca
   como «pendiente de revisión» los grupos sin decisión trasladada.
   - Con `enlazar-normativa` y `revisar-enlaces-normativa` se obtienen
     candidatos. Confirmar a mano en `config/normativa-enlaces.csv` usando la
     `clave_grupo` actual.
   - En `config/requisitos-redaccion.csv`, asignar cada grupo nuevo a un
     `requisito_id` existente (mismo tema y texto) o crear uno nuevo
     `R-Txx-nn`. Los grupos sin fila conservan su enunciado representativo.
   - Al terminar, ejecutar `rag-gdb registrar-grupos`. Solo añade filas: las
     claves antiguas siguen sirviendo para trasladar decisiones.
7. **Entregables.** Regenerar `checklist`, `matriz` e `informe` y actualizar
   `docs/aceptacion-fase1.md`.
8. **Criterios 2 y 3.** Con los originales, revisar 20 PDF variados contra su
   conversión y cotejar a mano 10 documentos de observaciones (al menos 90 %
   recuperado, con la página correcta).

Independiente del punto anterior, Aramis debe validar la taxonomía y la
redacción (`docs/revision-editorial.md`; los tres puntos abiertos quedaron
resueltos el 2026-11-19). Sus correcciones se aplican editando
`config/requisitos-redaccion.csv`. El checklist abarca todo lo técnico de la
entrega y sirve de apoyo jurídico-contractual para redactar comunicados.

Para crear o revisar capas, `docs/diccionario-atributos.md` resume
`Productos_BDG` por feature dataset; se regenera con `rag-gdb diccionario --ods`
cuando cambie la exportación ODS. El ODS no está en Git: Aramis lo tiene junto al
alistamiento (`PresentacionPlanos/1.Base de Datos Geografica/Productos_BDG_valores.ods`);
si se regenera, comparar el SHA-256 que registra el documento.

## 4. Límites

- No regenerar `normativa-vigente.md` sin el alistamiento original `IDU-351-2020`.
- No modificar PDF originales ni versionar datos intermedios.
- No preparar versión ni crear tags hasta cerrar los entregables y recibir
  aceptación de Aramis. Cuando eso ocurra, el impacto acumulado corresponde a
  `0.2.0`.
- La consolidación y la revisión de enlaces dependen de Ollama. Sin Ollama solo
  se puede hacer trabajo editorial sobre lo ya consolidado.
