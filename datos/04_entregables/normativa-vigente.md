# Normativa vigente — contrato IDU 348 — construcción (récord)

> Paquete de alistamiento oficial de 2020 entregado por el IDU para los contratos 348 y 351.
> Para la entrega de construcción del 348 rige este paquete, no versiones posteriores.

| Código | Documento | Versión | Tipo | Aplica a construcción (récord) | Nota |
|---|---|---|---|---|---|
| BDG-v8 | Geodatabase plantilla del alistamiento | 8 | plantilla | si | Archivo nombrado 351 dentro del paquete oficial entregado por el IDU para los contratos 348 y 351 |
| BDG-v8-XML | Esquema XML de la geodatabase | 8 | plantilla | si |  |
| ConfiguracionCapaEstructura | Configuración de capas de estructura de pavimento | 2 | plantilla | si |  |
| EstructuraCarpetas | Estructura de carpetas por etapa | — | plantilla | si | Hoja Construcción (Récord); hay una copia en la raíz |
| FO-IC-05 | Lista de chequeo para revisión de archivos y planos | 1 | formato | si | Lista oficial por componente; tipo 6 = Construcción |
| FO-IC-09 | Reporte final de meta física | 1.0 | formato | si |  |
| GU-IC-06 | Guía entrega de productos en formato digital | 2 | guia | si | Guía principal; idéntica a la copia del corpus |
| GU-IC-07 | Elaboración de estudios topográficos | 2 | guia | si | Placas de amarre y topografía |
| GU-OC-02 | Registros fotográficos de intervenciones | 1.0 | guia | si |  |
| LayerFormatosIDU | Plantilla de layers CAD | 8 | plantilla | si |  |
| Productos_BDG | Catálogo, atributos, validaciones y reglas topológicas de la BDG | — | plantilla | si | Hojas VALIDACIONES_BDG y REGLAS_TOPOLOGICAS |
| Productos_DWG | Layers, layouts, escalas y nomenclatura de planos | — | plantilla | si | Hoja ElementosConstruccion (Récord) |
| ROTULO | Rótulo de planos | — | plantilla | si | Contiene macros: leer sin ejecutarlas |
| SimbologiaIDU | Simbología CAD | 2019 | plantilla | si |  |
| GU-GI-02 | Documento técnico de intervención de infraestructura vial y espacio público | 1 | guia | parcial | Tipos de intervención |
| GU-IC-08 | Diagnóstico básico de espacio público e inventario para la accesibilidad | 1.0 | guia | parcial | Atributos de accesibilidad |
| GuiaCodificacionLosa | Guía de codificación de losas | — | guia | parcial |  |
| GU-DP-01 | Alcance de entregables etapa de diseño | 1.0 | guia | no | Etapa de diseño |
| GU-FP-01 | Alcance de entregables prefactibilidad | 4.0 | guia | no |  |
| GU-FP-01 | Alcance de entregables factibilidad | 2.0 | guia | no |  |
| GuiaDiagnosticoEP | Guía de diagnóstico para espacio público | — | guia | no | Contexto |
| GuiaDisenoVias | Guía de diseño de vías urbanas de Bogotá | — | guia | no | Contexto |
| MG-GP-01 | Manual de gestión predial | 1.0 | guia | no |  |
| MetodologiaPuentes | Metodología de los puentes fase II | — | guia | no | Contexto |

## Catálogo de requisitos oficiales

Cada entrada conserva la fuente y sección de la que fue extraída. El enlace con las
observaciones se confirma por separado; una coincidencia semántica no sustituye la revisión.

### GU-IC-06

#### §1 OBJETIVO GENERAL

- **GU-IC-06 §1** — Establecer los estándares y parámetros para la entrega de productos digitales finales, en el desarrollo de las diferentes etapas adelantadas por quienes realicen proyectos de infraestructura asociados a los Sistemas de Movilidad y Espacio Público, en el Distrito Capital.
#### §1.1 OBJETIVOS ESPECÍFICOS

- **GU-IC-06 §1.1 ¶1** —  Señalar los lineamientos de entrega, para cada uno de los productos digitales, suministrados por quienes ejecuten proyectos de infraestructura y desarrollen tareas de interventoría en la ciudad, enmarcadas dentro de las competencias correspondientes al Instituto de desarrollo Urbano (IDU).  Definir el alcance de la información digital a ser entregada en las etapas de: Prefactibilidad, Factibilidad, Diseños, Construcción, Diagnóstico y Conservación, de los proyectos desarrollados en la infraestructura asociada a los Sistemas de Movilidad y Espacio Público.  Especificar el alcance de la Dirección Técnica Estratégica (DTE) respecto al análisis y la
- **GU-IC-06 §1.1 ¶2** — conformidad de los productos digitales, entregados en los proyectos desarrollados en la infraestructura asociada a los Sistemas de Movilidad y Espacio Público.  Unificar los criterios de elaboración y entrega de los productos digitales, que se reciben por parte de terceros y su alcance en cada una de las áreas ejecutoras del IDU.
#### §2 ALCANCE

- **GU-IC-06 §2** — El presente documento describe el proceso de entrega de los productos digitales para los proyectos información referente a rótulos, formatos y estructuras de datos espaciales y alfanuméricos, hasta la entrega de la información ante la DTE, con el fin de que los productos avalados permitan actualizar el Sistema de Información Geográfica IDU (SIGIDU) el cual es dispuesto para el análisis y consulta de todos los funcionarios del IDU y la ciudadanía en general.
#### §3 RESPONSABILIDADES

- **GU-IC-06 §3** — Las responsabilidades de los actores que intervienen en la producción, conservación y consecución de los productos digitales entregables del Instituto de Desarrollo Urbano (IDU), podrán ser consultadas en el acuerdo 002 de 2017 del IDU.
#### §4 MARCO NORMATIVO

- **GU-IC-06 §4 ¶1** —  Ley 527 de 1999, del Congreso de la República, “Por medio de la cual se define y reglamenta el acceso y uso de los mensajes de datos, del comercio electrónico y de las firmas digitales, y se establecen las entidades de certificación y se dictan otras disposiciones.  Ley 594 de 2000, del Congreso de la República, “Por la cual se dicta la Ley general de archivos y otras disposiciones”. En su artículo 21 establece que las entidades públicas deberán elaborar programas de gestión de documentos, pudiendo contemplar el uso de nuevas tecnologías y soportes, en cuya aplicación deberán observarse los principios y procesos archivísticos. El
- **GU-IC-06 §4 ¶2** — parágrafo de este artículo, menciona que los documentos emitidos por los citados medios gozarán de la validez y eficacia de un documento original, siempre que quede garantizada su autenticidad, su integridad y el cumplimiento de los requisitos exigidos por las Leyes procesales.  Ley 1712 de 2014, del Congreso de la República, “Por medio de la cual se crea la Ley de Transparencia y del Derecho de Acceso a la Información Pública Nacional y se dictan otras disposiciones”.  Decreto 2639 de 2012, de la Presidencia de la República, “Por el cual se reglamenta el Título V de la Ley 594 de 2000, parcialmente los artículos 58 y 59 de la Ley 1437 de 2011 y se dictan
- **GU-IC-06 §4 ¶3** — otras disposiciones en materia de Gestión Documental para todas las Entidades del Estado.  Decreto 333 de 2014, de la Presidencia de la República, “Por el cual se reglamenta el artículo 160 del Decreto-ley 19 de 2012”.  Norma Técnica Colombiana NTC 5043: Información geográfica: conceptos básicos de la calidad de los objetos geográficos.  Acuerdo 02 de 1999, del Concejo de Bogotá, “Por el cual se crea el sistema de información de la malla vial de Santa Fe de Bogotá, D.C.”, a cargo del Instituto de Desarrollo Urbano, I.D.U. o de quién haga sus veces, que unificará y compilará la información existente de estudios ya
- **GU-IC-06 §4 ¶4** — realizados y por realizar en las diferentes vías del Distrito Capital”, para lo cual el IDU creó el Sistema de Información Geográfica SIGIDU constituido por una base cartográfica y la información alfanumérica del componente de diagnóstico y geometría de cada tramo vial.  Acuerdo 130 de 2004, del Concejo de Bogotá, “por medio del cual se establece la infraestructura integrada de datos espaciales para el Distrito Capital y se dictan otras disposiciones”.  Acuerdo 547 de 2014, del Concejo de Bogotá, “por el cual se establece hacer pública la programación del mantenimiento periódico de la malla vial local y se dictan otras disposiciones”.
- **GU-IC-06 §4 ¶5** —  El Decreto 514 de 2006, de la Alcaldía Mayor de Bogotá D.C, “Por el cual se establece que toda entidad pública a nivel Distrital debe tener un Subsistema Interno de Gestión Documental y Archivos (SIGA) como parte del Sistema de Información Administrativa del Sector Público”, en su Artículo 4 establece “toda entidad de la administración Distrital debe contar con un Subsistema Interno de Gestión Documental y Archivo (SIGA).  Decreto 203 de 2011, de la Alcaldía Mayor de Bogotá D.C, “Por el cual se adopta el mapa de referencia como instrumento oficial de consulta para Bogotá D.C.”.  Decreto 653 2011, de la Alcaldía Mayor de Bogotá D.C, “por medio del cual se reglamenta la
- **GU-IC-06 §4 ¶6** — Infraestructura Integrada de Datos Espaciales para el Distrito Capital -IDECA, y se dictan otras disposiciones”.  Decreto 76 de 2013, de la Alcaldía Mayor de Bogotá D.C, “Por el cual se modifica el Decreto Distrital 203 del 17 de mayo de 2011”.  Resolución 305 de 2008, de la Comisión Distrital de Sistemas, “Por la cual se expiden políticas públicas para las entidades, organismos y órganos de control del Distrito Capital, en materia de Tecnologías de la Información y Comunicaciones respecto a la planeación, seguridad, democratización, calidad, racionalización del gasto, conectividad, infraestructura de Datos Espaciales y Software Libre”.
- **GU-IC-06 §4 ¶7** —  Resolución 002 de 2017, de la Comisión Distrital de Sistemas, “Por la cual se adoptan las políticas específicas, el reglamento general, los reglamentos específicos y los instrumentos para el desarrollo de la Infraestructura Integrada de Datos Espaciales para el Distrito Capital – IDECA”.  Resolución 1312 de 2011 de la Unidad Administrativa Especial de Catastro Distrital "Por el cual se establece la especificación técnica en cuanto al mantenimiento y versionamiento del Mapa de Referencia para Bogotá, Distrito Capital”.  Directiva 04 de 2012, de la Presidencia de la República, “Eficiencia administrativa y lineamientos de la política cero papeles en la administración pública”.
- **GU-IC-06 §4 ¶8** —  Acuerdo 002 de 2009, del Consejo Directivo del IDU, “Por el cual se establece la estructura organizacional del Instituto de Desarrollo Urbano, las funciones de sus dependencias y se dictan otras disposiciones”.  Acuerdo 02 de 2017, del Consejo Directivo del IDU, “Por la cual se modifica parcialmente el Acuerdo 002 de 2009”.
#### §5 SIGLAS Y DEFINICIONES

