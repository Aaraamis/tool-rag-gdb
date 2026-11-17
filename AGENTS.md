# Guía del repositorio

Este repositorio implementa un pipeline Python local para el corpus GDB del IDU.
La [especificación](ESPECIFICACION.md) define el objetivo; el [README](README.md)
describe los comandos actuales. Mantén la solución pequeña y ajusta la
especificación a partir de los resultados del piloto. Lucía apoya la gestión del
repo, pero la aplicación no depende de ella. Citadel es una guía, no un requisito
para añadir herramientas o capas.

## Inicio y verificación

1. Revisa `git status --short --branch`, `VERSION`, `CHANGELOG.md` y
   `DECISIONES.md`. Preserva ediciones ajenas.
2. Ejecuta `python3 tools/check_repo.py` y `PYTHONPATH=src python3 -m pytest -q`.
   En meraxes-f, usa `.venv/bin/python -m pytest -q` si el entorno existe.
3. Al cerrar una sesión, informa las pruebas ejecutadas, los cambios pendientes
   en `Unreleased`, la versión actual y si hay razones para preparar una nueva.
   Para retomar contexto puedes usar `lucia session-start --dir . --compact`.
   Registra decisiones o hitos verificables con `lucia memory --action add` y
   versiona `.lucia/memory.jsonl` junto con el cambio que describe. El índice
   local `.lucia/symbols.db` permanece fuera de Git.

## Versiones y cambios

- `VERSION` es la autoridad. `pyproject.toml` contiene el mismo valor para el
  paquete; el chequeo local impide que diverjan. Nunca cambies solo uno.
- Usa SemVer `MAJOR.MINOR.PATCH` y etiquetas `vMAJOR.MINOR.PATCH`. Mientras la
  API siga en `0.y.z`, una funcionalidad nueva o cambio incompatible sube
  `MINOR`; una corrección compatible sube `PATCH`. Describe migraciones cuando
  haya incompatibilidad. Al establecer un contrato estable, decide `1.0.0`
  explícitamente con Aramis.
- Los commits ordinarios acumulan cambios relevantes en la única sección
  `Unreleased`; **no** suben la versión automáticamente. Prepara una versión
  cuando Aramis acepte un hito para publicar o distribuir.
- En la preparación de una versión, el agente propone el número según el
  impacto total desde la última versión verificada, actualiza `VERSION` y
  `pyproject.toml` juntos, mueve las notas a `## [X.Y.Z] - AAAA-MM-DD`, deja
  `Unreleased` vacío y ejecuta las pruebas. No inventes un tag o fecha
  histórica: este repo aún no tiene un release verificado.
- Crear tag, push, GitHub Release o publicación son pasos separados. No los
  ejecutes como efecto de editar la versión.
- Usa títulos de commit convencionales (`feat:`, `fix:`, `docs:`, `chore:`);
  `!` o `BREAKING CHANGE:` señala incompatibilidad. Agrega archivos a Git de
  forma explícita; no uses `git commit -a` ni `git commit .`.

## Datos

Los PDF, el ODS de entrada y los JSON/Markdown intermedios no van a Git.
Versiona código, reglas, muestras y entregables finales revisados. No cambies
PDF originales. La ejecución principal ocurre en meraxes-f con rutas de datos
configurables.
