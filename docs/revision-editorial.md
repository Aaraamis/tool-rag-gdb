# Revisión editorial del checklist (2026-11-18)

Propuesta pendiente de validación de Aramis. Se aplica en el borrador mediante
`config/requisitos-redaccion.csv`; aceptar, cambiar o rechazar una decisión es
editar ese archivo y volver a ejecutar `rag-gdb checklist` y `rag-gdb matriz`.

## Criterios

- Cada requisito se redacta como una instrucción genérica y verificable, sin
  identificadores puntuales (CIV, PK_ID, nombres de plano) que solo valían para
  una entrega. Los casos concretos siguen visibles como ejemplos citados.
- Los grupos que piden lo mismo con otras palabras comparten requisito. La
  frecuencia se recalcula sobre la unión de sus radicados IDU distintos, y los
  enlaces normativos se suman. Los grupos y sus evidencias no cambian.
- Un requisito es práctica observada solo si ninguno de sus grupos tiene enlace
  normativo confirmado.

Resultado: 294 grupos → 93 requisitos (antes uno por grupo). 69 los observó el
IDU. 13 quedan como prácticas observadas, frente a 33 grupos antes.

## Taxonomía

Los 11 temas de `config/temas.csv` cubren el corpus sin huecos ni solapes que
obliguen a cambiarlos. Se proponen 7 reasignaciones de grupo:

| Grupo | De | A | Motivo |
|---|---|---|---|
| G031 | T03 | T02 | Trata del campo REFERENCIA del rótulo, no del XREF en sí |
| G058 | T03 | T04 | Pide el layer correcto de los elementos de exploración |
| G101 | T05 | T01 | Falta de planos de localización: completitud |
| G125 | T05 | T01 | No se presentaron los planos del componente vial: completitud |
| G131 | T10 | T06 | Valor del atributo costo de la tabla de seguimiento |
| G174 | T06 | T10 | SN efectivo frente al informe de deflectometría |
| G285 | T06 | T11 | Responder la tabla de validación de la GDB |

## Puntos resueltos (2026-11-19)

1. **R-T01-10** (mesa del 8/6/2021: DWG primero; PDF y firmas tras la
   aprobación) se mantiene como requisito propio. El repositorio controla todo
   lo técnico y sirve de apoyo jurídico-contractual para redactar comunicados,
   y el acuerdo de la mesa es útil como antecedente.
2. **R-T11-01** no se separa. Se redacta como control de calidad antes de
   entregar. Una nota contractual recuerda que el contenido, la calidad y la
   completitud de los archivos son responsabilidad del contratista
   (GU-IC-06 §11.1); sirve de apoyo para redactar comunicados. El repositorio es la fuente de
   verdad de la que se exporta lo que requieren las demás etapas, documentos y
   CAD, y la mayoría de las revisiones se harán aquí.
3. **R-T06-01** se separa por feature dataset de la BDG (`CATALOGO_BDG`):
   - R-T06-01 general: todos los atributos obligatorios, incluida la fecha de
     registro. Reúne G010, G013, G014, G103 y G200.
   - R-T06-09 InfraestructuraVial, Calzada y Losa. Reúne G052, G055, G088 y G227.
   - R-T06-10 ExploracionEnsayos, Exploración. Reúne G053 y G201.

   El detalle de los campos por clase está en `docs/diccionario-atributos.md`.

Resultado: 95 requisitos. De ellos, 82 tienen respaldo normativo y 13 son
prácticas observadas.