- **GU-IC-06 §5** — Las siglas, términos y definiciones aplicables al documento podrán ser consultados en el micrositio Direccionario de términos IDU (https://www.idu.gov.co/page/transparencia/informacion-de- interes/glosario).
#### §5.1 SIGLAS

- **GU-IC-06 §5.1** — DTE IDU JBB SDM SIGIDU STRF POT
#### §5.2 DEFINICIONES

- **GU-IC-06 §5.2** — Actor de infraestructura Conservación Alistamiento de información Construcción Altimetría Dataset Atributo Diccionario de Atributos Base de datos geográfica Diagnóstico Carga urbanística. Digitalización Código del Elemento Documento digital Código de identificación vial - CIV DSPACE Entregables Mantenimiento periódico: Elemento Mantenimiento preventivo Elementos viales Reservados Mantenimiento rutinario: Factibilidad: Normas APA Feature Layer Firma digital Losa. Planimetría Perfil longitudinal Formato DWG Producto digital. Geometría: Repositorio institucional Dspace Georreferenciación Sistema de coordenadas Interventoría Tercero Registro topográfico Topología Segmento vial
#### §6 PRESENTACIÓN DE ARCHIVOS, PLANOS E INFORMACIÓN DEL PROYECTO

- **GU-IC-06 §6 ¶1** — La información generada en el desarrollo de los proyectos que es requerida de manera contractual, deberá ser entregada al IDU en medio digital, correspondiente a la obligación contractual estipulada en el contrato IDU, en los términos de referencia, apéndices, anexos, propuesta técnica, guías de productos entregables y en el manual de interventoría, entre otros; para proyectos desarrollados por urbanizadores o terceros de acuerdo a la carga urbanística conforme a la etapa desarrollada. Esta guía es aplicable al actor que realice proyectos de infraestructura asociados a los Sistemas de Movilidad y Espacio Público del Distrito Capital.
- **GU-IC-06 §6 ¶2** — Los archivos deberán presentarse únicamente en formato digital, deberán ser avalados por los profesionales que intervienen en su elaboración, mediante firma digital y en formato .pdf, conforme a lo requerido en el documento referente a la Firma Digital del IDU, vigente al momento de la solicitud del alistamiento de la información digital. El archivo en formato .pdf deberá contener la misma información presentada en todos los productos digitales del formato de origen. Para proyectos adelantados directamente por las dependencias del IDU, por Urbanizadores o Terceros y Entidades Nacionales o Distritales, que suministran productos (entregables) al IDU, se podrán
- **GU-IC-06 §6 ¶3** — presentar los archivos sin firma digital (dependiendo de los requisitos del proyecto). No obstante, se debe tener en cuenta que, para ello, se debe realizar la entrega en medio físico (avalado con las respectivas firmas) y en medio digital al área supervisora en el IDU, quien avalara el contenido de la información presentada, previo a la remisión a la Dirección Técnica Estratégica (DTE). El documento físico deberá corresponder exactamente con la información presentada en los distintos productos digitales. Las firmas digitales no aplican para las etapas de Prefactibilidad y Factibilidad, así como la
- **GU-IC-06 §6 ¶4** — entrega de productos físicos firmados, siempre y cuando estas etapas sean realizadas por el IDU. Los productos entregables para las etapas de Prefactibilidad y Factibilidad son los señalados en las ENTREGABLES DE FACTIBILIDAD o en el documento vigente. El proceso de entrega y recibo de los productos digitales, elaborados y presentados por los contratistas, urbanizadores o terceros ante el IDU es el señalado en la Figura 1. Figura 1. Flujo del proceso de entrega y recibo de productos digitales de proyectos
#### §7 REPRESENTACIÓN DE LOS ELEMENTOS ESTANDARIZADOS

- **GU-IC-06 §7** — A continuación, se presenta el proceso para acceder a las guías y formatos exigidos por el IDU, para la estandarización de los productos digitales:
#### §7.1 INFORMACIÓN DEL ALISTAMIENTO

- **GU-IC-06 §7.1 ¶1** — En todo proyecto de infraestructura asociado a los Sistemas de Movilidad y Espacio Público del Distrito Capital, se deberá solicitar la información con la cual realizará la estandarización de los productos digitales conforme a las obligaciones contractuales adquiridas en el contrato o para la entrega de proyectos desarrollados por urbanizadores o terceros, esta información será exclusiva para cada contrato y se podrá solicitar a partir de la firma del acta de inicio, al correo electrónico SERVIDORDEMAPAS@IDU.GOV.CO relacionando la información básica del contrato:  Número de contrato  Año  Objeto del contrato IDU  Número del contrato de interventoría.
- **GU-IC-06 §7.1 ¶2** — Para proyectos desarrollados por URBANIZADORES O TERCEROS en el correo electrónico se deberá relacionar el nombre del urbanismo (nombre del proyecto urbanístico aprobado por la curaduría urbana), suministrado por la Dirección Técnica de Administración de Infraestructura DTAI, junto con el plano de urbanismo en formato dwg, y copia del plano aprobado por Curaduría Urbana en formato PDF y sellado. Adicionalmente, tener en cuenta el proceso señalado en el manual MG-GI-01 “INTERVENCIÓN DE URBANIZADORES Y/O TERCEROS” EJECUCIÓN DE PROYECTOS DE INFRAESTRUCTURA VIAL Y DE ESPACIO PÚBLICO EN EL DISTRITO CAPITAL EN CUMPLIMIENTO DE OBLIGACIONES
- **GU-IC-06 §7.1 ¶3** — URBANÍSTICAS Y DE MOVILIDAD”, en el numeral 38 del subcapítulo 9.1. OBLIGACIONES DEL URBANIZADOR Y/O TERCERO. Para los proyectos de diseños y construcción que tienen dentro de su objeto la elaboración, actualización, ajustes a los diseños entre otros, la Base de Datos Geográfica (BDG) no incluirá elementos geográficos por tanto se deberá realizar el siguiente proceso para que sean remitidos los elementos con códigos oficiales. 1. Solicitar el alistamiento para realizar la estandarización de los productos digitales al correo electrónico SERVIDORDEMAPAS@IDU.GOV.CO. 2. Generar los polígonos y polilíneas correspondientes a los elementos del Diseño del proyecto en
- **GU-IC-06 §7.1 ¶4** — la BDG suministrada desde el correo electrónico descrito en el numeral 1 y señalados en el archivo Excel Productos_BDG.xlsx en la hoja de cálculo CATALOGO_BDG identificada con color , posteriormente remitir al correo electrónico SERVIDORDEMAPAS@IDU.GOV.CO la BDG con los elementos creados, y los planos en planta en formato dwg. 3. La información digital será suministrada por medio de un correo electrónico al correo del solicitante, con los archivos del alistamiento, la codificación y segmentación oficial de los elementos; esta deberá ser de conocimiento del contratista, urbanizador o tercero, el área supervisora, e interventoría.
- **GU-IC-06 §7.1 ¶5** — La información será suministrada en una carpeta con el nombre del contrato IDU o el nombre del urbanismo que agrupará las siguientes carpetas: 1. BaseDatosGeografica 2. FormatosDWG 3. Guías 4. EstructuraCarpetas A continuación, se presenta el contenido detallado de cada una de las carpetas que contiene el alistamiento de la información:
#### §7.1.1 CARPETA BASEDATOSGEOGRAFICA

- **GU-IC-06 §7.1.1 ¶1** — ARCHIVOS DESCRIPCIÓN Base de Datos Geográfica (BDG) Estructura lógica de todos los elementos que conforman la infraestructura de (Nombre del contrato los Sistemas de Movilidad y Espacio Público, a cargo del IDU. o urbanismo).gdb Archivo que contiene múltiples hojas de cálculo para cada uno de los elementos de la BDG, detalla los atributos con la respectiva descripción, dominios y rangos a incorporar en la BDG. Se establecen también los atributos mínimos obligatorios a ser entregados por cada etapa del proyecto. Están identificadas con color Hoja CATALOGO_BDG: lista los elementos de la base de datos geográfica y el Dataset al que pertenecen. Esta identificada con color
- **GU-IC-06 §7.1.1 ¶2** — Productos_BDG.xlsx Hoja VALIDACIONES_BDG: Comprende todas las validaciones que deben ser realizadas por el contratista, urbanizador o tercero e interventoría, respecto a la calidad de la información presentada en la BDG. Esta identificada con color Hoja REGLAS_TOPOLÓGICAS contiene las reglas Topológicas que se deben validar en la BDG por el contratista urbanizador o tercero y la interventoría. Explica la relación geográfica entre los elementos que conforman la infraestructura de los Sistemas de Movilidad y Espacio Público, a cargo del IDU. Esta identificada con color Archivo que deberá ser diligenciado con la información de todos los elementos
- **GU-IC-06 §7.1.1 ¶3** — FO-IC-09 intervenidos en la ejecución del contrato (aplica para cualquier etapa del _REPORTE_FINAL_ contrato). La información dispuesta en este archivo debe corresponder con la META_FISICA.xlsx cantidad de elementos representados en la BDG y con la cantidad de elementos representados para los planos en planta en formato .DWG. Tabla 1. Contenido Carpeta BaseDatosGeografica Dependiendo del objeto contractual del contrato y las diferentes etapas desarrolladas en el mismo o la carga urbanística, se entregará la respectiva cartografía en la BDG con los elementos viales los cuales han sido reservados previamente por el área supervisora mediante los formatos:
- **GU-IC-06 §7.1.1 ¶4** —  FOIC01 REPORTE DE ELEMENTOS VIALES OBJETO DE LA CONTRATACION  FOIC02_REPORTE PARA LA ACTUALIZACIÓN DE LOS ESTUDIOS, DIAGNOSTICOS, DISEÑOS E INTERVENCIONES REALIZADAS EN LA INFRAESTRUCTURA VIAL DE LA CIUDAD La BDG contiene la estructura lógica de todos los elementos que conforman la infraestructura de los Sistemas de Movilidad y Espacio Público del Distrito Capital a cargo del IDU; y que se encuentran contenidos en el Sistema de información Geográfica del Instituto de Desarrollo Urbano (SIGIDU). (Conjunto de Elementos Geográficos) (Elementos Geográficos) Figura 2. Estructura Básica de la BDG La estructura de la BDG no debe ser modificada por el contratista, urbanizador o tercero, en caso de
- **GU-IC-06 §7.1.1 ¶5** — requerir agregar un nuevo elemento, atributo o dominio se deberá hacer el requerimiento a la DTE a través del correo electrónico SERVIDORDEMAPAS@IDU.GOV.CO o mediante una reunión programada con la Dirección Técnica Estratégica DTE. La información referente al sistema de coordenadas utilizada en la BDG es la siguiente: SISTEMA DE COORDENADAS SISTEMA DE COORDENADAS GEOGRÁFICO PROYECTADO Nombre CGS_CartMAGBOG Nombre PCS_CartMAGBOG Datum CGS_CartMAGBOG Proyección Transversa Mercator Elipsoide GRS80 modificado F Falso norte 109 320,965 Semieje mayor 6378388 + 2550 = Falso oeste 92 334,879 (6380938) Semieje menor 6359293,764 Meridiano Central -74,14659167 Achatamiento (1/f) 298,2572221
- **GU-IC-06 §7.1.1 ¶6** — Meridiano de referencia Greenwich Latitud de referencia 4,680486111 Longitud 0º 0’ 0’’ Factor de escala 1 Unidad angular Grado Unidad lineal Metro Radianes por unidad 0,01745329 Metros por unidad 1 Tabla 2. Parámetros del Sistema de Referencia de la BDG
#### §7.1.2 CARPETA FORMATOSDWG

- **GU-IC-06 §7.1.2 ¶1** — ARCHIVOS DESCRIPCIÓN Archivo en formato .dwg, que contiene los rótulos de los planos en el LayerFormato formato IDU, así como la nomenclatura de los elementos (intervenidos) en IDU.dwg los nombres de los layers. Este archivo es un complemento del archivo Productos_DWG.xlsx. La hoja LAYERCAD contiene la definición de los elementos a representar, los nombres de los layers a emplear, el tipo de geometría de cada layer que deberán ser utilizados en los archivos .DWG. Está identificada con color . La hoja NUEVOSLAYERS es la hoja donde se deben documentar todos los nuevos layers empleados, para la representación de los elementos objeto del contrato y que no están contemplados en la hoja
- **GU-IC-06 §7.1.2 ¶2** — Productos_ DescripcionLayers. La hoja INSTRUCTIVO_NUEVOSLAYERS señala DWG .xlsx como debe ser diligenciada. Están identificadas con color . La hoja LAYOUT_CIV relaciona los archivos DWG, con los códigos CIV representados en cada uno de los layouts. La hoja INSTRUCTIVO_LAYOUT_CIV señala como debe ser diligenciada. Están identificadas con color . Las hojas con los prefijos Elementos contienen algunos de los elementos y parámetros mínimos a incorporar en los planos DWG. Están identificadas con color . La hoja ConfiguracionCapaEstructura permite incorporar la información de capas y ensayos para los materiales instalados en la ejecución del
- **GU-IC-06 §7.1.2 ¶3** — proyecto. Se debe duplicar o crear un NUEVO ARCHIVO si en el proyecto se tiene más de un tipo de estructura en las calzadas o losas. Está identificada con color . La hoja RelacionElementoConfiguración se utiliza cuando se presenta Configuracion más de un tipo de configuración de estructura del pavimento instalado; es decir, se necesita más de un ARCHIVO ConfiguracionCapaEstructura CapaEstructur a.xlsx para representar la totalidad de las estructuras instaladas y diseñadas, en esta se debe relacionar el código de elemento (PK_ID_Calzada y/o PK_ID_losa), CIV y cual ARCHIVO ConfiguracionCapaEstructura se está relacionando. Esta identificada con color .
- **GU-IC-06 §7.1.2 ¶4** — La hoja GUÍA contiene las pautas para el diligenciamiento de la hoja ConfiguracionCapaEstructura con respecto a los ensayos realizados en las múltiples capas de la estructura de las calzadas y losas. La hoja Bloque Rotulo, contiene la explicación completa del ROTULO.xlsm diligenciamiento de los elementos requeridos en el rotulo. Tabla 3 Contenido Carpeta Formatos DWG La dimensión para los formatos de presentación de planos digitales es la siguiente: LayerFormatosIDU.dwg (1,00 m. X 0,70 m.) Los layers incorporados en el archivo LayerFormatosIDU.dwg están nombrados y organizados por filtros con la misma estructura de la BDG como se muestra en la Figura 3.
- **GU-IC-06 §7.1.2 ¶5** — Figura 3 Estructura de layers en los archivos .dwg
#### §7.1.3 CARPETA GUÍAS

- **GU-IC-06 §7.1.3 ¶1** — Es la Carpeta que contiene las guías, manuales, instructivos para la estandarización de la información: NOMBRE ARCHIVO DESCRIPCIÓN GUIC06_GUIA_ENTREGA_P Describe los estándares y parámetros para la presentación de RODUCTOS_FORMATO_DIG productos digitales finales en el desarrollo de proyectos en la ITAL infraestructura de los Sistemas de Movilidad y Espacio Público del Distrito Capital. GUIC07_ELABORACION_DE Requerimientos técnicos para la realización de los estudios _ESTUDIOS_TOPOGRAFICO topográficos requeridos en proyectos realizados en la S infraestructura de los sistemas de movilidad. Tabla 4 Contenido Carpeta Guías
- **GU-IC-06 §7.1.3 ¶2** — Las anteriores guías hacen referencia a los documentos internos que se deberán tener en cuenta en el proceso para cualquier tipo de contrato, siendo la guía directriz la GU-IC-06 versión 2.0 las demás componentes y especialidades. Dentro de los documentos del alistamiento también se podrán encontrar de acuerdo al tipo de contrato que esté desarrollando los siguientes documentos de propiedad del Instituto los cuales darán las pautas para la realización de los productos relacionados con el contrato: ETAPA NOMBRE ARCHIVO DESCRIPCIÓN Productos (entregables) de los GU-FP-01 ALCANCE PREFACTIBILIDAD componentes de la etapa de ENTREGABLES PREFACTIBILIDAD prefactibilidad.
- **GU-IC-06 §7.1.3 ¶3** — Productos (entregables) de los GU-FP-03 ALCANCE DE LOS FACTIBILIDAD componentes de la ENTREGABLES DE FACTIBILIDAD Etapa de factibilidad. GUDP01_GUÍA "ALCANCE DE LOS Productos (entregables) de los ENTREGABLES EN LA ETAPA DE componentes de la etapa de estudios DISEÑO y diseños. DISEÑO Resume la metodología y propone GU-IC-019 GUÍA “DISEÑO DE alternativas de diseño de estructuras PAVIMENTOS PARA BAJOS de pavimentos flexibles, rígidos y VOLÚMENES DE TRÁNSITO Y VÍAS articulados para vías locales con bajos LOCALES PARA BOGOTÁ D.C.” niveles de tránsito en Bogotá. MGGI01_MANUAL “INTERVENCIÓN DE Establece los lineamientos generales URBANIZADORES Y/O para la participación del Instituto en la
- **GU-IC-06 §7.1.3 ¶4** — TERCEROS” formulación de los instrumentos de EJECUCIÓN DE PROYECTOS DE planeación y el acompañamiento RECORD INFRAESTRUCTURA VIAL Y DE técnico para la entrega y recibo de los TERCEROS ESPACIO PÚBLICO EN EL proyectos de infraestructura vial y del DISTRITO CAPITAL EN espacio público realizados por CUMPLIMIENTO DE Urbanizadores y/o Terceros OBLIGACIONES URBANÍSTICAS Y particulares o públicos. DE MOVILIDAD ETAPA NOMBRE ARCHIVO DESCRIPCIÓN GU-IC-08 DIAGNOSTICO BASICO Guía para la ejecución de las ESPACIO PUBLICO E INVENTARIO actividades de diagnóstico que se ELEMENTOS PARA LA deben realizar para determinar el ACCESIBILIDAD estado del espacio público. GU-IC-01 GUÍA "TOMA DE
- **GU-IC-06 §7.1.3 ¶5** — DIAGNÓSTICO INFORMACIÓN TÉCNICA DE INVENTARIO, DIAGNOSTICO Y y controles de la toma de información ENSAYOS, para los elementos necesarios en las PARA LA GESTION DE LA actividades de inventario, diagnóstico INFRAESTRUCTURA VIAL Y, y ensayo. ESPACIO PUBLICO DE BOGOTA D.C" Tabla 5 Documentos adicionales de propiedad del IDU Además de las guías anteriores, se deberá tener en cuenta el manual MGGC01_MANUAL_INTERVENTORIA_Y_O_SUPERVISION_DE_CONTRATOS, los requerimientos realizados por la supervisión del contrato en el IDU, la interventoría y los anexos técnicos separables del contrato IDU. La norma técnica sobre la cual está estructurada la BDG y los archivos anexos es la IDU-ET-2011
- **GU-IC-06 §7.1.3 ¶6** — Versión 3.0, las Normas de Ensayo de Materiales para Carreteras del Instituto Nacional de Vías – INVIAS 2013, la Norma Técnica Colombiana – NTC y de ser necesario la Normativa Internacional. Los documentos anteriormente señalados podrán cambiar de acuerdo a la vigencia de los mismos al momento de la solicitud del alistamiento de la información.
#### §7.1.4 CARPETA ESTRUCTURA DE PRESENTACIÓN

- **GU-IC-06 §7.1.4 ¶1** — Es la carpeta en la cual el consultor organizará la totalidad de la información estandarizada para la entrega ante el IDU, de acuerdo a la etapa del contrato que esté presentando. Existen 7 carpetas dependiendo de la etapa del contrato a presentar:  PreFactibilidad  Factibilidad  Diseño  RecordConstruccion  RecordTerceros  Diagnostico  RecordConservacion Cada etapa sujeta a estandarización, está estipulada en el contrato, el anexo técnico separable y apéndices, estas deberán ser entregadas de manera independiente y radicadas de forma oficial al IDU. La forma de organizar e incorporar los productos finales, en cada una de las carpetas, se encuentra en
- **GU-IC-06 §7.1.4 ¶2** — el archivo Excel EstructuraCarpetas.xlsx; para cada etapa del contrato existe una hoja de cálculo con el nombre de la etapa que se requiere entregar, en la que se especifica el lugar y orden en el cual se deben presentar los archivos estandarizados. Se deberá contar con la aceptación del estándar por la DTE para cada una de las etapas, para el proceso de liquidación del contrato.
#### §8 PRODUCTOS ENTREGABLES PARA TODOS LOS PROYECTOS

- **GU-IC-06 §8 ¶1** — Después de describir la información del alistamiento a continuación se relacionan los productos finales entregables generales, para todos los tipos de contratos y etapas. Los elementos representados tanto en los archivos .dwg como en la BDG deberán corresponder a las geometrías de: punto, línea, polígono o bloque, contenidos en layers (Capas) para productos en formato .dwg y para la BDG en el Feature Class (Clase de entidad). Las geometrías están descritas en el archivo Excel Productos_DWG.xlsx en la hoja de cálculo LAYERCAD y en el archivo Excel Productos_BDG.xlsx en la hoja de cálculo CATALOGO_BDG, archivos suministrados en la información del alistamiento.
- **GU-IC-06 §8 ¶2** — El proceso de estandarización podrá ser realizado conforme a la comodidad del contratista, urbanizador o tercero sin embargo en proyectos que comprenden las etapas de Diseño o Ejecución de Obra se recomienda partir desde los archivos en formato .dwg como base para la generación de la BDG, mientras que para proyectos que no modificaran la geometría de los elementos es pertinente partir desde los elementos remitidos en la BDG por parte del IDU, y finalizar con productos en formato .DWG. La versión de los archivos remitidos por el IDU, será la vigente al momento de la solicitud de la información del alistamiento para la estandarización de los productos. Estos aplicaran para la entrega
- **GU-IC-06 §8 ¶3** — al IDU durante todo el desarrollo del proyecto, por lo cual es necesario realizar la entrega de la información sobre la versión de los documentos enviados. (Ver NOTA 2). Las etapas de los proyectos desarrolladas por cualquiera de las dependencias del IDU, también deberán ser entregadas a la DTE, obedeciendo a los parámetros de la presente guía. Los productos estandarizados corresponderán a 4 grupos: 1. Archivos en formato .dwg 2. Reporte en los archivos Excel 3. Base de Datos Geográfica (No aplica para Prefactibilidad y Factibilidad) 4. Estructura de Carpetas 8.1 ARCHIVOS EN FORMATO .DWG El archivo LayerFormatosIDU.dwg cuenta con múltiples layouts dependiendo de la etapa del contrato
- **GU-IC-06 §8 ¶4** — o entidad que entrega la información como se muestra en la Figura 4, de acuerdo con esto, el contratista elegirá el layout de su etapa o temática y eliminará los layouts que no se utilicen. Figura 4 Layouts del archivo LayerFormatosIDU.dwg Los layers a utilizar para la representación de los componentes del proyecto, se encuentran incorporados en el archivo y también podrán ser consultados en el archivo Excel Productos_DWG.xlsx en la hoja de cálculo LAYERCAD identificada con color . Se deberá respetar el tipo de geometría empleado, grosor, color, filtro y el nombre que está especificado. Los layers están nombrados
- **GU-IC-06 §8 ¶5** — y organizados por filtros con la misma estructura de la BDG como se muestra en la Figura 3, aquellos layers que no se utilicen deberán ser eliminados. Según la etapa del contrato a presentar, se debe incluir el sufijo en el nombre del layer, de acuerdo al archivo Excel Productos_DWG.xlsx en la hoja de cálculo LAYERCAD, con un guion al piso y el sufijo (D) Diseñados, (E) Existentes, (C) Construidos, por ejemplo, el elemento ANDEN podrá ser nombrado según la necesidad de las siguientes formas: ANDEN_E ANDEN_C ANDEN_D En caso de que el consultor no encuentre un layer para representar los elementos, podrá crear tantos
- **GU-IC-06 §8 ¶6** — layers como necesite para la representación de los elementos, utilizando nombres de fácil comprensión e incorporarlos en el filtro NUEVOSLAYERS. Estos layers deberán estar relacionados en la hoja de cálculo NUEVOSLAYERS identificada con color , la forma de diligenciarla está en la hoja de cálculo INSTRUCTIVO_NUEVOSLAYERS del mismo archivo. Para la estandarización de los planos en planta, se debe incorporar la información principal de todos los elementos señalados en la hoja de cálculo LAYERCAD del archivo Excel Productos_DWG.xlsx y que fueron empleados en el desarrollo del proyecto, en un archivo Base en
- **GU-IC-06 §8 ¶7** — formato .dwg que se usará como referencia externa en todos los planos en planta presentados para cada componente. Esta información se presentará en el Model Space (plataforma de dibujo) y debe encontrarse georreferenciada con UCS World, unidades de dibujo en metros y precisión de 3 decimales. La información correspondiente a textos, grilla de coordenadas, entre otros elementos que no se encuentran definidos en los archivos suministrados en el alistamiento, se deben incorporar en diferentes layers y ser nombrados de una manera fácilmente identificable dentro del grupo Rotulo. 8.1.1 Archivo BASE.DWG Este archivo debe cumplir con los siguientes requerimientos:
- **GU-IC-06 §8 ¶8** — 1. Contener únicamente los elementos de competencia del IDU, con su respectiva geometría relacionada en los archivos de Productos_DWG.xlsx. en la hoja de cálculo LAYERCAD y en el archivo LayerFormatosIDU.dwg. 2. Mantener la estructura de los layers enviada en el archivo LayerFormatosIDU.dwg. 3. Crear un filtro de clasificación para los elementos que no hacen parte del contrato o los elementos existentes, según al tipo de contrato (conservación, diseño, diagnóstico y construcción). La forma de nombrar los archivos BASE para contratos IDU será BASE-WWW-IDU-XXX-YYYY.dwg:  Las letras WWW hacen referencia al número consecutivo del archivo Base, en caso de usar más de uno.
- **GU-IC-06 §8 ¶9** —  Las letras XXX hacen referencia al número del contrato.  Las letras YYYY al año del contrato. Por ejemplo, BASE-01-IDU-5-2014. En el caso de proyectos de terceros y/o urbanizadores el archivo debe llamarse BASE-WWW-IDU-URB-ZZZ.dwg las letras ZZZ hacen referencia al nombre del urbanismo otorgado por la DTAI, por ejemplo BASE-7-IDU-URB-FELICIDAD.dwg. Este archivo debe ser utilizado como referencia externa (xref) para la presentación de todos los temas a entregar en vista de planta, para cada una de las etapas del proyecto, las demás referencias externas deben estar nombradas de igual forma, de acuerdo a la funcionalidad de la referencia (achurado, texto, bloques). Achurados (Hatch)
- **GU-IC-06 §8 ¶10** — Para la representación de los achurados se podrán generar tantos archivos como sean necesarios y se deberán utilizar en los demás productos como referencias externas para incorporarlos en los componentes de los planos a presentar. El nombre de los layers y hatch será el de la representación de los materiales de superficie utilizados en la ejecución de la etapa que este presentando. Referencia Externa La referencia externa es una ruta que existe como un enlace dentro de un archivo .dwg la cual relaciona otros archivos dentro del model y los layout existentes en este. Se utiliza para complementar la
- **GU-IC-06 §8 ¶11** — información que aparece en otros archivos y que es necesaria para la presentación del plano o de la base a entregar. Al guardar las referencias externas, estas deben quedar enlazadas a la ruta relativa (Relative path) para su despliegue en otros equipos computacionales, como se muestra en la Figura 5. Figura 5 Ventana de referencia externa en AutoCad 8.1.2 Temáticas entregables en formato .dwg Junto con los archivos Base que contienen los elementos IDU, achurados y bloques se deberán entregar los planos que complementen la información en formato .dwg con su respectiva nomenclatura de plano por cada temática (según el alcance del proyecto), con el rotulo establecido y la información
- **GU-IC-06 §8 ¶12** — asociada solicitada por componente para cada plano. Estos deben cumplir con los parámetros señalados en el archivo Excel Productos_DWG.xlsx, en las hojas de cálculo que tienen los siguientes nombres, según la etapa que se presentara: ElementosPrefactibilidad ElemetosFactibilidad ElementosDiseño ElementosConstruccion ElementosDiagnostico ElementosConservacion ElementosConstruccionUrbanizadores Y que se identifican mediante el color , también deberá cumplir con los productos señalados en los apéndices, anexos técnicos separables del contrato de obra y del contrato de interventoría, los señalados en las guías de productos entregables de prefactibilidad, factibilidad, diseños, y los demás
- **GU-IC-06 §8 ¶13** — que sean requeridos tanto por la interventoría como por la supervisión del contrato. Después de contar con la información estandarizada en los respectivos espacios del MODEL, se deben generar las respectivas salidas gráficas de los planos en los Layout (espacio papel) conteniendo únicamente un plano por cada layout, el cual presentará sus unidades de dibujo en metros los layouts serán nombrados con el mismo nombre empleado en el rotulo en el espacio PLANCHA No. del archivo Excel ROTULO.xlsm. Un archivo podrá contener tantos layouts como planos presentados y podrá representar tantos elementos le sean posibles teniendo en cuenta las escalas especificadas en el archivo ROTULO.xlsm
- **GU-IC-06 §8 ¶14** — en el cuadro ESCALA. Se deberá generar un archivo PDF que se incluirá en la misma carpeta del respectivo tema, con el nombre del layout, los archivos PDF deberán estar firmados con la firma digital vigente de los profesionales señalados en el rotulo. Los productos en formato .dwg comprenderán la totalidad de los productos para cualquier vista. Todos los elementos en PLANTA representados en los archivos dwg entregados, deberán corresponder a las geometrías punto, línea, polígono o bloque, en los layers (Capas) descritos en el archivo Productos_DWG.xlsx en la hoja de cálculo LayerCAD identificada con color . Cada
- **GU-IC-06 §8 ¶15** — representación en planta que se haga es la correspondiente al detalle de los elementos diseñados, diagnosticados o construidos como se muestra en la Figura 6. Deberán estar identificados plenamente señalando la nomenclatura vial, código CIV, e identificador PK correspondiente al empleado en la BDG. Figura 6 (A) Fotografía Obras ejecutadas en la Calle 156 con Carrera 96,(B) Representación de productos en formato .dwg Vista de planta.
#### §8.1.3 DESCRIPCIÓN DEL ROTULO DE LOS PLANOS

- **GU-IC-06 §8.1.3** — Las instrucciones para diligenciar el rotulo podrán ser consultadas en el archivo Excel ROTULO.xlsm.
#### §8.1.4 PRODUCTOS DE LAS EMPRESAS DE SERVICIOS PÚBLICOS Y ENTIDADES DISTRITALES

- **GU-IC-06 §8.1.4 ¶1** — Los productos avalados por las entidades públicas se deben presentar en los formatos .dwg y .pdf, entre estos están:  Empresa de Servicios Públicos  Inventario Silvicultural (Jardín Botánico de Bogotá)  Señalización (Secretaria Distrital de Movilidad)  Y aquellos requeridos de manera contractual en el contrato en los anexos técnicos separables, apéndices y capítulos del contrato de consultoría e interventoría. Estos deberán estar incluidos en la estructura de carpetas suministrada por el IDU en la información del alistamiento, bajo el estándar de la respectiva entidad competente en cada temática.
- **GU-IC-06 §8.1.4 ¶2** — Para los proyectos de urbanizadores o terceros se deberán incluir los planos de la Curaduría Urbana en formato .dwg y .pdf.
#### §8.2 REPORTE EN ARCHIVOS EXCEL

- **GU-IC-06 §8.2 ¶1** — La ejecución de los proyectos en las etapas de (Diseño, Ejecución, Diagnostico, Conservación) generará como producto obligatorio la entrega de los siguientes productos en formato Excel:  Productos_BDG.xlsx, según los elementos intervenidos en las hojas de cálculo identificadas con color .  FOIC09_REPORTE_FINAL_META_FISICA.xlsx  Productos_DWG.xlsx hoja de cálculo LAYOUT_CIV.xlsx identificada con color Para proyectos que ejecuten intervención en los elementos de Calzada y/o Losas en las etapas de Diseños y Construcción:  ConfiguracionCapaEstructura.xlsx Para proyectos que empleen layers que no se encuentren mencionados en el archivo Excel Productos_DWG.xlsx en la hoja de cálculo LAYERCAD:
- **GU-IC-06 §8.2 ¶2** —  Productos_DWG.xlsx hoja de cálculo NUEVOSLAYERS identificada con color . 8.2.1 Productos_BDG.xlsx Archivo que contiene el Diccionario de Atributos de los elementos representados en la BDG separados por hojas de cálculo identificadas en color azul oscuro . Este archivo deberá estar diligenciado por el consultor y la interventoría, y cuenta como una lista de chequeo de los atributos que deben estar diligenciados en la BDG (ver NOTA 1). La entrega del documento diligenciado, representa la aprobación por parte de la interventoría de la información incorporada en la BDG. Por cada etapa que conforma el proyecto, se debe efectuar la entrega de una BDG (no aplica para
- **GU-IC-06 §8.2 ¶3** — Prefactibilidad y Factibilidad), junto con el archivo en formato Excel Productos_BDG.xlsx debidamente diligenciado en las hojas de cálculo color azul oscuro que le correspondan según el contrato. Este archivo contiene la descripción de los campos y dominios de cada elemento presente en la BDG, los atributos mínimos a ser entregados por cada etapa separadas en las columnas, estarán identificados con una X en color rojo. Este archivo se deberá entregar para cada una de las etapas del proyecto. Las columnas llamadas contratista e interventoría deberán ser diligenciadas de la siguiente manera: Contratista: En este campo, se deberá diligenciar con una X, cada atributo que está entregando el
- **GU-IC-06 §8.2 ¶4** — actor de infraestructura, en el marco del alcance del proyecto en cuestión. Interventoría: Al igual que en el campo anterior, la interventoría validará con una X, la información diligenciada en el campo “Contratista”. La validación respecto a los ensayos y estudios a incorporar en la BDG deberá ser validada por la interventoría y la supervisión del contrato mediante la evaluación del archivo Excel Productos_BDG.xlsx en las hojas de cálculo de color azul oscuro . Los estudios y ensayos no incorporados o presentados en la información estandarizada deberán ser plenamente justificados de manera técnica y
- **GU-IC-06 §8.2 ¶5** — contractual por el contratista ante la interventoría quien realizará el aval de dicha justificación mediante una respuesta oficial. Posteriormente, el supervisor del contrato validará la pertinencia de la justificación previo al envío de la información estandarizada a la DTE. NOTA 1: El archivo entregado contendrá exclusivamente las hojas de cálculo de color azul oscuro , con los elementos que se intervinieron en el contrato, eliminando el resto de las hojas. 8.2.2 FOIC09_REPORTE_FINAL_META_FISICA.xlsx Es el formato Excel de reporte final, en donde se deberá detallar la meta física final de cada etapa del proyecto. Se realizará una entrega de archivo por cada etapa que contemple el proyecto
- **GU-IC-06 §8.2 ¶6** — Ésta información debe ser revisada y aprobada por la interventoría y validada por el área supervisora del contrato, deberá contener la meta física que será validada por la DTE de acuerdo a la información entregada en los demás productos. 8.2.3 Productos_DWG.xlsx En la hoja de cálculo LAYOUT_CIV, se deben relacionar los códigos CIV con cada uno de los layouts. En la hoja de cálculo NUEVOSLAYERS, se especificaran los layers empleados en la presentación de los planos .dwg que no fueron previamente entregados en el alistamiento por la DTE, pero que son necesarios para la representación de la información por parte del contratista. 8.2.4 ConfiguracionCapaEstructura.xlsx
- **GU-IC-06 §8.2 ¶7** — Archivo(s) Excel que contiene la estructura(s) instalada(s) o diseñada(s) de los elementos calzada y losa, junto con los resultados de los ensayos de laboratorio, de las distintas capas de la estructura empleada. Deberá estar acompañado de los respectivos soportes de las pruebas y ensayos de laboratorio, contemplados contractualmente, en sus apéndices, anexos técnicos separables, instructivos, guías afines y los que sean realizados por el contratista o la interventoría, que serán incorporados en la misma carpeta donde se encuentre el archivo ConfiguracionCapaEstructura.xlsx.
#### §8.3 BASE DE DATOS GEOGRÁFICA

- **GU-IC-06 §8.3 ¶1** — Se entregará una BDG por cada etapa del contrato, los elementos representados en la BDG deberán corresponder a la geometría de: punto, línea o polígono; representándolos en los Feature Class (Clase de entidad), suministrados al inicio del proyecto en la información del alistamiento, simbolizando únicamente los contornos de los elementos, como se muestra en la figura 7. La BDG se encuentra estructurada de tal forma, que una vez se encuentre representado el elemento geográficamente se debe proceder al diligenciamiento de la información solicitada tanto en el elemento, como en las tablas relacionadas según lo señalado en el archivo Excel Productos_BDG.xlsx, en las
- **GU-IC-06 §8.3 ¶2** — hojas de cálculo de color azul oscuro dependiendo del elemento se podrá seleccionar la respectiva hoja de cálculo. Los valores de los estudios y los ensayos a incorporar en la BDG, deben provenir de los realizados durante el contrato por el contratista o por la interventoría, esto aplica para cualquiera de las etapas del contrato. Además, se deberán adjuntar los respectivos soportes de los estudios o los ensayos entregados en su formato origen y .pdf. Las geometrías entregadas en la información estandarizada de la BDG, deben provenir de los estudios topográficos. En los casos en que los proyectos NO CONTEMPLEN estudios topográficos, las
- **GU-IC-06 §8.3 ¶3** — geometrías de los elementos suministrados en la BDG, no deberán ser modificadas a menos de que sea necesario, con el fin de que el elemento represente completamente la realidad. Por consiguiente; solo debe ser incorporada la información atributiva solicitada para cada elemento. A Figura 7 (A) Fotografía Obras ejecutadas en la Calle 156 con Carrera 96, (B) Representación de productos en la BD Feature class (ELEMENTO) ÁREA DE INTERVENCIÓN En el caso de realizar una actividad parcial sobre un elemento determinado, este además deberá ser clasificado en el FeatureClass (elemento) “ÁreaIntervencion” del DataSet (Conjunto)
- **GU-IC-06 §8.3 ¶4** — IntervencionInfraestructuraVial, lo anterior con, el fin de representar el área real intervenida. Cuando se cuente con información de toma de ensayos se deberá además representar el elemento completo que se está interviniendo; esto con el fin de delimitar el área real intervenida e incorporar los atributos de ensayos y estudios solicitados.
#### §8.4 ESTRUCTURA DE CARPETAS

- **GU-IC-06 §8.4 ¶1** — Conforme a la estructura de carpetas suministradas, se deberá incorporar la totalidad de la información estandarizada, incluyendo todos los soportes de los estudios y los ensayos realizados en cualquiera de las etapas del proyecto, aun cuando estos no sean de obligatoria incorporación en la BDG. El actor de infraestructura deberá presentar los archivos digitales producto del desarrollo del proyecto, en su respectiva carpeta de acuerdo al archivo Excel EstructuraCarpetas.xlsx. Así mismo, se debe depurar (borrar) todas aquellas carpetas en las cuales no se cuenta con información, sin realizar ninguna modificación en el nombre de las restantes. Cada carpeta deberá contener el formato de origen
- **GU-IC-06 §8.4 ¶2** — (Word, Excel, AutoCAD, JPG, entre otros) y a su vez el archivo en formato .PDF. La carpeta principal de cada proyecto deberá identificarse con el código completo del contrato o nombre del urbanismo (según la resolución de urbanismo). Si por la magnitud del proyecto es necesario dividir el alcance del contrato en tramos, cada tramo se deberá entregar con todos los componentes en una estructura de carpeta independiente. En este caso se deberá nombrar la carpeta con la palabra Tramo y un consecutivo según el número de carpetas que se entreguen. Los tramos deberán venir debidamente identificados por CIV en el formato FOIC09_REPORTE_FINAL_META_FISICA.xlsx en el campo OBJETO DEL PROYECTO O
- **GU-IC-06 §8.4 ¶3** — CONTRATO (un formato para cada tramo). La división de los tramos será avalada por la interventoría y la supervisión del contrato IDU; en el memorando de remisión a la DTE se deberá especificar el CIV de inicio y de fin para cada uno de los tramos. Los nombres de los archivos deberán describir la estructura del documento de tal forma que se identifique con claridad capítulos, anexos, cuadros, tablas, entre otros. Los cuadros y las tablas deberán estar nombrados con el consecutivo que los identifica y permitir su ubicación dentro del contenido del documento. NOTA 2: Los documentos y los formatos relacionados en la presente guía, deben corresponder a
- **GU-IC-06 §8.4 ¶4** — los productos obtenidos durante la ejecución del contrato en cualquiera de sus etapas; y deberán estar estandarizados conforme con las versiones oficiales remitidas en los archivos de ALISTAMIENTO, específicamente para cada contrato y/o proyecto, o aquellos que los reemplacen. En caso de que transcurridos 2 meses, posteriores, a la terminación de cualquier etapa del contrato y no se haya entregado y radicado oficialmente la información estandarizada de los productos digitales, el contratista o tercero deberá solicitar nuevamente, las versiones vigentes, para el alistamiento de la información, a la fecha de la nueva solicitud.
- **GU-IC-06 §8.4 ¶5** — Así mismo, después de realizar una radicación oficial que cuente con una devolución formal por parte del IDU, el contratista o tercero contará con un plazo máximo de 3 meses para realizar una nueva radicación. En caso de que no se realice, se deberá: 1. Solicitar nuevamente la información del alistamiento con las versiones vigentes a la fecha. 2. Ajustar la información antes de realizar la nueva radicación de la información.
#### §8.4.1 REGISTROS FOTOGRÁFICOS

- **GU-IC-06 §8.4.1 ¶1** — En esta carpeta se deberá anexar el registro fotográfico, relacionado con la etapa entregada. Los registros fotográficos se deberán agrupar por código de identificación vial (CIV), en las carpetas: Antes, Durante y Después. Se deberá crear una carpeta por cada CIV intervenido, donde se incluirá el registro fotográfico, que detalle los elementos, que hacen parte de la ejecución del CIV. La estructura de las carpetas es la presentada en la Figura 8. Figura 8 Esquema de presentación de Registros Fotográficos. Para cada etapa entregada, se presentará un registro fotográfico, en el caso de las etapas de diseño y diagnóstico, se presentará el registro fotográfico en la carpeta “Antes”.
- **GU-IC-06 §8.4.1 ¶2** — La toma de los registros fotográficos deberá ser descriptiva con respecto a los elementos que se intervinieron y hacen parte de la entrega al IDU, estos deberán ser tomados en sentido del avance de la nomenclatura, sin importar el número de imágenes que se deban anexar; para lograr el detalle solicitado. Adicionalmente, se deberán crear archivos en formato KMZ para cada tiempo del contrato (antes, durante y después) donde se deben asociar las imágenes a la ubicación espacial a la que pertenecen.
#### §8.4.2 CARPETA VIDEOS

- **GU-IC-06 §8.4.2** — Los videos en su parte inicial, deben aclarar la duración, la ubicación geográfica, fecha de realización de la grabación y demás datos descriptivos que se consideren necesarios para su identificación. NOTA 3: Se recomienda realizar el proceso de quemado de información en CD’s o DVD’s de lectura, no utilizar la opción de copiar, pegar o arrastre de carpetas, esto puede ocasionar perdida de la información.
#### §8.5 ESPECIFICACIONES TÉCNICAS DE LOS ARCHIVOS PDF Y EDITABLES

- **GU-IC-06 §8.5** — Estas especificaciones se deberán tener en cuenta para todos los archivos entregables descritos en este documento, en cada una de las Etapas.
#### §8.5.1 ARCHIVOS PDF

- **GU-IC-06 §8.5.1 ¶1** —  El peso de los archivos debe ser máximo de 500 MB. En la medida en que avance la tecnología este parámetro se irá ajustando.  Debe contener las firmas digitales de las personas que intervinieron en la validación, revisión y aprobación del documento, en la hoja de control de versiones.  Deben ser compatibles con PDF/A de conservación a largo plazo.  No deben permitir su modificación o copiar el texto, pero sí permitir su impresión.  Para los casos en los cuales se incluyan imágenes digitalizadas, debe ser a 300 DPI, tener reconocimiento óptico de caracteres OCR de tal manera que se puedan realizar búsquedas de
- **GU-IC-06 §8.5.1 ¶2** — texto dentro de los archivos, tener la misma orientación del texto digital y no incluir hojas en blanco.  Deben tener la marca de agua estándar (definida por el IDU) en todas las páginas excepto donde haya imágenes como: gráficas, fotos, cuadros, ente otras. Ésta es remitida en los archivos del alistamiento en la carpeta GUÍAS. Figura 9 Marca de agua.
#### §8.5.2 ARCHIVOS EDITABLES

- **GU-IC-06 §8.5.2 ¶1** —  El peso de los archivos debe ser máximo de 500 MB. En la medida en que avance la tecnología este parámetro se irá ajustando.  Los archivos Excel, gráficas y otro tipo de documentos como cuadros deben contener las fórmulas completas, con una escala definida para impresión, de manera que no se corte el texto o el cuadro. Los documentos que no son propiedad intelectual del Instituto (Ley 23 de 1982 sobre derechos de autor) pero hacen parte del documento original, deben ser entregados en los archivos de origen y excluidos de los PDF. Ejemplo: partes completas de libros, manuales, planos elaborados por otras entidades, entre otros.
- **GU-IC-06 §8.5.2 ¶2** — Así mismo y en cumplimiento a la Ley 1266 de 2008, Habeas Data, las copias de los documentos de identidad, hojas de vida, diplomas, soportes de hojas de vida, anexos a la hoja de vida, constancias laborales y otros documentos que contengan información de una persona, no pueden ser liberados en el Repositorio Institucional. Por lo anterior, deben ser entregados en los archivos de origen y excluidos de los PDF.
#### §9 PRODUCTOS ESPECÍFICOS ENTREGABLES POR ETAPA

- **GU-IC-06 §9** — En el siguiente capítulo, se referencia la información específica a entregar para cada una de las etapas que contemple el alcance del proyecto, teniendo en cuenta que cada etapa requiere información específica.
#### §9.1 PREFACTIBILIDAD

- **GU-IC-06 §9.1 ¶1** — Los productos entregables se describen en la guía GU-FP-01 “ALCANCE_ENTREGABLES_PREFACTIBILIDAD” o el documento vigente que haga sus veces al momento de la solicitud de la información de alistamiento. Cada uno de los productos entregables deberá cumplir con los parámetros mínimos establecidos en el archivo Excel Productos_DWG.xlsx en la hoja ElementosPreFactibilidad identificada con color , los solicitados en el contrato, en el anexo técnico separable, apéndices y capítulos del contrato de consultoría, construcción e interventoría y por la supervisión del contrato. En los productos en planta se deberán incluir layers con
- **GU-IC-06 §9.1 ¶2** — la geometría de polilineas cerradas que señalen las alternativas propuestas nombradas consecutivamente desde la Alternativa 1 hasta la Alternativa n, y deberán estar relacionados con la información de los soportes y anexos entregados. Las alternativas se deberán presentar en formato .dwg, shapefile, kmz.
#### §9.2 FACTIBILIDAD

- **GU-IC-06 §9.2 ¶1** — Los productos entregables se describen en la que haga sus veces al momento de la solicitud de la información de alistamiento. La estandarización de los productos se realizará para cada una de las alternativas propuestas en los archivos en formatos .dwg. Cada uno de los productos entregables deberá cumplir con los parámetros mínimos establecidos en el archivo Excel Productos_DWG.xlsx en la hoja ElementosFactibilidad identificada con color , los solicitados contractualmente en el anexo técnico separable, apéndices y capítulos del contrato de consultoría, construcción e interventoría y por la supervisión del contrato. En los productos
- **GU-IC-06 §9.2 ¶2** — en planta se deberá incluir un layers con la geometría de polilinea cerrada que señale la alternativa seleccionada y esta deberá estar relacionada con la información de los soportes y anexos entregados. La alternativa se deberá presentar en formato .dwg, shapefile, kmz.
#### §9.3 ESTUDIOS Y DISEÑOS, AJUSTES Y/O COMPLEMENTACIÓN A LOS DISEÑOS

- **GU-IC-06 §9.3 ¶1** — Los productos entregables corresponderán con los señalados en la guía: GU-DP- 01_GUIA_ALCANCE_ENTREGABLES_ETAPA_DISENO o la versión vigente al momento de solicitar la información de alistamiento. Cada uno de los productos deberá cumplir con los parámetros mínimos establecidos en el archivo Excel Productos_DWG.xlsx en la hoja ElementosDiseño identificada con color , los solicitados contractualmente en el anexo técnico separable, apéndices y capítulos del contrato de consultoría e interventoría y por la supervisión del contrato. (Ver NOTA 4). Se presentara una BDG del proyecto que contendrá todos los elementos e información diseñada y los
- **GU-IC-06 §9.3 ¶2** — estudios y ensayos tomados para el diseño realizado de acuerdo al archivo Productos_BDG.xlsx en las hojas de cálculo con color azul oscuro . NOTA 4: En caso de que el contrato contemple modificaciones, ajustes, complementaciones o actualizaciones a diseños preexistentes, todos los entregables son los mismos que los de un diseño nuevo. En dado caso deberá hacerse referencia a si se acogen o apropian, total o parcialmente a los diseños preexistentes, lo cual deberá estar contenido en la carpeta de informes con el visto bueno de la interventoría, esto incluye desde criterios técnicos, vigencia total o parcial de los estudios y ensayos realizados anteriormente, esto se relacionará en el
- **GU-IC-06 §9.3 ¶3** — memorando o radicado dirigido a la DTE. De lo anterior, en caso de que el contratista o consultor no se apropie de los diseños entregados y realicé sus propios estudios y ensayos, deberá presentar una entrega de la etapa de diseños además de la entrega de Construcción.
#### §9.4 RECORD CONSTRUCCIÓN (CONTRATOS IDU)

- **GU-IC-06 §9.4 ¶1** — Los productos entregables corresponderán con los señalados en el archivo Excel Productos_DWG.xlsx en la hoja ElementosConstruccion (Récord) identificada con color , los solicitados en el contrato, en el anexo técnico separable, apéndices y capítulos del contrato de consultoría e interventoría, por la supervisión del contrato, y en los casos que aplique, de construcción que afecten la etapa de estudios y diseños (Ver Nota 4). Para contratos donde no se contemplen estudios y diseños, la DTE suministrará la información base de los elementos que reposan en la BDG de seguimiento del IDU, con el fin de que sea incorporada
- **GU-IC-06 §9.4 ¶2** — toda la información obtenida a través del desarrollo de esta etapa, donde se realizarán los ajustes necesarios a los elementos de acuerdo a la ejecución. Los tramos testigo deberán ser informados por parte del supervisor del contrato adjuntando, el acta de reunión o la comunicación oficial donde se hayan definido los códigos CIV y PK (identificador del elemento) en el memorando dirigido a la DTE. La información producto de la ejecución de obra, los ensayos, el control de calidad realizado por el contratista o la interventoría, estarán acordes con las Especificaciones Técnicas Vigentes al momento de ejecución de la etapa del contrato, anexando los resultados de laboratorio en la información
- **GU-IC-06 §9.4 ¶3** — estandarizada. Para esta etapa se requiere del estudio topográfico y los planos viales y de espacio público de control de obras ejecutadas, respecto al diseño geométrico planteado, junto con la cartera de nivelación conjunta o la realizada por la interventoría.
#### §9.5 DIAGNÓSTICO

- **GU-IC-06 §9.5 ¶1** — Los productos entregables corresponderán con los señalados en el archivo Excel Productos_DWG.xlsx en la hoja ElementosDiagnostico identificada con color , los solicitados en el contrato, en el anexo técnico separable, por la supervisión del contrato, apéndices y capítulos del contrato de consultoría e interventoría, y en los casos que aplique, de construcción que afecten la etapa de estudios y diseños. (Ver NOTA 4). Teniendo en cuenta que el objetivo de esta etapa es diagnosticar elementos existentes, la DTE entregara en la información del alistamiento una BDG con la geometría de los elementos reservados
- **GU-IC-06 §9.5 ¶2** — para el diagnóstico; esto con el fin de que el contratista incluya la información correspondiente a los ensayos y los datos relacionados al diagnóstico, sin cambiar la geometría de los elementos. En caso de que dentro de la BDG falten elementos, se deberá solicitar de nuevo el alistamiento incluyendo el formato Excel de reporte FO-IC-02, diligenciado por el área supervisora, en donde deberán relacionarse los elementos incluidos en el contrato. Para la entrega de los productos en esta etapa, se deberán tener en cuenta los siguientes ítems:  Los archivos en formato .dwg en planta deberán mostrar los elementos objeto de diagnóstico,
- **GU-IC-06 §9.5 ¶3** — junto con la clasificación asignada del tipo de mantenimiento a realizar después del análisis de los datos. Por tal razón, los layers incluidos en el archivo base .dwg deberán corresponder únicamente a elementos existentes.  La BDG entregada al IDU deberá contener únicamente los elementos donde se realizó el diagnóstico, en caso de diagnosticar elementos que no fueron entregados en la BDG remitida por el IDU se deberá solicitar de nuevo el alistamiento incluyendo el formato Excel de reporte FO-IC-02, diligenciado por el área supervisora.  En esta etapa no es necesario realizar el levantamiento de las losas, pero si se debe asociar a
- **GU-IC-06 §9.5 ¶4** — las unidades de muestreo el número de losas que las componen. En caso de que dentro de la información entregada por el IDU se incluya el inventario de las losas, estas deben ser asociadas a la unidad de muestreo mediante la relación en la BDG.  En el elemento calzada, las evaluaciones que se entregan para todos los tipos de superficie son: la estructural y la superficial además de las señaladas contractualmente. En caso de existir algún tipo de aclaración técnica o contractual, esta debe quedar especificada en el archivo Productos_BDG.xlsx en las hojas de cálculo identificadas en color azul oscuro en la columna de observaciones, en donde la interventoría deberá especificar las comunicaciones
- **GU-IC-06 §9.5 ¶5** — oficiales que avalen las justificaciones.  La etapa de Diagnóstico o Preliminares no contempla topografía de los elementos diagnosticados; no obstante, en el caso de que los elementos no existan en la BDG, se asumirán como elementos nuevos, por ende, se debe realizar una georreferenciación espacial de los mismos.  El diagnóstico de puentes, se hará de acuerdo a los entregables de la Guía de Diagnóstico de Puentes vigente en el IDU o de acuerdo a lo estipulado en el anexo técnico separable del contrato.  Para definir la superficie de la calzada, en los elementos con superficies mixtas, se deberá tener
- **GU-IC-06 §9.5 ¶6** — en cuenta que para que se presente más de una (1) superficie, el área con la superficie menor debe corresponder a por lo menos una unidad de muestreo con las especificaciones de la metodología usada. En el caso contrario, se tomará como superficie del elemento la que predomine. Para las superficies mixtas que contengan losas, se deberá relacionar el número de losas en las unidades de muestreo correspondiente.  Los puntos de las evaluaciones que se deben presentar en esta etapa deben estar debidamente georreferenciados de acuerdo a los atributos de la BDG (abcisado, CoordenadasX y CoordenadasY) en cualquiera de los casos según la metodología empleada.
#### §9.6 RECORD CONSERVACIÓN

- **GU-IC-06 §9.6 ¶1** — Los productos entregables corresponderán con los señalados en el archivo Excel Productos_DWG.xlsx en la hoja ElementosConservacion identificada con color , los solicitados en el contrato, en el anexo técnico separable, apéndices y capítulos del contrato de consultoría e interventoría, y los anexos técnicos separables del contrato y por la supervisión del contrato (Ver Nota 4). La DTE suministrará la información del alistamiento de los elementos incluidos en el contrato, para que sea incorporada toda la información obtenida a través del desarrollo de esta etapa, por lo que no se debe efectuar modificación a los elementos suministrados, salvo si existe mejoramiento geométrico en
- **GU-IC-06 §9.6 ¶2** — consecuencia además se entregarán los productos de los estudios topográficos. Cuando los elementos intervenidos no se encuentren en la BDG, el área supervisora del proyecto a través de comunicación oficial, deberá efectuar la actualización en el archivo en formato Excel FO-IC-02, para actualizar la BDG. Para los tramos con tipo de intervención rehabilitación o reconstrucción que incluyan estudios y ensayos, deberán ser incluidos en la BDG únicamente los tomados después de la ejecución. En calzadas de acuerdo a las actividades que se realicen en la ejecución del contrato, el contratista deberá entregar al IDU la información asociada a los elementos intervenidos, teniendo en cuenta el tipo
- **GU-IC-06 §9.6 ¶3** — de mantenimiento:
#### §9.6.1 MANTENIMIENTO RUTINARIO

- **GU-IC-06 §9.6.1** — Para calzadas y losas, reparaciones puntuales en concreto flexible o rígido.
#### §9.6.2 MANTENIMIENTO PERIÓDICO

- **GU-IC-06 §9.6.2** —  Parcheos  Bacheos  Sobrecarpetas  Fresados estabilizados  Renivelaciones
#### §9.6.3 REHABILITACIÓN – RECONSTRUCCIÓN

- **GU-IC-06 §9.6.3** — Todos los tramos intervenidos con este tipo de mantenimiento deben presentarse en los planos estandarizados. Para los tramos con superficie rígida en los cuales se contemplen intervenciones de rehabilitación y reconstrucción, se deberá presentar el plano de losas con la modulación final. Los archivos en formato .dwg deberán presentar la intervención realizada. También se presentará la información de las secciones típicas con las estructuras y espesores instalados en la ejecución de la obra.
#### §9.7 URBANIZADORES O TERCEROS

- **GU-IC-06 §9.7 ¶1** — La información de productos estandarizados deberá ser entregada conforme a lo establecido en el Manual “INTERVENCIÓN DE URBANIZADORES Y/O TERCEROS”- EJECUCIÓN DE PROYECTOS DE INFRAESTRUCTURA VIAL Y DE ESPACIO PÚBLICO EN EL DISTRITO CAPITAL EN CUMPLIMIENTO DE OBLIGACIONES URBANÍSTICAS Y DE MOVILIDAD” o el documento vigente que haga sus veces al momento de la solicitud del alistamiento, así como lo contemplado en el archivos Excel Productos_DWG.xlsx, en la hoja ElementosConstruccionUrbanizado identificada con color , por la supervisión del contrato y lo contemplado en el documento del convenio o el documento vigente al momento de la solicitud de alistamiento.
- **GU-IC-06 §9.7 ¶2** — Para los proyectos de infraestructura vial y de espacio público en el marco del cumplimiento de obligaciones urbanísticas y de movilidad, derivados de instrumentos de planeación diferentes a las licencias urbanísticas, deberán entregar la información estandarizada para cada una de las etapas mencionadas anteriormente de acuerdo al tipo de intervención a realizar (Diagnostico, Diseño, Construcción). Para los proyectos, cuya intervención esté definida por licencias urbanísticas, estarán obligados a presentar la información de productos estandarizados únicamente para la etapa de ejecución de obra.
#### §9.8 ESTRUCTURAS

- **GU-IC-06 §9.8 ¶1** — Los productos entregables para contratos concernientes a estructuras especiales, como puentes, muros, entre otros, deberán corresponder a los productos solicitados en la metodología de diagnóstico de estructuras vigente, los parámetros exigidos en el archivo Excel Productos_DWG.xlsx, de acuerdo a la etapa a desarrollar, y los solicitados en el anexo técnico separable del contrato para la consultoría, construcción e interventoría; así como aquellos productos derivados por el consultor e interventor en el control del contrato y por la supervisión del contrato. Para los contratos de puentes se deberán presentar las intervenciones realizadas en los siguientes elementos:
- **GU-IC-06 §9.8 ¶2** —  Baranda  Viga  Losa de Aproximación  Barrera  Aleta Estribo  Pila  Cercha  Caisson  Pilote  Diafragma  Columna  Rampa Puente  GuardaRueda  Dado  Tablero  Junta de Dilatación  Estribo NOTA 5: En el memorando u oficio de radicación dirigido a la DTE, se informará por parte de la supervisión del contrato, los estudios y ensayos que están obligados a entregar los contratistas y están señalados en la BDG y en el archivo Excel Productos_BDG.xlsx para cada uno de los elementos que se entreguen. Los estudios y ensayos que no se presenten, deberán estar plenamente justificados de manera técnica y contractual, ante la interventoría,
- **GU-IC-06 §9.8 ¶3** — quien realizará la validación de dicha justificación, para generar posteriormente el aval por parte de la supervisión del contrato en el IDU.
#### §10 EVALUACIONES DE CALIDAD

- **GU-IC-06 §10 ¶1** — La información anexa a la radicación oficial deberá estar completa, en caso de que la información no cuente con alguno de los archivos obligatorios, no se llevará a cabo la revisión y se devolverá. Toda la información proveniente del actor de infraestructura, deberá tener la aprobación de la interventoría o área supervisora, cumpliendo todas las evaluaciones presentes en la hoja de cálculo VALIDACIONES_BDG identificadas con color , del archivo Excel Productos_BDG.xlsx, para cualquier etapa del proyecto. Las evaluaciones de calidad consisten en revisar el conjunto de datos geográficos, que han sido capturados o generados según las especificaciones técnicas previamente determinadas. Mediante el
- **GU-IC-06 §10 ¶2** — cumplimiento de la Norma Técnica Colombiana “INFORMACIÓN GEOGRÁFICA. CONCEPTOS BÁSICOS DE LA CALIDAD DE LOS DATOS GEOGRÁFICOS” - NTC-5043 e (ICONTEC, 2004), o la vigente al momento de la solicitud de la información de alistamiento, con el fin de satisfacer la necesidad establecida e implícita, dando cumplimiento a los requerimientos especificados.
#### §11 PRESENTACIÓN DE INFORMES

- **GU-IC-06 §11 ¶1** — La producción documental que genera el Instituto es el resultado de procesos de investigación realizados durante la ejecución contractual de los proyectos en la infraestructura de los Sistemas de Movilidad y Espacio Público. Con el objeto de asegurar que la presentación escrita de la producción documental sea consistente, clara y uniforme, el Instituto sugiere la aplicación de las normas APA de la Asociación Americana de Psicología por ser uno de los estándares más reconocidos para la trasmisión del conocimiento. Los documentos presentados por el contratista o tercero deben cumplir con la metodología APA que se aplica con el objetivo de normalizar y unificar la información:  Títulos
- **GU-IC-06 §11 ¶2** —  Puntuación y abreviaturas  Presentación de números y estadísticas  Construcción de tablas y figuras  Citación de referencias Teniendo en cuenta que el Instituto tiene la libertad de variar algunos de estos parámetros, se solicita tener en cuenta las siguientes excepciones en la aplicación de la norma:  Textos justificados y con doble espacio entre los párrafos.  Utilizar el nivel 2 para los títulos: Alineado a la izquierda y en Negrita.  Todas las hojas deben ser paginadas en la parte inferior centrada con números arábigos enteros. A continuación, se describen los datos mínimos que deben contener la portada, la hoja de control de
- **GU-IC-06 §11 ¶3** — versiones, tabla de contenido y listas especiales. Estas hojas preliminares son de gran importancia para el proceso de análisis de información, ya que de ellas se extraen los metadatos que se constituyen en puntos de acceso para la posterior búsqueda y recuperación de los productos dentro del repositorio. Portada La portada debe contener encabezado con el logo del IDU; en la parte central escribir el objeto del contrato, número de contrato, nombre del producto y en la parte inferior razón social del actor de infraestructura, fecha (año, mes, día) de edición. Incluir el número del contrato de interventoría y el
- **GU-IC-06 §11 ¶4** — nombre de la empresa interventora. Si se trata de un informe final de interventoría, la portada debe incluir los mismos datos. Ejemplo: Figura 10 Portada de producto documental Hoja control de versiones La hoja control de versiones deberá contener como mínimo los siguientes datos:  En el encabezado registrar el objeto del contrato y el número del mismo, o nombre del proyecto (según la resolución de urbanismo).  Título del producto (entregable) que se describe dentro del documento.  Control de versiones: En el campo “Versión” registrar la versión del documento debidamente aprobada y con números enteros. (Versión 1, Versión 2). Se utilizará una secuencia numérica
- **GU-IC-06 §11 ¶5** — iniciando en el 1 (1, 2, 3, 4…). En la descripción de la versión, indicar el ajuste realizado de manera general respecto a la versión anterior. Así mismo se debe registrar la fecha y los folios de la versión. El control de versiones debe conservar el registro de todas las versiones generadas.  La Hoja Control de Versiones debe contener los nombres, cargos y firmas digitales de las personas que intervinieron en la validación, revisión y aprobación del documento. Ejemplo: Figura 11 Hoja Control Versiones Se recomienda que la tabla de contenido y listas especiales, tengan la siguiente presentación: Tabla de contenido para documentos  “Tabla de contenido”. Título centrado.
- **GU-IC-06 §11 ¶6** —  Capítulos iniciales como: Introducción, Justificación, entre otros.  Relación de capítulos del 1 hasta el nivel 5.  Identificar con números arábigos las páginas en que se encuentran los elementos anteriores. Ejemplo: Figura 12 Tabla de contenido Listas especiales Hace referencia a la lista de figuras, tablas y anexos. Estas listas van en hojas separadas, cada hoja lleva el título de la lista que va a enunciar, cada elemento de la lista se referencia con el número que le corresponde en la secuencia, el título y la página de su ubicación en el documento. Ejemplo: Figura 13 Listas especiales Índices de figuras y de tablas, etc.
- **GU-IC-06 §11 ¶7** — Si el informe incluye anexos y planos se debe incluir la relación de éstos en lista de anexos y lista de planos.
#### §11.1 VALIDACIÓN DE PRODUCTOS

- **GU-IC-06 §11.1 ¶1** — El contenido de los archivos, su calidad, su completitud y autenticidad de la firma digital, es responsabilidad de los actores de infraestructura, por tanto, el Centro de Documentación no es responsable de los errores que se puedan presentar. El Centro de Documentación se encargará de validar que:  Cumplan con los aspectos básicos solicitados en la presente metodología, esto es: datos solicitados en la portada, hoja de versiones con firmas digitales, carpeta de archivos editables y carpeta con sus respectivos .PDF, cumplimiento especificaciones técnicas de los archivos PDF.  El producto no haya sido transferido con anterioridad.
- **GU-IC-06 §11.1 ¶2** —  Corresponda a una versión superior a la ya existente. Las versiones anteriores no se liberan en el repositorio, se conservan en el inventario para su consulta. La devolución se realizará con la Lista de Chequeo que maneja el Centro de Documentación, en donde se podrá ver la causa de la devolución o a través del sistema que esté vigente en el Instituto. Una vez los documentos transferidos cumplan con lo establecido en esta guía serán cargados en el repositorio institucional.
#### §11.2 REPOSITORIO INSTITUCIONAL

- **GU-IC-06 §11.2 ¶1** — El Centro de Documentación es el encargado de recibir, analizar, alistar y liberar en el repositorio institucional, los productos finales que le son transferidos por los actores de infraestructura, quienes son los responsables por el contenido intelectual de los productos. El Repositorio Institucional del IDU es una herramienta esencial y fundamental de búsqueda y recuperación del texto completo de los proyectos de infraestructura de los sistemas de movilidad y espacio público del Distrito Capital, desarrollados por el IDU. Está disponible para entes de gobierno, organismos de control, funcionarios de la entidad, estudiantes y en general para toda la comunidad a nivel mundial.
- **GU-IC-06 §11.2 ¶2** — Las políticas a tener en cuenta para la publicación de los productos finales en el repositorio son:  Cada producto será un registro en el repositorio.  Los productos en formato original serán cargados en la Comunidad Productos Formato Editable de consulta restringida.  Los archivos Excel o planos en DWG que no tengan su correspondiente archivo en .PDF, no serán cargados dentro del registro del producto.  El Centro de Documentación analiza, alista y carga la información en la misma forma en que esté identificada en las carpetas y nombres de los archivos.  Los productos se cargarán en el repositorio según el orden en el que sean recibidos. El tiempo
- **GU-IC-06 §11.2 ¶3** — de cargue depende del número de productos y de la complejidad de la información.
#### §12 DOCUMENTOS DE REFERENCIA

- **GU-IC-06 §12** — Los siguientes documentos pueden ser tomados como referencia en sus versiones vigentes:  Guía Cero Papel del Instituto de Desarrollo Urbano.  Reglas de catalogación Angloamericanas 2ª. Ed.  Circular IDU 1 de 2016, “Uso de la información”.  Guía alcance de los entregables de factibilidad.  Guía alcance de los entregables de prefactibilidad.  Guía alcance a los entregables de la etapa de diseño.  Manual Interventoría y Supervisión de Contratos. Además, se podrán consultar el documento:  Listas de Encabezamientos de Materias para bibliotecas / Biblioteca Luis Ángel Arango.

### FO-IC-05

#### A.1. Meta Física

- **FO-IC-05 A.1** — No. CIVs reportados en CAD No. de segmentos viales presentados en los archivos CAD Observaciones: Aclaraciones cuando no hay correspondencia entre los segmentos reportados en SIGIDU y los suministrados por el contratista
#### A.2. Topografía

- **FO-IC-05 A.2.a** — Georreferenciación: Las coordenadas planas y geográficas se encuentran ajustadas al sistema de referencia Magna Sirgas
- **FO-IC-05 A.2.b** — Layers: Los layes o capas de cada objeto se nombran según lo establecido en el instructivo para presentación de planos y archivos vigente
- **FO-IC-05 A.2.c** — Norte magnético: El plano presenta el norte magnético según la grilla de coordenadas planas
- **FO-IC-05 A.2.d** — Sección transversal: Se presenta la sección transversal de la vía existente o proyectada
- **FO-IC-05 A.2.e** — Sección típica: Se incluye la sección típica actual o proyectada de la estructura del pavimento
- **FO-IC-05 A.2.f** — Cuadro coordenadas placas de amarre: Cuadro de coordenadas Norte, Este y altura de las placas o puntos de amarre topográfico
- **FO-IC-05 A.2.g** — Nomenclatura vial: Los planos presentan la nomenclatura vial actual de los corredores viales y vías conectantes del proyecto o contrato
- **FO-IC-05 A.2.h** — Convenciones: Se presenta el cuadro de convenciones de los objetos representados en los planos
- **FO-IC-05 A.2.i** — Curvas de nivel: Se presentan las curvas de nivel el área del proyecto o contrato
- **FO-IC-05 A.2.j** — Placas de amarre: Se presentan las placas o puntos de amarre según la convención del IDU
- **FO-IC-05 A.2.k** — Grilla coordenadas: Representación de la cuadricula de coordenadas cada 50 o 100 mts, según escala del plano
- **FO-IC-05 A.2.l** — Completitud información rótulo: Diligenciamiento de la información solicitada en el rótulo de los planos, correspondiente al proyecto y profesionales
- **FO-IC-05 A.2.m** — Numeración planos: Numeración de planos de acuerdo al instructivo para la presentación de planos y archivos vigente
- **FO-IC-05 A.2.n** — Nombre layouts: Nombre de layouts según la nomenclatura del plano según el instructivo para la presentación de planos y archivos vigente
- **FO-IC-05 A.2.o** — Nombre archivos: Nombre de los archivos CAD según instructivo para presentación de planos y archivos vigente
#### A.3. Geometría

- **FO-IC-05 A.3.a** — Georreferenciación: Las coordenadas planas y geográficas se encuentran ajustadas al sistema de referencia Magna Sirgas
- **FO-IC-05 A.3.b** — Layers: Los layes o capas de cada objeto se nombran según lo establecido en el instructivo para presentación de planos y archivos
- **FO-IC-05 A.3.c** — Norte magnético: El plano presenta el norte magnético según la grilla de coordenadas planas
- **FO-IC-05 A.3.d** — Sección transversal: Se presenta la sección transversal de la vía existente o proyectada
- **FO-IC-05 A.3.e** — Sección típica: Se incluye la sección típica actual o proyectada de la estructura del pavimento
- **FO-IC-05 A.3.f** — Eje vía: Representación del eje o ejes geométricos según el instructivo para la presentación de planos y archivos
- **FO-IC-05 A.3.g** — Nomenclatura vial: Los planos presentan la nomenclatura vial actual de los corredores viales y vías conectantes del proyecto o contrato
- **FO-IC-05 A.3.h** — Elementos diseño geométrico horizontal: Cuadro de elementos que definen el diseño horizontal como coordenadas, radios, tangentes, longitudes, etc.
- **FO-IC-05 A.3.i** — Elementos curvatura esquinas y accesos: Elementos que definen el diseño horizontal como radios, tangentes, longitudes etc.
- **FO-IC-05 A.3.j** — Estructura pavimento calzada y anden: Detalle de las capas de la estructura del pavimento de las calzadas construidas o diseñas
- **FO-IC-05 A.3.k** — Convenciones: Se presenta el cuadro de convenciones de los objetos representados en los planos
- **FO-IC-05 A.3.l** — Perfil longitudinal: Representación del perfil longitudinal de la vía con una relación de escalas horizontal y vertical 1:10
- **FO-IC-05 A.3.m** — Áreas de intervención: Polígonos que representan las intervenciones en la vía cuando éstas son menores al área de la calzada o anden como parcheos, bacheos etc
- **FO-IC-05 A.3.n** — Placas de amarre: Presentación de las placas o puntos de amarre del levantamiento topográfico con sus respectivas coordenadas Norte, Este y Altura
- **FO-IC-05 A.3.o** — Grilla coordenadas: Representación de la cuadrícula de coordenadas cada 50 o 100 mts, según escala del plano
- **FO-IC-05 A.3.p** — Completitud información rótulo: Diligenciamiento de la información solicitada en el rótulo de los planos, correspondiente al proyecto y profesionales
- **FO-IC-05 A.3.q** — Numeración planos: Numeración de planos de acuerdo al instructivo para la presentación de planos y archivos vigente
- **FO-IC-05 A.3.r** — Nombre layouts: Nombre de layouts según la nomenclatura del plano
- **FO-IC-05 A.3.s** — Nombre archivos: Nombre de los archivos CAD según instructivo para presentación de planos y archivos vigente
#### A.4. Espacio Público

- **FO-IC-05 A.4.a** — Georreferenciación: Las coordenadas planas y geográficas se encuentran ajustadas al sistema de referencia Magna Sirgas
- **FO-IC-05 A.4.b** — Layers: Los layes o capas de cada objeto se nombran según lo establecido en el instructivo para presentación de planos y archivos
- **FO-IC-05 A.4.c** — Norte magnético: El plano presenta el norte magnético según la grilla de coordenadas planas
- **FO-IC-05 A.4.d** — Sección típica - Alzado: Se presenta la sección transversal o alzado existente o proyectada
- **FO-IC-05 A.4.e** — Estándar Bloques: Los bloque son los establecidos por el IDU y suministrado a los contratistas y terceros en archivo CAD
- **FO-IC-05 A.4.f** — Escalas planta: Las escalas en planta corresponden a las establecidas en el manual para la presentación de planos y archivos vigente
- **FO-IC-05 A.4.g** — Escalas detalles: Las escalas de detalle se presentan en un rango de escalas estándar (múltiplo de 5) entre 1:10 a 1:100
- **FO-IC-05 A.4.h** — Tipos de material: Los tipos de material utilizado en andenes, plazoletas o cualquier elemento de espacio público se encuentran representados como polígonos
- **FO-IC-05 A.4.i** — Grilla coordenadas: Representación de la cuadrícula de coordenadas cada 50 o 100 mts, según escala del plano
- **FO-IC-05 A.4.j** — Convenciones: Cuadro de convenciones utilizadas para representar cada objeto geográfico
- **FO-IC-05 A.4.k** — Completitud información rótulo: Diligenciamiento de la información solicitada en el rótulo de los planos, correspondiente al proyecto y profesionales
- **FO-IC-05 A.4.l** — Numeración planos: Numeración de planos de acuerdo al instructivo para la presentación de planos y archivos vigente
- **FO-IC-05 A.4.m** — Nombre layouts: Nombre de layouts según la nomenclatura del plano
- **FO-IC-05 A.4.n** — Nombre archivos: Nombre de los archivos CAD según instructivo para presentación de planos y archivos vigente
#### A.5. Localización Estructuras

- **FO-IC-05 A.5.a** — Georreferenciación: Las coordenadas planas y geográficas se encuentran ajustadas al sistema de referencia Magna Sirgas
- **FO-IC-05 A.5.b** — Layers: Los layes o capas de cada objeto se nombran según lo establecido en el instructivo para presentación de planos y archivos
- **FO-IC-05 A.5.c** — Sección típica: Se presenta la sección transversal de la vía existente o proyectada
- **FO-IC-05 A.5.d** — Convenciones: Cuadro de convenciones utilizadas para representar cada objeto geográfico
- **FO-IC-05 A.5.e** — Escalas planta: Las escalas en planta corresponden a las establecidas en el instructivo para la presentación de planos y archivos
- **FO-IC-05 A.5.f** — Escalas detalles: Las escalas de detalle se presentan en un rango de escalas estándar (múltiplo de 5) entre 1:10 a 1:100
- **FO-IC-05 A.5.g** — Completitud información rótulo: Diligenciamiento de la información solicitada en el rótulo de los planos, correspondiente al proyecto y profesionales
- **FO-IC-05 A.5.h** — Numeración planos: Numeración de planos de acuerdo al instructivo para la presentación de planos y archivos vigente
- **FO-IC-05 A.5.i** — Nombre Layouts: Nombre de layouts según la nomenclatura del plano
- **FO-IC-05 A.5.j** — Nombre archivos: Nombre de los archivos CAD según instructivo para presentación de planos y archivos
#### A.6. Servicios Públicos

- **FO-IC-05 A.6.a** — Redes de acueducto: Relación de archivos y planos de redes de acueducto aprobado por la Empresa de Acueducto de Bogota, presentados en el CD
- **FO-IC-05 A.6.b** — Redes de alcantarillado pluvial: Relación de archivos y planos de redes de alcantarillado pluvial aprobado por la Empresa de Acueducto de Bogota, presentados en el CD
- **FO-IC-05 A.6.c** — Redes de alcantarillado sanitario: Relación de archivos y planos de redes de redes de alcantarillado sanitario, aprobado por la Empresa de Acueducto de Bogota, presentados en el CD
- **FO-IC-05 A.6.d** — Estructuras acueducto / alcantarillado: Relación de archivos y planos de estructuras de acueducto o alcantarillado, aprobado por la Empresa de Acueducto de Bogota, presentados en el CD
- **FO-IC-05 A.6.e** — Redes ETB: Relación de archivos y planos de redes de canalización telefónica, aprobados por la ETB y presentados en el CD
- **FO-IC-05 A.6.f** — Redes Une: Relación de archivos y planos de redes de canalización telefónica, aprobados por la UNE- EPM y presentados en el CD
- **FO-IC-05 A.6.g** — Redes movistar: Relación de archivos y planos de redes de canalización telefónica, aprobados por la MOVISTAR y presentados en el CD
- **FO-IC-05 A.6.h** — Redes Telecom: Relación de archivos y planos de redes de canalización telefónica, aprobados por TELECOM y presentados en el CD
- **FO-IC-05 A.6.i** — Redes Codensa: Relación de archivos y planos de redes de canalización de energía eléctrica de CODENSA presentados en el CD
- **FO-IC-05 A.6.j** — Redes gas natural: Relación de archivos y planos de redes de GAS NATURAL SA presentados en el CD
- **FO-IC-05 A.6.k** — Señalización horizontal y vertical: Relación de archivos y planos de la señalización horizontal y vertical aprobados por la SDM presentados en el CD
- **FO-IC-05 A.6.l** — Otras: Relación de archivos y planos otra entidades no incluida anteriormente
#### B.1. Alcance De La Informacion

- **FO-IC-05 B.1** — La información cumple con el alcance del contrato según la Geodatabase suministrada al contratista SI NO Observaciones: Los tramos viales presentados son corresponden al alcance del contrato o a la meta de la resolución de urbanismo
#### B.2. Georreferenciación

- **FO-IC-05 B.2** — La cartografía se ajusta al sistema de referencia Magna-Sirgas SI NO Observaciones: Las coordenadas planas y geográficas se encuentran ajustadas al sistema de referencia Magna Sirgas
#### B.3. Exactitud Posicional

- **FO-IC-05 B.3** — La cartografía cumple con la exactitud posicional respecto al plano CAD récord o de diseño del contrato o mapa de referencia o imagen digital SI NO Observaciones: El componente cartográfico guarda una exactitud posicional menor a 5 cms con respecto a los planos presentado en CAD o menor a 20 cms respecto a la ultima imagen del Distrito Capital.
#### B.4. Topología

- **FO-IC-05 B.4** — La cartografía cumple las siguientes reglas topológicas SI NO Observaciones: Los polígonos o líneas de una o varias cobertura cumple con estas reglas topológicas validadas en el software Arcgis
- **FO-IC-05 B.4.a** — Superposición elementos
- **FO-IC-05 B.4.b** — Continuidad elementos
- **FO-IC-05 B.4.c** — Contenencia elementos
- **FO-IC-05 B.4.d** — Intersección de líneas
#### B.5. Codificación De Elementos

- **FO-IC-05 B.5** — Los elementos se encuentran codificados SI NO Observaciones: Todos los elementos se encuentran codificados según la base geográfica suministrada por el IDU o los rangos de codificación suministrados.
#### B.6. Completitud Información

- **FO-IC-05 B.6.a** — Se presentan todos los elementos de la sección transversal y mobiliario urbano: SI NO Observaciones: Todos los elementos objeto del contrato correspondientes a la sección transversal del corredor vial como: anden, calzada, cicloruta etc, se encuentran en la geodatabase
- **FO-IC-05 B.6.b** — Se cumple con la completitud de registros: SI NO Observaciones: Los registros tienen todos los campos objeto del contrato diligenciados.
- **FO-IC-05 B.6.c** — Cuantos elementos se presentan en la geodatabase: Observaciones: Número total de elementos presentados en la geodatabase
#### B.7. Valores De Atributos

- **FO-IC-05 B.7.a** — Los dominios son los suministrados en la geodatabase: SI NO Completitud % Observaciones: Los dominios presentados en cada tabla corresponden a los suministrados por el IDU
- **FO-IC-05 B.7.b** — Los elementos nuevos se codifican según rangos suministrados: SI NO Completitud % Observaciones: Los elementos nuevos se codifican según los rangos suministrados por el IDU.

### Productos_BDG

#### VALIDACIONES_BDG 1. TOTALIDAD DE LA INFORMACIÓN

- **VALIDACIONES_BDG 1. Verificación del cumplimiento de la meta** — Verificación del cumplimiento de la meta física: Se verifica el formato de reporte de seguimiento final entregado e incorporado en la base de datos geográfica vs el resultado de la consulta en el SIGIDU en su componente de seguimiento a proyectos.
- **VALIDACIONES_BDG 1. Verificación de los atributos incorporad** — Verificación de los atributos incorporados: Se verifica que los atributos incorporados en la base de datos geográfica, correspondan con los solicitados en el diccionario de atributos.
- **VALIDACIONES_BDG 1. Verificación de las relación entre eleme** — Verificación de las relación entre elementos y/o tablas: Se verifica la relación entre elementos y/o tablas (el dato que debe ser incorporado en el atributo “FK_ID_Xxxxx” es de tipo numérico y debe corresponder al mismo número del atributo “PK_ID_Xxxxxx” del elemento o tabla con la cual está relacionado)
#### VALIDACIONES_BDG 2.1. CONSISTENCIA CONCEPTUAL

- **VALIDACIONES_BDG 2.1. Verificación de duplicidad del atributo ** — Verificación de duplicidad del atributo PK_ID_Xxxxx de cada elemento y/o tabla: Inexistencia de duplicidad del atributo PK_ID_Xxxxx de cada elemento y/o tabla.
- **VALIDACIONES_BDG 2.1. Verificación de registros vacíos** — Verificación de registros vacíos: Inexistencia de registros vacíos es decir que los registros tienen diligenciados todos los campos alcance del proyecto
- **VALIDACIONES_BDG 2.1. Verificación de la codificación de los e** — Verificación de la codificación de los elementos: La codificación de los elementos debe estar acorde a la base de datos geográfica suministrada por el IDU o los rangos de codificación establecidos
#### VALIDACIONES_BDG 2.2. CONSISTENCIA DE DOMINIO

- **VALIDACIONES_BDG 2.2. Verificación de dominios** — Verificación de dominios: Se revisa que todos los elementos cuyos atributos tienen un dominio asociado, cumplan con el mismo
#### VALIDACIONES_BDG 2.3. CONSISTENCIA DE FORMATO

- **VALIDACIONES_BDG 2.3. Verificación del tipo de dato y la longi** — Verificación del tipo de dato y la longitud: se valida que todos los atributos propios de cada elemento, cumplan con el tipo de dato y la longitud del mismo.
#### VALIDACIONES_BDG 2.4. CONSISTENCIA TOPOLÓGICA

- **VALIDACIONES_BDG 2.4. La cartografía cumple las siguientes reg** — La cartografía cumple las siguientes reglas topológicas: Los polígonos, líneas y puntos de una o varias cobertura denben cumplir con las siguientes reglas topológicas
- **VALIDACIONES_BDG 2.4. a. Superposición elementos** — a. Superposición elementos: No debe existir superposición de elementos, consigo mismo o con otros. Esta regla aplica para elementos de tipo línea, punto y polígono
- **VALIDACIONES_BDG 2.4. b. Huecos entre elementos** — b. Huecos entre elementos: Esta regla precisa que no haya vacíos dentro de un elemento o entre polígonos de elementos adyacentes.
- **VALIDACIONES_BDG 2.4. c. Contenencia elementos** — c. Contenencia elementos: Requiere que los polígonos o puntos de un elemento de entidad estén contenido en polígonos o puntos de otro elemento
#### VALIDACIONES_BDG 3.1. EXACTITUD ABSOLUTA O EXTERNA

- **VALIDACIONES_BDG 3.1. Proyectos que cuentan con topografía** — Proyectos que cuentan con topografía: Se evalúa la exactitud de posición de la base de datos geográfica con los archivos CAD.
#### VALIDACIONES_BDG 3.2. EXACTITUD RELATIVA O INTERNA

- **VALIDACIONES_BDG 3.2. Información geográfica entregada inicial** — Información geográfica entregada inicialmente: Se evalúa que Información geográfica entregada inicialmente en la base de datos geográfica (Información Base), coicida con la entregada.
#### VALIDACIONES_BDG 4.1. EXACTITUD DE LA CLASIFICACIÓN

- **VALIDACIONES_BDG 4.1. Atributos cualitativos de los elementos** — Atributos cualitativos de los elementos: la revisión de este ítem se realiza a los atributos cualitativos de los elementos entregados por el proyecto , verificando que corresponden con las características en el mundo real.
#### VALIDACIONES_BDG 4.2. EXACTITUD DEL VALOR DADO A UN ATRIBUTO CUANTITATIVO

- **VALIDACIONES_BDG 4.2. Atributos cuantitativos** — Atributos cuantitativos: Se revisará la totalidad de los atributos cuantitativos, mediante el uso de modelos que permiten calcular los valores finales y así certificar la veracidad de la información.
#### VALIDACIONES_BDG 5. ENTREGA DE SOPORTES

- **VALIDACIONES_BDG 5. Documentos soportes** — Documentos soportes: verificación de la entrega de todos los soportes (archivos crudos e informes).
#### VALIDACIONES_BDG 6. CANTIDAD DE ELEMENTOS

- **VALIDACIONES_BDG 6. Cantidad de elementos** — Cantidad de elementos: Cantidad de elementos revisados
#### REGLAS_TOPOLOGICAS

- **REGLAS_TOPOLOGICAS 1** — 1. MUST NOT OVERLAP: NO DEBE HABER SUPERPOSICIÓN (aplica por elemento según la hoja)
- **REGLAS_TOPOLOGICAS 2** — 2. MUST NOT OVERLAP WITH: NO HAY SUPERPOSICIÓN CON (aplica por elemento según la hoja)
- **REGLAS_TOPOLOGICAS 3** — 3. ÁREA BOUNDARY MUST BE COVERED BY BOUNDARY OF: LOS LIMITES SON COINCIDENTES DE DOS CLASES (aplica por elemento según la hoja)
- **REGLAS_TOPOLOGICAS 4** — 4. MUST BE PROPRLY INSIDE POLYGONS: DEBE ESTAR DENTRO DEL POLÍGONO (aplica por elemento según la hoja)
- **REGLAS_TOPOLOGICAS 5** — 5. MUST NOT HAVE GAPS: NO DEBE HABER HUECOS (aplica por elemento según la hoja)
- **REGLAS_TOPOLOGICAS 6** — 6. MUST NOT HAVE DANGLES: NO DEBE HABER LÍNEAS SUELTAS (aplica por elemento según la hoja)
- **REGLAS_TOPOLOGICAS 7** — 7. MUST NOT OVERLAP: NO DEBE HABER SUPERPOSICIÓN (aplica por elemento según la hoja)
- **REGLAS_TOPOLOGICAS 8** — 8. MUST NOT INTERSECT: NO DEBE HABER INTERSECCIÓN (aplica por elemento según la hoja)
- **REGLAS_TOPOLOGICAS 9** — 9. MUST NOT INTERSECT OR TOUCH INTERIOR: TODAS LAS INTERSECCIONES DE LÍNEA SON NODO (aplica por elemento según la hoja)
- **REGLAS_TOPOLOGICAS 10** — 10. MUST NOT OVERLAP WITH: NO HAY SUPERPOSICIÓN CON (aplica por elemento según la hoja)
- **REGLAS_TOPOLOGICAS 11** — 11. MUST NOT SELF OVERLAP: NO DEBE HABER SUPERPOSICIÓN CON SI MISMA (aplica por elemento según la hoja)
- **REGLAS_TOPOLOGICAS 12** — 12. MUST NOT SELF INTERSECT: NO DEBE HABER INTERSECCIÓN CON SI MISMA (aplica por elemento según la hoja)
- **REGLAS_TOPOLOGICAS 13** — 13. MUST BE SINGLE PART: DEBE SER UNA SOLA ENTIDAD (aplica por elemento según la hoja)
- **REGLAS_TOPOLOGICAS 14** — 14. MUST BE COVERED BY BOUNDARY OF: EL LIMITE DE LÍNEA DEBE COINCIDIR CON LIMITE DE POLÍGONO (aplica por elemento según la hoja)

### Productos_DWG

#### ElementosConstruccion (Récord) — Estudio Topografico

- **Productos_DWG Récord F7** — Georreferenciación
- **Productos_DWG Récord F8** — Layers
- **Productos_DWG Récord F9** — Norte
- **Productos_DWG Récord F10** — Poligonal*
- **Productos_DWG Récord F11** — Deltas (Vértices del levantamiento)
- **Productos_DWG Récord F12** — Placas de amarre - Puntos GPS/GNSS (Línea Base)
- **Productos_DWG Récord F13** — Cuadro de mojones plano urbanístico con áreas
- **Productos_DWG Récord F14** — Nomenclatura vial, Civ
- **Productos_DWG Récord F15** — Convenciones
- **Productos_DWG Récord F16** — Cuadro coordenadas placas de amarre
- **Productos_DWG Récord F17** — Grilla coordenadas
- **Productos_DWG Récord F18** — Completitud datos rótulo
- **Productos_DWG Récord F19** — Numeración planos
- **Productos_DWG Récord F20** — Nombre Layouts
- **Productos_DWG Récord F21** — Nombre archivos
- **Productos_DWG Récord F22** — Sistema de referencia
- **Productos_DWG Récord F23** — Plano urbanístico vigente aprobado por curaduría (.DWG y .PDF)
- **Productos_DWG Récord F24** — Escala numérica - Escala grafica
#### ElementosConstruccion (Récord) — Vial

- **Productos_DWG Récord F26** — Planta Perfil: En planta se deben presentar las líneas de ejes, bordes, sumideros, limite de intervención y abcisado, en el perfil longitudinal de tener las líneas de rasante del eje y bordes, pendiente longitudinal, cinta de cotas
- **Productos_DWG Récord F27** — Estructuras especiales (puentes, pontones, box) si aplica
- **Productos_DWG Récord F28** — Sección típica con espesores y tipo de materiales utilizados, pendiente Transversal, acotados
- **Productos_DWG Récord F29** — Plano de Cotas del pavimento cada 5m (incluye ubicación de sumideros)
- **Productos_DWG Récord F30** — Cuadro de convenciones
- **Productos_DWG Récord F31** — Planos de Secciones Transversales (niveles en eje y bordes, pendientes transversales, estructura del pavimento con espesores construidos)
- **Productos_DWG Récord F32** — Georreferenciación
- **Productos_DWG Récord F33** — Layers
- **Productos_DWG Récord F34** — Norte
- **Productos_DWG Récord F35** — Nomenclatura vial, Códigos CIV
- **Productos_DWG Récord F36** — Grilla coordenadas
- **Productos_DWG Récord F37** — Completitud datos rótulo
- **Productos_DWG Récord F38** — Numeración planos
- **Productos_DWG Récord F39** — Nombre Layouts
- **Productos_DWG Récord F40** — Nombre archivos
- **Productos_DWG Récord F41** — Sistema de referencia
- **Productos_DWG Récord F42** — Escala numérica - Escala grafica
- **Productos_DWG Récord F43** — Nomenclatura vial
- **Productos_DWG Récord F44** — Cartera de nivelación conjunta realizada por la interventoría.
- **Productos_DWG Récord F45** — Detalles
#### ElementosConstruccion (Récord) — Arquitectónico Espacio Público Y Paisajistico

- **Productos_DWG Récord F47** — Plano arquitectónico en planta
- **Productos_DWG Récord F48** — Plano arquitectónico de los Detalles a escala ampliada (vados peatonales, rampas vehiculares, prefabricados, contenedores de raíz, mobiliario urbano)
- **Productos_DWG Récord F49** — Vados peatonales, rampas
- **Productos_DWG Récord F50** — Perfil Longitudinal (Pendiente Longitudinal)
- **Productos_DWG Récord F51** — Sección típica Longitudinal (espesores y tipo de materiales utilizados, pendiente longitudinal)
- **Productos_DWG Récord F52** — Detalles de confinamiento
- **Productos_DWG Récord F53** — Alumbrado Publico
- **Productos_DWG Récord F54** — Mobiliario Urbano
- **Productos_DWG Récord F55** — Señalización Horizontal y Vertical
- **Productos_DWG Récord F56** — Secciones transversales (entre sardineles y bordillos de confinamiento) incluyendo rampas , vados peatonales, prefabricados ,contenedores de raíz, pendientes transversales, cota terreno, cota rasante)
- **Productos_DWG Récord F57** — Cuadro de convenciones de elementos prefabricados
- **Productos_DWG Récord F58** — Cuadro de convenciones de mobiliario urbano
- **Productos_DWG Récord F59** — Sumideros
- **Productos_DWG Récord F60** — Cotas en planta
- **Productos_DWG Récord F61** — Cotas de nivel
- **Productos_DWG Récord F62** — Nomenclatura vial, Códigos CIV
- **Productos_DWG Récord F63** — Detalles elementos prefabricados utilizados
- **Productos_DWG Récord F64** — Georreferenciación
- **Productos_DWG Récord F65** — Layers
- **Productos_DWG Récord F66** — Norte magnético
- **Productos_DWG Récord F67** — Grilla coordenadas
- **Productos_DWG Récord F68** — Convenciones
- **Productos_DWG Récord F69** — Completitud datos rótulo
- **Productos_DWG Récord F70** — Numeración planos
- **Productos_DWG Récord F71** — Nombre Layouts
- **Productos_DWG Récord F72** — Escalas planta
- **Productos_DWG Récord F73** — Escalas detalles
- **Productos_DWG Récord F74** — Nombre archivos
- **Productos_DWG Récord F75** — Sistema de referencia
- **Productos_DWG Récord F76** — Escala numérica - Escala grafica
- **Productos_DWG Récord F77** — Detalles
#### ElementosConstruccion (Récord) — Pavimentos

