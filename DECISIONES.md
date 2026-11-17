# Decisiones

| Fecha | Decisión | Evidencia |
|---|---|---|
| 2026-11-17 | Ejecutar fase 1 por hitos; primero inventario y conversión piloto | Acuerdo con Aramis |
| 2026-11-17 | Los criterios de 20 PDF, 10 documentos y 90 % son metas de cierre | Acuerdo con Aramis |
| 2026-11-17 | Copiar y verificar el ZIP en meraxes-f, sin borrar el origen | Evita pérdida antes de la revisión |
| 2026-11-17 | Mantener 18 PDF del inventario como ausentes con motivo pendiente | 508 descargados en ODS frente a 490 PDF en ZIP |
| 2026-11-17 | Usar Lucía para gestión del repo, no como dependencia de ejecución | Acuerdo con Aramis |

## Primer inventario en meraxes-f

- ZIP, ODS y CSV copiados con SHA-256 idéntico en ambos equipos.
- 490 PDF extraídos, 490 coincidencias por hash, cero huérfanos y 18 filas
  `DESCARGADO` sin archivo. El manifiesto conserva las 18 claves.
- Perfil completo: 490 PDF sin errores; 18 con alguna página de texto escaso.
  El umbral de 40 caracteres es provisional y se revisará con el piloto.
- La extracción con `unzip` alteró nombres con tildes. Se repitió con `zipfile`
  de Python y las cuatro rutas de la muestra coincidieron con el manifiesto.
- Docling convirtió los cuatro PDF de `muestras/piloto.txt` sin errores. Los
  JSON conservan 14, 41, 21 y 2 páginas respectivamente.
- El traslado MAB de dos páginas menciona ocho folios anexos que no están en
  ese PDF; se considera contexto y no fuente directa de observaciones.
- La revisión del piloto confirmó que mapas, capturas y marcas rojas pueden
  aportar significado que Markdown no conserva. Para esos casos, la extracción
  de observaciones debe cotejar el PDF y citar la página original.
