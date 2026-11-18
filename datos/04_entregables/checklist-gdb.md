# Checklist GDB — borrador

> Generado por `rag-gdb checklist` el 2026-11-18 a partir de 504 observaciones de 41 documentos, agrupadas en 294 grupos y 93 requisitos.
> **Pendiente:** la taxonomía de temas (`config/temas.csv`) requiere validación de Aramis; la revisión normativa está confirmada para los 294 grupos; 13 requisitos quedan identificados como prácticas observadas sin respaldo escrito localizado. 93 requisitos tienen redacción propuesta en `config/requisitos-redaccion.csv`, pendiente de validación de Aramis.

Cómo leer cada requisito: **IDU ×n** es el número de radicados IDU distintos que lo observaron (un traslado o una copia no suma); **interventoría ×m** es el número de documentos de la interventoría que lo plantean. Entre comillas invertidas van los grupos de observaciones que lo respaldan.

## Resumen por tema

| Tema | Requisitos | Observados por el IDU | Radicados IDU (suma) |
|---|---:|---:|---:|
| T09. Consistencia entre CAD, GDB y meta física | 8 | 7 | 60 |
| T06. Atributos de la GDB y diccionario de atributos | 8 | 7 | 43 |
| T08. Geometría y topología de la GDB | 8 | 6 | 32 |
| T05. Contenido gráfico de los planos | 14 | 10 | 31 |
| T01. Estructura de carpetas y completitud de la entrega | 10 | 5 | 25 |
| T02. Nomenclatura de archivos y planos | 10 | 8 | 25 |
| T10. Ensayos e información técnica asociada | 9 | 9 | 20 |
| T07. Codificación CIV y PK_ID | 8 | 5 | 17 |
| T04. Layers, filtros y geometría en CAD | 9 | 5 | 13 |
| T11. Proceso de entrega y control de calidad | 4 | 2 | 12 |
| T03. Archivo base CAD y referencias externas | 5 | 5 | 10 |

## T09. Consistencia entre CAD, GDB y meta física

- [ ] **R-T09-02** Hacer coincidir la cantidad de elementos por tipo entre el archivo base CAD, la BDG y el reporte de meta física FOIC09. — IDU ×18 · interventoría ×2 `G004` `G017` `G046` `G081` `G092` `G107` `G127` `G145` `G210`
  - Normativa directo: **GU-IC-06 §7.1.1 ¶3** — FO-IC-09 intervenidos en la ejecución del contrato (aplica para cualquier etapa del _REPORTE_FINAL_ contrato). La información dispuesta en este archivo debe …
  - Normativa parcial: **VALIDACIONES_BDG 1. Verificación del cumplimiento de la meta** — Verificación del cumplimiento de la meta física: Se verifica el formato de reporte de seguimiento final entregado e incorporado en la base de datos geográfica …
  - Normativa directo: **FO-IC-05 B.6.a** — Se presentan todos los elementos de la sección transversal y mobiliario urbano: SI NO Observaciones: Todos los elementos objeto del contrato correspondientes a …
  - Normativa directo: **GU-IC-06 §8.3 ¶1** — Se entregará una BDG por cada etapa del contrato, los elementos representados en la BDG deberán corresponder a la geometría de: punto, línea o polígono; …
  - Normativa parcial: **GU-IC-06 §8.3 ¶3** — geometrías de los elementos suministrados en la BDG, no deberán ser modificadas a menos de que sea necesario, con el fin de que el elemento represente …
  - «4. Se recomienda verificar el reporte de meta física FOIC09_REPORTE_FINAL_META_FISICA_V_ 1.0, ya que los elementos definidos no concuerdan con lo establecido …» (DTE 20212150071823, `IDU/2021-03-15_20212150071823.pdf`, p. 3)
  - «4. Se recomienda verificar el reporte de meta física FOIC09_REPORTE_FINAL_META_FISICA_V_ 1.0, ya que los elementos definidos no concuerdan con lo establecido …» (DTE 20212150063343, `IDU/2021-03-12_178_20212150063343anexo.pdf`, p. 3)
- [ ] **R-T09-01** Incluir en las tablas de reporte de los planos todas las intervenciones dibujadas, y viceversa, en todos los planos. — IDU ×16 `G001` `G112`
  - Normativa parcial: **GU-IC-06 §7.1.1 ¶3** — FO-IC-09 intervenidos en la ejecución del contrato (aplica para cualquier etapa del _REPORTE_FINAL_ contrato). La información dispuesta en este archivo debe …
  - «1. Se reitera la siguiente observación: se recomienda realizar una revisión de todos los planos del archivo “MVGPL01” con el fin de garantizar que en las …» (DTINI 20212350355403, `IDU/2021-10-29_120213861635311_00002.pdf`, p. 2)
  - «4. Se reitera que en el archivo MVGVPL01.dwg – Layout MVGVPL06 se debe verificar que en las tablas de reporte se encuentren todas las intervenciones. Ejemplo …» (DTE 20212150074443, `IDU/2021-03-19_120213560460101_00002.pdf`, p. 4)