- **Productos_DWG Récord F79** — Layers
- **Productos_DWG Récord F80** — Norte
- **Productos_DWG Récord F81** — Georreferenciación
- **Productos_DWG Récord F82** — Grilla coordenadas
- **Productos_DWG Récord F83** — Convenciones
- **Productos_DWG Récord F84** — Completitud datos rótulo
- **Productos_DWG Récord F85** — Plano de localización con la ubicación de los apiques y/o perforaciones
- **Productos_DWG Récord F86** — Plano de perfil estratigráfico (espesor, clasificación USCS, límite líquido, índice Plástico, CBR suelo de subrasante)
- **Productos_DWG Récord F87** — Plano de modulación de losas y detalles constructivos****
- **Productos_DWG Récord F88** — Nomenclatura vial, códigos CIV
- **Productos_DWG Récord F89** — Numeración planos
- **Productos_DWG Récord F90** — Nombre Layouts
- **Productos_DWG Récord F91** — Escalas planta
- **Productos_DWG Récord F92** — Escalas detalles
- **Productos_DWG Récord F93** — Nombre archivos
- **Productos_DWG Récord F94** — Sistema de referencia
- **Productos_DWG Récord F95** — Escala numérica - Escala grafica
#### ElementosConstruccion (Récord) — Geotecnia

