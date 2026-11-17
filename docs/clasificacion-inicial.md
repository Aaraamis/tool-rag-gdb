# Clasificación inicial del corpus

Estado: 2026-11-17. Resultado completo en meraxes-f:
`~/repos/tool-rag-gdb/datos/01_inventario/clasificacion.csv` (490 filas).
Comando: `rag-gdb clasificar --leer-texto`.

| Campo | Resultado |
|---|---|
| Emisor | 85 interventoría, 87 obra, 68 diseños, 4 IDU, 246 por revisar |
| Tipo | 40 revisión/observaciones, 7 traslados, 84 respuestas, 29 actas, 3 guías/instructivos, 148 comunicados, 179 por revisar |
| Señal GDB | 153 confirmadas por nombre o revisión manual, 208 probables por mención en PDF, 13 posibles por SIG/CAD, 116 por revisar |
| Filas que aún requieren revisar algún campo | 350 |

Las reglas usan el código **inicial** del archivo para el emisor. Una mención
posterior de `STEST` o `C.1443` en una respuesta no cambia su emisor. `MAB-1463`
y `MV2` se identificaron como interventorías por sus primeras páginas; otros
códigos MAB siguen pendientes. La ausencia de términos GDB en el texto no
demuestra irrelevancia, especialmente en PDF escaneados.

Las decisiones revisadas se guardan en `config/clasificacion-manual.csv` por
SHA-256 con página y justificación. El lote
`muestras/lote-observaciones-1.txt` selecciona ocho documentos de
interventoría con revisión u observaciones y señal GDB. Dos documentos MV2 de
ese lote son traslados del IDU, confirmados al leer sus páginas únicas. Los
traslados se mantienen separados para no duplicar la frecuencia del radicado
IDU de origen.