- [ ] **R-T09-03** Hacer coincidir áreas de intervención y fechas entre GDB, planos, FOIC09 y tablas de seguimiento. — IDU ×14 `G002` `G134` `G153`
  - Normativa parcial: **GU-IC-06 §7.1.1 ¶3** — FO-IC-09 intervenidos en la ejecución del contrato (aplica para cualquier etapa del _REPORTE_FINAL_ contrato). La información dispuesta en este archivo debe …
  - Normativa directo: **VALIDACIONES_BDG 1. Verificación de las relación entre eleme** — Verificación de las relación entre elementos y/o tablas: Se verifica la relación entre elementos y/o tablas (el dato que debe ser incorporado en el atributo …
  - «2. Se reitera la observación número 5 del memorando 20212150011573 “En la GDB del proyecto las Áreas de Intervención y la fecha de registro es diferente a la …» (DTE 20212150071823, `IDU/2021-03-15_20212150071823.pdf`, p. 2)
  - «6. En la GDB del proyecto las Áreas de Intervención y la fecha de registro es diferente a la reportada en los planos CAD y en el archivo …» (DTE 20212150011563, `IDU/2021-02-02_DTE 20212150011563 RECORD 2019.pdf`, p. 6)
- [ ] **R-T09-04** Diligenciar el FOIC09 completo: Entidad o Dependencia IDU, nombres de tipo de elemento del modelo, todos los elementos reportados (áreas de intervención, apiques) y mobiliario desagregado por tipo. — IDU ×6 · interventoría ×1 `G022` `G054` `G059` `G064` `G069` `G076` `G124`
  - Normativa parcial: **GU-IC-06 §7.1.1 ¶3** — FO-IC-09 intervenidos en la ejecución del contrato (aplica para cualquier etapa del _REPORTE_FINAL_ contrato). La información dispuesta en este archivo debe …
  - Normativa directo: **VALIDACIONES_BDG 1. Verificación de los atributos incorporad** — Verificación de los atributos incorporados: Se verifica que los atributos incorporados en la base de datos geográfica, correspondan con los solicitados en el …
  - «9. En el archivo FOIC09_REPORTE_FINAL_META_FISICA_V_1.0, diligenciar el campo de ENTIDAD O DEPENDENCIA IDU.» (DTE 20212150024523, `IDU/2021-02-12_DTE 20212150024523.pdf`, p. 6)
  - «12. En el archivo FOIC09_REPORTE_FINAL_META_FISICA_V_1.0 complementar el campo: Entidad o Dependencia IDU» (DTE 20212150011573, `IDU/2021-01-22_167_anexo_20212150011573_SI.pdf`, p. 9)
- [ ] **R-T09-05** Reportar el tipo de intervención coherente entre FOIC09, tablas de seguimiento y etapa (en preconstrucción: Estudios y Diseños). — IDU ×3 `G062` `G067` `G097`
  - Normativa directo: **GU-IC-06 §8.2 ¶4** — actor de infraestructura, en el marco del alcance del proyecto en cuestión. Interventoría: Al igual que en el campo anterior, la interventoría validará con una …
  - Normativa parcial: **GU-IC-06 §7.1.1 ¶3** — FO-IC-09 intervenidos en la ejecución del contrato (aplica para cualquier etapa del _REPORTE_FINAL_ contrato). La información dispuesta en este archivo debe …
  - «Se aclara que las variables como Funcionalidad Losa-Orden-FilaPosición-Ancho-Área-Espesor Losa-Modulo Rotura etc., no tiene relación con la justificación del …» (DTE 20202150245873, `IDU/2020-11-25_120203560946451_00002.pdf`, p. 14)
  - «Se solicita ajustar el tipo de intervención porque en el archivo de Excel “FOIC09_Reporte_Final_Meta_Fisica_V1.0” se encuentra que es mantenimiento periódico, …» (DTINI 20212350355403, `IDU/2021-10-29_120213861635311_00002.pdf`, p. 5)
- [ ] **R-T09-06** Hacer coincidir el número de registros de las tablas relacionadas con los elementos de su capa. — IDU ×2 `G051` `G140`
  - Normativa directo: **VALIDACIONES_BDG 1. Verificación de las relación entre eleme** — Verificación de las relación entre elementos y/o tablas: Se verifica la relación entre elementos y/o tablas (el dato que debe ser incorporado en el atributo …
  - «20. En el elemento Área Intervención se presentan 434 elementos, en la tabla DetalleAIntervencionCalCic, 329 registros, ajustar esta información y tener en …» (DTE 20202150245873, `IDU/2020-11-25_120203560946451_00002.pdf`, p. 13)
  - «6. Se debe verificar la información presentada en la Base de Datos Geográfica, toda vez que están presentando 50 elementos en la capa de calzada, sin embargo, …» (DTINI 202300000317753, `IDU/2023-11-07_202300000317753_DTINI observa planos record 1533-2018.pdf`, p. 4)
- [ ] **R-T09-07** Hacer coincidir el tipo de mezcla entre la BDG y los archivos CAD. — IDU ×1 `G168`
  - Normativa directo: **VALIDACIONES_BDG 1. Verificación de los atributos incorporad** — Verificación de los atributos incorporados: Se verifica que los atributos incorporados en la base de datos geográfica, correspondan con los solicitados en el …
  - Normativa parcial: **GU-IC-06 §7.1.1 ¶3** — FO-IC-09 intervenidos en la ejecución del contrato (aplica para cualquier etapa del _REPORTE_FINAL_ contrato). La información dispuesta en este archivo debe …
  - «11. Se debe verificar el Tipo de Mezcla en las intervenciones, se encuentran diferencias entre la BDG y los archivos CAD.» (DTE 20212150011573, `IDU/2021-01-22_167_anexo_20212150011573_SI.pdf`, p. 9)
- [ ] **R-T09-08** Entregar el reporte de meta física del propio proyecto y en su versión vigente. — interventoría ×1 `G231` `G232`
  - Normativa directo: **GU-IC-06 §7.1.1 ¶3** — FO-IC-09 intervenidos en la ejecución del contrato (aplica para cualquier etapa del _REPORTE_FINAL_ contrato). La información dispuesta en este archivo debe …
  - Normativa directo: **VALIDACIONES_BDG 1. Verificación del cumplimiento de la meta** — Verificación del cumplimiento de la meta física: Se verifica el formato de reporte de seguimiento final entregado e incorporado en la base de datos geográfica …
  - «El reporte de meta física no se corresponde al proyecto actual. Incluir la versión más reciente y ajustada.» (sin radicado, `IDU/2023-03-29_1443_443723_070700_CON_REVISION_BDG_V1.pdf`, p. 8)

## T06. Atributos de la GDB y diccionario de atributos

- [ ] **R-T06-01** Diligenciar todos los atributos obligatorios del DiccionarioAtributos en cada feature class y tabla de la etapa, incluida la fecha de registro. — IDU ×17 · interventoría ×2 `G010` `G013` `G014` `G052` `G053` `G055` `G088` `G103` `G200` `G201` `G227`
  - Normativa parcial: **GU-IC-06 §8.2 ¶2** —  Productos_DWG.xlsx hoja de cálculo NUEVOSLAYERS identificada con color . 8.2.1 Productos_BDG.xlsx Archivo que contiene el Diccionario de Atributos de los …
  - Normativa directo: **VALIDACIONES_BDG 1. Verificación de los atributos incorporad** — Verificación de los atributos incorporados: Se verifica que los atributos incorporados en la base de datos geográfica, correspondan con los solicitados en el …
  - «3. La información de la GDB se debe diligenciar de acuerdo al DiccionarioAtributos, de acuerdo a lo establecido en la GUIA 06; además si en algún momento un …» (DTE 20212150063343, `IDU/2021-03-12_178_20212150063343anexo.pdf`, p. 2)
  - «3. La información de la GDB se debe diligenciar de acuerdo al DiccionarioAtributos, de acuerdo a lo establecido en la GUIA 06; además si en algún momento un …» (DTE 20212150071823, `IDU/2021-03-15_20212150071823.pdf`, p. 2)
- [ ] **R-T06-05** Entregar el DiccionarioAtributos del alistamiento coherente con la BDG: tablas diligenciadas, elementos presentes y sin textos ajenos al atributo. — IDU ×7 `G057` `G068` `G082` `G126` `G160` `G167` `G188`
  - Normativa parcial: **VALIDACIONES_BDG 1. Verificación de los atributos incorporad** — Verificación de los atributos incorporados: Se verifica que los atributos incorporados en la base de datos geográfica, correspondan con los solicitados en el …
  - Normativa directo: **GU-IC-06 §8.2 ¶3** — Prefactibilidad y Factibilidad), junto con el archivo en formato Excel Productos_BDG.xlsx debidamente diligenciado en las hojas de cálculo color azul oscuro …
  - Normativa directo: **GU-IC-06 §8.2 ¶2** —  Productos_DWG.xlsx hoja de cálculo NUEVOSLAYERS identificada con color . 8.2.1 Productos_BDG.xlsx Archivo que contiene el Diccionario de Atributos de los …
  - «30. En el archivo Excel DiccionarioAtributos_V7.2, elemento Arealntervencion atributo» (DTE 20202150245873, `IDU/2020-11-25_R-IDU1384-0268-20 RTA MV2-365-20 REVISION ARCHIVOS FORMATO CAD Y BASE DATOS GEOGRAFICA ETAPA DIAGNOSTICOS.pdf`, p. 19)
  - «11. Ajustar en el archivo Excel DiccionarioAtributos_V7.2.xlsx el elemento Losa, el contratista manifiesta el no diligenciamiento de los atributos …» (DTE 20212150074493, `IDU/2021-03-19_120213560460121_00002.pdf`, p. 7)
- [ ] **R-T06-07** Verificar que los valores de los atributos correspondan a lo construido y a los productos digitales: códigos, dimensiones, espesores, costos, elementos embebidos y llaves foráneas. — IDU ×6 `G083` `G084` `G109` `G131` `G176` `G177` `G183`
  - Normativa parcial: **VALIDACIONES_BDG 1. Verificación de los atributos incorporad** — Verificación de los atributos incorporados: Se verifica que los atributos incorporados en la base de datos geográfica, correspondan con los solicitados en el …
  - Normativa directo: **VALIDACIONES_BDG 4.2. Atributos cuantitativos** — Atributos cuantitativos: Se revisará la totalidad de los atributos cuantitativos, mediante el uso de modelos que permiten calcular los valores finales y así …
  - Normativa directo: **VALIDACIONES_BDG 1. Verificación de las relación entre eleme** — Verificación de las relación entre elementos y/o tablas: Se verifica la relación entre elementos y/o tablas (el dato que debe ser incorporado en el atributo …
  - «5. Aún se encuentran información inconsistente en el atributo “Codigo Elemento”; por ejemplo, en el OBJECTID 20 y además el atributo de localización también …» (DTINI 202423500066313, `IDU/2024-02-28_202423500066313 resp DTINI.pdf`, p. 3)
  - «En la tabla DetalleAreaIntervencionCalzadaCiclorruta se encontraron varios campos sin información que son obligatorios para el tipo de intervención: Reparación …» (DTE 20212150242143, `IDU/2021-08-13_1.1 120213561214751_00002-memo.pdf`, p. 6)
- [ ] **R-T06-02** Poblar las tablas relacionadas del modelo de datos (seguimiento de losas, detalle de andén, mobiliario e intervención) y conectarlas a su elemento. — IDU ×4 · interventoría ×2 `G023` `G080` `G108` `G123` `G129` `G207`
  - Normativa directo: **GU-IC-06 §8.2 ¶2** —  Productos_DWG.xlsx hoja de cálculo NUEVOSLAYERS identificada con color . 8.2.1 Productos_BDG.xlsx Archivo que contiene el Diccionario de Atributos de los …
  - Normativa directo: **VALIDACIONES_BDG 1. Verificación de las relación entre eleme** — Verificación de las relación entre elementos y/o tablas: Se verifica la relación entre elementos y/o tablas (el dato que debe ser incorporado en el atributo …
  - Normativa directo: **VALIDACIONES_BDG 1. Verificación de los atributos incorporad** — Verificación de los atributos incorporados: Se verifica que los atributos incorporados en la base de datos geográfica, correspondan con los solicitados en el …
  - «31. En el archivo Excel DiccionarioAtributos_V7.2 para el elemento Losa se debe diligenciar la tabla relacionada (Seguimiento).» (DTE 20202150245873, `IDU/2020-11-25_120203560946451_00002.pdf`, p. 18)
  - «10. Ajustar en el archivo Excel DiccionarioAtributos_V7.2.xlsx la tabla seguimiento relacionada al elemento Losa, el contratista manifiesta el no …» (DTE 20212150074493, `IDU/2021-03-19_120213560460121_00002.pdf`, p. 7)
- [ ] **R-T06-03** Justificar técnica o contractualmente en Observaciones cada atributo no diligenciado o N/A, con validación de la interventoría. — IDU ×4 `G037` `G119` `G150`
  - Normativa directo: **GU-IC-06 §8.2 ¶4** — actor de infraestructura, en el marco del alcance del proyecto en cuestión. Interventoría: Al igual que en el campo anterior, la interventoría validará con una …
  - Normativa directo: **VALIDACIONES_BDG 1. Verificación de los atributos incorporad** — Verificación de los atributos incorporados: Se verifica que los atributos incorporados en la base de datos geográfica, correspondan con los solicitados en el …
  - «En los casos donde un atributo no se encuentre totalmente diligenciado en la BDG o no aplique – N/A, debe existir la debida justificación de carácter técnico o …» (DTINI 20232350082573, `IDU/2023-04-24_20232350082573 (1).pdf`, p. 10)
  - «En los casos donde un atributo no se encuentre totalmente diligenciado en la BDG o no aplique – N/A, debe existir la debida justificación de carácter técnico o …» (DTINI 20222350336933, `IDU/2022-09-30_20222350336933 observaciones georref. (1).pdf`, p. 9)
- [ ] **R-T06-04** Diligenciar Productos_BDG.xlsx en todas sus hojas, con la X de contratista e interventoría y N/A justificado en lo opcional. — IDU ×3 · interventoría ×3 `G016` `G190`
  - Normativa directo: **GU-IC-06 §8.2 ¶3** — Prefactibilidad y Factibilidad), junto con el archivo en formato Excel Productos_BDG.xlsx debidamente diligenciado en las hojas de cálculo color azul oscuro …
  - Normativa parcial: **GU-IC-06 §8.2 ¶2** —  Productos_DWG.xlsx hoja de cálculo NUEVOSLAYERS identificada con color . 8.2.1 Productos_BDG.xlsx Archivo que contiene el Diccionario de Atributos de los …
  - «Se requiere en la entrega del diccionario de atributos archivo (Productos_BDG.xlsx), se encuentre debidamente diligenciado» (STEST 202434601243021, `IDU/2024-10-23_1443_696124_070700_CON_OBSERV_DITINI_GEODATABASE_V3.pdf`, p. 10)
  - «14. Se requiere en la entrega del archivo (Productos_BDG.xlsx), que este se encuentre debidamente diligenciado por contratista e interventoría para todos los …» (DTINI 20232350082573, `IDU/2023-04-24_20232350082573 (1).pdf`, p. 10)
- [ ] **R-T06-06** Usar la estructura de la GDB enviada en el alistamiento, sin modificarla. — IDU ×2 `G040`
  - Normativa directo: **GU-IC-06 §7.1.1 ¶4** —  FOIC01 REPORTE DE ELEMENTOS VIALES OBJETO DE LA CONTRATACION  FOIC02_REPORTE PARA LA ACTUALIZACIÓN DE LOS ESTUDIOS, DIAGNOSTICOS, DISEÑOS E INTERVENCIONES …
  - «7. La estructura de la GDB no se debe modificar, se debe utilizar la enviada en la etapa de alistamiento.» (DTE 20212150056813, `IDU/2021-03-10_177_20212150056813anexo.pdf`, p. 4)
  - «5. Se recomienda verificar la estructura de la GDB enviada en la etapa de alistamiento, ya que se debe utilizar esta, y no se le debe cambiar su formato.» (DTE 20212150063343, `IDU/2021-03-12_178_20212150063343anexo.pdf`, p. 3)
- [ ] **R-T06-08** No eliminar registros de un feature class al corregirlo; justificar cualquier retiro. — interventoría ×1 `G267`
  - Normativa parcial: **GU-IC-06 §8.3 ¶3** — geometrías de los elementos suministrados en la BDG, no deberán ser modificadas a menos de que sea necesario, con el fin de que el elemento represente …
  - «en esta ocasión se han eliminado los registros del Feature Class» (sin radicado, `IDU/2023-07-27_1443_501423_070700_CON_REVISION_BDG_V2.pdf`, p. 16)

## T08. Geometría y topología de la GDB

- [ ] **R-T08-01** Corregir superposiciones y huecos entre elementos según el archivo Reglas Topológicas, revisando todos los planos y sin afectar otros elementos. — IDU ×12 `G006` `G012` `G024` `G071` `G158`
  - Normativa directo: **VALIDACIONES_BDG 2.4. a. Superposición elementos** — a. Superposición elementos: No debe existir superposición de elementos, consigo mismo o con otros. Esta regla aplica para elementos de tipo línea, punto y …
  - Normativa directo: **VALIDACIONES_BDG 2.4. b. Huecos entre elementos** — b. Huecos entre elementos: Esta regla precisa que no haya vacíos dentro de un elemento o entre polígonos de elementos adyacentes.
  - «10. Se presentan errores de topología, como se muestra en el ejemplo de la ilustración 8, donde se evidencia el error de superposición (Overlap) y de espacio …» (DTINI 20222350336933, `IDU/2022-09-30_20222350336933 observaciones georref. (1).pdf`, p. 8)
  - «11. Se presentan errores de topología, como se muestra en el ejemplo de la ilustración 7, donde se evidencia el error de superposición (Overlap) y de espacio …» (DTINI 20232350082573, `IDU/2023-04-24_20232350082573 (1).pdf`, p. 9)
- [ ] **R-T08-03** Segmentar según las reglas: áreas de intervención en el límite de cada calzada, sardineles por elemento de espacio público y CIV, andenes donde corresponda y redes de ciclorruta con conectividad. — IDU ×7 `G027` `G028` `G045` `G070` `G159`
  - Normativa parcial: **REGLAS_TOPOLOGICAS 6** — 6. MUST NOT HAVE DANGLES: NO DEBE HABER LÍNEAS SUELTAS (aplica por elemento según la hoja)
  - Normativa parcial: **REGLAS_TOPOLOGICAS 14** — 14. MUST BE COVERED BY BOUNDARY OF: EL LIMITE DE LÍNEA DEBE COINCIDIR CON LIMITE DE POLÍGONO (aplica por elemento según la hoja)
  - Normativa parcial: **REGLAS_TOPOLOGICAS 3** — 3. ÁREA BOUNDARY MUST BE COVERED BY BOUNDARY OF: LOS LIMITES SON COINCIDENTES DE DOS CLASES (aplica por elemento según la hoja)
  - Normativa parcial: **GU-IC-06 §8.3 ¶3** — geometrías de los elementos suministrados en la BDG, no deberán ser modificadas a menos de que sea necesario, con el fin de que el elemento represente …
  - «7. Se debe tener en cuenta en la representación del elemento (RedCiclorruta) la conectividad de la red y su segregación por cada cambio de elemento sobre el …» (DTINI 20222350336933, `IDU/2022-09-30_20222350336933 observaciones georref. (1).pdf`, p. 6)
  - «5. Se debe tener en cuenta en la representación del elemento (RedCiclorruta) la conectividad de la red y su segregación por cada 6» (STESV 202333601342401, `IDU/2023-08-09_1202333601342401_00001.pdf`, p. 6)
- [ ] **R-T08-04** Clasificar correctamente cada elemento según su definición: pompeyano solo en cruces con calzada (su área se incorpora a la calzada), rampa en ingresos a predio y sin materas o cunetas inexistentes. — IDU ×5 `G095` `G096` `G102` `G111` `G128` `G155` `G165`
  - Normativa directo: **VALIDACIONES_BDG 4.1. Atributos cualitativos de los elementos** — Atributos cualitativos de los elementos: la revisión de este ítem se realiza a los atributos cualitativos de los elementos entregados por el proyecto , …
  - Normativa parcial: **GU-IC-06 §8.3 ¶3** — geometrías de los elementos suministrados en la BDG, no deberán ser modificadas a menos de que sea necesario, con el fin de que el elemento represente …
  - Normativa parcial: **VALIDACIONES_BDG 2.4. a. Superposición elementos** — a. Superposición elementos: No debe existir superposición de elementos, consigo mismo o con otros. Esta regla aplica para elementos de tipo línea, punto y …
  - «3. De los pompeyanos 16 pompeyanos presentados, se solicita eliminar el pompeyano identificado con (PK_ID_Pompeyano – 4600002) por corresponder con un desnivel …» (DTINI 20232350161243, `IDU/2023-07-04_20232350161243(1).pdf`, p. 6)
  - «7. Se solicita eliminar la rampa (PK_ID_5100049). 8.» (DTINI 202323500285933, `IDU/2023-09-07_1202323500285933_00001--observaciones Georreferenciacion..pdf`, p. 7)
- [ ] **R-T08-02** Cumplir las relaciones de contenencia: rampas dentro del andén y elementos de puente y cunetas dentro del límite de intervención. — IDU ×4 `G047` `G116` `G169`
  - Normativa directo: **VALIDACIONES_BDG 2.4. a. Superposición elementos** — a. Superposición elementos: No debe existir superposición de elementos, consigo mismo o con otros. Esta regla aplica para elementos de tipo línea, punto y …
  - Normativa directo: **VALIDACIONES_BDG 2.4. c. Contenencia elementos** — c. Contenencia elementos: Requiere que los polígonos o puntos de un elemento de entidad estén contenido en polígonos o puntos de otro elemento
  - «9. Se deben tener en cuenta las relaciones espaciales que existen entre los elementos con el fin que al momento de su representación esta corresponda con la …» (DTINI 20222350336933, `IDU/2022-09-30_20222350336933 observaciones georref. (1).pdf`, p. 8)
  - «8. Se reitera el ítem 9 del memorando 20222350336933, donde se expresa que se debe tener en cuenta las relaciones espaciales que existen entre los elementos …» (DTINI 20232350161243, `IDU/2023-07-04_20232350161243(1).pdf`, p. 8)
- [ ] **R-T08-05** No representar elementos duplicados ni polígonos multiparte con el mismo PK_ID. — IDU ×2 `G075` `G117`
  - Normativa parcial: **VALIDACIONES_BDG 2.1. Verificación de duplicidad del atributo ** — Verificación de duplicidad del atributo PK_ID_Xxxxx de cada elemento y/o tabla: Inexistencia de duplicidad del atributo PK_ID_Xxxxx de cada elemento y/o tabla.
  - Normativa directo: **REGLAS_TOPOLOGICAS 13** — 13. MUST BE SINGLE PART: DEBE SER UNA SOLA ENTIDAD (aplica por elemento según la hoja)
  - «3. Verificar en los documentos entregados que no exista duplicidad, como se evidencia en el ejemplo de la ilustración 3.» (DTINI 20232350082573, `IDU/2023-04-24_20232350082573 (1).pdf`, p. 6)
  - «8. Los elementos representados en la Base de Datos Geográfica no deben ser representados como polígonos multipartes, como en el ejemplo que se muestra en la …» (DTINI 20222350336933, `IDU/2022-09-30_20222350336933 observaciones georref. (1).pdf`, p. 7)
- [ ] **R-T08-06** Representar en la BDG todos los elementos intervenidos dentro del límite del proyecto, incluidas estructuras, puentes y deprimidos, zonas verdes y mobiliario. — IDU ×2 `G141` `G148` `G149` `G162` `G185` `G186` `G187`
  - Normativa directo: **GU-IC-06 §9.8 ¶2** —  Baranda  Viga  Losa de Aproximación  Barrera  Aleta Estribo  Pila  Cercha  Caisson  Pilote  Diafragma  Columna  Rampa Puente  GuardaRueda  Dado …
  - Normativa parcial: **VALIDACIONES_BDG 3.1. Proyectos que cuentan con topografía** — Proyectos que cuentan con topografía: Se evalúa la exactitud de posición de la base de datos geográfica con los archivos CAD.
  - Normativa parcial: **VALIDACIONES_BDG 1. Verificación del cumplimiento de la meta** — Verificación del cumplimiento de la meta física: Se verifica el formato de reporte de seguimiento final entregado e incorporado en la base de datos geográfica …
  - Normativa parcial: **GU-IC-06 §8.3 ¶3** — geometrías de los elementos suministrados en la BDG, no deberán ser modificadas a menos de que sea necesario, con el fin de que el elemento represente …
  - Normativa directo: **GU-IC-06 §8.3 ¶1** — Se entregará una BDG por cada etapa del contrato, los elementos representados en la BDG deberán corresponder a la geometría de: punto, línea o polígono; …
  - Normativa parcial: **VALIDACIONES_BDG 1. Verificación de los atributos incorporad** — Verificación de los atributos incorporados: Se verifica que los atributos incorporados en la base de datos geográfica, correspondan con los solicitados en el …
  - «embargo, el deprimido y los elementos que lo conforman no están representados ni en la Base de Datos Geográfica (BDG). Se requiere que la representación del …» (DTINI 202623500078293, `IDU/2026-03-04_1202623500078293_00001 Observaciones Planos Record.pdf`, p. 4)
  - «Existen áreas contempladas en el límite del proyecto que no son representadas en la Base de Datos Geográfica – BDG, por lo cual se recuerda que todas las áreas …» (STESV 202333601342401, `IDU/2023-08-09_1202333601342401_00001.pdf`, p. 5)
- [ ] **R-T08-07** Eliminar los registros sin geometría. — interventoría ×2 `G203`
  - Normativa directo: **GU-IC-06 §8.3 ¶1** — Se entregará una BDG por cada etapa del contrato, los elementos representados en la BDG deberán corresponder a la geometría de: punto, línea o polígono; …
  - «se incluye un (1) elemento sin representación gráfica (OBJECTID 44)» (sin radicado, `IDU/2023-03-29_1443_443723_070700_CON_REVISION_BDG_V1.pdf`, p. 19)
  - «se incluye un (1) elemento sin representación gráfica (OBJECTID 44)» (sin radicado, `IDU/2023-07-27_1443_501423_070700_CON_REVISION_BDG_V2.pdf`, p. 16)

## T05. Contenido gráfico de los planos

- [ ] **R-T05-04** Incluir convenciones completas del plano base y del tema, acordes con lo dibujado y con los colores del archivo base. — IDU ×7 · interventoría ×4 `G019` `G035` `G074` `G138` `G194` `G248` `G249`
  - Normativa directo: **FO-IC-05 A.2.h** — Convenciones: Se presenta el cuadro de convenciones de los objetos representados en los planos
  - Normativa parcial: **Productos_DWG Récord F31** — Planos de Secciones Transversales (niveles en eje y bordes, pendientes transversales, estructura del pavimento con espesores construidos)
  - Normativa directo: **FO-IC-05 A.3.k** — Convenciones: Se presenta el cuadro de convenciones de los objetos representados en los planos
  - «4. En los planos de Planta Perfil, las convenciones deben estar acorde a los elementos presentados en los planos, falta mobiliario urbano, elementos de …» (DTE 20202150245873, `IDU/2020-11-25_120203560946451_00002.pdf`, p. 3)
  - «4. En los planos de Planta Perfil, las convenciones deben estar acorde a los elementos presentados en los planos, falta mobiliario urbano, elementos de …» (OTE 20202150245873, `IDU/2020-11-25_R-IDU1384-0268-20 RTA MV2-365-20 REVISION ARCHIVOS FORMATO CAD Y BASE DATOS GEOGRAFICA ETAPA DIAGNOSTICOS.pdf`, p. 4)
- [ ] **R-T05-07** Incluir en los planos planta-perfil y de rehabilitación las placas de amarre certificadas (IGAC) y anexar el informe de topografía. — IDU ×5 · interventoría ×1 `G009` `G259`
  - Normativa parcial: **FO-IC-05 A.2.j** — Placas de amarre: Se presentan las placas o puntos de amarre según la convención del IDU
  - Normativa directo: **FO-IC-05 A.2.f** — Cuadro coordenadas placas de amarre: Cuadro de coordenadas Norte, Este y altura de las placas o puntos de amarre topográfico
  - «2. En los planos de tramos de rehabilitación vial se debe incluir las placas de amarre y anexar su respectivo informe de topografía.» (DTE 20212150074443, `IDU/2021-03-19_120213560460101_00002.pdf`, p. 3)
  - «1. Se reitera observación, en los planos de los tramos de rehabilitación vial se debe incluir las placas de amarre y anexar su respectivo informe de topografía» (DTE 20212150074493, `IDU/2021-03-19_120213560460121_00002.pdf`, p. 2)
- [ ] **R-T05-02** Presentar escala gráfica y numérica claras y coherentes con el rótulo y el viewport en cada vista del plano. — IDU ×4 · interventoría ×4 `G034` `G039` `G171` `G193` `G196` `G197` `G239`
  - Normativa parcial: **GU-IC-06 §8 ¶7** — formato .dwg que se usará como referencia externa en todos los planos en planta presentados para cada componente. Esta información se presentará en el Model …
  - Normativa parcial: **Productos_DWG Récord F42** — Escala numérica - Escala grafica
  - Normativa parcial: **Productos_DWG Récord F24** — Escala numérica - Escala grafica
  - «Se solicita verificar el tema de las escalas presentadas, se recuerda que las escalas gráficas» (STEST 202434601243021, `IDU/2024-10-23_1443_696124_070700_CON_OBSERV_DITINI_GEODATABASE_V3.pdf`, p. 6)
  - «Se recuerda que deben coincidir las escalas gráficas, las distancias que representan, el valor de las grillas, las escalas numéricas, las incorporadas en los …» (DTINI 202623500078293, `IDU/2026-03-04_1202623500078293_00001 Observaciones Planos Record.pdf`, p. 6)
- [ ] **R-T05-01** Incluir en cada plano los mínimos de la guía: un solo norte sobre la grilla, grilla de coordenadas, convenciones, escalas y rótulo completo. — IDU ×3 · interventoría ×1 `G048` `G118` `G152` `G288` `G289`
  - Normativa parcial: **GU-IC-06 §9.4 ¶1** — Los productos entregables corresponderán con los señalados en el archivo Excel Productos_DWG.xlsx en la hoja ElementosConstruccion (Récord) identificada con …
  - Normativa parcial: **VALIDACIONES_BDG 2.4. a. Superposición elementos** — a. Superposición elementos: No debe existir superposición de elementos, consigo mismo o con otros. Esta regla aplica para elementos de tipo línea, punto y …
  - Normativa directo: **Productos_DWG Récord F42** — Escala numérica - Escala grafica
  - Normativa directo: **Productos_DWG Récord F35** — Nomenclatura vial, Códigos CIV
  - Normativa directo: **FO-IC-05 A.2.k** — Grilla coordenadas: Representación de la cuadricula de coordenadas cada 50 o 100 mts, según escala del plano
  - Normativa directo: **FO-IC-05 A.3.o** — Grilla coordenadas: Representación de la cuadrícula de coordenadas cada 50 o 100 mts, según escala del plano
  - Normativa directo: **FO-IC-05 A.2.c** — Norte magnético: El plano presenta el norte magnético según la grilla de coordenadas planas
  - Normativa directo: **FO-IC-05 A.3.c** — Norte magnético: El plano presenta el norte magnético según la grilla de coordenadas planas
  - «Los planos deben contener toda la información correspondiente a la respetiva especialidad que representa» (STEST 202434601243021, `IDU/2024-10-23_1443_696124_070700_CON_OBSERV_DITINI_GEODATABASE_V3.pdf`, p. 3)
  - «8. Los planos deben contener solo un bloque norte ubicado en la intersección de la grilla y verificar que no tenga superposición con los elementos de Área …» (DTE 20212150011563, `IDU/2021-02-02_DTE 20212150011563 RECORD 2019.pdf`, p. 7)
- [ ] **R-T05-03** Usar en secciones transversales y estructuras las escalas definidas en Productos_DWG y en ParametrosPresentacionPlanos. — IDU ×3 · interventoría ×2 `G026` `G133` `G221` `G238`
  - Normativa directo: **FO-IC-05 A.5.f** — Escalas detalles: Las escalas de detalle se presentan en un rango de escalas estándar (múltiplo de 5) entre 1:10 a 1:100
  - Normativa directo: **FO-IC-05 A.5.e** — Escalas planta: Las escalas en planta corresponden a las establecidas en el instructivo para la presentación de planos y archivos
  - Normativa directo: **Productos_DWG Escalas F21** — 5.2. Secciones transversales (Incluye la toma en terreno de la ST) y sección típica: 1 : 50, 1 : 100
  - Normativa parcial: **Productos_DWG Récord F42** — Escala numérica - Escala grafica
  - «2. En los planos de Secciones Transversales se debe ajustar la escala, en el rotulo se encuentra como escala 1:500 pero las escalas de las secciones son 1:100.» (OTE 20212150024523, `IDU/2021-02-12_R-IDU1385-0014-21 RTA MAB-2-1463-0173-20 RAD IDU 20205261211672 ARCHIVOS CAD Y BASE DATOS GEOGRAFICA ETAPA DISEÑO 2019.pdf`, p. 4)
  - «2. En los planos de Secciones Transversales se debe ajustar la escala, en el rotulo se encuentra como escala 1:500 pero las escalas de las secciones son 1:100.» (DTE 20212150024523, `IDU/2021-02-12_DTE 20212150024523.pdf`, p. 3)
- [ ] **R-T05-06** Incluir en los planos planta-perfil las cotas de rasante del eje y de los bordes izquierdo y derecho. — IDU ×3 `G038` `G077`
  - Normativa directo: **Productos_DWG Récord F26** — Planta Perfil: En planta se deben presentar las líneas de ejes, bordes, sumideros, limite de intervención y abcisado, en el perfil longitudinal de tener las …
  - «2. Los planos de Planta Perfil, el perfil debe contener las cotas de rasante del eje, Borde Izquierdo – Derecho.» (DTE 20202150245873, `IDU/2020-11-25_120203560946451_00002.pdf`, p. 3)
  - «2. Los planos de Planta Perfil, el perfil debe contener las cotas de rasante del eje, Borde Izquierdo - Derecho.» (OTE 20202150245873, `IDU/2020-11-25_R-IDU1384-0268-20 RTA MV2-365-20 REVISION ARCHIVOS FORMATO CAD Y BASE DATOS GEOGRAFICA ETAPA DIAGNOSTICOS.pdf`, p. 4)
- [ ] **R-T05-09** Ubicar textos de grilla e intervenciones legibles y sin superposiciones. — IDU ×3 `G043` `G073`
  - Normativa parcial: **FO-IC-05 A.2.k** — Grilla coordenadas: Representación de la cuadricula de coordenadas cada 50 o 100 mts, según escala del plano
  - «9. Se solicita rotar los textos de las intervenciones del archivo MVGVPL01.dwg, de tal manera que facilite su lectura.» (DTE 20202150245873, `IDU/2020-11-25_120203560946451_00002.pdf`, p. 6)
  - «3. Se reitera que en el archivo MVGVPL01.dwg se debe rotar los textos de las intervenciones para tener una mejor lectura de los mismos. Ejemplo Intervenciones …» (DTE 20212150074443, `IDU/2021-03-19_120213560460101_00002.pdf`, p. 3)
- [ ] **R-T05-08** Mostrar legibles en los planos en planta la nomenclatura vial y los CIV de calzadas y andenes. — IDU ×1 · interventoría ×3 `G105` `G199`
  - Normativa directo: **Productos_DWG Récord F35** — Nomenclatura vial, Códigos CIV
  - Normativa directo: **FO-IC-05 A.2.g** — Nomenclatura vial: Los planos presentan la nomenclatura vial actual de los corredores viales y vías conectantes del proyecto o contrato
  - Normativa parcial: **Productos_DWG INSTRUCTIVO_LAYOUT_CIV C2** — CIV: Código de Identificación Vial de los tramos relacionados para el contrato
  - «7. No se presenta en los planos el código de identificación vial - CIV, por lo cual se requieres sea incluido en los diferentes planos en planta.» (STESV 202333601342401, `IDU/2023-08-09_1202333601342401_00001.pdf`, p. 7)
  - «no incluyen la nomenclatura vial y códigos de CIV de calzada y andenes» (STEST 202434601243021, `IDU/2024-10-23_1443_696124_070700_CON_OBSERV_DITINI_GEODATABASE_V3.pdf`, p. 4)
- [ ] **R-T05-10** Indicar el tipo de mezcla asfáltica en los cuadros de descripción de intervenciones. — IDU ×1 `G106`
  - Normativa parcial: **Productos_DWG Récord F28** — Sección típica con espesores y tipo de materiales utilizados, pendiente Transversal, acotados
  - «11. En los cuadros de descripción de las intervenciones se debe incluir el tipo de mezcla asfáltica utilizada.» (DTE 20212150011563, `IDU/2021-02-02_DTE 20212150011563 RECORD 2019.pdf`, p. 8)
- [ ] **R-T05-11** Representar los elementos existentes, como las calzadas, en los planos de intervención. — IDU ×1 `G110`
  - Normativa directo: **Productos_DWG LAYERCAD 59** — Calzada: layer CAD CALZADA, geometría POLÍGONO, estados E: EXISTENTE D: DISEÑO C: INTERVENIDO
  - «2. En los planos MVGVPL01.dwg se debe incluir las calzadas existentes.» (DTE 20212150011563, `IDU/2021-02-02_DTE 20212150011563 RECORD 2019.pdf`, p. 3)
- [ ] **R-T05-12** Mostrar en los planos de diseño geométrico la estructura de pavimento de calzada y andén. — interventoría ×1 `G256`
  - Normativa directo: **Productos_DWG Récord F31** — Planos de Secciones Transversales (niveles en eje y bordes, pendientes transversales, estructura del pavimento con espesores construidos)
  - «La estructura no se encuentra en los planos de DG.» (sin radicado, `IDU/2023-03-29_1443_443723_070700_CON_REVISION_BDG_V1.pdf`, p. 13)

## T01. Estructura de carpetas y completitud de la entrega

- [ ] **R-T01-02** Verificar que no falten productos de ninguna especialidad: planos de localización, topografía, planta-perfil, componente vial, estructuras, espacio público y elementos como protectores de árboles. — IDU ×9 `G020` `G099` `G101` `G125` `G147` `G157` `G161`
  - Normativa directo: **Productos_DWG Récord F26** — Planta Perfil: En planta se deben presentar las líneas de ejes, bordes, sumideros, limite de intervención y abcisado, en el perfil longitudinal de tener las …
  - Normativa parcial: **GU-IC-06 §9.4 ¶1** — Los productos entregables corresponderán con los señalados en el archivo Excel Productos_DWG.xlsx en la hoja ElementosConstruccion (Récord) identificada con …
  - Normativa parcial: **GU-IC-06 §8.4 ¶1** — Conforme a la estructura de carpetas suministradas, se deberá incorporar la totalidad de la información estandarizada, incluyendo todos los soportes de los …
  - Normativa directo: **GU-IC-06 §10 ¶1** — La información anexa a la radicación oficial deberá estar completa, en caso de que la información no cuente con alguno de los archivos obligatorios, no se …
  - «1. No se entregaron planos de Planta Perfil, se recomienda revisar la información.» (DTE 20212150071823, `IDU/2021-03-15_20212150071823.pdf`, p. 2)
  - «1. No se entregaron planos de Planta Perfil, se recomienda revisar la informacion.» (DTE 20212150063343, `IDU/2021-03-12_178_20212150063343anexo.pdf`, p. 2)
- [ ] **R-T01-01** Entregar la totalidad de los productos de la etapa, con los anexos de cada carpeta del alistamiento (registro fotográfico, informes finales, entidades diferentes al IDU); la revisión se repite sobre todos ellos. — IDU ×8 `G005` `G044`
  - Normativa directo: **GU-IC-06 §8.4 ¶1** — Conforme a la estructura de carpetas suministradas, se deberá incorporar la totalidad de la información estandarizada, incluyendo todos los soportes de los …
  - «Se debe realizar la entrega de la totalidad de los productos, dado que la revisión de la información se realiza nuevamente sobre todos los productos.» (DTE 20212150175853, `IDU/2021-06-18_120213560877971_00002.pdf`, p. 4)
  - «Se debe realizar la entrega de la totalidad de los productos, dado que la revisión de la información se realiza nuevamente sobre todos los productos.» (DTE 20212150175863, `IDU/2021-06-21_2.1 120213560877981_00002-obs GIS20-15-jun-21.pdf`, p. 3)
- [ ] **R-T01-06** Diligenciar EstructuraCarpetas.xlsx: registrar en CONTRATISTAS la entrega o no de cada carpeta, justificar contractual y técnicamente las no entregadas y no marcar «Ok» lo que no está. — IDU ×4 · interventoría ×1 `G015` `G268`
  - Normativa parcial: **GU-IC-06 §7.1.4 ¶2** — el archivo Excel EstructuraCarpetas.xlsx; para cada etapa del contrato existe una hoja de cálculo con el nombre de la etapa que se requiere entregar, en la que …
  - Normativa parcial: **GU-IC-06 §8.4 ¶1** — Conforme a la estructura de carpetas suministradas, se deberá incorporar la totalidad de la información estandarizada, incluyendo todos los soportes de los …
  - «15. Es necesario presentar el archivo (1. EstructuraCarpetas .xlsx), y en el campo (CONTRATISTAS) realizar la respectiva observación de la entrega o no de …» (DTINI 20232350082573, `IDU/2023-04-24_20232350082573 (1).pdf`, p. 11)
  - «15. Es necesario presentar el archivo (EstructuraCarpetas .xlsx), y en el campo (CONTRATISTAS) realizar la respectiva observación de la entrega o no de …» (DTINI 20222350336933, `IDU/2022-09-30_20222350336933 observaciones georref. (1).pdf`, p. 11)
- [ ] **R-T01-05** No entregar carpetas obligatorias vacías ni archivos sueltos: incorporar la información o depurar la carpeta sin alterar la numeración. — IDU ×3 · interventoría ×1 `G036` `G121` `G243`
  - Normativa directo: **GU-IC-06 §8.4 ¶1** — Conforme a la estructura de carpetas suministradas, se deberá incorporar la totalidad de la información estandarizada, incluyendo todos los soportes de los …
  - Normativa directo: **GU-IC-06 §10 ¶1** — La información anexa a la radicación oficial deberá estar completa, en caso de que la información no cuente con alguno de los archivos obligatorios, no se …
  - «2. Como se muestra en el ejemplo de la ilustración 3, se encuentran carpetas que no contienen información, por lo cual se solicita, incorporar la información o …» (DTINI 20222350336933, `IDU/2022-09-30_20222350336933 observaciones georref. (1).pdf`, p. 5)
  - «1. Se solicita verificar la información presentada y depurar las diferentes carpetas que no contienen información, se recuerda que no se deben presentar …» (DTINI 202300000317753, `IDU/2023-11-07_202300000317753_DTINI observa planos record 1533-2018.pdf`, p. 2)
- [ ] **R-T01-07** Entregar los planos en DWG y en PDF, y los informes en DOCX editable y en PDF, en todas las carpetas. — IDU ×1 · interventoría ×2 `G156` `G204` `G236` `G240`
  - Normativa directo: **GU-IC-06 §8.4 ¶2** — (Word, Excel, AutoCAD, JPG, entre otros) y a su vez el archivo en formato .PDF. La carpeta principal de cada proyecto deberá identificarse con el código …
  - Normativa directo: **GU-IC-06 §11.1 ¶1** — El contenido de los archivos, su calidad, su completitud y autenticidad de la firma digital, es responsabilidad de los actores de infraestructura, por tanto, …
  - Normativa directo: **GU-IC-06 §8 ¶14** — en el cuadro ESCALA. Se deberá generar un archivo PDF que se incluirá en la misma carpeta del respectivo tema, con el nombre del layout, los archivos PDF …
  - «5. Se solicita la entrega de las salidas gráficas en formato .PDF de los planos presentados.» (DTINI 202300000317753, `IDU/2023-11-07_202300000317753_DTINI observa planos record 1533-2018.pdf`, p. 4)
  - «no se encuentran archivos editables en formato DOCX» (sin radicado, `IDU/2023-07-27_1443_501423_070700_CON_REVISION_BDG_V2.pdf`, p. 5)
- [ ] **R-T01-04** Conservar exactamente la estructura de carpetas del alistamiento: nombres con su escritura exacta, niveles, codificación y numeración, cada informe en su carpeta y sin carpetas duplicadas. — interventoría ×3 `G217` `G251` `G260` `G266` `G272` `G281` `G283` `G287` `G291`
  - Normativa directo: **GU-IC-06 §8.4 ¶1** — Conforme a la estructura de carpetas suministradas, se deberá incorporar la totalidad de la información estandarizada, incluyendo todos los soportes de los …
  - Normativa directo: **GU-IC-06 §7.1.4 ¶2** — el archivo Excel EstructuraCarpetas.xlsx; para cada etapa del contrato existe una hoja de cálculo con el nombre de la etapa que se requiere entregar, en la que …
  - «se ha nombrado el folder con la numeración D.5.2.1» (sin radicado, `IDU/2023-07-27_1443_501423_070700_CON_REVISION_BDG_V2.pdf`, p. 4)
  - «Las estructuras de directorios, codificación y nombre deben ser la misma proporcionada al inicio del contrato con el alistamiento.» (sin radicado, `IDU/2023-03-29_1443_443723_070700_CON_REVISION_BDG_V1.pdf`, p. 8)
- [ ] **R-T01-03** Incluir y recodificar todos los planos modificados, aunque no se hubieran presentado antes, junto con el listado de diseños modificados. — interventoría ×2 `G205` `G244`
  - Normativa parcial: **GU-IC-06 §8.4 ¶1** — Conforme a la estructura de carpetas suministradas, se deberá incorporar la totalidad de la información estandarizada, incluyendo todos los soportes de los …
  - «En caso de que existan planos que no se hayan presentado pero hayan sido objeto de modificación, estos deberán incluirse en futuras entregas» (sin radicado, `IDU/2023-03-29_1443_443723_070700_CON_REVISION_BDG_V1.pdf`, p. 8)
  - «En caso de que existan planos que no se hayan presentado, pero hayan sido objeto de modificación, estos deberán incluirse en futuras entregas» (sin radicado, `IDU/2023-07-27_1443_501423_070700_CON_REVISION_BDG_V2.pdf`, p. 3)
- [ ] **R-T01-08** Firmar digitalmente los PDF de planos e informes por todos los responsables de contratista e interventoría (revisó y aprobó). — interventoría ×2 `G220` `G241`
  - Normativa directo: **GU-IC-06 §6 ¶2** — Los archivos deberán presentarse únicamente en formato digital, deberán ser avalados por los profesionales que intervienen en su elaboración, mediante firma …
  - «los siguientes informes carecen de una o varias firmas» (sin radicado, `IDU/2023-07-27_1443_501423_070700_CON_REVISION_BDG_V2.pdf`, p. 5)
  - «Los planos e informes en PDF deben venir firmados digitalmente por todos los profesionales responsables del contratista de obra y la interventoría.» (sin radicado, `IDU/2023-03-29_1443_443723_070700_CON_REVISION_BDG_V1.pdf`, p. 8)
- [ ] **R-T01-09** Entregar las versiones aprobadas por la interventoría, no las iniciales. — interventoría ×1 `G235`
  - Normativa directo: **GU-IC-06 §10 ¶1** — La información anexa a la radicación oficial deberá estar completa, en caso de que la información no cuente con alguno de los archivos obligatorios, no se …
  - «Las versiones de planos no corresponden a las versiones aprobadas (planos versión inicial). Verificar.» (sin radicado, `IDU/2023-03-29_1443_443723_070700_CON_REVISION_BDG_V1.pdf`, p. 6)

## T02. Nomenclatura de archivos y planos

- [ ] **R-T02-05** Numerar planos y planchas de forma única y continua dentro de cada temática, siguiendo el orden de las carpetas (carátula y localización primero), sin repetidos ni saltos y con el total igual al entregado. — IDU ×6 · interventoría ×3 `G091` `G094` `G122` `G135` `G142` `G172` `G230` `G253`
  - Normativa parcial: **FO-IC-05 A.2.m** — Numeración planos: Numeración de planos de acuerdo al instructivo para la presentación de planos y archivos vigente
  - «Se requiere revisar y ajustar el consecutivo de los planos debido a que como se muestra en la ilustración 5» (STEST 202434601243021, `IDU/2024-10-23_1443_696124_070700_CON_OBSERV_DITINI_GEODATABASE_V3.pdf`, p. 5)
  - «5. Se presenta el archivo (CVGNLP01.dwg) pero el plano no contiene ningún tipo de información, como se puede observar en la ilustración 4, pero es diligenciada …» (DTINI 20222350336933, `IDU/2022-09-30_20222350336933 observaciones georref. (1).pdf`, p. 5)
- [ ] **R-T02-02** Nombrar cada DWG según la codificación de la guía y nombrar su layout igual al plano; el layout es único y el nombre coincide con el reportado en el rótulo. — IDU ×4 · interventoría ×2 `G033` `G093` `G132` `G202` `G255`
  - Normativa directo: **FO-IC-05 A.2.o** — Nombre archivos: Nombre de los archivos CAD según instructivo para presentación de planos y archivos vigente
  - Normativa directo: **GU-IC-06 §8 ¶13** — que sean requeridos tanto por la interventoría como por la supervisión del contrato. Después de contar con la información estandarizada en los respectivos …
  - Normativa directo: **FO-IC-05 A.2.n** — Nombre layouts: Nombre de layouts según la nomenclatura del plano según el instructivo para la presentación de planos y archivos vigente
  - Normativa directo: **FO-IC-05 A.2.m** — Numeración planos: Numeración de planos de acuerdo al instructivo para la presentación de planos y archivos vigente
  - «8. Se debe ajustar el nombre del archivo AutoCAD, presenta diferencia con el reportado en el formato de los planos.» (DTE 20202150245873, `IDU/2020-11-25_120203560946451_00002.pdf`, p. 5)
  - «8. Se debe ajustar el nombre del archivo AutoCAD, presenta diferencia con el reportado en el formato de los planos. IDU-1384-2017» (OTE 20202150245873, `IDU/2020-11-25_R-IDU1384-0268-20 RTA MV2-365-20 REVISION ARCHIVOS FORMATO CAD Y BASE DATOS GEOGRAFICA ETAPA DIAGNOSTICOS.pdf`, p. 6)
- [ ] **R-T02-06** Usar el rótulo del alistamiento (ROTULO.xlsm) sin editar sus bloques ni eliminar campos, como los del topógrafo de constructor e interventoría. — IDU ×4 `G032` `G085` `G089`
  - Normativa parcial: **GU-IC-06 §8.1.3** — Las instrucciones para diligenciar el rotulo podrán ser consultadas en el archivo Excel ROTULO.xlsm.
  - «1. El formato presentado no es el suministrado en el alistamiento del proyecto, se recuerda que no se debe realizar ningún ajuste a la información …» (DTE 20212150011573, `IDU/2021-01-22_167_anexo_20212150011573_SI.pdf`, p. 2)
  - «1. El plano MVGVPL01.dwg no se presenta con el formato suministrado en la información de alistamiento del proyecto, se recuerda que no se debe realizar ningún …» (DTE 20212150011563, `IDU/2021-02-02_DTE 20212150011563 RECORD 2019.pdf`, p. 2)
- [ ] **R-T02-09** Citar en el campo REFERENCIA del rótulo todos los archivos de referencia externa reales, con su nombre exacto. — IDU ×3 · interventoría ×3 `G031` `G065` `G198`
  - Normativa parcial: **GU-IC-06 §8 ¶11** — información que aparece en otros archivos y que es necesaria para la presentación del plano o de la base a entregar. Al guardar las referencias externas, estas …
  - Normativa parcial: **GU-IC-06 §8.1.3** — Las instrucciones para diligenciar el rotulo podrán ser consultadas en el archivo Excel ROTULO.xlsm.
  - «11. En el archivo MVGVPL01.dwg, el campo del formato REFERENCIA se diligenció con un solo archivo como XREF o referencia externa y como se aprecia en la imagen …» (DTE 20202150245873, `IDU/2020-11-25_120203560946451_00002.pdf`, p. 7)
  - «6. En el campo del formato REFERENCIA solamente se diligenció un solo archivo como XREF o referencia externa y como se aprecia en la imagen se tienen (2) …» (OTE 20202150245873, `IDU/2020-11-25_R-IDU1384-0268-20 RTA MV2-365-20 REVISION ARCHIVOS FORMATO CAD Y BASE DATOS GEOGRAFICA ETAPA DIAGNOSTICOS.pdf`, p. 6)
- [ ] **R-T02-07** Diligenciar todos los campos del rótulo, incluidos CONSECUTIVO y cantidad de planchas, de forma coherente con los layouts. — IDU ×3 `G090` `G139` `G182`
  - Normativa parcial: **GU-IC-06 §8.1.3** — Las instrucciones para diligenciar el rotulo podrán ser consultadas en el archivo Excel ROTULO.xlsm.
  - Normativa directo: **FO-IC-05 A.2.n** — Nombre layouts: Nombre de layouts según la nomenclatura del plano según el instructivo para la presentación de planos y archivos vigente
  - «2. El campo del formato: CONSECTIVO del archivo MVGVPL01.dwg debe estar debidamente diligenciado.» (DTE 20212150074493, `IDU/2021-03-19_120213560460121_00002.pdf`, p. 3)
  - «Se solicita verificar la integridad de todos los rótulos presentados en la especialidad de Geotecnia» (sin radicado, `IDU/2024-06-24_1443_637224_070700_CON_REV_OBSERV_DITINI_GEODATABASE_V3.pdf`, p. 6)
- [ ] **R-T02-01** Nombrar el archivo base CAD según la GU-IC-06 (BASE-IDU-XXX-YYYY.dwg). — IDU ×2 `G042`
  - Normativa directo: **GU-IC-06 §8 ¶8** — 1. Contener únicamente los elementos de competencia del IDU, con su respectiva geometría relacionada en los archivos de Productos_DWG.xlsx. en la hoja de …
  - «1. Se reitera la observación respecto al nombre del archivo base del proyecto CAD que es utilizado como referencia externa dado que no cumple con la …» (DTE 20212150074443, `IDU/2021-03-19_120213560460101_00002.pdf`, p. 2)
  - «1. El nombre del archivo de la base del proyecto CAD no cumple con la nomenclatura de acuerdo a la GUIC06_GUIA_ENTREGA_PRODUCTOS_FORMATO_ DIGITAL_V_1.0, en el …» (DTE 20202150245873, `IDU/2020-11-25_120203560946451_00002.pdf`, p. 2)
- [ ] **R-T02-04** Nombrar los archivos de configuración de capas de las estructuras según la GU-IC-06. — IDU ×2 `G113` `G136`
  - Normativa parcial: **GU-IC-06 §7.1.2 ¶3** — proyecto. Se debe duplicar o crear un NUEVO ARCHIVO si en el proyecto se tiene más de un tipo de estructura en las calzadas o losas. Está identificada con …
  - «2. Se reitera observación, en el archivo RelacionElementoConfiguración la nomenclatura de los archivos de las configuraciones de las capas de la estructura no …» (DTE 20212150103483, `IDU/2021-04-26_Anexo MAB-1-1463-0025-21(2).pdf`, p. 3)
  - «6. Se reitera la observación referente a los nombres de los archivos exel con las configuraciones de las capas de las estructuras.» (DTE 20212150034243, `IDU/2021-02-22_141732_1.pdf`, p. 5)
- [ ] **R-T02-08** Completar la tabla de modificaciones del rótulo con todas las versiones y sus fechas. — interventoría ×4 `G191` `G225`
  - Normativa directo: **FO-IC-05 A.2.l** — Completitud información rótulo: Diligenciamiento de la información solicitada en el rótulo de los planos, correspondiente al proyecto y profesionales
  - Normativa parcial: **GU-IC-06 §8.1.3** — Las instrucciones para diligenciar el rotulo podrán ser consultadas en el archivo Excel ROTULO.xlsm.
  - «La información de modificaciones en el rótulo para algunos planos se encuentra incompleta (fecha)» (STEST 202434601243021, `IDU/2024-10-23_1443_696124_070700_CON_OBSERV_DITINI_GEODATABASE_V3.pdf`, p. 4)
  - «Se debe tener especialmente cuidado con la información en los planos, donde se registran las modificaciones de los archivos DWG» (sin radicado, `IDU/2023-03-29_1443_443723_070700_CON_REVISION_BDG_V1.pdf`, p. 8)

## T10. Ensayos e información técnica asociada

- [ ] **R-T10-03** Hacer coincidir espesores y tipo de mezcla entre tablas de la BDG, cuadros de reporte y planos. — IDU ×3 `G021` `G143` `G170`
  - Normativa parcial: **Productos_DWG Récord F28** — Sección típica con espesores y tipo de materiales utilizados, pendiente Transversal, acotados
  - Normativa directo: **VALIDACIONES_BDG 4.2. Atributos cuantitativos** — Atributos cuantitativos: Se revisará la totalidad de los atributos cuantitativos, mediante el uso de modelos que permiten calcular los valores finales y así …
  - «21. En la tabla DetalleAIntervencionCalCic, se reporta el espesor de rodadura asfáltica en de 2 cm, pero en los cuadros de los planos CAD se presentan …» (DTE 20202150245873, `IDU/2020-11-25_120203560946451_00002.pdf`, p. 13)
  - «8. Se reitera que en la tabla DetalleAIntervencionCalCic, se reporta un espesor de rodadura asfáltica de 81 cm, se solicita revisar y ajustar» (DTE 20212150074443, `IDU/2021-03-19_120213560460101_00002.pdf`, p. 5)
- [ ] **R-T10-02** Anexar los informes aprobados de los ensayos (deflectometría, evaluación estructural). — IDU ×3 `G029` `G154`
  - Normativa directo: **GU-IC-06 §8.2 ¶7** — Archivo(s) Excel que contiene la estructura(s) instalada(s) o diseñada(s) de los elementos calzada y losa, junto con los resultados de los ensayos de …
  - «12. Se debe anexar los informes aprobados de los ensayos de Deflectometria ya que solamente se realiza la entrega de los anexos.» (DTE 20212150074493, `IDU/2021-03-19_120213560460121_00002.pdf`, p. 8)
  - «14. Se solicita anexar los informes aprobados de los ensayos de Deflectometria ya que únicamente se realiza la entrega de los anexos.» (DTE 20212150074443, `IDU/2021-03-19_120213560460101_00002.pdf`, p. 8)
- [ ] **R-T10-04** Diligenciar las tablas de ensayos cuando los informes los registran; justificar solo lo que el alcance excluye. — IDU ×2 `G056` `G060`
  - Normativa parcial: **GU-IC-06 §9.5 ¶4** — las unidades de muestreo el número de losas que las componen. En caso de que dentro de la información entregada por el IDU se incluya el inventario de las …
  - Normativa directo: **GU-IC-06 §8.2 ¶4** — actor de infraestructura, en el marco del alcance del proyecto en cuestión. Interventoría: Al igual que en el campo anterior, la interventoría validará con una …
  - «23. En el archivo DiccionarioAtributos_V7.2. el contratista justifica en la hoja de Losa lo siguiente “El alcance del contrato no contempla levantamiento …» (DTE 20202150245873, `IDU/2020-11-25_120203560946451_00002.pdf`, p. 14)
  - «7. No se fue diligenciada la tabla P_RegistroCampo, aunque se encuentra la justificación en el DiccionarioAtributos_V7.2 1385 del no diligenciamiento, sin …» (DTE 20212150024523, `IDU/2021-02-12_DTE 20212150024523.pdf`, p. 5)
- [ ] **R-T10-05** Revisar los valores de los reportes de estructura de pavimento y de mezcla (carpeta C11.3/CEP). — IDU ×2 `G061` `G137`
  - Normativa directo: **GU-IC-06 §8.2 ¶7** — Archivo(s) Excel que contiene la estructura(s) instalada(s) o diseñada(s) de los elementos calzada y losa, junto con los resultados de los ensayos de …
  - «32. Revisar los valores consignados en el archivo de reporte de la estructura de pavimento de la carpeta de C11.3/CEP.» (DTE 20202150245873, `IDU/2020-11-25_120203560946451_00002.pdf`, p. 18)
  - «13. Se reitera que en la carpeta de C11.3/CEP se deben revisar los valores presentados en el formato de la mezcla utilizada.» (DTE 20212150074443, `IDU/2021-03-19_120213560460101_00002.pdf`, p. 7)
- [ ] **R-T10-06** Reportar un solo registro por calzada en EvaluacionEstructural, con SN efectivo coherente con el informe de deflectometría. — IDU ×2 `G130` `G174`
  - Normativa directo: **VALIDACIONES_BDG 2.1. Verificación de duplicidad del atributo ** — Verificación de duplicidad del atributo PK_ID_Xxxxx de cada elemento y/o tabla: Inexistencia de duplicidad del atributo PK_ID_Xxxxx de cada elemento y/o tabla.
  - Normativa directo: **VALIDACIONES_BDG 4.2. Atributos cuantitativos** — Atributos cuantitativos: Se revisará la totalidad de los atributos cuantitativos, mediante el uso de modelos que permiten calcular los valores finales y así …
  - «8. En la tabla EvaluacionEstructural del elemento calzada, se encontraron varios registros y de acuerdo al archivo Excel DiccionarioAtributos_V7.2, se debe …» (DTE 20212150074493, `IDU/2021-03-19_120213560460121_00002.pdf`, p. 6)
  - «3. En la tabla EvaluacionEstructural de la GDB del proyecto se debe verificar la información incorporada en el atributo SN Efectivo, dado que es diferente a la …» (DTE 20212150103483, `IDU/2021-04-26_Anexo MAB-1-1463-0025-21(2).pdf`, p. 4)
- [ ] **R-T10-08** Enlazar correctamente las exploraciones con sus tablas asociadas (S_Piezometros). — IDU ×1 `G175`
  - Normativa directo: **VALIDACIONES_BDG 1. Verificación de las relación entre eleme** — Verificación de las relación entre elementos y/o tablas: Se verifica la relación entre elementos y/o tablas (el dato que debe ser incorporado en el atributo …
  - «2. Se debe verificar la información incorporada en la tabla Exploración ya que existe un elemento con enlace de la tabla S_Piezometros.» (DTE 20202150230133, `IDU/2020-12-01_02 DTE 20202150230133.pdf`, p. 5)

## T07. Codificación CIV y PK_ID

- [ ] **R-T07-01** Identificar cada elemento con el CIV y el PK_ID del alistamiento publicados en el SIGIDU, sin codificación propia del contrato. — IDU ×7 · interventoría ×4 `G007` `G050` `G104` `G192` `G211` `G224`
  - Normativa parcial: **FO-IC-05 A.1** — No. CIVs reportados en CAD No. de segmentos viales presentados en los archivos CAD Observaciones: Aclaraciones cuando no hay correspondencia entre los …
  - Normativa directo: **FO-IC-05 B.5** — Los elementos se encuentran codificados SI NO Observaciones: Todos los elementos se encuentran codificados según la base geográfica suministrada por el IDU o …
  - Normativa directo: **GU-IC-06 §9.8 ¶2** —  Baranda  Viga  Losa de Aproximación  Barrera  Aleta Estribo  Pila  Cercha  Caisson  Pilote  Diafragma  Columna  Rampa Puente  GuardaRueda  Dado …
  - Normativa directo: **FO-IC-05 B.7.b** — Los elementos nuevos se codifican según rangos suministrados: SI NO Completitud % Observaciones: Los elementos nuevos se codifican según los rangos …
  - Normativa directo: **VALIDACIONES_BDG 1. Verificación de los atributos incorporad** — Verificación de los atributos incorporados: Se verifica que los atributos incorporados en la base de datos geográfica, correspondan con los solicitados en el …
  - «2. Se reitera la siguiente observación: en el archivo de AutoCAD “MVGVPL01.DWG” se deben identificar todas las calzadas con su respectivo CIV y PK_ID.» (DTE 20212150248313, `IDU/2021-08-14_2. 1. 120213561231691_00002-memo.pdf`, p. 8)
  - «2. Se reitera la siguiente observación: en el archivo de AutoCAD “MVGVPL01.DWG” se deben identificar todas las calzadas con su respectivo CIV y PK_ID.» (DTE 20212150313383, `IDU/2021-10-01_120213561457741_00002.pdf`, p. 6)
- [ ] **R-T07-04** Hacer coincidir CIV y PK_ID entre planos, tablas de reporte, GDB y FOIC09. — IDU ×6 `G011` `G178`
  - Normativa directo: **GU-IC-06 §8.2 ¶6** — Ésta información debe ser revisada y aprobada por la interventoría y validada por el área supervisora del contrato, deberá contener la meta física que será …
  - Normativa directo: **GU-IC-06 §7.1.1 ¶3** — FO-IC-09 intervenidos en la ejecución del contrato (aplica para cualquier etapa del _REPORTE_FINAL_ contrato). La información dispuesta en este archivo debe …
  - «2. El registro de las intervenciones en los planos CAD debe coincidir con la presentada en la GDB, y el archivo de Excel …» (DTE 20212150303513, `IDU/2021-09-28_120213561432511_00002.pdf`, p. 3)
  - «4. Se reitera la siguiente observación: los CIV y PK_ID que se encuentran en las tablas de reporte deben coincidir no solo con los planos, sino también con la …» (DTE 20212150313383, `IDU/2021-10-01_120213561457741_00002.pdf`, p. 7)
- [ ] **R-T07-08** Diligenciar RELACION_CAD_CIV.xlsx y RelacionElementoConfiguración de forma coherente con la BDG. — IDU ×2 `G098` `G180`
  - Normativa directo: **GU-IC-06 §8.2 ¶6** — Ésta información debe ser revisada y aprobada por la interventoría y validada por el área supervisora del contrato, deberá contener la meta física que será …
  - Normativa directo: **GU-IC-06 §7.1.2 ¶3** — proyecto. Se debe duplicar o crear un NUEVO ARCHIVO si en el proyecto se tiene más de un tipo de estructura en las calzadas o losas. Está identificada con …
  - Normativa parcial: **FO-IC-05 B.5** — Los elementos se encuentran codificados SI NO Observaciones: Todos los elementos se encuentran codificados según la base geográfica suministrada por el IDU o …
  - «14. Se solicita la entrega del archivo (RELACION_CAD_CIV.xlsx) con la información solicitada, para las dos fases presentadas.» (DTINI 20222350336933, `IDU/2022-09-30_20222350336933 observaciones georref. (1).pdf`, p. 11)
  - «Se solicita verificar y realizar los ajustes respectivos en el archivo (RelacionElementoConfiguración_IDU-1533.xlsx) toda vez que son presentados códigos de …» (DTINI 202323500285933, `IDU/2023-09-07_1202323500285933_00001--observaciones Georreferenciacion..pdf`, p. 9)
- [ ] **R-T07-03** No repetir un PK_ID entre registros del mismo feature class ni entre elementos en los planos. — IDU ×1 · interventoría ×1 `G066` `G265`
  - Normativa directo: **VALIDACIONES_BDG 2.1. Verificación de duplicidad del atributo ** — Verificación de duplicidad del atributo PK_ID_Xxxxx de cada elemento y/o tabla: Inexistencia de duplicidad del atributo PK_ID_Xxxxx de cada elemento y/o tabla.
  - «4. En el archivo digital MVGVPL01.dwg ajustar el texto PK_Calzada, en dos calzadas se incorporó el texto con el mismo identificador.» (DTE 20212150074493, `IDU/2021-03-19_120213560460121_00002.pdf`, p. 4)
  - «Se presenta duplicidad de registros con el mismo numero de PK_ID» (sin radicado, `IDU/2023-03-29_1443_443723_070700_CON_REVISION_BDG_V1.pdf`, p. 20)
- [ ] **R-T07-07** Unificar los identificadores de elementos continuos (redes de ciclorruta, andenes) según lo indicado por el IDU. — IDU ×1 `G163` `G164`
  - Normativa parcial: **GU-IC-06 §8.3 ¶3** — geometrías de los elementos suministrados en la BDG, no deberán ser modificadas a menos de que sea necesario, con el fin de que el elemento represente …
  - «6. En el elemento Red de Ciclorruta es necesario unificar las redes identificadas: (PK_ID_RedCiclorruta – 5300005 y 5300006) en (PK_ID_RedCiclorruta – …» (DTINI 20232350161243, `IDU/2023-07-04_20232350161243(1).pdf`, p. 7)
- [ ] **R-T07-02** Asegurar que todo registro con CIV tenga PK_ID y viceversa. — interventoría ×2 `G208`
  - Normativa directo: **VALIDACIONES_BDG 1. Verificación de las relación entre eleme** — Verificación de las relación entre elementos y/o tablas: Se verifica la relación entre elementos y/o tablas (el dato que debe ser incorporado en el atributo …
  - Normativa parcial: **FO-IC-05 B.5** — Los elementos se encuentran codificados SI NO Observaciones: Todos los elementos se encuentran codificados según la base geográfica suministrada por el IDU o …
  - «existen registros con número de CIV pero sin PK (OBJECTID 86) y viceversa» (sin radicado, `IDU/2023-03-29_1443_443723_070700_CON_REVISION_BDG_V1.pdf`, p. 19)
  - «existen registros con número de CIV pero sin PK (OBJECTID 86) y viceversa» (sin radicado, `IDU/2023-07-27_1443_501423_070700_CON_REVISION_BDG_V2.pdf`, p. 15)
- [ ] **R-T07-05** No borrar los CIV entregados por la DTINI al corregir atributos. — interventoría ×1 `G262`
  - Normativa directo: **FO-IC-05 B.5** — Los elementos se encuentran codificados SI NO Observaciones: Todos los elementos se encuentran codificados según la base geográfica suministrada por el IDU o …
  - «se han omitido en la mayoría de Feature Class los CIV, a pesar de que estos han sido proporcionados por la DTINI» (sin radicado, `IDU/2023-07-27_1443_501423_070700_CON_REVISION_BDG_V2.pdf`, p. 16)
- [ ] **R-T07-06** Para elementos sin codificación IDU, solicitar por medio de la interventoría la actualización del alistamiento. — interventoría ×1 `G286`
  - Normativa directo: **GU-IC-06 §7.1.1 ¶5** — requerir agregar un nuevo elemento, atributo o dominio se deberá hacer el requerimiento a la DTE a través del correo electrónico SERVIDORDEMAPAS@IDU.GOV.CO o …
  - Normativa parcial: **FO-IC-05 B.7.b** — Los elementos nuevos se codifican según rangos suministrados: SI NO Completitud % Observaciones: Los elementos nuevos se codifican según los rangos …
  - «existen elementos como pompeyanos, estaciones, y elementos puente que no contienen codificación asignada por el IDU» (STEST 202434601243021, `IDU/2025-01-09_1443_723824_070700_CON_REV_OBSERV_DITINI_GEODATABASE_V3.pdf`, p. 8)

## T04. Layers, filtros y geometría en CAD

- [ ] **R-T04-01** Dibujar cada elemento en el layer que le corresponde según DefinicionesElementos y LAYERCAD, incluidos exploraciones y mobiliario; nada de diseño en el Layer 0. — IDU ×5 · interventoría ×1 `G025` `G030` `G058` `G072` `G216` `G263`
  - Normativa directo: **Productos_DWG LAYERCAD 25** — Matera: layer CAD MATERA, geometría PUNTO, estados E: EXISTENTE D: DISEÑO C: INTERVENIDO
  - Normativa parcial: **Productos_DWG LAYERCAD regla** — Representar cada elemento en el layer CAD, tipo de geometría y estado definidos en LAYERCAD.
  - Normativa parcial: **FO-IC-05 B.5** — Los elementos se encuentran codificados SI NO Observaciones: Todos los elementos se encuentran codificados según la base geográfica suministrada por el IDU o …
  - Normativa directo: **Productos_DWG LAYERCAD 8** — Exploración: layer CAD EXPLORACION, geometría PUNTO, estados E: EXISTENTE D: DISEÑO C: INTERVENIDO
  - Normativa directo: **Productos_DWG LAYERCAD 9** — Bloque Exploración: layer CAD EXPLORACION, geometría BLOQUE, estados E: EXISTENTE D: DISEÑO C: INTERVENIDO
  - «3. En el plano de Diseño Geométrico se encuentra el layer MU_MATERA_C pero la etapa entregada es de Estudios y Diseños, se debe ajustar de acuerdo al archivo …» (DTE 20212150024523, `IDU/2021-02-12_DTE 20212150024523.pdf`, p. 3)
  - «3. En el plano de Diseño Geométrico se encuentra el layer MU_MATERA_C pero la etapa entregada es de Estudios y Diseños, se debe ajustar de acuerdo al archivo …» (OTE 20212150024523, `IDU/2021-02-12_R-IDU1385-0014-21 RTA MAB-2-1463-0173-20 RAD IDU 20205261211672 ARCHIVOS CAD Y BASE DATOS GEOGRAFICA ETAPA DISEÑO 2019.pdf`, p. 4)
- [ ] **R-T04-04** Agrupar todos los layers de todos los planos en los filtros por temática del alistamiento, no solo en el archivo base. — IDU ×3 · interventoría ×2 `G079` `G115` `G181` `G213` `G214` `G222` `G275`
  - Normativa directo: **GU-IC-06 §8 ¶4** — o entidad que entrega la información como se muestra en la Figura 4, de acuerdo con esto, el contratista elegirá el layout de su etapa o temática y eliminará …
  - Normativa directo: **GU-IC-06 §8 ¶5** — y organizados por filtros con la misma estructura de la BDG como se muestra en la Figura 3, aquellos layers que no se utilicen deberán ser eliminados. Según la …
  - Normativa directo: **Productos_DWG LAYERCAD regla** — Representar cada elemento en el layer CAD, tipo de geometría y estado definidos en LAYERCAD.
  - «4. Aún se encuentran archivos que no cumplen el estándar de capas; por ejemplo, el archivo “CVURAR01” no cumple con la agrupación de las capas por filtros. …» (DTINI 202423500066313, `IDU/2024-02-28_202423500066313 resp DTINI.pdf`, p. 3)
  - «1. Los Layers del plano BASE-1531-2018.DWG deben estar dentro de los filtros que se encuentran establecidos en el alistamiento, y su nomenclatura debe» (STESV 20233360084541, `IDU/2023-01-25_20233360084541.pdf`, p. 5)
- [ ] **R-T04-05** Eliminar los layers sin información y los elementos que no pertenecen al dibujo. — IDU ×3 `G018`
  - Normativa directo: **GU-IC-06 §8 ¶5** — y organizados por filtros con la misma estructura de la BDG como se muestra en la Figura 3, aquellos layers que no se utilicen deberán ser eliminados. Según la …
  - «7. De acuerdo a la Guía GUIC06 se debe eliminar los elementos o layers que no se encuentre en el dibujo.» (OTE 20202150245873, `IDU/2020-11-25_R-IDU1384-0268-20 RTA MV2-365-20 REVISION ARCHIVOS FORMATO CAD Y BASE DATOS GEOGRAFICA ETAPA DIAGNOSTICOS.pdf`, p. 6)
  - «7. De acuerdo a la Guía GUIC06 se debe eliminar los elementos o layers que no se encuentre en el dibujo.» (DTE 20202150245873, `IDU/2020-11-25_120203560946451_00002.pdf`, p. 5)
- [ ] **R-T04-02** Usar la geometría definida por LAYERCAD: una sola geometría por layer y bloques con el mismo criterio en todos los planos, sin mezclar líneas, polilíneas, bloques o achurados. — IDU ×1 · interventoría ×3 `G063` `G218` `G269` `G282` `G293` `G294`
  - Normativa directo: **Productos_DWG LAYERCAD 76** — Red de Ciclorruta: layer CAD REDCICLORRUTA, geometría LÍNEA, estados E: EXISTENTE D: DISEÑO C: INTERVENIDO
  - Normativa directo: **Productos_DWG LAYERCAD regla** — Representar cada elemento en el layer CAD, tipo de geometría y estado definidos en LAYERCAD.
  - «6. En el archivo base presentado (BASE-IDU-1533-2018.dwg) en algunos elementos son utilizado más de un tipo (ver tabla 2), por lo cual se solicita realizar el …» (DTINI 202323500285933, `IDU/2023-09-07_1202323500285933_00001--observaciones Georreferenciacion..pdf`, p. 7)
  - «se encuentran elementos con geometría Polilínea y Bloques (más de una geometría, no permitido)» (sin radicado, `IDU/2024-06-24_1443_637224_070700_CON_REV_OBSERV_DITINI_GEODATABASE_V3.pdf`, p. 3)
- [ ] **R-T04-09** Entregar los reportes de productos CAD: hoja LAYOUT_CIV diligenciada, NUEVOSLAYER y ConfiguracionCapaEstructura, sin hojas sobrantes de la plantilla. — IDU ×1 · interventoría ×2 `G100` `G226` `G233` `G234` `G237` `G247`
  - Normativa parcial: **GU-IC-06 §8.2 ¶1** — La ejecución de los proyectos en las etapas de (Diseño, Ejecución, Diagnostico, Conservación) generará como producto obligatorio la entrega de los siguientes …
  - Normativa directo: **GU-IC-06 §8.2 ¶6** — Ésta información debe ser revisada y aprobada por la interventoría y validada por el área supervisora del contrato, deberá contener la meta física que será …
  - «3. Se debe entregar la Hoja LAYOUT_CIV según los lineamientos de la hoja INSTRUCTIVO LAYOUT_CIV y eliminar el resto de hojas del archivo “Productos_DWG.xlsx” …» (DTINI 202300000317753, `IDU/2023-11-07_202300000317753_DTINI observa planos record 1533-2018.pdf`, p. 3)
  - «tampoco se ha diligenciado la hoja denominada LAYOUT_CIV» (sin radicado, `IDU/2023-07-27_1443_501423_070700_CON_REVISION_BDG_V2.pdf`, p. 8)
- [ ] **R-T04-03** Añadir a todos los layers, incluidos achurados, capas adicionales y mobiliario, el sufijo de estado (E, D o C) de la etapa. — interventoría ×2 `G209`
  - Normativa directo: **GU-IC-06 §8 ¶5** — y organizados por filtros con la misma estructura de la BDG como se muestra en la Figura 3, aquellos layers que no se utilicen deberán ser eliminados. Según la …
  - «Los layers contenidos en achurados no indican estado (E,D,P,C).» (sin radicado, `IDU/2023-07-27_1443_501423_070700_CON_REVISION_BDG_V2.pdf`, p. 11)
  - «Los nombres de layers no indican el estado en todos los casos (E, D, P).» (sin radicado, `IDU/2023-03-29_1443_443723_070700_CON_REVISION_BDG_V1.pdf`, p. 10)
- [ ] **R-T04-06** Dibujar cada achurado en la capa de su elemento y organizarlo en su filtro. — interventoría ×2 `G215` `G264` `G274`
  - Normativa directo: **GU-IC-06 §8 ¶10** — Para la representación de los achurados se podrán generar tantos archivos como sean necesarios y se deberán utilizar en los demás productos como referencias …
  - Normativa parcial: **GU-IC-06 §8 ¶5** — y organizados por filtros con la misma estructura de la BDG como se muestra en la Figura 3, aquellos layers que no se utilicen deberán ser eliminados. Según la …
  - «no existe consistencia en las capas de los achurados, ya que existen entidades como coberturas vegetales incluidos en los achurados de concreto» (sin radicado, `IDU/2023-07-27_1443_501423_070700_CON_REVISION_BDG_V2.pdf`, p. 11)
  - «Existen achurados en niveles de otros elementos.» (sin radicado, `IDU/2023-03-29_1443_443723_070700_CON_REVISION_BDG_V1.pdf`, p. 10)
- [ ] **R-T04-08** Registrar en Productos_DWG.xlsx todos los layers y niveles de los planos, los layers nuevos y el conteo de elementos por layer. — interventoría ×2 `G223` `G276` `G277` `G280`
  - Normativa parcial: **Productos_DWG LAYERCAD regla** — Representar cada elemento en el layer CAD, tipo de geometría y estado definidos en LAYERCAD.
  - «No todos los niveles del archivo BASE-02 se encuentran descritos en el reporte» (sin radicado, `IDU/2024-06-24_1443_637224_070700_CON_REV_OBSERV_DITINI_GEODATABASE_V3.pdf`, p. 3)
  - «este no se ha diligenciado integralmente. No se incluyen todos los niveles o layers contenidos en los planos» (sin radicado, `IDU/2023-07-27_1443_501423_070700_CON_REVISION_BDG_V2.pdf`, p. 8)

## T11. Proceso de entrega y control de calidad

- [ ] **R-T11-01** Revisar integralmente y aplicar control de calidad a cada producto digital antes de entregar, de forma que lo entregado sea la versión aprobada y firmada y que las correcciones no afecten otros elementos; es responsabilidad del contratista. — IDU ×11 · interventoría ×2 `G003` `G144` `G245` `G246` `G250` `G279`
  - Normativa parcial: **GU-IC-06 §10 ¶1** — La información anexa a la radicación oficial deberá estar completa, en caso de que la información no cuente con alguno de los archivos obligatorios, no se …
  - Normativa parcial: **GU-IC-06 §11.1 ¶1** — El contenido de los archivos, su calidad, su completitud y autenticidad de la firma digital, es responsabilidad de los actores de infraestructura, por tanto, …
  - «Se recomienda revisar integralmente todos y cada uno de los productos a entregar, de manera que puedan garantizar, tras las actividades de ajuste o corrección, …» (DTE 20212150024523, `IDU/2021-02-12_DTE 20212150024523.pdf`, p. 6)
  - «Se recomienda revisar integralmente todos y cada uno de los productos a entregar, de manera que puedan garantizar, tras las actividades de ajuste o corrección, …» (DTE 20212150071823, `IDU/2021-03-15_20212150071823.pdf`, p. 3)
- [ ] **R-T11-02** Responder una a una las observaciones previas, incluidas las tablas de revisión y de validación de la GDB. — interventoría ×2 `G219` `G284` `G285`
  - Normativa directo: **GU-IC-06 §10 ¶1** — La información anexa a la radicación oficial deberá estar completa, en caso de que la información no cuente con alguno de los archivos obligatorios, no se …
  - Normativa parcial: **VALIDACIONES_BDG 1. Verificación de los atributos incorporad** — Verificación de los atributos incorporados: Se verifica que los atributos incorporados en la base de datos geográfica, correspondan con los solicitados en el …
  - «este no contiene respuesta tácita al tratamiento de cada observación elevado por la interventoría» (sin radicado, `IDU/2024-12-10_1443_715424_070700_CON_OBSERV_DITINI_GEODATABASE_V3.pdf`, p. 2)
  - «el contratista no da respuesta a las observaciones contenidas en las tablas 3, 4, 5, 6, 7 y 8» (sin radicado, `IDU/2023-07-27_1443_501423_070700_CON_REVISION_BDG_V2.pdf`, p. 12)

## T03. Archivo base CAD y referencias externas

- [ ] **R-T03-02** Verificar que todas las referencias externas carguen sin errores, con rutas relativas. — IDU ×3 · interventoría ×2 `G041` `G114` `G254` `G278`
  - Normativa directo: **GU-IC-06 §8 ¶11** — información que aparece en otros archivos y que es necesaria para la presentación del plano o de la base a entregar. Al guardar las referencias externas, estas …
  - «4. Algunas referencias de los planos no están cargando correctamente, por lo tanto, se solicita realizar los ajustes pertinentes.» (STESV 20233360084541, `IDU/2023-01-25_20233360084541.pdf`, p. 6)
  - «3. Las referencias de los planos no cargan de manera correcta, se recomienda realizar los ajustes necesarios.» (DTE 20212150313383, `IDU/2021-10-01_120213561457741_00002.pdf`, p. 6)
- [ ] **R-T03-01** Mantener un único archivo base con solo los elementos de la meta física y coherente con la BDG; los elementos ajenos van en BASE-02 como referencia externa. — IDU ×3 `G086` `G087` `G184`
  - Normativa directo: **GU-IC-06 §8 ¶8** — 1. Contener únicamente los elementos de competencia del IDU, con su respectiva geometría relacionada en los archivos de Productos_DWG.xlsx. en la hoja de …
  - Normativa directo: **GU-IC-06 §8 ¶11** — información que aparece en otros archivos y que es necesaria para la presentación del plano o de la base a entregar. Al guardar las referencias externas, estas …
  - «.5.1 ArchivÓ Base Es necesariocrear un único archivo en formato ('.dwg), que contenga únicamentelos elementosde la meta física del proyecto. El nombre de este …» (OTE 20202150245873, `IDU/2020-11-25_R-IDU1384-0268-20 RTA MV2-365-20 REVISION ARCHIVOS FORMATO CAD Y BASE DATOS GEOGRAFICA ETAPA DIAGNOSTICOS.pdf`, p. 4)
  - «2. Depurar el archivo base CAD “ BASE-IDU-1531-2018”. Se recuerda que en este archivo solo debe presentar los elementos de la meta física, los que deben ser …» (DTINI 202423500066313, `IDU/2024-02-28_202423500066313 resp DTINI.pdf`, p. 2)
- [ ] **R-T03-05** Configurar las unidades de dibujo en metros en todos los DWG (DWGUNITS). — IDU ×2 `G078` `G151`
  - Normativa directo: **GU-IC-06 §8 ¶7** — formato .dwg que se usará como referencia externa en todos los planos en planta presentados para cada componente. Esta información se presentará en el Model …
  - «3. Aún se encuentran archivos con unidades de dibujo diferentes a metros; por ejemplo, en los archivos “BASE-IDU-1531-2018” y “CVURAR01”. Use el comando …» (DTINI 202423500066313, `IDU/2024-02-28_202423500066313 resp DTINI.pdf`, p. 3)
  - «4. Se requiere validar la totalidad de archivos en formato .dwg y realizar el ajuste de la unidad de medida a metros, conforme a lo establecido en el numeral …» (DTINI 202623500078293, `IDU/2026-03-04_1202623500078293_00001 Observaciones Planos Record.pdf`, p. 5)
- [ ] **R-T03-04** Ubicar las referencias externas en la carpeta xRef (escrita así) dentro de D.2.BaseDWG. — IDU ×1 · interventoría ×3 `G049` `G189`
  - Normativa parcial: **GU-IC-06 §8 ¶11** — información que aparece en otros archivos y que es necesaria para la presentación del plano o de la base a entregar. Al guardar las referencias externas, estas …
  - «En el ejemplo de la ilustración 3, se presenta una subcarpeta» (STEST 202434601243021, `IDU/2024-10-23_1443_696124_070700_CON_OBSERV_DITINI_GEODATABASE_V3.pdf`, p. 2)
- [ ] **R-T03-03** Presentar todos los temas con el archivo base como referencia externa; los planos de localización van como dibujo, no como imagen. — IDU ×1 · interventoría ×1 `G166` `G257`
  - Normativa directo: **GU-IC-06 §8 ¶9** —  Las letras XXX hacen referencia al número del contrato.  Las letras YYYY al año del contrato. Por ejemplo, BASE-01-IDU-5-2014. En el caso de proyectos de …
  - Normativa directo: **GU-IC-06 §8 ¶11** — información que aparece en otros archivos y que es necesaria para la presentación del plano o de la base a entregar. Al guardar las referencias externas, estas …
  - Normativa parcial: **GU-IC-06 §8 ¶7** — formato .dwg que se usará como referencia externa en todos los planos en planta presentados para cada componente. Esta información se presentará en el Model …
  - «Este archivo debe ser utilizado como referencia externa (xref) para la presentaciónde todos los temas a entregar para cada una de las etapas objeto del …» (OTE 20202150245873, `IDU/2020-11-25_R-IDU1384-0268-20 RTA MV2-365-20 REVISION ARCHIVOS FORMATO CAD Y BASE DATOS GEOGRAFICA ETAPA DIAGNOSTICOS.pdf`, p. 4)
  - «el mismo corresponde a una imagen con problemas de referencia externa» (sin radicado, `IDU/2024-06-24_1443_637224_070700_CON_REV_OBSERV_DITINI_GEODATABASE_V3.pdf`, p. 2)

## Prácticas observadas sin respaldo escrito localizado

Exigencias recurrentes en las observaciones para las que no se confirmó una regla escrita entre los candidatos normativos revisados. Se indica el tema de cada una.

- [ ] **R-T08-08** (T08) Hacer coincidir los polígonos del DWG y de la BDG, con límites por CIV. — interventoría ×2 `G206`
  - Práctica observada: no se confirmó respaldo escrito entre los candidatos revisados.
  - «los polígonos que se describen en el DWG y la BDG difieren (límites por CIV). Ajustar plano DWG.» (sin radicado, `IDU/2023-03-29_1443_443723_070700_CON_REVISION_BDG_V1.pdf`, p. 18)
  - «los polígonos que se describen en el DWG y la BDG difieren (límites por CIV). Ajustar plano DWG.» (sin radicado, `IDU/2023-07-27_1443_501423_070700_CON_REVISION_BDG_V2.pdf`, p. 13)
- [ ] **R-T05-05** (T05) Incluir en cada plano el cuadro del sistema de referencia, con su época. — interventoría ×4 `G195` `G228` `G290`
  - Práctica observada: no se confirmó respaldo escrito entre los candidatos revisados.
  - «Los planos deben incluir el sistema de referencia empleado (coordenadas cartesianas)» (STEST 202434601243021, `IDU/2024-10-23_1443_696124_070700_CON_OBSERV_DITINI_GEODATABASE_V3.pdf`, p. 4)
  - «información del sistema de referencia geodésico de manera incompleta (época)» (sin radicado, `IDU/2023-03-29_1443_443723_070700_CON_REVISION_BDG_V1.pdf`, p. 13)
- [ ] **R-T05-13** (T05) Incluir las coordenadas de los puntos en el esquema de ubicación de perforaciones. — interventoría ×1 `G229`
  - Práctica observada: no se confirmó respaldo escrito entre los candidatos revisados.
  - «No se incluye coordenadas de puntos» (sin radicado, `IDU/2023-03-29_1443_443723_070700_CON_REVISION_BDG_V1.pdf`, p. 14)
- [ ] **R-T05-14** (T05) Incluir en los planos la nota aclaratoria de que la interventoría no aprueba diseños. — interventoría ×1 `G258`
  - Práctica observada: no se confirmó respaldo escrito entre los candidatos revisados.
  - «carecen de la leyenda aclaratoria de interventoría» (sin radicado, `IDU/2023-07-27_1443_501423_070700_CON_REVISION_BDG_V2.pdf`, p. 6)
- [ ] **R-T01-10** (T01) Acordar en mesa de trabajo el momento de entrega de PDF y firmas; en la mesa del 8/6/2021 se acordó DWG en la entrega inicial y PDF firmados tras la aprobación. — interventoría ×1 `G212`
  - Práctica observada: no se confirmó respaldo escrito entre los candidatos revisados.
  - «Los planos en formato PDF deberán ser entregados una vez se cuente con la aprobación de la interventoría y la DTINI.» (sin radicado, `IDU/2023-07-27_1443_501423_070700_CON_REVISION_BDG_V2.pdf`, p. 4)
- [ ] **R-T02-10** (T02) Indicar en las tablas de reporte el formato de fecha utilizado (año/mes/día). — IDU ×1 `G120`
  - Práctica observada: no se confirmó respaldo escrito entre los candidatos revisados.
  - «3. Se encontró que en los siguientes planos: MVGVPL11.DWG y MVGVPL49.DWG, el formato de fecha es Año/Mes/Día, por ser los únicos planos con este formato …» (DTE 20212150248313, `IDU/2021-08-14_2. 1. 120213561231691_00002-memo.pdf`, p. 8)
- [ ] **R-T02-03** (T02) Nombrar los informes solo con su codificación, sin nombres extensos ni sufijos. — interventoría ×2 `G261` `G273`
  - Práctica observada: no se confirmó respaldo escrito entre los candidatos revisados.
  - «tiene por objeto evitar problemas al momento de copiar la información dada la extensión de nombres de archivos y carpetas» (sin radicado, `IDU/2023-07-27_1443_501423_070700_CON_REVISION_BDG_V2.pdf`, p. 6)
  - «Los nombres de archivos de informes deben ser coherentes con la estructura de codificación.» (sin radicado, `IDU/2023-03-29_1443_443723_070700_CON_REVISION_BDG_V1.pdf`, p. 8)
- [ ] **R-T10-01** (T10) Verificar que las coordenadas de la tabla Deflectometria queden dentro de su calzada. — IDU ×5 `G008`
  - Práctica observada: no se confirmó respaldo escrito entre los candidatos revisados.
  - «10. Se reitera que en la tabla Deflectometria se debe verificar las coordenadas, algunas se encuentran por fuera de sus respectivas calzadas.» (DTE 20212150074443, `IDU/2021-03-19_120213560460101_00002.pdf`, p. 6)
  - «24. En la tabla Deflectometria se deben verificar las coordenadas, algunos puntos se encuentran por fuera de la respectiva calzada.» (DTE 20202150245873, `IDU/2020-11-25_120203560946451_00002.pdf`, p. 14)
- [ ] **R-T10-07** (T10) Verificar que no se repitan deflexiones entre segmentos en DeflexionCalculo. — IDU ×1 `G173`
  - Práctica observada: no se confirmó respaldo escrito entre los candidatos revisados.
  - «5. Se reitera la observación sobre la información capturada en la tabla DeflexionCalculo, las relaciones no cumplen lo establecido en la estructura de la base …» (DTE 20212150034243, `IDU/2021-02-22_141732_1.pdf`, p. 5)
- [ ] **R-T10-09** (T10) Verificar la inclusión de índices y ensayos del alcance contractual según la especificación IDU 510-11. — IDU ×1 `G179`
  - Práctica observada: no se confirmó respaldo escrito entre los candidatos revisados.
  - «13. En el tema de las Evaluaciones Estructural y Superficial, es necesario verificar la observación “La especificación IDU 510-11 no establece esta valor como …» (DTINI 20222350336933, `IDU/2022-09-30_20222350336933 observaciones georref. (1).pdf`, p. 11)
- [ ] **R-T04-07** (T04) Ubicar grillas, coordenadas y textos del rótulo en los layers del filtro ROTULO. — interventoría ×1 `G242`
  - Práctica observada: no se confirmó respaldo escrito entre los candidatos revisados.
  - «Los niveles de grillas y coordenadas no se encuentran definidos en el grupo o filtro ROTULO.» (sin radicado, `IDU/2023-03-29_1443_443723_070700_CON_REVISION_BDG_V1.pdf`, p. 11)
- [ ] **R-T11-04** (T11) Solicitar mesa de trabajo con la DTINI solo después de atender todas las observaciones. — IDU ×1 · interventoría ×1 `G146` `G252`
  - Práctica observada: no se confirmó respaldo escrito entre los candidatos revisados.
  - «3. Se reitera la solicitud de Mesa de trabajo requerida mediante correo electrónico de 23/07/2020. Aunque el memorando de observaciones a tratar en la mesa de …» (DTE 20202150230133, `IDU/2020-12-01_02 DTE 20202150230133.pdf`, p. 6)
  - «dicha mesa de trabajo se gestionará con el IDU una vez el Interventor verifique» (sin radicado, `IDU/2025-01-09_1443_723824_070700_CON_REV_OBSERV_DITINI_GEODATABASE_V3.pdf`, p. 10)
- [ ] **R-T11-03** (T11) No reincidir en observaciones anteriores, no re-radicar archivos sin cambios y no empeorar la calidad de una entrega previa; en esos casos la entrega se objeta. — interventoría ×3 `G270` `G271` `G292`
  - Práctica observada: no se confirmó respaldo escrito entre los candidatos revisados.
  - «reinciden en las observaciones y hallazgos de versiones previas» (sin radicado, `IDU/2025-01-09_1443_723824_070700_CON_REV_OBSERV_DITINI_GEODATABASE_V3.pdf`, p. 10)
  - «las versiones de los archivos son las mismas entre los productos radicados» (sin radicado, `IDU/2024-12-10_1443_715424_070700_CON_OBSERV_DITINI_GEODATABASE_V3.pdf`, p. 7)