- **Productos_DWG Récord F97** — Layers
- **Productos_DWG Récord F98** — Norte
- **Productos_DWG Récord F99** — Georreferenciación
- **Productos_DWG Récord F100** — Abcisado
- **Productos_DWG Récord F101** — Nomenclatura vial, códigos CIV
- **Productos_DWG Récord F102** — Plano de localización de exploraciones geotécnicas georreferenciado, incluyendo localización e identificación de las estructuras construidas, con cuadro resumen
- **Productos_DWG Récord F103** — Perfil estratigráfico de cada uno de los sondeos realizados, identificando los estratos, profundidad, descripción, clasificación, propiedades físicas y mecánicas, y nivel freático.
- **Productos_DWG Récord F104** — Planos Planta perfil por estructura que incluyan de manera simultánea: perfil topográfico, perfil estratigráfico, implantación y alzado de la estructura, localización exacta de los apoyos de la estructura y las exploraciones geotécnicas, características físicas y mecánicas de cada uno de los estratos identificados, configuración en planta y profundidad de la cimentación construida. Cuadro del modelo geotécnico utilizado con los parámetros geotécnicos correspondientes.
- **Productos_DWG Récord F105** — Planos de obras de estabilización geotécnica en planta - perfil, que incluyan de manera simultánea: perfil topográfico, perfil estratigráfico, localización de las exploraciones geotécnicas, características físicas y mecánicas de cada uno de los estratos identificados, implantación y alzado de obras de contención construidas, detalles constructivos específicos de cada uno de los elementos que conforman la solución, indicando especificaciones de materiales y obras de drenaje. Cuadro del modelo geotécnico utilizado con los parámetros geotécnicos correspondientes.
- **Productos_DWG Récord F106** — Secciones Transversales
- **Productos_DWG Récord F107** — Convenciones
- **Productos_DWG Récord F108** — Numeración planos
- **Productos_DWG Récord F109** — Nombre Layouts
- **Productos_DWG Récord F110** — Escalas planta
- **Productos_DWG Récord F111** — Escalas detalles
- **Productos_DWG Récord F112** — Nombre archivos
- **Productos_DWG Récord F113** — Sistema de referencia
- **Productos_DWG Récord F114** — Escala numérica - Escala grafica
- **Productos_DWG Récord F115** — Grilla coordenadas
- **Productos_DWG Récord F116** — Completitud datos rótulo
#### ElementosConstruccion (Récord) — Estructuras

- **Productos_DWG Récord F118** — Plano de localización general georreferenciado identificando las estructuras construidas
- **Productos_DWG Récord F119** — Plano de Ejes de la estructura, conectantes, tramos de estructura.
- **Productos_DWG Récord F120** — Secciones transversales por cada luz y perfiles con geometría, dimensiones y detalle del refuerzo de las obras de contención a construir, incluyendo el perfil del terreno, estructuras anexas, detalles generales y de refuerzo de las obras de drenaje, cuadro de traslapos y ganchos, parámetros geotécnicos y de diseño utilizados.
- **Productos_DWG Récord F121** — Planos para prueba de carga, cuadro de deflexiones, características de los materiales, localización de los equipos, fases de carga, puntos de control.
- **Productos_DWG Récord F122** — Especificaciones generales de la estructura
- **Productos_DWG Récord F123** — Cotas
- **Productos_DWG Récord F124** — Plano Secciones longitudinales (ejes, longitudes, alturas, gálibos horizontales, verticales, juntas de dilatación pendientes)
- **Productos_DWG Récord F125** — Planos de detalle por cada componente del puente: Superestructura, subestructura, cimentación, con escala en múltiplos de 5.**
- **Productos_DWG Récord F126** — Plano en planta de cada uno de los niveles que compone la estructura.
- **Productos_DWG Récord F127** — Detalles de los elementos estructurales.
- **Productos_DWG Récord F128** — Plano de despieces de todos los elementos estructurales tanto existentes como proyectados (cimentaciones y rampas), además de los despieces de refuerzo de elementos de concreto.
- **Productos_DWG Récord F129** — Especificación de los materiales.
- **Productos_DWG Récord F130** — Especificación de las cargas de diseño.
- **Productos_DWG Récord F131** — Especificaciones especiales sobre la fundación de estructuras.
- **Productos_DWG Récord F132** — Planos de detalles de construcción (niveles de demolición, protección de excavaciones y secuencias de montaje).
- **Productos_DWG Récord F133** — Detalles constructivos especiales.
- **Productos_DWG Récord F134** — Para estructuras metálicas presentar los planos de fabricación y montaje.
- **Productos_DWG Récord F135** — Georreferenciación
- **Productos_DWG Récord F136** — Layers
- **Productos_DWG Récord F137** — Norte
- **Productos_DWG Récord F138** — Grilla coordenadas
- **Productos_DWG Récord F139** — Convenciones
- **Productos_DWG Récord F140** — Completitud datos rótulo
- **Productos_DWG Récord F141** — Convenciones
- **Productos_DWG Récord F142** — Escalas planta
- **Productos_DWG Récord F143** — Escalas Detalles
- **Productos_DWG Récord F144** — Planos de taller ***
- **Productos_DWG Récord F145** — Fundación de estructuras
- **Productos_DWG Récord F146** — Completitud datos rótulo
- **Productos_DWG Récord F147** — Numeración planos
- **Productos_DWG Récord F148** — Nombre Layouts
- **Productos_DWG Récord F149** — Nombre archivos
- **Productos_DWG Récord F150** — Escala numérica - Escala grafica
#### LAYERCAD

- **Productos_DWG LAYERCAD regla** — Representar cada elemento en el layer CAD, tipo de geometría y estado definidos en LAYERCAD.
- **Productos_DWG LAYERCAD 1** — Árbol: layer CAD ARBOL, geometría PUNTO, estados E: EXISTENTE D: DISEÑO P: PLANTADO
- **Productos_DWG LAYERCAD 2** — BloqueArbol: layer CAD ARBOL, geometría BLOQUE, estados E: EXISTENTE D: DISEÑO C: INTERVENIDO
- **Productos_DWG LAYERCAD 3** — Alameda: layer CAD ALAMEDA, geometría POLÍGONO, estados E: EXISTENTE D: DISEÑO C: INTERVENIDO
- **Productos_DWG LAYERCAD 4** — Andén: layer CAD ANDEN, geometría POLÍGONO, estados E: EXISTENTE D: DISEÑO C: INTERVENIDO
- **Productos_DWG LAYERCAD 5** — Plaza: layer CAD PLAZA, geometría POLÍGONO, estados E: EXISTENTE D: DISEÑO C: INTERVENIDO
- **Productos_DWG LAYERCAD 6** — Pompeyano: layer CAD POMPEYANO, geometría POLÍGONO, estados E: EXISTENTE D: DISEÑO C: INTERVENIDO
- **Productos_DWG LAYERCAD 7** — Rampa: layer CAD RAMPA, geometría POLÍGONO, estados E: EXISTENTE D: DISEÑO C: INTERVENIDO
- **Productos_DWG LAYERCAD 8** — Exploración: layer CAD EXPLORACION, geometría PUNTO, estados E: EXISTENTE D: DISEÑO C: INTERVENIDO
- **Productos_DWG LAYERCAD 9** — Bloque Exploración: layer CAD EXPLORACION, geometría BLOQUE, estados E: EXISTENTE D: DISEÑO C: INTERVENIDO
- **Productos_DWG LAYERCAD 10** — Escalera: layer CAD ESCALERA, geometría POLÍGONO, estados E: EXISTENTE D: DISEÑO C: INTERVENIDO
- **Productos_DWG LAYERCAD 11** — Muro: layer CAD MURO, geometría POLÍGONO, estados E: EXISTENTE D: DISEÑO C: INTERVENIDO
- **Productos_DWG LAYERCAD 12** — Talud: layer CAD TALUD, geometría POLÍGONO, estados E: EXISTENTE D: DISEÑO C: INTERVENIDO
- **Productos_DWG LAYERCAD 13** — Terraplén: layer CAD TERRAPLEN, geometría POLÍGONO, estados E: EXISTENTE D: DISEÑO C: INTERVENIDO
- **Productos_DWG LAYERCAD 14** — Banca: layer CAD BANCA, geometría PUNTO, estados E: EXISTENTE D: DISEÑO C: INTERVENIDO
- **Productos_DWG LAYERCAD 15** — Bloque Banca: layer CAD BLOQUEBANCA, geometría BLOQUE, estados E: EXISTENTE D: DISEÑO C: INTERVENIDO
- **Productos_DWG LAYERCAD 16** — Baranda Peatonal: layer CAD BARANDAPEATONAL, geometría LÍNEA, estados E: EXISTENTE D: DISEÑO C: INTERVENIDO
- **Productos_DWG LAYERCAD 17** — Bolardo: layer CAD BOLARDO, geometría PUNTO, estados E: EXISTENTE D: DISEÑO C: INTERVENIDO
- **Productos_DWG LAYERCAD 18** — Bloque Bolardo: layer CAD BLOQUEBOLARDO, geometría BLOQUE, estados E: EXISTENTE D: DISEÑO C: INTERVENIDO
- **Productos_DWG LAYERCAD 19** — Caneca: layer CAD CANECA, geometría PUNTO, estados E: EXISTENTE D: DISEÑO C: INTERVENIDO
- **Productos_DWG LAYERCAD 20** — Bloque Caneca: layer CAD BLOQUECANECA, geometría BLOQUE, estados E: EXISTENTE D: DISEÑO C: INTERVENIDO
- **Productos_DWG LAYERCAD 21** — CicloParqueadero: layer CAD CICLOPARQUEADERO, geometría PUNTO, estados E: EXISTENTE D: DISEÑO C: INTERVENIDO
- **Productos_DWG LAYERCAD 22** — Bloque CicloParqueadero: layer CAD CICLOPARQUEADERO, geometría BLOQUE, estados E: EXISTENTE D: DISEÑO C: INTERVENIDO
- **Productos_DWG LAYERCAD 23** — Contenedor de Raíz: layer CAD CONTENEDORRAIZ, geometría PUNTO, estados E: EXISTENTE D: DISEÑO C: INTERVENIDO
- **Productos_DWG LAYERCAD 24** — Bloque Contenedor Raíz: layer CAD BLOQUECONTENEDORRAIZ, geometría BLOQUE, estados E: EXISTENTE D: DISEÑO C: INTERVENIDO
- **Productos_DWG LAYERCAD 25** — Matera: layer CAD MATERA, geometría PUNTO, estados E: EXISTENTE D: DISEÑO C: INTERVENIDO
- **Productos_DWG LAYERCAD 26** — Bloque Matera: layer CAD MATERA, geometría BLOQUE, estados E: EXISTENTE D: DISEÑO C: INTERVENIDO
- **Productos_DWG LAYERCAD 27** — Protector de Árbol: layer CAD PROTECTORARBOL, geometría PUNTO, estados E: EXISTENTE D: DISEÑO C: INTERVENIDO
- **Productos_DWG LAYERCAD 28** — Bloque Protector Árbol: layer CAD BLOQUEPROTECTORARBOL, geometría BLOQUE, estados E: EXISTENTE D: DISEÑO C: INTERVENIDO
- **Productos_DWG LAYERCAD 29** — Módulo: layer CAD MODULO, geometría PUNTO, estados E: EXISTENTE D: DISEÑO C: INTERVENIDO
- **Productos_DWG LAYERCAD 30** — Pileta: layer CAD PILETA, geometría POLÍGONO, estados E: EXISTENTE D: DISEÑO C: INTERVENIDO
- **Productos_DWG LAYERCAD 31** — Aleta de Estribo: layer CAD ALETAESTRIBO, geometría POLÍGONO, estados E: EXISTENTE D: DISEÑO C: INTERVENIDO
- **Productos_DWG LAYERCAD 32** — Baranda: layer CAD BARANDA, geometría LÍNEA, estados E: EXISTENTE D: DISEÑO C: INTERVENIDO
- **Productos_DWG LAYERCAD 33** — Barrera Puente: layer CAD BARRERAPUENTE, geometría LÍNEA, estados E: EXISTENTE D: DISEÑO C: INTERVENIDO
- **Productos_DWG LAYERCAD 34** — Caisson: layer CAD CAISSON, geometría POLÍGONO, estados E: EXISTENTE D: DISEÑO C: INTERVENIDO
- **Productos_DWG LAYERCAD 35** — Cercha: layer CAD CERCHA, geometría LÍNEA, estados E: EXISTENTE D: DISEÑO C: INTERVENIDO
- **Productos_DWG LAYERCAD 36** — Columna: layer CAD COLUMNA, geometría POLÍGONO, estados E: EXISTENTE D: DISEÑO C: INTERVENIDO
- **Productos_DWG LAYERCAD 37** — Dado: layer CAD DADO, geometría POLÍGONO, estados E: EXISTENTE D: DISEÑO C: INTERVENIDO
- **Productos_DWG LAYERCAD 38** — Diafragma: layer CAD DIAFRAGMA, geometría LÍNEA, estados E: EXISTENTE D: DISEÑO C: INTERVENIDO
- **Productos_DWG LAYERCAD 39** — Estribo: layer CAD ESTRIBO, geometría POLÍGONO, estados E: EXISTENTE D: DISEÑO C: INTERVENIDO
- **Productos_DWG LAYERCAD 40** — Guarda Ruedas: layer CAD GUARDARUEDAS, geometría LÍNEA, estados E: EXISTENTE D: DISEÑO C: INTERVENIDO
- **Productos_DWG LAYERCAD 41** — Junta de Dilatación: layer CAD JUNTADILATACION, geometría LÍNEA, estados E: EXISTENTE D: DISEÑO C: INTERVENIDO
- **Productos_DWG LAYERCAD 42** — Losa de Aproximación: layer CAD LOSAAPROXIMACION, geometría POLÍGONO, estados E: EXISTENTE D: DISEÑO C: INTERVENIDO
- **Productos_DWG LAYERCAD 43** — Pila: layer CAD PILA, geometría POLÍGONO, estados E: EXISTENTE D: DISEÑO C: INTERVENIDO
- **Productos_DWG LAYERCAD 44** — Pilote: layer CAD PILOTE, geometría POLÍGONO, estados E: EXISTENTE D: DISEÑO C: INTERVENIDO
- **Productos_DWG LAYERCAD 45** — Puente: layer CAD PUENTE, geometría POLÍGONO, estados E: EXISTENTE D: DISEÑO C: INTERVENIDO
- **Productos_DWG LAYERCAD 46** — Rampa de Puente: layer CAD RAMPAPUENTE, geometría POLÍGONO, estados E: EXISTENTE D: DISEÑO C: INTERVENIDO
- **Productos_DWG LAYERCAD 47** — Tablero: layer CAD TABLERO, geometría POLÍGONO, estados E: EXISTENTE D: DISEÑO C: INTERVENIDO
- **Productos_DWG LAYERCAD 48** — Viga: layer CAD VIGA, geometría LÍNEA, estados E: EXISTENTE D: DISEÑO C: INTERVENIDO
- **Productos_DWG LAYERCAD 49** — Estación: layer CAD ESTACION, geometría POLÍGONO, estados E: EXISTENTE D: DISEÑO C: INTERVENIDO
- **Productos_DWG LAYERCAD 50** — Línea Transporte Masivo: layer CAD LINEATM, geometría LÍNEA, estados E: EXISTENTE D: DISEÑO C: INTERVENIDO
- **Productos_DWG LAYERCAD 51** — Paradero: layer CAD PARADERO, geometría PUNTO, estados E: EXISTENTE D: DISEÑO C: INTERVENIDO
- **Productos_DWG LAYERCAD 52** — Bloque Paradero: layer CAD PARADERO, geometría BLOQUE, estados E: EXISTENTE D: DISEÑO C: INTERVENIDO
- **Productos_DWG LAYERCAD 53** — PatioGaraje: layer CAD PATIOGARAJE, geometría POLÍGONO, estados E: EXISTENTE D: DISEÑO C: INTERVENIDO
- **Productos_DWG LAYERCAD 54** — Portal: layer CAD PORTAL, geometría POLÍGONO, estados E: EXISTENTE D: DISEÑO C: INTERVENIDO
- **Productos_DWG LAYERCAD 55** — Torre Cable: layer CAD TORRECABLE, geometría POLÍGONO, estados E: EXISTENTE D: DISEÑO C: INTERVENIDO
- **Productos_DWG LAYERCAD 56** — Bahía: layer CAD BAHIA, geometría POLÍGONO, estados E: EXISTENTE D: DISEÑO C: INTERVENIDO
- **Productos_DWG LAYERCAD 57** — Barrera: layer CAD BARRERA, geometría POLÍGONO, estados E: EXISTENTE D: DISEÑO C: INTERVENIDO
- **Productos_DWG LAYERCAD 58** — Berma: layer CAD BERMA, geometría POLÍGONO, estados E: EXISTENTE D: DISEÑO C: INTERVENIDO
- **Productos_DWG LAYERCAD 59** — Calzada: layer CAD CALZADA, geometría POLÍGONO, estados E: EXISTENTE D: DISEÑO C: INTERVENIDO
- **Productos_DWG LAYERCAD 60** — Defensa: layer CAD DEFENSA, geometría LÍNEA, estados E: EXISTENTE D: DISEÑO C: INTERVENIDO
- **Productos_DWG LAYERCAD 61** — Losa: layer CAD LOSA, geometría POLÍGONO, estados E: EXISTENTE D: DISEÑO C: INTERVENIDO
- **Productos_DWG LAYERCAD 62** — Losa Caja: layer CAD LOSACAJA, geometría POLÍGONO, estados E: EXISTENTE D: DISEÑO C: INTERVENIDO
- **Productos_DWG LAYERCAD 63** — Losa Camara: layer CAD LOSACAMARA, geometría POLÍGONO, estados E: EXISTENTE D: DISEÑO C: INTERVENIDO
- **Productos_DWG LAYERCAD 64** — Losa Pozo: layer CAD LOSAPOZO, geometría POLÍGONO, estados E: EXISTENTE D: DISEÑO C: INTERVENIDO
- **Productos_DWG LAYERCAD 65** — Losa Sumidero: layer CAD LOSASUMIDERO, geometría POLÍGONO, estados E: EXISTENTE D: DISEÑO C: INTERVENIDO
- **Productos_DWG LAYERCAD 66** — Sardinel: layer CAD SARDINEL, geometría LÍNEA, estados E: EXISTENTE D: DISEÑO C: INTERVENIDO
- **Productos_DWG LAYERCAD 67** — Segmento: layer CAD SEGMENTO, geometría LÍNEA, estados E: EXISTENTE D: DISEÑO C: INTERVENIDO
- **Productos_DWG LAYERCAD 68** — Separador: layer CAD SEPARADOR, geometría POLÍGONO, estados E: EXISTENTE D: DISEÑO C: INTERVENIDO
- **Productos_DWG LAYERCAD 69** — Separador Lineal: layer CAD SEPARADORLINEAL, geometría POLÍGONO, estados E: EXISTENTE D: DISEÑO C: INTERVENIDO
- **Productos_DWG LAYERCAD 70** — Área de Intervención: layer CAD AREAINTERVENCION, geometría POLÍGONO, estados E: EXISTENTE D: DISEÑO C: INTERVENIDO
- **Productos_DWG LAYERCAD 71** — Material de Superficie: layer CAD MATERIALSUPERFICIE, geometría POLÍGONO, estados E: EXISTENTE D: DISEÑO C: INTERVENIDO
- **Productos_DWG LAYERCAD 72** — Cuneta: layer CAD CUNETA, geometría POLÍGONO, estados E: EXISTENTE D: DISEÑO C: INTERVENIDO
- **Productos_DWG LAYERCAD 73** — CicloEstación: layer CAD CICLOESTACION, geometría PUNTO, estados E: EXISTENTE D: DISEÑO C: INTERVENIDO
- **Productos_DWG LAYERCAD 74** — Bloque CicloEstación: layer CAD CICLOESTACION, geometría BLOQUE, estados E: EXISTENTE D: DISEÑO C: INTERVENIDO
- **Productos_DWG LAYERCAD 75** — Ciclorruta: layer CAD CICLORRUTA, geometría POLÍGONO, estados E: EXISTENTE D: DISEÑO C: INTERVENIDO
- **Productos_DWG LAYERCAD 76** — Red de Ciclorruta: layer CAD REDCICLORRUTA, geometría LÍNEA, estados E: EXISTENTE D: DISEÑO C: INTERVENIDO
- **Productos_DWG LAYERCAD 77** — Curva de Nivel: layer CAD CURVANIVEL, geometría LÍNEA, estados N / A
- **Productos_DWG LAYERCAD 78** — Delta: layer CAD DELTA, geometría BLOQUE, estados N / A
- **Productos_DWG LAYERCAD 79** — Placa de Amarre: layer CAD PLACAAMARRE, geometría BLOQUE, estados N / A
- **Productos_DWG LAYERCAD 80** — Poligonal: layer CAD POLIGONAL, geometría LÍNEA, estados N / A
- **Productos_DWG LAYERCAD 81** — Punto GPS / GNSS: layer CAD GPS, geometría BLOQUE, estados N / A
#### INSTRUCTIVO_NUEVOSLAYERS

- **Productos_DWG INSTRUCTIVO_NUEVOSLAYERS C1** — #: Numero consecutivo de los registros a relacionar
- **Productos_DWG INSTRUCTIVO_NUEVOSLAYERS C2** — ELEMENTO: nombre del elemento que se quiere representar fisico o abstracto
- **Productos_DWG INSTRUCTIVO_NUEVOSLAYERS C3** — NOMBRE LAYER: nombre del layer empleado en los planos .DWG
- **Productos_DWG INSTRUCTIVO_NUEVOSLAYERS C4** — TIPO DE GEOMETRÍA: TIPO DE GEOMETRIA EMPLEADO: PUNTO LINEA POLIGONO BLOQUE
- **Productos_DWG INSTRUCTIVO_NUEVOSLAYERS C5** — DEFINICIÓN: Breve descripcion del elemento dibujado
#### INSTRUCTIVO_LAYOUT_CIV

- **Productos_DWG INSTRUCTIVO_LAYOUT_CIV C1** — No.: Numero consecutivo de los registros a relacionar
- **Productos_DWG INSTRUCTIVO_LAYOUT_CIV C2** — CIV: Código de Identificación Vial de los tramos relacionados para el contrato
- **Productos_DWG INSTRUCTIVO_LAYOUT_CIV C3** — NUMERO CONTRATO / CONVENIO / URBANISMO: Relación de contrato, convenio o urbanismo de acuerdo al esquema: • IDU-XXXX-XXXX (IDU-NUMERO DE CONTRATO IDU-AÑO DE ADJUDICACIÓN DEL CONTRATO) • CNV-XXXX-XXXX (CONVENIO-NUMERO DEL CONVENIO-AÑO DE ADJUDICACIÓN DEL CONVENIO) • URB-XXXXX (URBANIZACIÓN-NOMBRE DE LA URBANIZACIÓN)
- **Productos_DWG INSTRUCTIVO_LAYOUT_CIV C4** — ETAPA DEL CONTRATO / CONVENIO / URBANISMO: ETAPA DEL CONTRATO QUE SE ESTANDARIZÓ: • PREFACTIBILIDAD • FACTIBILIDAD • DISEÑOS • DIAGNOSTICO • CONSTRUCCIÓN • CONSERVACIÓN
- **Productos_DWG INSTRUCTIVO_LAYOUT_CIV C5** — NOMBRE ARCHIVO: NOMBRE DEL ARCHIVO QUE CONTIENE LOS CÓDIGOS CIV DEL TRAMO A REPRESENTAR TENIENDO EN CUENTA LA PESTAÑA NomenclaturaPlano DEL ARCHIVO EXCEL ParametrosPresenacionPlanos_V1
- **Productos_DWG INSTRUCTIVO_LAYOUT_CIV C6** — NOMBRE LAYOUT: NOMBRE DEL LAYOUT QUE CONTIENE LOS CÓDIGOS CIV DEL TRAMO A REPRESENTAR TENIENDO EN CUENTA LA PESTAÑA NomenclaturaPlano DEL ARCHIVO EXCEL ParametrosPresenacionPlanos_V1
#### EscalasPlanos — 1. GENERAL

- **Productos_DWG Escalas F8** — 1.1. Carátula (Indice de planos): La que se requiera de acuerdo al tipo de proyecto, se debe validar con la Interventoría y la Supervisión del Contrato
#### EscalasPlanos — 2. DIAGNÓSTICO

- **Productos_DWG Escalas F11** — 2.1 Planta: 1 : 250, 1 : 500
#### EscalasPlanos — 3. URBANÍSTICOS

- **Productos_DWG Escalas F13** — 3.1. Espacio Público: 1 : 100, 1 : 200, 1 : 250
- **Productos_DWG Escalas F14** — 3.2. Paisajístico: 1 : 100, 1 : 200, 1 : 250
- **Productos_DWG Escalas F15** — 3.3. Arquitectónico: 1 : 100, 1 : 200, 1 : 250
- **Productos_DWG Escalas F16** — 3.4. Detalles Zonas de interes: 1 : 50
#### EscalasPlanos — 4. TOPOGRAFÍA

- **Productos_DWG Escalas F18** — 4.1. Estudio Topografico: 1 : 200, 1 : 500
#### EscalasPlanos — 5. DISEÑO GEOMÉTRICO

- **Productos_DWG Escalas F20** — 5.1. Planta - Perfil (incluye la nivelación del terreno): 1 : 250, 1 : 500, 1 : 750
- **Productos_DWG Escalas F21** — 5.2. Secciones transversales (Incluye la toma en terreno de la ST) y sección típica: 1 : 50, 1 : 100
- **Productos_DWG Escalas F22** — 5.3. Planta General: 1 : 500, 1 : 750, 1 : 1.000, 1 : 2.000, 1 : 5.000
- **Productos_DWG Escalas F23** — 5.4. Planta Detalle: 1 : 100, 1 : 200, 1 : 250
- **Productos_DWG Escalas F24** — 5.5. Detalles Zonas de interes: 1 : 50, 1 : 100, 1 : 200, 1 : 250
#### EscalasPlanos — 6. GEOTECNIA

- **Productos_DWG Escalas F26** — 6.1. Evaluación Estructural de Pavimento: 1 : 50, 1 : 100, 1 : 200, 1 : 250, 1 : 500
#### EscalasPlanos — 7. ESTRUCTURAS

- **Productos_DWG Escalas F28** — 7.1. Localización de estructuras existentes: 1 : 50, 1 : 100, 1 : 200, 1 : 250, 1 : 500
- **Productos_DWG Escalas F29** — 7.2. Localización de estructuras nuevas: 1 : 50, 1 : 100, 1 : 200, 1 : 250, 1 : 500
#### EscalasPlanos — 9. PREDIOS

- **Productos_DWG Escalas F32** — 9.1. Tira Predial: 1 : 50, 1 : 100, 1 : 200, 1 : 250, 1 : 500, 1 : 750, 1 : 1.000, 1 : 2.000, 1 : 5.000
#### EscalasPlanos — 10. CONSERVACIÓN

- **Productos_DWG Escalas F34** — 10.1. Rehabilitación: 1 : 200, 1 : 250, 1 : 500
- **Productos_DWG Escalas F35** — 10.2. Reconstrucción: 1 : 200, 1 : 250, 1 : 500
- **Productos_DWG Escalas F36** — 10.3. Mantenimiento Periódico: 1 : 200, 1 : 250, 1 : 500
#### EscalasPlanos — 11.ARQUEOLOGÍA

- **Productos_DWG Escalas F38** — 11.1BIC: Depende del proyecto y del tipo de intervención que se vaya a realizar
#### NomenclaturaPlano

- **Productos_DWG Nomenclatura tipo de proyecto F6** — Código de tipo de proyecto PF: Prefactibilidad
- **Productos_DWG Nomenclatura especialidad F6** — Código de especialidad GN: General
- **Productos_DWG Nomenclatura tipo de proyecto F7** — Código de tipo de proyecto FA: Factibilidad
- **Productos_DWG Nomenclatura especialidad F7** — Código de especialidad ET: Estudio Topográfico
- **Productos_DWG Nomenclatura plano F7** — Código de plano CA: Carátula (Indice de Planos)
- **Productos_DWG Nomenclatura tipo de proyecto F8** — Código de tipo de proyecto DI: Diseños
- **Productos_DWG Nomenclatura especialidad F8** — Código de especialidad DG: Diseño Geométrico
- **Productos_DWG Nomenclatura plano F8** — Código de plano LP: Localización del proyecto
- **Productos_DWG Nomenclatura tipo de proyecto F9** — Código de tipo de proyecto DV: Diseño vial
- **Productos_DWG Nomenclatura especialidad F9** — Código de especialidad UR: Urbanístico
- **Productos_DWG Nomenclatura tipo de proyecto F10** — Código de tipo de proyecto DE: Diseño Espacio Público
- **Productos_DWG Nomenclatura especialidad F10** — Código de especialidad GT: Geotecnia
- **Productos_DWG Nomenclatura plano F10** — Código de plano EP: Espacio Público
- **Productos_DWG Nomenclatura tipo de proyecto F11** — Código de tipo de proyecto DA: Diagnóstico Vial
- **Productos_DWG Nomenclatura especialidad F11** — Código de especialidad PV: Pavimentos
- **Productos_DWG Nomenclatura plano F11** — Código de plano PA: Paisajístico
- **Productos_DWG Nomenclatura tipo de proyecto F12** — Código de tipo de proyecto DP: Diagnóstico Espacio Público
- **Productos_DWG Nomenclatura especialidad F12** — Código de especialidad ES: Estructuras
- **Productos_DWG Nomenclatura plano F12** — Código de plano AR: Arquitectónico
- **Productos_DWG Nomenclatura tipo de proyecto F13** — Código de tipo de proyecto CV: Construcción Vial
- **Productos_DWG Nomenclatura especialidad F13** — Código de especialidad RH: Redes Hidrosanitarias
- **Productos_DWG Nomenclatura tipo de proyecto F14** — Código de tipo de proyecto CE: Construcción Espacio Público
- **Productos_DWG Nomenclatura especialidad F14** — Código de especialidad RS: Redes Secas
- **Productos_DWG Nomenclatura plano F14** — Código de plano TO: Topografía
- **Productos_DWG Nomenclatura tipo de proyecto F15** — Código de tipo de proyecto MV: Conservación Vial
- **Productos_DWG Nomenclatura especialidad F15** — Código de especialidad EM: Electromecánico
- **Productos_DWG Nomenclatura tipo de proyecto F16** — Código de tipo de proyecto ME: Conservación Espacio Público
- **Productos_DWG Nomenclatura especialidad F16** — Código de especialidad AM: Ambiental
- **Productos_DWG Nomenclatura plano F16** — Código de plano PL: Planta
- **Productos_DWG Nomenclatura especialidad F17** — Código de especialidad PR: Predial
- **Productos_DWG Nomenclatura plano F17** — Código de plano PE: Perfil longitudinal
- **Productos_DWG Nomenclatura especialidad F18** — Código de especialidad AR: Arqueología
- **Productos_DWG Nomenclatura plano F18** — Código de plano PP: Planta Perfil
- **Productos_DWG Nomenclatura especialidad F19** — Código de especialidad IP: Inventario Puentes
- **Productos_DWG Nomenclatura plano F19** — Código de plano CP: Cotas de Pavimento
- **Productos_DWG Nomenclatura especialidad F20** — Código de especialidad IV: Inventario Vías
- **Productos_DWG Nomenclatura plano F20** — Código de plano ST: Secciones transversales
- **Productos_DWG Nomenclatura especialidad F21** — Código de especialidad IE: Inventario Espacio Público
- **Productos_DWG Nomenclatura plano F21** — Código de plano DG: Detalles geométricos
- **Productos_DWG Nomenclatura plano F23** — Código de plano PG: Planos de diseño geotécnico
- **Productos_DWG Nomenclatura plano F25** — Código de plano EX: Ubicación plan de exploración propuesta
- **Productos_DWG Nomenclatura plano F26** — Código de plano IP: Ubicación exploración información primaria y secundaria
- **Productos_DWG Nomenclatura plano F27** — Código de plano TH: Sectorización tramos homogeneos
- **Productos_DWG Nomenclatura plano F28** — Código de plano ES: Plano o esquema de secciones típicas de las diferentes secciones transversales de pavimentos para vía y espacio público asociado
- **Productos_DWG Nomenclatura plano F29** — Código de plano PS: Perfiles estratigráficos
- **Productos_DWG Nomenclatura plano F30** — Código de plano VD: Vias de desvío propuestas
- **Productos_DWG Nomenclatura plano F32** — Código de plano LE: Localización estructuras existentes
- **Productos_DWG Nomenclatura plano F33** — Código de plano LN: Localización estructuras nuevas
- **Productos_DWG Nomenclatura plano F34** — Código de plano DD: Detalles de diseño
- **Productos_DWG Nomenclatura plano F36** — Código de plano RE: Planos de redes existentes y proyectadas
- **Productos_DWG Nomenclatura plano F38** — Código de plano DR: Diseño redes
- **Productos_DWG Nomenclatura plano F40** — Código de plano TP: Tira topográfica
- **Productos_DWG Nomenclatura plano F41** — Código de plano RT: Registro topográfico
- **Productos_DWG Nomenclatura plano F43** — Código de plano BI: BIC
- **Productos_DWG Nomenclatura plano F44** — Código de plano AQ: Arqueología
