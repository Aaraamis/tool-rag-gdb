# Diccionario de atributos de la BDG — proyecto de construcción

> Generado por `rag-gdb diccionario` el 2026-11-19 desde `Productos_BDG_valores.ods` (sha256 `33b5af986dc1ca21…`), exportación a ODS de `Productos_BDG.xlsm` del alistamiento IDU 2020. La plantilla original rige; este documento la resume para crear y revisar capas.
> **Marca** para «Proyecto: Construcción»: **obligatorio** (X roja en la plantilla), **según alcance** (X verde: obligatorio si el contrato interviene ese elemento) o vacío (no aplica). El color de la fuente se lee del ODS; «X sin convención de color» indica una marca que hay que confirmar en la plantilla.

## Resumen por feature dataset

| Feature dataset | Clase de entidad | Geometría | Tablas relacionadas | Obligatorios | Según alcance |
|---|---|---|---:|---:|---:|
| Ambiental | [Arbol](#arbol) | PUNTO | 0 | 7 | 0 |
| DirectorioProveedores | [Proveedores](#proveedores) | PUNTO | 1 | 0 | 0 |
| EspacioPublico | [Alameda](#alameda) | POLÍGONO | 0 | 7 | 0 |
| EspacioPublico | [Anden](#anden) | POLÍGONO | 3 | 22 | 0 |
| EspacioPublico | [Plaza](#plaza) | POLÍGONO | 1 | 16 | 0 |
| EspacioPublico | [Pompeyano](#pompeyano) | POLÍGONO | 0 | 7 | 0 |
| EspacioPublico | [Rampa](#rampa) | POLÍGONO | 0 | 8 | 0 |
| ExploracionEnsayos | [Exploracion](#exploracion) | PUNTO | 8 | 36 | 86 |
| InfraestructuraEspecial | [Escalera](#escalera) | POLÍGONO | 0 | 11 | 0 |
| InfraestructuraEspecial | [Muro](#muro) | POLÍGONO | 0 | 9 | 0 |
| InfraestructuraEspecial | [Talud](#talud) | POLÍGONO | 0 | 12 | 0 |
| InfraestructuraEspecial | [Terraplen](#terraplen) | POLÍGONO | 0 | 9 | 0 |
| InfraestructuraMobiliario | [BarandaPeatonal](#barandapeatonal) | LÍNEA | 1 | 12 | 0 |
| InfraestructuraMobiliario | [Mobiliario](#mobiliario) | PUNTO | 1 | 11 | 0 |
| InfraestructuraMobiliario | [Pileta](#pileta) | POLÍGONO | 0 | 5 | 0 |
| InfraestructuraPuente | [Puente](#puente) | POLÍGONO | 5 | 27 | 2 |
| InfraestructuraPuente | [PuenteElementoLinea](#puenteelementolinea) | LÍNEA | 3 | 20 | 0 |
| InfraestructuraPuente | [PuenteElementoPoligono](#puenteelementopoligono) | POLÍGONO | 3 | 20 | 0 |
| InfraestructuraTransporte | [Estacion](#estacion) | POLÍGONO | 0 | 8 | 0 |
| InfraestructuraTransporte | [LineaTM](#lineatm) | LÍNEA | 0 | 13 | 0 |
| InfraestructuraTransporte | [Paradero](#paradero) | PUNTO | 2 | 17 | 0 |
| InfraestructuraTransporte | [PatioGaraje](#patiogaraje) | POLÍGONO | 0 | 5 | 0 |
| InfraestructuraTransporte | [Portal](#portal) | POLÍGONO | 0 | 6 | 0 |
| InfraestructuraTransporte | [TorreCable](#torrecable) | POLÍGONO | 0 | 14 | 0 |
| InfraestructuraVial | [Bahia](#bahia) | POLÍGONO | 0 | 6 | 0 |
| InfraestructuraVial | [Barrera](#barrera) | POLÍGONO | 0 | 5 | 0 |
| InfraestructuraVial | [Berma](#berma) | POLÍGONO | 0 | 8 | 0 |
| InfraestructuraVial | [Calzada](#calzada) | POLÍGONO | 24 | 76 | 64 |
| InfraestructuraVial | [Defensa](#defensa) | LÍNEA | 0 | 5 | 0 |
| InfraestructuraVial | [Losa](#losa) | POLÍGONO | 3 | 24 | 7 |
| InfraestructuraVial | [Sardinel](#sardinel) | LÍNEA | 0 | 13 | 0 |
| InfraestructuraVial | [Segmento](#segmento) | LÍNEA | 0 | 6 | 0 |
| InfraestructuraVial | [Separador](#separador) | POLÍGONO | 3 | 22 | 0 |
| InfraestructuraVial | [SeparadorLineal](#separadorlineal) | POLÍGONO | 0 | 5 | 0 |
| IntervencionInfraestructuraVial | [AreaIntervencion](#areaintervencion) | POLÍGONO | 2 | 28 | 0 |
| IntervencionInfraestructuraVial | [Diseno](#diseno) | POLÍGONO | 1 | 0 | 0 |
| IntervencionInfraestructuraVial | [SeguimientoLinea](#seguimientolinea) | LÍNEA | 1 | 0 | 0 |
| IntervencionInfraestructuraVial | [SeguimientoPoligono](#seguimientopoligono) | POLÍGONO | 1 | 14 | 1 |
| IntervencionInfraestructuraVial | [SeguimientoPunto](#seguimientopunto) | PUNTO | 1 | 0 | 0 |
| RedInfraestructuraCicloInclusiva | [CicloEstacion](#cicloestacion) | PUNTO | 0 | 6 | 0 |
| RedInfraestructuraCicloInclusiva | [Ciclorruta](#ciclorruta) | POLÍGONO | 3 | 23 | 12 |
| RedInfraestructuraCicloInclusiva | [RedCiclorruta](#redciclorruta) | LÍNEA | 0 | 8 | 0 |
| RedesAguaAlcantarillado | [Cuneta](#cuneta) | POLÍGONO | 0 | 12 | 0 |

## Ambiental

### Arbol

Geometría **punto**; elementos: Árbol.
Planta leñosa con un tronco principal que sostiene un follaje denominado copa, de arquitectura según la especie, cuya altura en estado adulto no sea inferior a tres (3) metros, medidos desde el nivel del suelo. El codigo correspondera al relacionado en el SIGAU

Atributos de **Arbol**

| Campo | Alias | Tipo | Unidad | Dominio o rango | Marca |
|---|---|---|---|---|---|
| `CodigoArbol` | Código Árbol | Texto | N / A |  | obligatorio |
| `CodigoEspecia` | Código Especie | Entero | N / A |  | obligatorio |
| `NombreEspecie` | Nombre Especie | Texto | N / A |  | obligatorio |
| `AlturaTotal` | Altura Total | Decimal | Metro (m) | rango 1.5 a 20 | obligatorio |
| `TipoEmplazamiento` | Tipo Emplazamiento | Texto | N / A | `1` Rondas nacimientos y quebradas; `2` Rondas ríos y canales; `3` Parques: metrop., zonales, barriales; `4` Plazas; `5` Plazoletas; `6` Franja de control ambiental; `7` Antejardines; `8` Corredores férreos; `9` Conformación espacio vehicular; `10` Separador blando angosto; `11` Separador blando ancho; `12` Separador mixto angosto; `13` Separador superficie dura; `14` Glorieta e intersección vial; `15` Orejas de puentes; `16` Ciclorrutas Vías peatonales (V-9); `17` Andén sin zona verde (3 m en adelante); `18` Alameda; `19` Andén con zona verde angosta; `20` Andén con zona verde ancha; `21` Areneras; `22` Gravilleras; `23` Chircales; `24` Basureros; `25` Escombreras; `26` Líneas conducción energía; `27` Redes matrices servicios públicos | obligatorio |
| `IntervencionIDU` | Intervencion IDU | Entero | N / A | `1` Tala; `2` Bloqueo y Traslado; `3` Permanencia; `4` Plantados; `5` Poda | obligatorio |
| `FechaActualizacion` | Fecha de actualización | Fecha | N / A |  | obligatorio |

## DirectorioProveedores

### Proveedores

Geometría **punto**; elementos: Proveedores.
Cobertura informativa que detalla los proveedores registrados en el "Directorio de Proveedores de Materiales de Construcción, Sitios de Disposición final, Aprovechamiento y Tratamiento de Residuos de Construcción y Demolición RCD del IDU" con geometría Punto y toda la informacion asociada a la base de datos (SIAC) del directorio.

Atributos de **Proveedores**

| Campo | Alias | Tipo | Unidad | Dominio o rango | Marca |
|---|---|---|---|---|---|
| `PK_ID_Proveedores` | PK_ID_Proveedores | Entero Largo | N / A |  |  |
| `InscripcionIDU` | Inscripción IDU | Entero Largo | N / A |  |  |
| `ano` | año Inscripción | Entero Largo | N / A |  |  |
| `Categoria` | Categoría | Entero Corto | N / A | `1` Agregados pétreos; `2` Agregados pétreos a partir de material de escombros reciclados; `3` Concreto hidráulico; `4` Disposición final de escombros; `5` Disposición final de escombros estériles y materiales seleccionados; `6` Disposición final de material de excavación; `7` Ladrillo y productos de arcilla; `8` Mezclas asfálticas; `9` Prefabricados; `10` Reciclaje y aprovechamiento de residuos de construcción y demolición |  |
| `RazonSocial` | Nombre Empresa | Texto | N / A |  |  |
| `NIT` | Numero de Identificación Tributaria | Texto | N / A |  |  |
| `Representante` | Representante Legal | Texto | N / A |  |  |
| `Direccion` | Dirección de Correspondencia | Texto | N / A |  |  |
| `Telefono` | Numero telefónico | Texto | N / A |  |  |
| `Municipio` | Municipio del Predio o Lote | Texto | N / A |  |  |
| `Predio` | Predio o Lote | Texto | N / A |  |  |
| `PermisoMinero` | Permiso Minero | Texto | N / A |  |  |
| `V_A_A_Minero` | Vigencia Acto Administrativo Minero | Texto | N / A |  |  |
| `PermisoAmbiental` | Permiso Ambiental | Texto | N / A |  |  |
| `V_A_A_Ambiental` | Vigencia Acto Administrativo Ambiental | Texto | N / A |  |  |
| `Tipo de permiso` | Tipo de Permiso | Texto | N / A |  |  |
| `AutoridadAmbiental` | Autoridad Ambiental | Entero Corto | N / A | `1` ALCALDIA DE SOACHA; `2` ANLA; `3` CAR; `4` CAR - ALCALDIA MOSQUERA; `5` CORTOLIMA; `6` CORMACARENA; `7` SDA; `8` CORPORINOQUIA; `9` CAR - ALCALDIA SOACHA |  |
| `Contacto` | Persona de Contacto | Texto | N / A |  |  |
| `Correo` | contacto email | Texto | N / A |  |  |
| `FechaRadicadoIDU` | Fecha Radicado IDU | Fecha | N / A |  |  |
| `Radicado_IDU` | Radicado IDU | Texto | N / A |  |  |
| `Estado` | Estado | Entero Corto | N / A | `1` ACTIVO; `2` INACTIVO |  |
| `FechaVigencia` | Fecha de vigencia | Fecha | N / A |  |  |
| `Productos` | Productos | Texto | N / A |  |  |
| `Observacion` | Observaciones Generales | Texto | N / A |  |  |

Tabla relacionada **Registro_Proveedores** (Registro de Proveedores), de Proveedores

| Campo | Alias | Tipo | Unidad | Dominio o rango | Marca |
|---|---|---|---|---|---|
| `PK_ID_Proveedores` | PK_ID_Proveedores | Entero Largo | N / A |  |  |
| `FK_ID_Proveedores` | PK_ID_Proveedores | Entero Largo | N / A |  |  |
| `InscripcionIDU` | Inscripción IDU | Entero Largo | N / A |  |  |
| `ano` | año Inscripción | Entero Largo | N / A |  |  |
| `Categoria` | Categoría | Entero Corto | N / A | `1` Agregados pétreos; `2` Agregados pétreos a partir de material de escombros reciclados; `3` Concreto hidráulico; `4` Disposición final de escombros; `5` Disposición final de escombros estériles y materiales seleccionados; `6` Disposición final de material de excavación; `7` Ladrillo y productos de arcilla; `8` Mezclas asfálticas; `9` Prefabricados; `10` Reciclaje y aprovechamiento de residuos de construcción y demolición |  |
| `RazonSocial` | Nombre Empresa | Texto | N / A |  |  |
| `NIT` | Numero de Identificación Tributaria | Texto | N / A |  |  |
| `Representante` | Representante Legal | Texto | N / A |  |  |
| `Direccion` | Dirección de Correspondencia | Texto | N / A |  |  |
| `Telefono` | Numero telefónico | Texto | N / A |  |  |
| `Municipio` | Municipio del Predio o Lote | Texto | N / A |  |  |
| `Predio` | Predio o Lote | Texto | N / A |  |  |
| `PermisoMinero` | Permiso Minero | Texto | N / A |  |  |
| `V_A_A_Minero` | Vigencia Acto Administrativo Minero | Texto | N / A |  |  |
| `PermisoAmbiental` | Permiso Ambiental | Texto | N / A |  |  |
| `V_A_A_Ambiental` | Vigencia Acto Administrativo Ambiental | Texto | N / A |  |  |
| `Tipo de permiso` | Tipo de Permiso | Texto | N / A |  |  |
| `AutoridadAmbiental` | Autoridad Ambiental | Entero Corto | N / A | `1` ALCALDIA DE SOACHA; `2` ANLA; `3` CAR; `4` CAR - ALCALDIA MOSQUERA; `5` CORTOLIMA; `6` CORMACARENA; `7` SDA; `8` CORPORINOQUIA; `9` CAR - ALCALDIA SOACHA |  |
| `Contacto` | Persona de Contacto | Texto | N / A |  |  |
| `Correo` | contacto email | Texto | N / A |  |  |
| `FechaRadicadoIDU` | Fecha Radicado IDU | Fecha | N / A |  |  |
| `Radicado_IDU` | Radicado IDU | Texto | N / A |  |  |
| `Estado` | Estado | Entero Corto | N / A | `1` ACTIVO; `2` INACTIVO |  |
| `FechaVigencia` | Fecha de vigencia | Fecha | N / A |  |  |
| `Productos` | Productos | Texto | N / A |  |  |
| `Observacion` | Observaciones Generales | Texto | N / A |  |  |
| `FechaModificacion` | Fecha | Fecha | N / A |  |  |
| `ObservacionModificacion` | Observaciones de la Modificación | Texto | N / A |  |  |
| `Responsable` | Responsable de la Modificación | Texto | N / A |  |  |
| `Origen` | Origen de la Modificación | Texto | N / A |  |  |

## EspacioPublico

### Alameda

Geometría **polígono**; elementos: Alameda.
Franja de circulación peatonal arborizada y dotada del respectivo mobiliario urbano.

Atributos de **Alameda**

| Campo | Alias | Tipo | Unidad | Dominio o rango | Marca |
|---|---|---|---|---|---|
| `PK_ID_Alameda` | PK_ID_Alameda | Entero Largo | N / A |  | obligatorio |
| `CIV` | CIV | Entero Largo | N / A |  | obligatorio |
| `Nombre` | Nombre de la Alameda | Texto | N / A |  | obligatorio |
| `Estado` | Estado de condición | Texto | N / A | `B` Bueno; `R` Regular; `M` Malo | obligatorio |
| `LongitudAlameda` | Longitud de la Alameda | Decimal | Metro (m) | rango 100 a 2000 | obligatorio |
| `AnchoAlameda` | Ancho de la Alameda | Decimal | Metro (m) | rango 5 a 50 | obligatorio |
| `FechaRegistro` | Fecha de Registro | Fecha | N / A |  | obligatorio |

### Anden

Geometría **polígono**; elementos: Andén.
Zona o franja paralela a la vía de uso vehicular, destinada a la permanencia o tránsito de peatones. Su superficie debe ser dura para su circulación no obstante, dependiendo de la tipología que se defina, pueden generarse composiciones con superficies blandas (zonas verdes). Generalmente el andén se encuentra a un nivel superior al de la calzada para proteger al peatón del tráfico de la …

Atributos de **Anden**

| Campo | Alias | Tipo | Unidad | Dominio o rango | Marca |
|---|---|---|---|---|---|
| `PK_ID_Anden` | PK_ID_Anden | Entero Largo | N / A |  | obligatorio |
| `CIV` | CIV | Entero Largo | N / A |  | obligatorio |
| `TipoMaterial` | Tipo de material del andén | Entero | N / A | `1` Concreto; `2` Adoquín; `3` Tableta; `4` Mixto; `6` Tierra; `7` Grama | obligatorio |
| `Localidad` | Localidad | Entero | N / A | `1` Usaquen; `2` Chapinero; `3` Santa Fe; `4` San Cristóbal; `5` Usme; `6` Tunjuelito; `7` Bosa; `8` Kennedy; `9` Fontibon; `10` Engativa; `11` Suba; `12` Barrios Unidos; `13` Teusaquillo; `14` Los Mártires; `15` Antonio Nariño; `16` Puente Aranda; `17` La Candelaria; `18` Rafael Uribe Uribe; `19` Ciudad Bolívar; `20` Sumapaz |  |
| `AnchoAnden` | Ancho del Andén | Decimal | Metro (m) | rango 0.5 a 15 | obligatorio |
| `LongitudAnden` | Longitud del Andén | Decimal | Metro (m) | rango 5 a 150 | obligatorio |
| `AreaAnden` | Área del Andén | Decimal | Metro cuadrado (m2) | rango 3 a 1500 | obligatorio |
| `FechaRegistro` | Fecha de Registro | Fecha | N / A |  | obligatorio |

Tabla relacionada **DetalleAndenSeparador** (Detalle Andén y Separador), de Anden

| Campo | Alias | Tipo | Unidad | Dominio o rango | Marca |
|---|---|---|---|---|---|
| `PK_ID_DetalleAndenSeparador` | PK_ID_DetalleAndenSeparador | Entero Largo | N / A |  | obligatorio |
| `FK_ID_DetalleAndenSeparador` | FK_ID_DetalleAndenSeparador | Entero Largo | N / A |  | obligatorio |
| `Estado` | Estado de condición | Texto | N / A | `B` Bueno; `R` Regular; `M` Malo | obligatorio |
| `Homogeneo` | Homogeneo | Entero | Porcentaje (%) | rango 0 a 100 | obligatorio |
| `Homologado` | Homologado | Entero | Porcentaje (%) | rango 0 a 100 | obligatorio |
| `Obstaculos` | Obstaculos | Entero | Porcentaje (%) | rango 0 a 100 | obligatorio |
| `CambioNiveles` | Cambio de Niveles | Texto | N / A | `S` Si; `N` No | obligatorio |
| `RedesSubterraneas` | Redes Subterraneas | Texto | N / A | `S` Si; `N` No | obligatorio |
| `ICEASEP` | Índice de Condición de Estado de Andenes y Separadores | Entero | Porcentaje (%) | rango 0 a 100 | obligatorio |
| `FechaMedicionICEASEP` | Fecha medición del ICEA | Fecha | N / A |  | obligatorio |

Tabla relacionada **AccesibilidadAndSep** (Accesibilidad Andén y Separador), de Anden

| Campo | Alias | Tipo | Unidad | Dominio o rango | Marca |
|---|---|---|---|---|---|
| `PK_ID_AccesibilidadAndenSeparador` | PK_ID_AccesibilidadAndenSeparador | Entero Largo | N / A |  | obligatorio |
| `FK_ID_Accesibilidad` | FK_ID_Accesibilidad | Entero Largo | N / A |  | obligatorio |
| `Senalinvidentes` | Señal Invidentes | Texto | N / A | `S` Si; `N` No | obligatorio |
| `Desnivel` | Accesibilidad | Texto | N / A | `S` Si; `N` No | obligatorio |
| `Vados` | Vados | Texto | N / A | `S` Si; `N` No | obligatorio |

Tabla relacionada **FallaAndenSeparador** (Fallas de Andén y Separador), de Anden

| Campo | Alias | Tipo | Unidad | Dominio o rango | Marca |
|---|---|---|---|---|---|
| `PK_ID_FallaAndenSeparador` | PK_ID_FallaAndenSeparador | Entero Largo | N / A |  |  |
| `FK_ID_FallaAndenSeparador` | FK_ID_FallaAndenSeparador | Entero Largo | N / A |  |  |
| `CodigoDano` | Codigo Daño | Texto | N / A | `D1` Abollado; `D2` Hundido; `D3` Fisurado; `D4` Roto; `D5` Partido; `D6` Golpeado; `D7` Inclinado; `D8` Obstaculización; `D9` Maleza; `D10` Perdida de sello; `D11` Grafiteado; `D12` Pintado; `D13` Desportillado; `D14` Faltante; `D15` Mal estado; `D16` Faltante de Pintura; `D17` Enterrado; `D18` No Se Reportan Daños; `D19` Bordeo; `D20` Destrucción de Alcorque |  |
| `AccionCorrectiva` | Accion Correctiva | Entero | N / A | `1` Reemplazar; `2` Retirar; `3` Reinstalar; `4` Reparar; `5` Mantener |  |
| `TipoMantenimiento` | Tipo Mantenimiento | Entero | N / A | `1` Correctivo; `2` Rehabilitación; `3` Rutinario |  |

### Plaza

Geometría **polígono**; elementos: Plaza.
Espacio abierto tratado como zona dura, que ocupa una manzana completa. Se encuentra destinado al ejercicio de actividades de convivencia ciudadana, recreación pasiva y congregación. Son grandes áreas con superficies duras y deben cumplir los mismos requisitos de los andenes en su periferia y en lo relativo a las discontinuidades que pueda tener su superficie.

Atributos de **Plaza**

| Campo | Alias | Tipo | Unidad | Dominio o rango | Marca |
|---|---|---|---|---|---|
| `PK_ID_Plaza` | PK_ID_Plaza | Entero Largo | N / A |  | obligatorio |
| `CIV` | CIV | Entero Largo | N / A |  | obligatorio |
| `Nombre` | Nombre de la plaza | Texto | N / A |  | obligatorio |
| `Estado` | Estado de condición | Texto | N / A | `B` Bueno; `M` Malo; `R` Regular | obligatorio |
| `Direccion` | Dirección | Texto | N / A |  | obligatorio |
| `AreaPlaza` | Área | Decimal | Metro cuadrado (m2) | rango 10 a 30000 | obligatorio |
| `TipoPlaza` | Tipo de plaza | Entero | N / A | `0` Plaza; `1` Plazoleta; `3` Plazuela | obligatorio |
| `FechaRegistro` | Fecha de Registro | Fecha | N / A |  | obligatorio |

Tabla relacionada **DetallePlaza** (Detalle Plaza), de Plaza

| Campo | Alias | Tipo | Unidad | Dominio o rango | Marca |
|---|---|---|---|---|---|
| `PK_ID_DetallePlaza` | PK_ID_DetallePlaza | Entero Largo | N / A |  | obligatorio |
| `FK_ID_Plaza` | FK_ID_Plaza | Entero Largo | N / A |  | obligatorio |
| `AreaPrestamo` | Área prestamo | Decimal | Metro cuadrado (m2) |  | obligatorio |
| `AreaZV` | Área zona verde | Decimal | Metro cuadrado (m2) |  | obligatorio |
| `AreaPLSE` | Área PLSE | Decimal | Metro cuadrado (m2) |  | obligatorio |
| `Canchas` | Canchas | Entero | Adimensional |  | obligatorio |
| `JuegosInfantiles` | Juegos infantiles | Texto | N / A | `S` Si; `N` No | obligatorio |
| `NumeroJuegos` | Número juegos | Entero | Adimensional |  | obligatorio |

### Pompeyano

Geometría **polígono**; elementos: Pompeyano.
Los pompeyanos son elementos cuyo objetivo es garantizar la seguridad del peatón y priorizar su paso de forma segura y autónoma cuando la franja de andén es interceptada por el paso vehicular, por lo general se ubican en la intersección de la malla vial arterial con la local.

Atributos de **Pompeyano**

| Campo | Alias | Tipo | Unidad | Dominio o rango | Marca |
|---|---|---|---|---|---|
| `PK_ID_Pompeyano` | PK_ID_Pompeyano | Entero Largo | N / A |  | obligatorio |
| `CIV` | CIV | Entero Largo | N / A |  | obligatorio |
| `TipoMaterialPompeyano` | Tipo de material del pompeyano | Entero | N / A | `0` Concreto; `1` Adoquín; `2` Concreto Estampado; `3` Adoquín Arcilla | obligatorio |
| `AnchoPompeyano` | Ancho | Decimal | Metro (m) |  | obligatorio |
| `AltoPompeyano` | Alto del pompeyano | Decimal | Metro (m) |  | obligatorio |
| `LongitudPompeyano` | Longitud | Decimal | Metro (m) |  | obligatorio |
| `FechaRegistro` | Fecha de Registro | Fecha | N / A |  | obligatorio |

### Rampa

Geometría **polígono**; elementos: Rampa.
Elemento arquitectónico mediante el cual se accede de un nivel a otro sin generar peldaños, gradas o escalas permitiendo continuidad a la circulación a través de una pendiente o inclinación moderada de la superficie y su estructura. Los porcentajes de inclinación de las rampas deben obedecer a usos específicos y a normas establecidas para tal fin.

Atributos de **Rampa**

| Campo | Alias | Tipo | Unidad | Dominio o rango | Marca |
|---|---|---|---|---|---|
| `PK_ID_Rampa` | DiccionarioAtributos | Entero Largo | N / A |  | obligatorio |
| `CIV` | CIV | Entero Largo | N / A |  | obligatorio |
| `Estado` | Estado de condición | Texto | N / A | `B` Bueno; `M` Malo; `R` Regular | obligatorio |
| `Tipo` | Tipo de rampa | Texto | N / A | `RC` Rampa para ciclo-ruta en calzada B15; `B5` Rampa peatonal estándar B5; `B10` B10 Rampa vehicular tipo A; `B12` B12 Rampa vehicular tipo B; `B13` B13 Rampa vehicular tipo C | obligatorio |
| `Ancho` | Ancho Rampa | Decimal | Metro (m) | rango 0.5 a 5 | obligatorio |
| `Longitud` | Longitud Rampa | Decimal | Metro (m) | rango 0.5 a 5 | obligatorio |
| `Area` | Area Rampa | Decimal | Metro cuadrado (m2) | rango 0.2 a 20 | obligatorio |
| `FechaRegistro` | Fecha Registro | Fecha | N / A |  | obligatorio |

## ExploracionEnsayos

### Exploracion

Geometría **punto**; elementos: Exploración.
Proceso para la identificación de los estratos de depósitos que subyacen bajo una estructura propuesta y sus características físicas

Atributos de **Exploracion**

| Campo | Alias | Tipo | Unidad | Dominio o rango | Marca |
|---|---|---|---|---|---|
| `PK_ID_Exploracion` | PK_ID_Exploracion | Entero Largo | N / A |  | obligatorio (Sondeo, Apique, Barreno, Trinchera manual) |
| `Tipo` | Tipo | Texto | N / A | `S` Sondeo; `A` Apique; `B` Barreno; `T` Trinchera Manual | obligatorio (Sondeo, Apique, Barreno, Trinchera manual) |
| `Ubicacion` | Ubicación | Entero | N / A | `1` Calzada; `2` Anden; `3` Zona Verde; `4` Separador; `5` Ciclorruta | obligatorio (Sondeo, Apique, Barreno, Trinchera manual) |
| `Costado` | Costado | Texto | N / A | `I` Izquierdo; `D` Derecho | obligatorio (Sondeo, Apique, Barreno, Trinchera manual) |
| `FechaInicio` | Fecha Inicio | Fecha | N / A |  | obligatorio (Sondeo, Apique, Barreno, Trinchera manual) |
| `FechaTerminacion` | Fecha Terminación | Fecha | N / A |  | obligatorio (Sondeo, Apique, Barreno, Trinchera manual) |
| `ProfundidadTotal` | Profundidad Total | Decimal | Metro (m) |  | obligatorio (Sondeo, Apique, Barreno, Trinchera manual) |
| `NumMuestras` | Número Muestras | Entero | Adimensional | rango 1 a — | obligatorio (Sondeo, Apique, Barreno, Trinchera manual) |
| `ProfundidadRoca` | Profundidad Roca | Decimal | Metro (m) |  | obligatorio (Sondeo, Apique, Barreno, Trinchera manual) |
| `CESuelo` | Exploración en Suelo | Decimal | Metro (m) |  | obligatorio (Sondeo, Apique, Barreno, Trinchera manual) |
| `CERoca` | Exploración en Roca | Decimal | Metro (m) |  | obligatorio (Sondeo, Apique, Barreno, Trinchera manual) |
| `CESueloP` | Exploración en Suelo Porcentaje | Decimal | Porcentaje (%) | rango 0 a 100 | obligatorio (Sondeo, Apique, Barreno, Trinchera manual) |
| `CERocaP` | Exploración en Roca Porcentaje | Decimal | Porcentaje (%) | rango 0 a 100 | obligatorio (Sondeo, Apique, Barreno, Trinchera manual) |
| `InstPiezómetro` | Instalación de Piezómetro | Texto | N / A | `S` Si; `N` No | obligatorio (Sondeo, Apique, Barreno, Trinchera manual) |

Tabla relacionada **P_EnsayoSPT** (Ensayo Campo SPT), de Exploracion

| Campo | Alias | Tipo | Unidad | Dominio o rango | Marca |
|---|---|---|---|---|---|
| `PK_ID_EnsayoSPT` | PK_ID_EnsayoSPT | Entero Largo | N / A |  | obligatorio (Sondeo) |
| `FK_ID_Exploracion` | FK_ID_Exploracion | Entero Largo | N / A |  | obligatorio (Sondeo) |
| `Prof_Inc` | Profundidad inicial muestra | Decimal | Metro (m) |  | obligatorio (Sondeo) |
| `Prof_Final` | Profundidad final muestra | Decimal | Metro (m) |  | obligatorio (Sondeo) |
| `F1_6_SPT` | 1_6__SPT | Entero | Adimensional |  | obligatorio (Sondeo) |
| `F2_6_SPT` | 2_6__SPT | Entero | Adimensional |  | obligatorio (Sondeo) |
| `F3_6_SPT` | 3_6__SPT | Entero | Adimensional |  | obligatorio (Sondeo) |
| `N` | N | Entero |  |  | obligatorio (Sondeo) |
| `NC` | N Corregido | Entero |  |  | obligatorio (Sondeo) |
| `R` | R | Decimal | Metro (m) |  | obligatorio (Sondeo) |
| `PR` | %R | Entero | Porcentaje (%) | rango 0 a 100 | obligatorio (Sondeo) |

Tabla relacionada **S_Piezometros** (Sondeo Piezometros), de Exploracion

| Campo | Alias | Tipo | Unidad | Dominio o rango | Marca |
|---|---|---|---|---|---|
| `PK_ID_Piezometros` | No de piezometro | Entero Largo | N / A |  | según alcance (Sondeo) |
| `FK_ID_Exploracion` | FK_ID_Exploracion | Entero Largo | N / A |  | según alcance (Sondeo) |
| `Profundidad` | Profundidad | Decimal | Metro (m) |  | según alcance (Sondeo) |
| `NFInicial` | Nivel Freatico Inicial | Decimal | Metro (m) | rango 0 a — | según alcance (Sondeo) |
| `NFFinal` | Nivel Freatico Final | Decimal | Metro (m) | rango 0 a — | según alcance (Sondeo) |
| `Tipo` | Tipo | Texto | N / A |  | según alcance (Sondeo) |
| `L_Fecha` | Lecturas Fecha | Fecha |  |  | según alcance (Sondeo) |
| `L_Agua` | Lecturas Agua | Texto |  |  | según alcance (Sondeo) |
| `ProfundidadLamina` | Profundidad Lamina | Decimal |  |  | según alcance (Sondeo) |
| `Rotura` | Rotura | Texto |  |  | según alcance (Sondeo) |
| `ProfundidadRotura` | Profundidad Rotura | Decimal |  |  | según alcance (Sondeo) |

Tabla relacionada **P_EnsayoCampo** (Ensayo Campo), de Exploracion

| Campo | Alias | Tipo | Unidad | Dominio o rango | Marca |
|---|---|---|---|---|---|
| `PK_ID_EnsayoCampo` | PK_ID_EnsayoCampo | Entero Largo | N / A |  | según alcance (Sondeo, Apique, Barreno, Trinchera manual) |
| `FK_ID_Exploracion` | FK_ID_Exploracion | Entero Largo | N / A |  | según alcance (Sondeo, Apique, Barreno, Trinchera manual) |
| `ProfundadInstrumento` | Profundidad Instrumento | Decimal | Metro (m) |  | según alcance (Sondeo, Apique, Barreno, Trinchera manual) |
| `RQD` | RQD | Decimal | Porcentaje (%) | rango 0 a 100 | según alcance (Sondeo, Apique, Barreno, Trinchera manual) |
| `CPT_Res_Cono_qc` | CPT Resistencia del Cono | Decimal | Kilogramo por centímetro cuadrado (kg/cm2) |  | según alcance (Sondeo, Apique, Barreno, Trinchera manual) |
| `CPT_Res_Fricc_fc` | CPT Resistencia por Fricción | Decimal | Kilogramo por centímetro cuadrado (kg/cm2) |  | según alcance (Sondeo, Apique, Barreno, Trinchera manual) |
| `Veleta_Suv` | Veleta Suv | Decimal | Kilogramo por centímetro cuadrado (kg/cm2) |  | según alcance (Sondeo, Apique, Barreno, Trinchera manual) |
| `Veleta_Surv` | Veleta Surv | Decimal | Kilogramo por centímetro cuadrado (kg/cm2) |  | según alcance (Sondeo, Apique, Barreno, Trinchera manual) |
| `Veleta_Stv` | Veleta Stv | Decimal | Adimensional |  | según alcance (Sondeo, Apique, Barreno, Trinchera manual) |
| `PenetrometroBolsillo_qu` | Penetrómetro de Bolsillo | Decimal | Kilogramo por centímetro cuadrado (kg/cm2) |  | según alcance (Sondeo, Apique, Barreno, Trinchera manual) |
| `NivelPiezometrico` | Nivel Piezométrico | Decimal | Metro (m) |  | según alcance (Sondeo, Apique, Barreno, Trinchera manual) |
| `Perme_Campo_Tipo` | Tipo Permeabilidad Suelo | Texto | N / A |  | según alcance (Sondeo, Apique, Barreno, Trinchera manual) |
| `Perme_Campo_K` | Permeabilidad hidráulica Suelo | Decimal | Centímetro por segundo (cm/s) |  | según alcance (Sondeo, Apique, Barreno, Trinchera manual) |

Tabla relacionada **P_RegistroCampo** (Registro Campo), de Exploracion

| Campo | Alias | Tipo | Unidad | Dominio o rango | Marca |
|---|---|---|---|---|---|
| `PK_ID_RegistroCampo` | PK_ID_RegistroCampo | Entero Largo | N / A |  | según alcance (Sondeo, Apique, Barreno, Trinchera manual) |
| `FK_ID_Exploracion` | FK_ID_Exploracion | Entero Largo | N / A |  | según alcance (Sondeo, Apique, Barreno, Trinchera manual) |
| `Revestimiento` | Revestimiento | Texto | N / A |  | según alcance (Sondeo, Apique, Barreno, Trinchera manual) |
| `SistemaAvance` | Sistema Avance | Texto | N / A |  | según alcance (Sondeo, Apique, Barreno, Trinchera manual) |
| `Material` | Material | Texto | N / A |  | según alcance (Sondeo, Apique, Barreno, Trinchera manual) |
| `Color` | Color | Texto | N / A |  | según alcance (Sondeo, Apique, Barreno, Trinchera manual) |
| `Humedad` | Humedad | Texto | N / A |  | según alcance (Sondeo, Apique, Barreno, Trinchera manual) |
| `Plasticidad` | Plasticidad | Texto | N / A |  | según alcance (Sondeo, Apique, Barreno, Trinchera manual) |
| `Consistencia` | Consistencia | Texto | N / A |  | según alcance (Sondeo, Apique, Barreno, Trinchera manual) |
| `Compacidad` | Compacidad | Texto | N / A |  | según alcance (Sondeo, Apique, Barreno, Trinchera manual) |

Tabla relacionada **E_EstructuraPavimento** (Estructura Pavimento), de Exploracion

| Campo | Alias | Tipo | Unidad | Dominio o rango | Marca |
|---|---|---|---|---|---|
| `PK_ID_EstructuraPavimento` | PK_ID_EstructuraPavimento | Entero Largo | N / A |  | obligatorio (Apique, Trinchera manual) |
| `FK_ID_Exploracion` | FK_ID_Exploracion | Entero Largo | N / A |  | obligatorio (Apique, Trinchera manual) |
| `PDC` | Penetrómetro Dinámico Cono | Decimal | mm/golpe |  | obligatorio (Apique, Trinchera manual) |
| `CBR_Correlacion` | CBR Correlación | Entero | Porcentaje (%) |  | según alcance (Apique, Trinchera manual) |
| `CBR_Inalterado` | CBR Inalterado | Entero | Porcentaje (%) |  | según alcance (Apique, Trinchera manual) |
| `CBR_Laboratorio` | CBR Laboratorio | Entero | Porcentaje (%) |  | obligatorio (Apique, Trinchera manual) |
| `Densidad_D_Inalterada` | Densidad Seca Inalterada | Decimal | g/cm3 |  | obligatorio (Apique, Trinchera manual) |
| `Humedad_Opt_PM` | Humedad Óptima PM | Decimal | Porcentaje (%) |  | obligatorio (Apique, Trinchera manual) |
| `Densidad_Seca_Opt_PM` | Densidad Seca Óptima PM | Decimal | g/cm3 |  | obligatorio (Apique, Trinchera manual) |
| `Humedad_Opt_PN` | Humedad Óptima PN | Decimal | Porcentaje (%) |  | obligatorio (Apique, Trinchera manual) |
| `Densidad_Seca_Opt_PN` | Densidad Seca Óptima PN | Decimal | g/cm3 |  | obligatorio (Apique, Trinchera manual) |
| `DensidadSueloTerreno` | Densidad Suelo Terreno | Decimal | g/cm3 |  | obligatorio (Apique, Trinchera manual) |
| `HumedadSueloTerreno` | Humedad Suelo Terreno | Decimal | Porcentaje (%) |  | obligatorio (Apique, Trinchera manual) |

Tabla relacionada **P_Muestra** (Muestra), de Exploracion

| Campo | Alias | Tipo | Unidad | Dominio o rango | Marca |
|---|---|---|---|---|---|
| `PK_ID_Muestra` | PK_ID_Muestra | Entero Largo | N / A |  | según alcance (Sondeo, Apique, Barreno, Trinchera manual) |
| `FK_ID_Exploracion` | FK_ID_Exploracion | Entero Largo | N / A |  | según alcance (Sondeo, Apique, Barreno, Trinchera manual) |
| `Nmuestra` | Número de la Muestra | Texto | N / A |  | según alcance (Sondeo, Apique, Barreno, Trinchera manual) |
| `Prof_Inc` | Profundidad Inicial Muestra | Decimal | Metro (m) |  | según alcance (Sondeo, Apique, Barreno, Trinchera manual) |
| `Prof_Final` | Profundidad Final Muestra | Decimal | Metro (m) |  | según alcance (Sondeo, Apique, Barreno, Trinchera manual) |
| `TipoMuestra` | Tipo Muestra | Texto | N / A | `A` Alterada; `I` Inalterada | según alcance (Sondeo, Apique, Barreno, Trinchera manual) |
| `MuestraEspecial` | Muestra especial | Texto | N / A | `S` Si; `N` No | según alcance (Sondeo, Apique, Barreno, Trinchera manual) |

Tabla relacionada **P_EnsayoLaboratorio** (Ensayo Laboratorio), de P_Muestra

| Campo | Alias | Tipo | Unidad | Dominio o rango | Marca |
|---|---|---|---|---|---|
| `PK_ID_EnsayoLaboratorio` | PK_ID_EnsayoLaboratorio | Entero Largo | N / A |  | según alcance (Sondeo, Apique, Barreno, Trinchera manual) |
| `FK_ID_Muestra` | FK_ID_Muestra | Entero Largo | N / A |  | según alcance (Sondeo, Apique, Barreno, Trinchera manual) |
| `Grava` | Tamizado Grava | Decimal | Porcentaje (%) |  | según alcance (Sondeo, Apique, Barreno, Trinchera manual) |
| `ArenaGruesa` | Tamizado Arena Gruesa | Decimal | Porcentaje (%) |  | según alcance (Sondeo, Apique, Barreno, Trinchera manual) |
| `ArenaMedia` | Tamizado Arena Media | Decimal | Porcentaje (%) |  | según alcance (Sondeo, Apique, Barreno, Trinchera manual) |
| `ArenaFina` | Tamizado Arena Fina | Decimal | Porcentaje (%) |  | según alcance (Sondeo, Apique, Barreno, Trinchera manual) |
| `Finos` | Tamizado Finos | Decimal | Porcentaje (%) |  | según alcance (Sondeo, Apique, Barreno, Trinchera manual) |
| `Cu` | Granulometría Cu | Decimal | Adimensional |  | según alcance (Sondeo, Apique, Barreno, Trinchera manual) |
| `Cc` | Granulometría Cc | Decimal | Adimensional |  | según alcance (Sondeo, Apique, Barreno, Trinchera manual) |
| `H_Limo` | Tamaño Limos | Decimal | Porcentaje (%) |  | según alcance (Sondeo, Apique, Barreno, Trinchera manual) |
| `H_Arcilla` | Tamaño Arcilla | Decimal | Porcentaje (%) |  | según alcance (Sondeo, Apique, Barreno, Trinchera manual) |
| `HumedadNatural` | Humedad Natural | Decimal | Porcentaje (%) |  | según alcance (Sondeo, Apique, Barreno, Trinchera manual) |
| `LimiteLiquido` | Límite Liquido | Decimal | Porcentaje (%) |  | según alcance (Sondeo, Apique, Barreno, Trinchera manual) |
| `LimitePlastico` | Límite Plastico | Decimal | Porcentaje (%) |  | según alcance (Sondeo, Apique, Barreno, Trinchera manual) |
| `LimiteContraccion` | Límite Contracción | Decimal | Porcentaje (%) |  | según alcance (Sondeo, Apique, Barreno, Trinchera manual) |
| `IndicePlasticidad` | Índice Plasticidad | Decimal | Porcentaje (%) |  | según alcance (Sondeo, Apique, Barreno, Trinchera manual) |
| `USC` | USC | Texto | N / A |  | según alcance (Sondeo, Apique, Barreno, Trinchera manual) |
| `AASHTO` | AASHTO | Texto | N / A |  | según alcance (Sondeo, Apique, Barreno, Trinchera manual) |
| `MateriaOrganica` | Contenido Materia Orgánica | Decimal | Porcentaje (%) |  | según alcance (Sondeo, Apique, Barreno, Trinchera manual) |
| `GravedadEspecifica` | Gravedad Específica Gs | Decimal | Adimensional |  | según alcance (Sondeo, Apique, Barreno, Trinchera manual) |
| `PH_Suelos` | PH Suelo | Decimal | Adimensional |  | según alcance (Sondeo, Apique, Barreno, Trinchera manual) |
| `EquivalenteArena` | Equivalente Arena | Decimal | Porcentaje (%) |  | según alcance (Sondeo, Apique, Barreno, Trinchera manual) |
| `PermeLabTipo` | Tipo Ensayo Permeabilidad | Texto | N / A |  | según alcance (Sondeo, Apique, Barreno, Trinchera manual) |
| `PermeLabK` | Permeabilidad hidráulica Suelo | Decimal | Centímetro por segundo (cm/s) |  | según alcance (Sondeo, Apique, Barreno, Trinchera manual) |

Tabla relacionada **S_E_EspecialesLaboratorio** (Sondeo E_EspecialesLaboratorio), de P_Muestra

| Campo | Alias | Tipo | Unidad | Dominio o rango | Marca |
|---|---|---|---|---|---|
| `PK_ID_EspecialesLaboratorio` | PK_ID_EspecialesLaboratorio | Entero Largo | N / A |  | según alcance (Sondeo, Apique, Barreno, Trinchera manual) |
| `FK_ID_Muestra` | FK_ID_Muestra | Entero Largo | N / A |  | según alcance (Sondeo, Apique, Barreno, Trinchera manual) |
| `I_Exp_Lambe` | Índice Expansión Lambe | Decimal | Megapascal (MPa) |  | según alcance (Sondeo, Apique, Barreno, Trinchera manual) |
| `CVP_Lambe` | Cambio Volumétrico Potencial Lambe | Decimal | Adimensional |  | según alcance (Sondeo, Apique, Barreno, Trinchera manual) |
| `R_Compre_Inconfi_qu` | Resistencia Compresión Inconfinada qu | Decimal | kilopascal (kPa) |  | según alcance (Sondeo, Apique, Barreno, Trinchera manual) |
| `R_Corte_c` | Cohesión Corte Directo | Decimal | kilopascal (kPa) |  | según alcance (Sondeo, Apique, Barreno, Trinchera manual) |
| `R_Corte_fi` | Ángulo Fricción Corte Directo | Entero | Grados |  | según alcance (Sondeo, Apique, Barreno, Trinchera manual) |
| `C_Ce` | Compresibilidad Ce | Decimal |  |  | según alcance (Sondeo, Apique, Barreno, Trinchera manual) |
| `C_s` | Compresibilidad s | Decimal |  |  | según alcance (Sondeo, Apique, Barreno, Trinchera manual) |
| `C_Cv` | Compresibilidad Cv | Decimal |  |  | según alcance (Sondeo, Apique, Barreno, Trinchera manual) |
| `RC_C` | Resistencia Corte C | Decimal |  |  | según alcance (Sondeo, Apique, Barreno, Trinchera manual) |
| `RC_f` | Resistencia Corte f | Decimal |  |  | según alcance (Sondeo, Apique, Barreno, Trinchera manual) |
| `RC_Consolidacion` | Resistencia Corte Consolidacion | Texto | N / A |  | según alcance (Sondeo, Apique, Barreno, Trinchera manual) |
| `RC_EtapaFalla` | Resistencia Corte EtapaFalla | Texto | N / A |  | según alcance (Sondeo, Apique, Barreno, Trinchera manual) |
| `RC_Ensayo` | Resistencia Corte Ensayo | Texto | N / A |  | según alcance (Sondeo, Apique, Barreno, Trinchera manual) |
| `Expansividad_se` | Expansividad se | Decimal |  |  | según alcance (Sondeo, Apique, Barreno, Trinchera manual) |
| `Expansividad_E` | Expansividad E | Decimal |  |  | según alcance (Sondeo, Apique, Barreno, Trinchera manual) |
| `E_Ensayo` | Expansividad Ensayo | Texto | N / A |  | según alcance (Sondeo, Apique, Barreno, Trinchera manual) |
| `Observacion` | Observacion | Texto | N / A |  | según alcance (Sondeo, Apique, Barreno, Trinchera manual) |

## InfraestructuraEspecial

### Escalera

Geometría **polígono**; elementos: Escalera.
Estructura conformada por peldaños, gradas o escalas que permite la circulación entre dos plantas o dos zonas con plantas de diferentes alturas.

Atributos de **Escalera**

| Campo | Alias | Tipo | Unidad | Dominio o rango | Marca |
|---|---|---|---|---|---|
| `PK_ID_Escalera` | PK_ID_Escalera | Entero Largo | N / A |  | obligatorio |
| `CIV` | CIV | Entero Largo | N / A |  | obligatorio |
| `TipoMaterialEscalera` | Tipo de material de la escalera | Entero | N / A | `0` Concreto; `1` Metálico; `2` Madera | obligatorio |
| `AnchoEscalera` | Ancho | Decimal | Metro (m) | rango 1 a 50 | obligatorio |
| `LongitudEscalera` | Longitud | Decimal | Metro (m) | rango 1 a 30 | obligatorio |
| `AltoEscalera` | Alto de la escalera | Decimal | Metro (m) | rango 0.5 a 7 | obligatorio |
| `AreaEscalera` | Área | Decimal | Metro cuadrado (m2) | rango 1 a 60 | obligatorio |
| `PendienteEscalera` | Pendiente de la escalera | Decimal | Porcentaje (%) | rango 7 a 75 | obligatorio |
| `VolumenEscalera` | Volumen de la escalera | Decimal | Metro cúbico (m3) | rango 0.5 a 20 | obligatorio |
| `EstructuraAsociada` | Estructura Asociada | Entero | N / A | `0` Puente; `1` Alameda; `2` Via Peatonal; `3` Plaza; `4` Anden; `5` Separador | obligatorio |
| `FechaRegistro` | Fecha de Registro | Fecha | N / A |  | obligatorio |

### Muro

Geometría **polígono**; elementos: Muro.
Toda estructura que de forma activa o pasiva produce un efecto estabilizador sobre una masa de terreno al proporcionarle a éste, soporte lateral.

Atributos de **Muro**

| Campo | Alias | Tipo | Unidad | Dominio o rango | Marca |
|---|---|---|---|---|---|
| `PK_ID_Muro` | PK_ID_Muro | Entero Largo | N / A |  | obligatorio |
| `CIV` | CIV | Entero Largo | N / A |  | obligatorio |
| `AnchoMuro` | Ancho | Decimal | Metro (m) | rango 0.1 a 2 | obligatorio |
| `AltoMuro` | Alto | Decimal | Metro (m) | rango 0.2 a 15 | obligatorio |
| `LongitudMuro` | Longitud | Decimal | Metro (m) | rango 1 a 300 | obligatorio |
| `AreaMuro` | Área | Decimal | Metro cuadrado (m2) | rango 1 a 500 | obligatorio |
| `VolumenMuro` | Volumen | Decimal | Metro cúbico (m3) | rango 1 a 300 | obligatorio |
| `TipoMuro` | Tipo de material | Entero | N / A | `1` Concreto Reforzado; `2` Bloque; `3` Tierra Armada; `4` Gaviones; `5` Pedraplen; `6` Madera; `7` Pantalla | obligatorio |
| `FechaRegistro` | Fecha de Registro | Fecha | N / A |  | obligatorio |

### Talud

Geometría **polígono**; elementos: Talud.
Paramento o superficie inclinada que limita lateralmente un corte o un terraplén.

Atributos de **Talud**

| Campo | Alias | Tipo | Unidad | Dominio o rango | Marca |
|---|---|---|---|---|---|
| `PK_ID_Talud` | PK_ID_Talud | Entero Largo | N / A |  | obligatorio |
| `CIV` | CIV | Entero Largo | N / A |  | obligatorio |
| `LongitudTalud` | Longitud del Talud | Decimal | Metro (m) | rango 2 a 50 | obligatorio |
| `ZonaInestable` | Zona Inestable | Entero | N / A | `1` Caídas; `2` Volcamientos; `3` Deslizamiento; `4` Flujos; `5` Movimientos complejos | obligatorio |
| `AnchoTalud` | Ancho del Talud | Decimal | Metro (m) | rango 1.5 a 8 | obligatorio |
| `AltoTalud` | Alto del Talud | Decimal | Metro (m) | rango 0.5 a 10 | obligatorio |
| `AreaTalud` | Área del Talud | Decimal | Metro cuadrado (m2) | rango 3 a 400 | obligatorio |
| `VolumenTalud` | Volumen del Talud | Decimal | Metro cúbico (m3) | rango 1 a 4000 | obligatorio |
| `NivelTalud` | Nivel del talud | Texto | N / A | `S` Sobre nivel de vía; `B` Bajo nivel de vía | obligatorio |
| `RevestimientoTalud` | Revestimiento del Talud | Entero | N / A | `1` Sin Revestimiento; `2` Concreto lanzado con refuerzo; `3` Concreto lanzado sin refuerzo; `4` Concreto reforzado; `5` Geomalla; `6` Sembrado | obligatorio |
| `RelacionHV` | Relación Horizontal Vertical | Texto | N / A |  | obligatorio |
| `FechaRegistro` | Fecha de Registro | Fecha | N / A |  | obligatorio |

### Terraplen

Geometría **polígono**; elementos: Terraplén.
Relleno de un terreno para levantar su nivel y formar un plano de apoyo adecuado para hacer una obra.

Atributos de **Terraplen**

| Campo | Alias | Tipo | Unidad | Dominio o rango | Marca |
|---|---|---|---|---|---|
| `PK_ID_Terraplen` | PK_ID_Terraplen | Entero Largo | N / A |  | obligatorio |
| `CIV` | CIV | Entero Largo | N / A |  | obligatorio |
| `AnchoTerraplen` | Ancho Terraplen | Decimal | Metro (m) | rango 1.5 a 30 | obligatorio |
| `VolumenTerraplen` | Volumen Terraplen | Decimal | Metro cúbico (m3) | rango 1 a 10000 | obligatorio |
| `AltoTerraplen` | Alto Terraplen | Decimal | Metro (m) | rango 0.5 a 10 | obligatorio |
| `LongitudTerraplen` | Longitud Terraplen | Decimal | Metro (m) | rango 2 a 50 | obligatorio |
| `AreaTerraplen` | Area Terraplen | Decimal | Metro cuadrado (m2) | rango 3 a 1500 | obligatorio |
| `PendienteLongitudinal` | Pendiente longitudinal | Entero | Porcentaje (%) | rango 0 a 25 | obligatorio |
| `FechaRegistro` | Fecha de intervención | Fecha | N / A |  | obligatorio |

## InfraestructuraMobiliario

### BarandaPeatonal

Geometría **línea**; elementos: Baranda Peatonal.
Es un elemento de delimitación y control del espacio público, el cual protege y guía al peatón. Tiene como función la delimitación de parques, marcando el límite entre circulaciones y zonas verdes.

Atributos de **BarandaPeatonal**

| Campo | Alias | Tipo | Unidad | Dominio o rango | Marca |
|---|---|---|---|---|---|
| `PK_ID_BarandaPeatonal` | PK_ID_BarandaPeatonal | Entero Largo | N / A |  | obligatorio |
| `CIV` | CIV | Entero Largo | N / A |  | obligatorio |
| `TipoBaranda` | Tipo Baranda | Texto | N / A | `CMN` Concreto y Metálica no Estandar; `CRN` Solo Concreto no Estandar; `M80` Baranda Metálica con un tubo M80; `M81` Baranda Metálica con dos tubos M81; `M82` Baranda Metálica con tres tubos M82; `MTN` Solo Metálica no Estandar | obligatorio |
| `LongitudBaranda` | Longitud Baranda | Decimal | Metro (m) | rango 2 a 100 | obligatorio |
| `FechaRegistro` | Fecha de Registro | Fecha | N / A |  | obligatorio |

Tabla relacionada **DetalleMobiliario** (Detalle Mobiliario), de BarandaPeatonal

| Campo | Alias | Tipo | Unidad | Dominio o rango | Marca |
|---|---|---|---|---|---|
| `PK_ID_DetalleMobiliario` | PK_ID_Detalle Mobiliario | Entero Largo | N / A |  | obligatorio |
| `FK_ID_Mobiliario` | FK_ID_Mobiliario | Entero Largo | N / A |  | obligatorio |
| `Estado` | Estado de condición | Texto | N / A | `B` Bueno; `M` Malo; `R` Regular | obligatorio |
| `CumpleFuncionalidad` | Cumple Funcionalidad | Texto | N / A | `S` Si; `N` No | obligatorio |
| `ICEMU` | Indice de Condición de Mobiliario Urbano | Entero | Porcentaje (%) | rango 0 a 100 | obligatorio |
| `FechaMedicionICEMU` | Fecha Medicion ICEMU | Fecha | N / A |  | obligatorio |
| `Dano` | Daño | Entero | N / A | `0` No presenta; `1` Ligero; `2` Moderado; `3` Semisevero; `4` Severo; `5` Completamente inservible | obligatorio |

### Mobiliario

Geometría **punto**; elementos: Banca, Bolardo, Caneca, CicloParqueadero, Contenedor de Raíz, Matera, Módulo, Protector de Árbol.
Elemento de alta resistencia para sentarse y descansar por tiempo prolongado, de uso en áreas relacionadas con el ocio, el esparcimiento y la recreación, como andenes, plazas, alamedas y parques.

Atributos de **Mobiliario**

| Campo | Alias | Tipo | Unidad | Dominio o rango | Marca |
|---|---|---|---|---|---|
| `PK_ID_Mobiliario` | PK_ID_Mobiliario | Entero Largo | N / A |  | obligatorio |
| `CIV` | CIV | Entero Largo | N / A |  | obligatorio |
| `Clase\Tipo` | Clase\Tipo | Texto | N / A | `M100` Ciclo-parqueadero tipo 1 M100; `M101` Ciclo-parqueadero tipo 2 M101; `M142` Modulo para albergar bicicletas; `NES` No estandar; `CMN` Concreto y metálica no estandar; `CRN` Solo concreto no estandar; `M40` Modular en concreto M40; `M50` Madera y hierro fundido M50; `MMN` Madera y metálica no estandar; `MTN` Solo metálica no estandar; `M30` Concreto con espaldar en malla M30; `M31` Concreto sin espaldar M31; `M41` Banca-bolardo en concreto M41; `M61` Prefabricado en concreto tamaño bajo M61; `M62` Prefabricado metálico tamaño bajo M62; `M63` Prefabricado metálico tamaño alto M63; `MIX` Concreto y metálico no estándar; `CON` Solo concreto no estándar; `MET` Solo metálico no estándar; `M60` Prefabricado en concreto tamaño normal M60; `BCU` Aro de CicloRuta; `M120` Caneca M120; `M121` Caneca en acero Inoxidable M121; `NES` No estandar; `B20A` Prefabricado Tipo A B20; `B25` Prefabricado Tipo B B25; `B26` Prefabricado Tipo C B26; `FIS` Fundido in situ; `No aplica` No aplica; `M141` Módulo de Servicio al Ciudadano M141; `M143` Módulo de Servicio sanitario M143; `M144` Módulo de café M144; `M145` Módulo de información M145; `M146` Módulo de ventas M146; `M147` Módulo de ventas (KIOSKO) - ZAR M147; `NHM` No Homologada; `V` Ventas no estandar; `M90` Protector de árbol M90; `M91` Protector de árbol de dos tubos M91; `NES` No estandar | obligatorio |
| `FechaRegistro` | Fecha de Registro | Fecha | N / A |  | obligatorio |

Tabla relacionada **DetalleMobiliario** (Detalle Mobiliario), de Mobiliario

| Campo | Alias | Tipo | Unidad | Dominio o rango | Marca |
|---|---|---|---|---|---|
| `PK_ID_DetalleMobiliario` | PK_ID_Detalle Mobiliario | Entero Largo | N / A |  | obligatorio |
| `FK_ID_Mobiliario` | FK_ID_Mobiliario | Entero Largo | N / A |  | obligatorio |
| `Estado` | Estado de condición | Texto | N / A | `B` Bueno; `M` Malo; `R` Regular | obligatorio |
| `CumpleFuncionalidad` | Cumple Funcionalidad | Texto | N / A | `S` Si; `N` No | obligatorio |
| `ICEMU` | Indice de Condición de Mobiliario Urbano | Entero | Porcentaje (%) | rango 0 a 100 | obligatorio |
| `FechaMedicionICEMU` | Fecha Medicion ICEMU | Fecha | N / A |  | obligatorio |
| `Dano` | Daño | Entero | N / A | `0` No presenta; `1` Ligero; `2` Moderado; `3` Semisevero; `4` Severo; `5` Completamente inservible | obligatorio |

### Pileta

Geometría **polígono**; elementos: Pileta.
Es un surtidor de agua, que como elemento arquitectónico suele estar situado en un espacio urbano con fines utilitarios, de confort ambiental o decorativos

Atributos de **Pileta**

| Campo | Alias | Tipo | Unidad | Dominio o rango | Marca |
|---|---|---|---|---|---|
| `PK_ID_Pileta` | PK_ID_Pileta | Entero Largo | N / A |  | obligatorio |
| `CIV` | CIV | Entero Largo | N / A |  | obligatorio |
| `Ancho` | Ancho pileta | Decimal (Float) | Metro (m) |  | obligatorio |
| `Longitud` | Longitud pileta | Decimal (Float) | Metro (m) |  | obligatorio |
| `FechaRegistro` | Fecha de Registro | Fecha | N / A |  | obligatorio |

## InfraestructuraPuente

### Puente

Geometría **polígono**; elementos: Puente.
Estructura que se construye principalmente en obstáculos naturales como ríos, quebradas, depresiones del terreno y en obstáculos artificiales: canales, vías, infraestructura urbana; con el fin de comunicar dos puntos. En la ciudad de Bogotá podemos encontrar los siguientes tipos de puentes: peatonal, vehicular y Ciclopuente.

Atributos de **Puente**

| Campo | Alias | Tipo | Unidad | Dominio o rango | Marca |
|---|---|---|---|---|---|
| `PK_ID_Puente` | PK_ID_Puente | Entero Largo | N / A |  | obligatorio |
| `CIV` | CIV | Entero Largo | N / A |  |  |
| `TipoPuente` | Tipo de Puente | Texto | N / A | `PVE` Puente Vehicular; `PPE` Puente Peatonal; `CPU` CicloPuente; `CPE` CicloPeatonal; `PON` Pontón; `BPE` Box Peatonal; `BVE` Box Vehicular | obligatorio |
| `ClasificacionPuente` | Clasificación del Puente | Entero | N / A | `1` PVE Vehicular sobre Vía Principal; `2` PPE Peatonal sobre Vía Principal; `3` PVC Vehicular sobre Agua; `4` PPC Peatonal sobre Agua; `5` PVI Vehicular sobre Vía Intermedia; `6` PPI Peatonal sobre Vía Intermedia; `7` PVL Vehicular sobre Vía Local; `8` PVL Peatonal sobre Vía Local | obligatorio |
| `TipoEstructura` | Tipo de Estructura | Entero | N / A | `1` Monolítico de Infraestructura tipo Péndulo; `2` Monolítico de Infraestructura tipo Pórtico; `3` Monolítico de Infraestructura tipo Pantalla; `4` No Monolítico de Infraestructura tipo Péndulo tipo Péndulo con Superestructura Isostática en Viga de Cajón; `5` No Monolítico Infraestructura tipo Péndulo con Superestructura Isostática con Viga Mas Placa; `6` No Monolítico. Infraestructura tipo Pórtico con Súper Estructura Isostática con Viga Mas Placa; `7` No Monolítico. Infraestructura tipo Pórtico con Superestructura Isostática Viga Cajón; `8` No Monolítico. Infraestructura tipo Pantalla con Superestructura Isostática con Viga Cajón; `9` No Monolítico. Infraestructura tipo Pantalla con Superestructura Isostática con Viga Mas losa; `10` No Monolítico. Infraestructura tipo Péndulo con Superestructura Hiperestática con Viga Cajón; `11` No Monolítico. Infraestructura tipo Pórtico con Superestructura Hiperestática con Viga de Cajón; `12` No Monolítico. Infraestructura tipo Pórtico con Superestructura Hiperestática con Otros Sistemas Diferentes a la Viga de Cajón; `13` No Monolítico. Infraestructura tipo Pantalla con Superestructura Hiperestática con Viga de Cajón; `14` No Monolítico. Infraestructura tipo Pantalla con Superestructura Hiperestática con Otros Sistemas Diferentes a la Viga de Cajón; `15` Tipo Box Coulvert; `16` Metálico reticulado en celosía simplemente apoyado; `17` Metálico reticulado en celosía continuo; `18` Metálico en arco de paso inferior; `19` Metálico en arco de paso superior; `20` Metálico arco en concreto de paso inferior; `21` Metálico arco en concreto de paso superior; `22` Puente Peatonal tipo 7; `23` Puente Peatonal tipo 8; `24` Puente Peatonal tipo 9; `25` Puente Peatonal tipo 10; `26` Puente Peatonal tipo 11; `27` Puente Peatonal tipo 12; `28` Puente Peatonal tipo 1; `29` Puente Peatonal tipo 2; `30` Puente Peatonal tipo 3; `31` Puente Peatonal tipo 4; `32` Puente Peatonal tipo 5; `33` Puente Peatonal tipo 6 | obligatorio |
| `PuenteNivel` | Nivel del Puente | Entero | N / A | `-1` Primer Nivel Inferior; `1` A Nivel; `2` Primer Nivel Superior; `3` Segundo Nivel Superior; `4` Tercer Nivel Superior | obligatorio |
| `CodigoVia` | CodigoVia | Entero | N / A | `0` Sin Clasificar; `1` Autopista Al Llano; `10` Avenida Callejas (diagonal 127a); `100` Conector Av la Sirena X Av Paseo de los Libertadores; `101` Conector Av Laureano Gomez X Av Pepe Sierra; `102` Conector Av Medellin X Av Boyaca; `103` Conector Av Medellin X Av Ciudad de Cali; `104` Conector Av Medellin X Av del Congraso Eucaristico; `105` Conector Av Medellin X Av España; `106` Conector Av Paseo del Country X Av Carlos Lleras Restrepo; `107` Conector Av Primero de Mayo X Av. Boyaca; `108` Conector Av Primero de Mayo X Av del Congreso Eucaristico; `109` Conector Av Primero de Mayo X Av Ferrocarril del sur; `11` Avenida Camino del Prado; `110` Conector Av Rodrigo Lara Bonilla X Av Paseo de los Libertadores; `111` Conector Carrera 11 X Av Callejas; `112` Glorieta Av Carlos Lleras Res. Av Paseo Country Av Laureano Gomez; `113` Glorieta Av Congreso Eucaristico X Av Jose Celestino Mutis; `114` Glorieta Av de la Constitucion; `115` Glorieta Av Ferrocarril del Sur Av Batallon Caldas Av Montes; `116` Glorieta Av Jose Celestino Mutis X Av Batallon Caldas; `117` Glorieta Av Jose Celestino Mutis X Av la Esmeralda; `118` Glorieta Av la Hortua Av Fucha Av General Santander; `119` Glorieta Av Primero de Mayo X Av Batallon Caldas; `12` Avenida Caracas; `120` Oreja Autonorte X Calle 170; `121` Oreja Av Alberto Lleras Camargo X Av Carlos Lleras Restrepo; `122` Oreja Av Boyaca X Av Centenario; `123` Oreja Av Callejas X Av Paseo de los Libertadores; `124` Oreja Av Centenario X Av Ciudad de Cali; `125` Oreja Av Chile X Av del Congreso Eucaristico; `126` Oreja Av Ciudad de Quito X Av Medellin; `127` Oreja Av Contador X Av Laureano Gomez; `128` Oreja Av Iberia X Av Paseo de los Libertadores; `129` Oreja Av Jorge Eliecer Gaitan X Av Ciudad de Cali; `13` Avenida Castilla; `130` Oreja Av Jose Celestino Mutis X Av Ciudad de Quito; `131` Oreja Av la Sirena X Av Paseo de los Libertadores; `132` Oreja Av Medellin X Av Boyaca; `133` Oreja Av Medellin X Av del Congreso Eucaristico; `134` Oreja Av Medellin X Av España; `135` Oreja Av Paseo de los Libertadores X Av Ciudad de Quito; `136` Oreja Av Primero de Mayo X Av. Boyaca; `137` Puente Av Alfredo d Bateman X Av Medellin; `138` Retorno Av Apaseo de los Libertadores; `139` Retorno Av Callejas; `14` Avenida Centenario; `140` Retorno Av Jose Celestino Mutis; `141` Avenida San Juan Bosco; `142` Via g; `143` Autopista del Sur y Avenida Ferrocarril; `144` Avenida 85; `145` Avenida a Cota; `146` Avenida Alsacia; `147` Avenida Bolivia; `148` Avenida Bosa; `149` Avenida Camino a Pasquilla; `15` Avenida Chile; `150` Avenida Camino de la Horqueta; `151` Avenida Circunvalar del sur; `152` Avenida de Agua; `153` Avenida de la Guacamaya; `154` Avenida de las Mercedes; `155` Avenida de los Alisos; `156` Avenida de los Muiscas; `157` Avenida del Ferrocarril del sur; `158` Avenida del Rio; `159` Avenida del Salitre; `16` Avenida Ciudad de Cali; `160` Avenida del Tabor; `161` Avenida del tam; `162` Avenida del Uval; `163` Avenida el Cortijo; `164` Avenida el Jardin; `165` Avenida el Polo; `166` Avenida el Rincon; `167` Avenida Gonzalo Ariza; `168` Avenida Guaymaral; `169` Avenida Industrial; `17` Avenida Ciudad de Lima; `170` Avenida Jose Asuncion Silva; `171` Avenida la Alameda del sur; `172` Avenida la Conejera; `173` Avenida la Victoria; `174` Avenida las Quintas; `175` Avenida Longitudinal de Occidente; `176` Avenida los Arrayanes; `177` Avenida Low Murtra; `178` Avenida Manuel Cepeda Vargas; `179` Avenida Morisca; `18` Avenida Ciudad de Quito; `180` Avenida Paisajistica de Tunjuelito; `181` Avenida Paramo; `182` Avenida Perimetral de Usme; `183` Avenida Poporo Quimbaya; `184` Avenida Puente Aranda; `185` Avenida San Antonio; `186` Avenida San Bernardino; `187` Avenida San Francisco; `188` Avenida Santa Fe; `189` Avenida Sumapaz; `19` Avenida Ciudad de Villavicencio; `190` Avenida Tibabita; `191` Avenida Tintal; `192` Avenida Tomas Carrasquilla; `193` Avenida Troncal de Juan rey; `194` Avenida Tunjuelito; `195` Avenida Ustminia; `196` Avenida Versalles; `197` Avenida Xue; `198` Carrera 103; `2` Avenida Carlos Lleras Restrepo; `20` Avenida Colombia; `21` Avenida Colon; `22` Avenida Cordoba; `23` Avenida Cundinamarca; `24` Avenida Dario Echandia; `25` Avenida de la Constitucion; `26` Avenida de la Hortua; `27` Avenida de la Sirena; `28` Avenida de las Americas; `29` Avenida de las Orquideas; `3` Avenida Alejandro Obregon; `30` Avenida de las Villas; `31` Avenida de los Cedritos; `32` Avenida de los Cerros; `33` Avenida de los Comuneros; `34` Avenida del Congreso Eucaristico; `35` Avenida del Contador; `36` Avenida del sur; `37` Avenida España; `38` Avenida Fernando Mazuera; `39` Avenida Ferrocarril de Occidente; `4` Avenida Agoberto Mejia Cifuentes; `40` Avenida Fontibon; `41` Avenida Francisco Miranda; `42` Avenida Fucha; `43` Avenida Gabriel Andrade Lleras; `44` Avenida General Santander; `45` Avenida German Arciniegas; `46` Avenida Iberia; `47` Avenida Jimenez de Quesada; `48` Avenida Jorge Eliecer Gaitan; `49` Avenida Jorge Gaitan Cortes; `5` Avenida Alberto Lleras Camargo; `50` Avenida Jorge Uribe Botero; `51` Avenida Jose Celestino Mutis; `52` Avenida la Esmeralda; `53` Avenida la Esperanza; `54` Avenida Laureano Gomez; `55` Avenida Luis Carlos Galan Sarmiento; `56` Avenida Mariscal Sucre; `57` Avenida Medellin; `58` Avenida Montes; `59` Avenida Pablo Vi; `6` Avenida Alfredo d Bateman; `60` Avenida Paseo de los Libertadores ( Autopista Norte); `61` Avenida Paseo del Country (ak 15); `62` Avenida Pedro Leon Trabuchy; `63` Avenida Pepe Sierra; `64` Avenida Primero de Mayo; `65` Avenida Quiroga; `66` Avenida Rodrigo Lara Bonilla; `67` Avenida San Jose; `68` Avenida Santa Barbara; `69` Avenida Santa Lucia; `7` Avenida Batallon Caldas; `70` Avenida Teusaquillo; `71` Avenida Transversal de Suba; `72` Carrera 106; `73` Carrera 11; `74` Conector Autonorte Calle 170; `75` Conector Av Alberto Lleras Camargo X Av Carlos Lleras Restrepo; `76` Conector Av Alberto Lleras Camargo X Av Contador; `77` Conector Av Alberto Lleras Camargo X Av Contador; `78` Conector Av Alberto Lleras Camargo X Av Pepe Sierra; `79` Conector Av Alberto Lleras Camargo X Av Pepe Sierra; `8` Avenida Boyaca; `80` Conector Av Alejandro Obregon X Av Paseo de los Libertadores; `81` Conector Av Alejandro Obregon X Av Paseo de los Libertadores; `82` Conector Av Alfredo d Bateman X Av Medellin; `83` Conector Av Callejas X Av Paseo de los Libertadores; `84` Conector Av Carlos Lleras Restrepo X Av Laureano Gomez; `85` Conector Av Centenario X Av Ciudad de Cali; `86` Conector Av Centenario X Av Colon; `87` Conector Av Centenario X Av del Congreso Eucaristico; `88` Conector Av Chile X Av Ciudad de Cali; `89` Conector Av Chile X Av del Congreso Eucaristico; `9` Avenida Calle 92; `90` Conector Av Ciudad de Quito X Av Alejandro Obregon; `91` Conector Av Ciudad de Quito X Av de los Comuneros; `92` Conector Av Ciudad de Quito X Av Paseo de los Libertadores; `93` Conector Av Contador X Av Laureano Gomez; `94` Conector Av Contador X Av. Paseo de los Libertadores; `95` Conector Av Francisco de Miranda X Av Ciudad de Quito; `96` Conector Av Iberia X Av Paseo de los Libertadores; `97` Conector Av Jorge Eliecer Gaitan X Av Ciudad de Cali; `98` Conector Av Jose Celestino Mutis X Av Ciudad de Quito; `99` Conector Av la Sirena X Av Paseo de los Libertadores; `199` Conector Av Congreso Eucaristico X Av Jose Celestino Mutis; `200` Conector Autopista Al Llano X Av Circunvalar Del Sur; `201` Oreja Av Jorge Eliecer Gaitan X Av Batallon Caldas; `202` Conector Av Jorge Eliecer Gaitan X Av Batallon Caldas; `203` Conector Av Batallon Caldas X Av Pablo VI; `204` Conector Av Boyaca X Av Centenario; `205` Conector Av Boyaca X Av Ciudad De Villavicencio; `206` Oreja Av Boyaca X Av Ciudad De Villavicencio; `207` Conector Av Boyaca X Av Mariscal Sucre; `208` Oreja Av Boyaca X Av Luis Carlos Galan Sarmiento; `209` Conector Av Boyaca X Av Luis Carlos Galan Sarmiento; `210` Conector Avenida Ciudad de Quito X Avenida Fucha; `233` Conector Av Teusaquillo X Av Jorge Eliecer Gaitan; `211` Conector Av De Las Americas X Av Boyaca; `212` Oreja Av De Las Americas X Av Boyaca; `213` Conector Av Del Congreso Eucaristico X Av Ciudad De Quito; `214` Conector Av Del Congreso Eucaristico X Av De Las Americas; `215` Oreja Av Del Congreso Eucaristico X Av De Las Americas; `216` Conector Av Del Sur X Av Ferrocarril Del Sur; `217` Oreja Av Del Sur X Av Boyaca; `218` Conector Av Del Sur X Av Boyaca; `219` Conector Av Batallon Caldas X Av Ciudad De Quito; `220` Glorieta Av Del Sur X Av Ciudad De Villavicencio; `221` Conector Av Del Sur X Av Ciudad De Villavicencio; `222` Oreja Av Ciudad De Quito X Av Pedro Leon Tabuchy; `224` Conector Av Gabriel Andrade Lleras X Av La Esmeralda; `223` Conector Av Ciudad De Quito X Av Pedro Leon Tabuchy; `225` Oreja Av Jorge Eliecer Gaitan X Av Congreso Eucaristico; `226` Conector Av Jorge Eliecer Gaitan X Av Congreso Eucaristico; `227` Conector Av Luis Carlos Galan Sarmiento X Av Congreso Eucaristico; `228` Oreja Av Luis Carlos Galan Sarmiento X Av Congreso Eucaristico; `229` Conector Av Jorge Eliecer Gaitan X Av Fernando Mazuera; `230` Oreja Av Jorge Eliecer Gaitan X Av Fernando Mazuera; `231` Conector Av Manuel Cepeda Vargas X Av Ciudad De Cali; `232` Glorieta Av Manuel Cepeda Vargas X Av Ciudad De Cali; `234` Oreja Av España X Av Paseo De Los Libertadores; `235` Conector Av España X Av Paseo De Los Libertadores; `236` Oreja Av Carlos Lleras Restrepo X Av Paseo De Los Libertadores; `237` Conector Av Carlos Lleras Restrepo X Av Paseo De Los Libertadores; `238` Conector Av Fernando Mazuera X Av Fucha; `239` Conector Av Fucha X Av Caracas; `240` Conector Av Mariscal De Sucre X Av Fucha; `241` Oreja Av Ciudad De Quito X Av Jorge Eliecer Gaitan; `242` Carrera 3 |  |
| `Ubicacion` | Ubicación | Texto | N / A |  | obligatorio |
| `AnchoPuente` | Ancho Puente | Decimal | Metro (m) |  | obligatorio |
| `LongitudPuente` | Longitud Puente | Decimal | Metro (m) |  | obligatorio |
| `AreaPuente` | Área Puente | Decimal | Metro cuadrado (m2) |  | obligatorio |
| `Galibo` | Galibo | Decimal | Metro (m) |  | obligatorio |
| `RedVital` | Red Vital | Decimal | N / A | `S` Si; `N` No |  |
| `CuerpoAgua` | Cuerpo de Agua | Texto | N / A |  | obligatorio |
| `AnchoCauce` | Ancho de Cauce | Decimal | Metro (m) |  | obligatorio |
| `MaterialPuente` | Material del Puente | Entero | N / A | `1` Concreto; `2` Metálico; `3` Mixto; `5` No Convencionales | obligatorio |
| `TipoFundacion` | TipoFundacion | Entero | N / A | `1` Superficial; `2` Profunda | obligatorio |
| `Localidad` | Localidad | Entero | N / A | `1` USAQUEN; `2` CHAPINERO; `3` SANTA FE; `4` SAN CRISTOBAL; `5` USME; `6` TUNJUELITO; `7` BOSA; `8` KENNEDY; `9` FONTIBON; `10` ENGATIVA; `11` SUBA; `12` BARRIOS UNIDOS; `13` TEUSAQUILLO; `14` LOS MARTIRES; `15` ANTONIO NARIÑO; `16` PUENTE ARANDA; `17` CANDELARIA; `18` RAFAEL URIBE URIBE; `19` CIUDAD BOLIVAR; `20` SUMAPAZ |  |
| `FechaRegistro` | Fecha de Registro | Fecha | N / A |  | obligatorio |

Tabla relacionada **DetallePuente** (Detalle Puente), de Puente

| Campo | Alias | Tipo | Unidad | Dominio o rango | Marca |
|---|---|---|---|---|---|
| `PK_ID_DetallePuente` | PK_ID_DetallePuente | Entero Largo | N / A |  | obligatorio |
| `FK_ID_Puente` | FK_ID_Puente | Entero Largo | N / A |  | obligatorio |
| `EquipoMonitoreo` | Equipo de Monitoreo | Texto | N / A | `S` Si; `N` No | obligatorio |
| `CantidadEquipos` | Cantidad de Equipos | Entero | Adimensional |  | obligatorio |
| `ProfundidadFundacion` | Profundidad de la Fundación | Decimal | Metro (m) |  | obligatorio |
| `AnchoFundacion` | Ancho de la Fundación | Decimal | Metro (m) |  | obligatorio |
| `LargoFundacion` | Largo de la Fundación | Decimal | Metro (m) |  | obligatorio |
| `VolumenFundacion` | Volumen de la Fundación | Decimal | Metro cúbico (m3) |  | obligatorio |
| `FechaInspeccion` | Fecha de Inspección | Fecha | N / A |  | obligatorio |
| `Inspector` | Inspector | Texto | N / A |  | según alcance |

Tabla relacionada **DetalleElementoPuente** (Detalle Elemento Puente), de Puente

| Campo | Alias | Tipo | Unidad | Dominio o rango | Marca |
|---|---|---|---|---|---|
| `PK_ID_DetalleElementoPuente` | PK_ID_DetalleElementoPuente | Entero Largo | N / A |  | obligatorio |
| `FK_ID_Puente` | FK_ID_Puente | Entero Largo | N / A |  | obligatorio |
| `AsentamientoMaximo` | Asentamiento Máximo | Decimal | Centímetro (cm) |  | obligatorio |
| `LongitudFisuracionMaxima` | Longitud Fisuracion Máxima | Decimal | Milímetro (mm) |  |  |
| `PinturaEspesor` | Pintura Espesor | Decimal | Milímetro (mm) |  | según alcance |

Tabla relacionada **DetalleCalificacionPuente** (Detalle Calificación Puente), de Puente

| Campo | Alias | Tipo | Unidad | Dominio o rango | Marca |
|---|---|---|---|---|---|
| `PK_ID_DCalifPuente` | PK_ID_DCalifPuente | Entero Largo | N / A |  |  |
| `FK_ID_Puente` | FK_ID_Puente | Entero Largo | N / A |  |  |
| `CGaliboVertical` | Calificación Galibo | Texto | N / A |  |  |
| `CTipoMallaVial` | Calificación Tipo de Malla Vial | Texto | N / A |  |  |
| `CRedEmergencia` | Calificación Red Emergencia | Texto | N / A |  |  |
| `CMicroZonaSismica` | Calificación Micro Zona Sísmica | Texto | N / A |  |  |
| `CEtapaMantenimiento` | Calificación Etapa de Mantenimiento | Texto | N / A |  |  |
| `CEvaluacionTrafico` | Calificación Evaluación de Trafico | Texto | N / A |  |  |
| `CVelocidad` | Calificación Velocidad | Texto | N / A |  |  |
| `CEvaluacionCarga` | Calificación Evaluación de Carga | Texto | N / A |  |  |
| `CCirculacionPeatonal` | Calificación CirculacionPeatonal | Texto | N / A |  |  |
| `CGaliboHorizontal` | Calificación Galibo Horizontal | Texto | N / A |  |  |
| `CCargasDiseno` | Calificación Cargas Diseño | Texto | N / A |  |  |
| `CEdad` | Calificación Edad | Texto | N / A |  |  |
| `CSuperPrincipal` | Calificación SuperEstructura Principal | Texto | N / A |  |  |
| `CSuperSecundaria` | Calificación SuperEstructura Secundaria | Texto | N / A |  |  |
| `CInfraestructuraPrincipal` | Calificación Infraestructura Principal | Texto | N / A |  |  |
| `CInfraestructuraSecundaria` | Calificación Infraestructura Secundaria | Texto | N / A |  |  |
| `CCimentacionPrincipal` | Calificación Cimentación Principal | Texto | N / A |  |  |
| `CCimentacionSecuendaria` | Calificación Cimentación Secundaria | Texto | N / A |  |  |
| `CAccesoriosEstructurales` | Calificación Elementos Accesorios Estructurales | Texto | N / A |  |  |
| `CAccesoriosFuncionales` | Calificación Elementos Accesorios Funcionales | Texto | N / A |  |  |
| `Observaciones` | Observaciones | Texto | N / A |  |  |

Tabla relacionada **DetallePatologiaPuente** (Detalle Patología Puente), de Puente

| Campo | Alias | Tipo | Unidad | Dominio o rango | Marca |
|---|---|---|---|---|---|
| `PK_ID_PatologiaPuente` | PK_ID_PatologiaPuente | Entero Largo | N / A |  |  |
| `FK_ID_Puente` | FK_ID_Puente | Entero Largo | N / A |  |  |
| `PVolumenMaximo` | Patología Volumen Máximo | Decimal | Adimensional |  |  |
| `PTraficoDiseno` | Patología Trafico Diseño | Decimal | Adimensional |  |  |
| `PTraficoDiagnostico` | Patología Trafico Diagnostico | Decimal | Adimensional |  |  |
| `PVelocidadDiseno` | Patología Velocidad Diseño | Decimal | Adimensional |  |  |
| `PVelocidadDiagnostico` | Patología Velocidad Diagnostico | Decimal | Adimensional |  |  |
| `PCargaVehicularDiseno` | Patología Carga Vehicular Diseño | Decimal | Adimensional |  |  |
| `PCargaVehicularDiagnostico` | Patología Carga Vehicular Diagnostico | Decimal | Adimensional |  |  |
| `PCargaPeatonalDiseno` | Patología Carga Peatonal Diseño | Decimal | Adimensional |  |  |
| `PCargaPeatonalDiagnostico` | Patología Carga Peatonal Diagnostico | Decimal | Adimensional |  |  |
| `PGaliboHorizontal` | Patología Galibo Horizontal | Decimal | Adimensional |  |  |

Tabla relacionada **PuenteCaracterizacion** (Puente Caracterizacion), de Puente

| Campo | Alias | Tipo | Unidad | Dominio o rango | Marca |
|---|---|---|---|---|---|
| `PK_ID_PuenteCaracterizacion` | PK_ID_PuenteCaracterizacion | Entero Largo | N / A |  |  |
| `FK_ID_Puente` | FK_ID_Puente | Entero Largo | N / A |  |  |
| `MallaVial` | Malla Vial | Texto | N / A | `AR` Arterial; `IN` Intermedia; `LO` Local; `RU` Rural; `CM` Circuito Movilidad; `EX` Expansion; `FD` Fuera del Distrito |  |
| `Troncal` | Troncal Trasmilenio | Entero | N / A | `1` Autopista Norte; `2` Av. Américas; `3` Av. Calle 13; `4` Av. Calle 26; `5` Av. Calle 80; `6` Av. Caracas Norte; `7` Av. Caracas Sur; `8` Av. Carrera 10; `9` Av. NQS; `10` Av. NQS Sur; `11` Suba; `12` AV. Calle 6; `13` No Troncal |  |
| `FichaDTE (Adjunto)` | Ficha de la Vista DTE |  | N / A |  |  |
| `Imagen (Adjunto)` | Fotografia del Puente |  | N / A |  |  |
| `EvalauacionDTAI` | Evalauacion DTAI | Double | Adimensional | rango 0 a 5 |  |
| `FichaDTAI (Adjunto)` | Ficha de la Vista DTAI |  | N / A |  |  |
| `Visita` | Visita al Puente | Texto | N / A | `S` SI; `N` NO |  |
| `AccesoTM` | Acceso Estacion TM | Texto | N / A | `S` SI; `N` NO |  |
| `Historico` | Historico | Short | Adimensional |  |  |
| `LimiteDistrito` | Puente Sobre el Limite Distrito | Texto | N / A | `S` SI; `N` NO |  |
| `Fase` | Fase | Texto | N / A |  |  |
| `Observacion` | Observacion | Texto | N / A |  |  |
| `ZonaGeologica` | Zona Geológica | Texto | N / A | `1` Rellenos de Basura; `2` Rellenos de Excavación; `3` Suelo Residual; `4` Rondas de Ríos y Humedales; `6` Piedemonte; `8` Suelos Duros; `9` Arcilla Blanda; `9A` Transición entre Zonas 2y 4; `9B` Transición entre Zonas 2 y 6; `9C` Transición entre Zonas 4 y 6; `9D` Transición entre Zonas 4 y 7; `9E` Transición entre Zonas 5 y 7; `9F` Transición entre Zonas 5 y 8; `9G` Transición entre Zonas 6 y 7; `12` Roca |  |
| `ZonaSisimica` | Zona Sísmica | Texto | N / A | `1` Cerros; `2` Piedemonte; `3` Lacustre A; `4` Lacustre B; `5A` Terrazas y Conos Orientales; `5B` Terrazas y Conos Occidentales; `7` Transición entre Zonas 1 y 2; `8` Transición entre Zonas 1 y 5; `9` Transición entre Zonas 1 y 5 a; `10` Transición entre Zonas 2 y 3; `11` Transición entre Zonas 2 y 5 a; `12` Transición entre Zonas 3 y 4; `13` Transición entre Zonas 3 y 5 a; `14` Transición entre Zonas 5 y 5 a |  |
| `TipoTransmilenio` | Tipo Transmielnio | Texto | N / A | `S` SI; `N` NO |  |

### PuenteElementoLinea

Geometría **línea**; elementos: Baranda, Barrera Puente, Cercha, Diafragma, Guarda Ruedas, Junta de Dilatación, Viga.
Elemento que corresponde a la contención peatonal cuando existe flujo compartido entre vehículo y peatón

Atributos de **PuenteElementoLinea**

| Campo | Alias | Tipo | Unidad | Dominio o rango | Marca |
|---|---|---|---|---|---|
| `PK_ID_ElementoPuente_L` | PK_ID_ElementoPuente_L | Entero Largo | N / A |  | obligatorio |
| `FK_ID_Puente` | FK_ID_Puente | Entero Largo | N / A |  | obligatorio |
| `CIV` | CIV | Entero | N / A |  | obligatorio |
| `Clase / Tipo` | Clase / Tipo | Texto | N / A | `CMN` Concreto y Metálica no Estandar; `CRN` Solo Concreto no Estandar; `M80` Baranda Metálica con un tubo M80; `M81` Baranda Metálica con dos tubos M81; `M82` Baranda Metálica con tres tubos M82; `MTN` Solo Metálica no Estandar; `A130` Barrera ciclorruta - pieza continua A130; `A140` Barrera ciclorruta - pieza aislada A140; `A150` Barrera ciclorruta - pieza de remate A150; `A160` Barrera ciclorruta - pieza rampa A160; `A170` Borde separador verde A170; `A180` A 180 Barrera de seguridad de concreto Tipo A; `BNJM` Barrera Monodireccional (New Jersey); `BNJB` Barrera Bidireccional (New Jersey); `1` No aplica; `1` No aplica; `1` No aplica; `1` No aplica; `C` Cabezal; `L` Longitudinal | obligatorio |
| `Ancho` | Ancho | Decimal | Metro (m) | rango 0.05 a 1 | obligatorio |
| `Alto` | Alto | Decimal | Metro (m) | rango 0.05 a 5 | obligatorio |
| `Largo` | Largo | Decimal | Metro (m) | rango 1 a 80 | obligatorio |
| `Volumen` | Volumen | Decimal | Metro cúbico (m3) | rango 0.01 a 5 | obligatorio |
| `TipoMaterial` | Tipo Material | Entero | N / A | `1` Concreto; `2` Metálico; `3` Mixto; `5` No Convencionales | obligatorio |
| `FechaRegistro` | Fecha de Registro | Fecha | N / A |  | obligatorio |

Tabla relacionada **DetallePuenteElemento** (Detalle Puente Elemento), de PuenteElementoLinea

| Campo | Alias | Tipo | Unidad | Dominio o rango | Marca |
|---|---|---|---|---|---|
| `PK_ID_DetallePuenteElemento` | PK_ID_DetallePuenteElemento | Entero Largo | N / A |  | obligatorio |
| `FK_ID_PuenteLP` | FK_ID_PuenteLP | Entero Largo | Adimensional | `SemAreaTotal` Area Total de Soldadura de Elementos Metálicos; `SemEspesorDiseno` Espesor Soldadura del diseño; `PinturaEspesorDiseno` Espesor Pintura del diseño; `AfAreaTotal` Area Superficial Total del elemento que corresponde a la suma de todas las caras del elemento; `DMaxPermitida` Deflexion Maxima Permitida; `SemAreaTotal` Area Total de Soldadura de Elementos Metálicos; `SemEspesorDiseno` Espesor Soldadura del diseño; `PinturaEspesorDiseno` Espesor Pintura del diseño; `AfAreaTotal` Area Superficial Total del elemento que corresponde a la suma de todas las caras del elemento; `DMaxPermitida` Deflexion Maxima Permitida; `SemAreaTotal` Area Total de Soldadura de Elementos Metálicos; `SemEspesorDiseno` Espesor Soldadura del diseño; `PinturaEspesorDiseno` Espesor Pintura del diseño; `AfAreaTotal` Area Superficial Total del elemento que corresponde a la suma de todas las caras del elemento; `DMaxPermitida` Deflexion Maxima Permitida; `SemAreaTotal` Area Total de Soldadura de Elementos Metálicos; `SemEspesorDiseno` Espesor Soldadura del diseño; `PinturaEspesorDiseno` Espesor Pintura del diseño; `AfAreaTotal` Area Superficial Total del elemento que corresponde a la suma de todas las caras del elemento; `DMaxPermitida` Deflexion Maxima Permitida; `SemAreaTotal` Area Total de Soldadura de Elementos Metálicos; `SemEspesorDiseno` Espesor Soldadura del diseño; `PinturaEspesorDiseno` Espesor Pintura del diseño; `AfAreaTotal` Area Superficial Total del elemento que corresponde a la suma de todas las caras del elemento; `DMaxPermitida` Deflexion Maxima Permitida; `SemAreaTotal` Area Total de Soldadura de Elementos Metálicos; `SemEspesorDiseno` Espesor Soldadura del diseño; `PinturaEspesorDiseno` Espesor Pintura del diseño; `AfAreaTotal` Area Superficial Total del elemento que corresponde a la suma de todas las caras del elemento; `DMaxPermitida` Deflexion Maxima Permitida | obligatorio |
| `SemAreaTotal` | SemArea Total | Según el parametro evaluado |  |  | obligatorio |
| `SemEspesorDiseno` | Espesor Soldadura Diseño | Según el parametro evaluado |  |  | obligatorio |
| `PinturaEspesorDiseno` | Espesor Pintura Diseño | Según el parametro evaluado | Milímetro (mm) |  | obligatorio |
| `AfAreaTotal` | Area Superficial Total | Según el parametro evaluado | Metro cuadrado (m2) | rango 0.1 a 50 | obligatorio |
| `DMaxPermitida` | Deflexion Maxima Permitida | Según el parametro evaluado |  |  | obligatorio |

Tabla relacionada **DetalleParametroPuente** (Detalle Parametro Puente), de PuenteElementoLinea

| Campo | Alias | Tipo | Unidad | Dominio o rango | Marca |
|---|---|---|---|---|---|
| `PK_ID_DetalleParametroPuente` | PK_ID_DetalleParametroPuente | Entero Largo | N / A |  | obligatorio |
| `FK_ID_ElementoPuente` | FK_ID_ElementoPuente | Entero Largo | N / A |  | obligatorio |
| `ElementoPuente / Aspecto` | ElementoPuente / Aspecto | Entero |  | `1` CHormigueros; `1` AreaSoldaduraDis; `1` AreaHumedad; `2` LongitudFisuracionMaxima |  |
| `Valor` | Valor | Según el parametro evaluado |  |  | obligatorio |

Tabla relacionada **DiagnosticoElemento** (Diagnostico Elemento), de PuenteElementoLinea

| Campo | Alias | Tipo | Unidad | Dominio o rango | Marca |
|---|---|---|---|---|---|
| `PK_ID_DiagnosticoElemento` | PK_ID_DiagnosticoElemento | Entero Largo | N / A |  | sin columna de etapa: ver plantilla |
| `FK_PK_ElementoPuente` | FK_PK_ElementoPuente | Entero Largo | N / A |  | sin columna de etapa: ver plantilla |
| `Fase` | Fase | Texto | N / A |  | sin columna de etapa: ver plantilla |
| `Contrato` | Contrato | Texto | N / A |  | sin columna de etapa: ver plantilla |
| `ElementoPuente` | Elemento Puente | Texto | N / A | `ALE` Aleta de Estribo; `BRP` Baranda; `BRC` Barrera; `CAS` Caisson; `CER` Cercha; `COL` Columna; `DAD` Dado; `DRF` Diafragma; `ETB` Estribo; `GUR` Guardaruedas; `JTA` Juntas de Dilatación; `LAP` Losa de Aproximación; `PIL` Pila; `PLT` Pilote; `RAM` Rampa Puente; `TAB` Tablero; `VIG` Viga | sin columna de etapa: ver plantilla |

### PuenteElementoPoligono

Geometría **polígono**; elementos: Aleta de Estribo, Caisson, Columna, Dado, Estribo, Losa de Aproximación, Pila, Pilote, Rampa de Puente, Tablero.
Elemento del estribo que tiene la función de contener o proteger lateralmente los terraplenes de los accesos del puente.

Atributos de **PuenteElementoPoligono**

| Campo | Alias | Tipo | Unidad | Dominio o rango | Marca |
|---|---|---|---|---|---|
| `PK_ID_ElementoPuente_P` | PK_ID_ElementoPuente_P | Entero |  |  | obligatorio |
| `FK_ID_Puente` | FK_ID_Puente | Entero |  |  | obligatorio |
| `CIV` | CIV | Entero |  |  | obligatorio |
| `Clase` | Clase | Entero |  | `0` Aleta Estribo; `1` Caisson; `2` Columna; `3` Dado; `4` Estribo; `5` Losa de Aproximacion; `6` Pila; `7` Pilote; `8` Rampa Puente; `9` Tablero | obligatorio |
| `Ancho` | Ancho | Decimal |  |  | obligatorio |
| `Alto` | Alto | Decimal |  |  | obligatorio |
| `Largo` | Largo | Decimal |  |  | obligatorio |
| `Volumen` | Volumen | Decimal |  |  | obligatorio |
| `TipoMaterial` | Tipo Material | Entero |  | `1` Concreto; `2` Metálico; `3` Mixto; `5` No Convencionales | obligatorio |
| `FechaRegistro` | Fecha de Registro | Fecha |  |  | obligatorio |

Tabla relacionada **DetallePuenteElemento** (Detalle Puente Elemento), de PuenteElementoPoligono

| Campo | Alias | Tipo | Unidad | Dominio o rango | Marca |
|---|---|---|---|---|---|
| `PK_ID_DetallePuenteElemento` | PK_ID_DetallePuenteElemento | Entero Largo |  |  | obligatorio |
| `FK_ID_PuenteLP` | FK_ID_PuenteLP | Entero Largo |  |  | obligatorio |
| `Tipo` | Tipo Elemento puente | Entero |  | rango 1 a 1000; `SemAreaTotal` Area Total de Soldadura de Elementos Metálicos; `SemEspesorDiseno` Espesor Soldadura del diseño; `PinturaEspesorDiseno` Espesor Pintura del diseño; `AfAreaTotal` Area Superficial Total del elemento que corresponde a la suma de todas las caras del elemento; `DMaxPermitida` Deflexion Maxima Permitida; `SemAreaTotal` Area Total de Soldadura de Elementos Metálicos; `SemEspesorDiseno` Espesor Soldadura del diseño; `PinturaEspesorDiseno` Espesor Pintura del diseño; `AfAreaTotal` Area Superficial Total del elemento que corresponde a la suma de todas las caras del elemento; `DMaxPermitida` Deflexion Maxima Permitida; `SemAreaTotal` Area Total de Soldadura de Elementos Metálicos; `SemEspesorDiseno` Espesor Soldadura del diseño; `PinturaEspesorDiseno` Espesor Pintura del diseño; `AfAreaTotal` Area Superficial Total del elemento que corresponde a la suma de todas las caras del elemento; `DMaxPermitida` Deflexion Maxima Permitida; `SemAreaTotal` Area Total de Soldadura de Elementos Metálicos; `SemEspesorDiseno` Espesor Soldadura del diseño; `PinturaEspesorDiseno` Espesor Pintura del diseño; `AfAreaTotal` Area Superficial Total del elemento que corresponde a la suma de todas las caras del elemento; `DMaxPermitida` Deflexion Maxima Permitida; `SemAreaTotal` Area Total de Soldadura de Elementos Metálicos; `SemEspesorDiseno` Espesor Soldadura del diseño; `PinturaEspesorDiseno` Espesor Pintura del diseño; `AfAreaTotal` Area Superficial Total del elemento que corresponde a la suma de todas las caras del elemento; `DMaxPermitida` Deflexion Maxima Permitida; `SemAreaTotal` Area Total de Soldadura de Elementos Metálicos; `SemEspesorDiseno` Espesor Soldadura del diseño; `PinturaEspesorDiseno` Espesor Pintura del diseño; `AfAreaTotal` Area Superficial Total del elemento que corresponde a la suma de todas las caras del elemento; `DMaxPermitida` Deflexion Maxima Permitida; `SemAreaTotal` Area Total de Soldadura de Elementos Metálicos; `SemEspesorDiseno` Espesor Soldadura del diseño; `PinturaEspesorDiseno` Espesor Pintura del diseño; `AfAreaTotal` Area Superficial Total del elemento que corresponde a la suma de todas las caras del elemento; `DMaxPermitida` Deflexion Maxima Permitida; `SemAreaTotal` Area Total de Soldadura de Elementos Metálicos; `SemEspesorDiseno` Espesor Soldadura del diseño; `PinturaEspesorDiseno` Espesor Pintura del diseño; `AfAreaTotal` Area Superficial Total del elemento que corresponde a la suma de todas las caras del elemento; `DMaxPermitida` Deflexion Maxima Permitida; `SemAreaTotal` Area Total de Soldadura de Elementos Metálicos; `SemEspesorDiseno` Espesor Soldadura del diseño; `PinturaEspesorDiseno` Espesor Pintura del diseño; `AfAreaTotal` Area Superficial Total del elemento que corresponde a la suma de todas las caras del elemento; `DMaxPermitida` Deflexion Maxima Permitida; `SemAreaTotal` Area Total de Soldadura de Elementos Metálicos; `SemEspesorDiseno` Espesor Soldadura del diseño; `PinturaEspesorDiseno` Espesor Pintura del diseño; `AfAreaTotal` Area Superficial Total del elemento que corresponde a la suma de todas las caras del elemento; `DMaxPermitida` Deflexion Maxima Permitida |  |
| `SemAreaTotal` | SemArea Total | Según el parametro evaluado |  |  | obligatorio |
| `SemEspesorDiseno` | Espesor Soldadura Diseño | Según el parametro evaluado |  |  | obligatorio |
| `PinturaEspesorDiseno` | Espesor Pintura Diseño | Según el parametro evaluado |  |  | obligatorio |
| `AfAreaTotal` | Area Superficial Total | Según el parametro evaluado |  | rango 0.1 a 50 | obligatorio |
| `DMaxPermitida` | Deflexion Maxima Permitida | Según el parametro evaluado |  |  | obligatorio |

Tabla relacionada **DetalleParametroPuente** (Detalle Parametro Puente), de PuenteElementoPoligono

| Campo | Alias | Tipo | Unidad | Dominio o rango | Marca |
|---|---|---|---|---|---|
| `PK_ID_DetalleParametroPuente` | PK_ID_DetalleParametroPuente | Entero Largo |  |  | obligatorio |
| `FK_ID_ElementoPuente` | FK_ID_ElementoPuente | Entero Largo |  |  | obligatorio |
| `ElementoPuente / Aspecto` | ElementoPuente / Aspecto | Entero |  | `1` Vexcavacion; `2` CantidadAcero; `3` AMaxPermitido; `4` LFMaxPermitido; `1` Radio; `1` AMaxPermitido; `2` LFMaxPermitido; `3` Radio; `4` AHVerticalidad; `5` AHAlineamiento; `1` AMaxPermitido; `2` LFMaxPermitido; `3` VEstructuralDiseno; `4` Edad; `5` Area; `1` AMaxPermitido; `2` LFMaxPermitido; `3` AHVerticalidad; `4` AHAlineamiento; `1` AMaxPermitido; `2` AHVerticalidad; `3` AHAlineamiento; `4` Area; `1` AMaxPermitido; `2` Area; `3` Tipo; `1` AMaxPermitido; `2` Pendiente; `1` LFMaxPermitido; `2` AHVerticalidad; `3` AHAlineamiento |  |
| `Valor` | Valor | Según el parametro evaluado |  |  | obligatorio |

Tabla relacionada **DiagnosticoElemento** (Diagnostico Elemento), de PuenteElementoPoligono

| Campo | Alias | Tipo | Unidad | Dominio o rango | Marca |
|---|---|---|---|---|---|
| `PK_ID_DiagnosticoElemento` | PK_ID_DiagnosticoElemento | Entero Largo |  |  | sin columna de etapa: ver plantilla |
| `FK_PK_ElementoPuente` | FK_PK_ElementoPuente | Entero Largo |  |  | sin columna de etapa: ver plantilla |
| `Fase` | Fase | Texto |  |  | sin columna de etapa: ver plantilla |
| `Contrato` | Contrato | Texto |  |  | sin columna de etapa: ver plantilla |
| `ElementoPuente` | Elemento Puente | Texto |  | `ALE` Aleta de Estribo; `BRP` Baranda; `BRC` Barrera; `CAS` Caisson; `CER` Cercha; `COL` Columna; `DAD` Dado; `DRF` Diafragma; `ETB` Estribo; `GUR` Guardaruedas; `JTA` Juntas de Dilatación; `LAP` Losa de Aproximación; `PIL` Pila; `PLT` Pilote; `RAM` Rampa Puente; `TAB` Tablero; `VIG` Viga | sin columna de etapa: ver plantilla |

## InfraestructuraTransporte

### Estacion

Geometría **polígono**; elementos: Estación.
Son puntos de parada sobre los corredores troncales, en donde ascienden o descienden pasajeros, ubicadas en el separador central de cada vía. Su espaciamiento está entre 500 y 700 metros aproximadamente y operan únicamente con vehículos del sistema troncal. Su tamaño depende de la demanda específica, teniéndose tipologías de 1, 2 y 3 vagones en cada estación, en las estaciones de integración o en …

Atributos de **Estacion**

| Campo | Alias | Tipo | Unidad | Dominio o rango | Marca |
|---|---|---|---|---|---|
| `PK_ID_Estacion` | PK_ID_Estacion | Entero | N / A |  | obligatorio |
| `CIV` | Codigo de Identificaicon Vial | Entero | N / A |  | obligatorio |
| `NombreEstacion` | Nombre Estación | Texto | N / A |  | obligatorio |
| `Capacidad` | Capacidad | Entero | Adimensional |  | obligatorio |
| `Estado` | Estado Condición | Texto | N / A | `B` Bueno; `M` Malo; `R` Regular | obligatorio |
| `TipoServicio / Estacion` | Tipo Servicio Tipo Estacion | Entero | N / A | `0` Sin Especificacion; `1` Retorno; `2` Matriz; `3` Intermedia; `4` Parkin; `0` Sin Especificacion; `0` Sin Especificacion; `0` Sin Especificacion; `0` Sin Especificacion; `5` Patrón 1: 3 vagones - 2 accesos; `6` Patrón 2: 2 vagones - 2 accesos; `7` Patrón 2: 2 vagones - 1 acceso; `8` Patrón 3: 2 vagones - 2 accesos; `9` Patrón 3: 2 vagones - 1 acceso; `10` Patrón 4: 1 vagón - 1 acceso; `0` Sin Especificacion | obligatorio |
| `Nivel` | Niveles Estacion | Entero | N / A | `1` Embarque (abordaje); `2` Acceso; `3` Matriz; `4` Area disponible | obligatorio |
| `FechaRegistro` | Fecha de Registro | Fecha | N / A |  | obligatorio |

### LineaTM

Geometría **línea**; elementos: Línea Transporte Masivo.

Atributos de **LineaTM**

| Campo | Alias | Tipo | Unidad | Dominio o rango | Marca |
|---|---|---|---|---|---|
| `PK_ID_LineaTM` | PK_ID_LineaTM | Entero Largo | N / A |  | obligatorio |
| `NombreLinea` | Nombre Linea | Texto | N / A |  | obligatorio |
| `LongitudLinea` | Longitud Linea | Decimal | Metro (m) | rango 10000 a 500000 | obligatorio |
| `Capacidad` | Capacidad Linea | Entero | Adimensional |  | obligatorio |
| `NumVehiculos` | Numero Vehiculos | Entero corto | Adimensional | rango 1 a 200 | obligatorio |
| `Velocidad` | Velocidad Operación | Decimal | Metro por segundo (m/s) | rango 0.2 a 10 | obligatorio |
| `NumEstaciones` | Numero Estaciones | Entero corto | Adimensional | rango 2 a 20 | obligatorio |
| `TipoVehiculo` | Tipo Vehiculo | Entero | N / A | `1` 10 MGD; `2` 8 MGD; `3` 15 MGD | obligatorio |
| `TiempoRecorrido` | Tiempo de recorrido | Decimal | Minuto (min) | rango 1 a 50 | obligatorio |
| `Servicio` | Servicio | Entero | N / A | `0` Alimentador; `1` Cable; `2` Complementario; `3` Especial; `4` Metro; `5` Metro Ligero; `6` TransMilenio; `7` Urbano | obligatorio |
| `TipoCable` | Tipo cable | Texto | N / A |  | obligatorio |
| `DiametroCable` | Diametro cable | Decimal | Pulgada (") | rango 1 a 5 | obligatorio |
| `CantidadTorres` | Cantidad de torres | Entero | Adimensional | rango 1 a 100 | obligatorio |

### Paradero

Geometría **punto**; elementos: Paradero.
Es un elemento que demarca y señala los sitios de parada del transporte público protegiendo al usuario de la lluvia y el sol.

Atributos de **Paradero**

| Campo | Alias | Tipo | Unidad | Dominio o rango | Marca |
|---|---|---|---|---|---|
| `PK_ID_Paradero` | PK_ID_Paradero | Entero Largo | N / A |  | obligatorio |
| `CIV` | CIV | Entero Largo | N / A |  | obligatorio |
| `TipoParadero` | Tipo de paradero | Texto | N / A | `M10` Paradero M10; `SA1` Señal Alimentador; `ST1` Señal Tipo 1: De 1 a 2 rutas; `ST2` Señal Tipo 2: De 3 a 5 rutas; `ST3` Señal Tipo 3: De 6 a 8 rutas; `ST4` Señal Tipo 4: De 9 a 11 rutas; `ST5` Señal Tipo 5: De 12 a 20 rutas | obligatorio |
| `LongitudParadero` | Longitud | Decimal | Metro (m) | rango 5 a 50 | obligatorio |
| `AnchoParadero` | Ancho | Decimal | Metro (m) | rango 1 a 10 | obligatorio |
| `AreaParadero` | Área | Decimal | Metro cuadrado (m2) | rango 5 a 200 | obligatorio |
| `FechaRegistro` | Fecha de Registro | Fecha | N / A |  | obligatorio |

Tabla relacionada **ServicioParadero** (Servicio Paradero), de Paradero

| Campo | Alias | Tipo | Unidad | Dominio o rango | Marca |
|---|---|---|---|---|---|
| `PK_ID_TipoServicio` | PK_ID_TipoServicio | Entero Largo |  |  | obligatorio |
| `FK_ID_Paradero` | FK_ID_Paradero | Entero Largo |  |  | obligatorio |
| `TipoServicio` | Tipo de servicio | Entero |  | `0` TransMilenio; `1` Alimentador; `2` Metro; `3` Metro Ligero; `4` Cable; `5` Urbano; `6` Complementario; `7` Especial; `8` SITP | obligatorio |

Tabla relacionada **DetalleMobiliario** (Detalle Mobiliario), de Paradero

| Campo | Alias | Tipo | Unidad | Dominio o rango | Marca |
|---|---|---|---|---|---|
| `PK_ID_DetalleMobiliario` | PK_ID_Detalle Mobiliario | Entero Largo | N / A |  | obligatorio |
| `FK_ID_Mobiliario` | FK_ID_Mobiliario | Entero Largo | N / A |  | obligatorio |
| `Estado` | Estado de condición | Texto | N / A | `B` Bueno; `M` Malo; `R` Regular | obligatorio |
| `CumpleFuncionalidad` | Cumple Funcionalidad | Texto | N / A | `S` Si; `N` No | obligatorio |
| `ICEMU` | Indice de Condición de Mobiliario Urbano | Entero | Porcentaje (%) | rango 0 a 100 | obligatorio |
| `FechaMedicionICEMU` | Fecha Medicion ICEMU | Fecha | N / A |  | obligatorio |
| `Dano` | Daño | Entero | N / A | `0` No presenta; `1` Ligero; `2` Moderado; `3` Semisevero; `4` Severo; `5` Completamente inservible | obligatorio |

### PatioGaraje

Geometría **polígono**; elementos: PatioGaraje.
Espacio destinado a realizar las labores de mantenimiento de los buses de Transmilenio y su estacionamiento al finalizar la operación.

Atributos de **PatioGaraje**

| Campo | Alias | Tipo | Unidad | Dominio o rango | Marca |
|---|---|---|---|---|---|
| `PK_ID_PatioGaraje` | PK_ID_PatioGaraje | Entero Largo | N / A |  | obligatorio |
| `AreaPatioGaraje` | Área | Decimal | Metro cuadrado (m2) | rango 5000 a 50000 | obligatorio |
| `TipoServicio` | Tipo de servicio SITP | Entero | N / A | `0` TransMilenio; `1` Alimentador; `2` Metro; `3` Metro Ligero; `4` Cable; `5` Urbano; `6` Complementario; `7` Especial | obligatorio |
| `NombrePatioGaraje` | Nombre del garaje | Texto | N / A |  | obligatorio |
| `FechaRegistro` | Fecha de Registro | Fecha | N / A |  | obligatorio |

### Portal

Geometría **polígono**; elementos: Portal.
Estaciones de Integración de Cabecera o “Portales”: Son los puntos de inicio y finalización de las rutas troncales. En estas estaciones se realizan transbordos entre rutas troncales y rutas alimentadoras e intermunicipales. La función de estas estaciones es permitir los transbordos de pasajeros entre las rutas alimentadoras y las rutas troncales de forma ágil y eficiente.

Atributos de **Portal**

| Campo | Alias | Tipo | Unidad | Dominio o rango | Marca |
|---|---|---|---|---|---|
| `PK_ID_Portal` | PK_ID_Portal | Entero Largo | N / A |  | obligatorio |
| `NombrePortal` | Nombre Portal | Texto | N / A |  | obligatorio |
| `AreaPortal` | Área | Decimal | Metro cuadrado (m2) | rango 10000 a 500000 | obligatorio |
| `Estado` | Estado de condición | Texto | N / A | `B` Bueno; `M` Malo; `R` Regular | obligatorio |
| `TipoServicio` | Tipo Servicio | Entero | N / A | `0` Transmilenio; `1` SITP; `2` Metro; `3` Metro Ligero | obligatorio |
| `FechaRegistro` | Fecha de Registro | Fecha | N / A |  | obligatorio |

### TorreCable

Geometría **polígono**; elementos: Torre Cable.

Atributos de **TorreCable**

| Campo | Alias | Tipo | Unidad | Dominio o rango | Marca |
|---|---|---|---|---|---|
| `PK_ID_TorreCable` | PK_ID_TorreCable | Entero | N / A |  | obligatorio |
| `NombreTorre` | Nombre Torre | Texto | N / A |  | obligatorio |
| `Codigo` | Codigo Torre | Texto | N / A |  | obligatorio |
| `TrenPolea` | Tren Polea | Texto | N / A |  | obligatorio |
| `Linea` | Línea | Texto | N / A |  | obligatorio |
| `Abscisa` | Abscisa | Decimal | Metro (m) |  | obligatorio |
| `CotaFundacion` | Cota fundación | Decimal | Metro (m) |  | obligatorio |
| `Altura` | Altura de la torre | Decimal | Metro (m) |  | obligatorio |
| `InclinacionVertical` | Inclinación vertical de la torre | Texto | Grado sexagesimal (° ' ") |  | obligatorio |
| `TipoAcero` | Tipo de acero | Texto | N / A |  | obligatorio |
| `Estado` | Estado de condición | Texto | N / A | `B` Bueno; `M` Malo; `R` Regular | obligatorio |
| `TipoMaterial` | Tipo de material de la torre | Entero | N / A | `0` Concreto; `1` Metalica | obligatorio |
| `TipologiaTorre` | Tipología de la torre | Entero | N / A | `1` TRACCION; `2` COMPRESION; `3` COMBINADO | obligatorio |
| `FechaRegistro` | Fecha de Registro | Fecha | N / A |  | obligatorio |

## InfraestructuraVial

### Bahia

Geometría **polígono**; elementos: Bahía.
Parte complementaria de la vía localizada entre la calzada y el andén que cuenta con una zona de aproximación, una de transición de ingreso, una zona de parada y una transición de salida. Usualmente se destina al estacionamiento de vehículos.

Atributos de **Bahia**

| Campo | Alias | Tipo | Unidad | Dominio o rango | Marca |
|---|---|---|---|---|---|
| `PK_ID_Bahia` | PK_ID_Bahia | Entero Largo | N / A |  | obligatorio |
| `CIV` | CIV | Entero Largo | N / A |  | obligatorio |
| `AreaBahia` | Área | Decimal | Metro cuadrado (m2) | rango 10 a 500 | obligatorio |
| `AnchoBahia` | Ancho | Decimal | Metro (m) | rango 1 a 10 | obligatorio |
| `LongitudBahia` | Longitud | Decimal | Metro (m) | rango 3 a 100 | obligatorio |
| `FechaRegistro` | Fecha de Registro | Fecha | N / A |  | obligatorio |

### Barrera

Geometría **polígono**; elementos: Barrera.
Elemento de separación de la calzada y andenes estrechos en condiciones críticas de circulación, o cuando se presenten diferentes niveles entre la calzada y el anden o entre tramos o franjas de anden.

Atributos de **Barrera**

| Campo | Alias | Tipo | Unidad | Dominio o rango | Marca |
|---|---|---|---|---|---|
| `PK_ID_Barrera` | PK_ID_Barrera | Entero Largo | N / A |  | obligatorio |
| `CIV` | CIV | Entero Largo | N / A |  | obligatorio |
| `TipoBarrera` | Tipo Barrera | Texto | N / A | `A130` Barrera ciclorruta - pieza continua A130; `A140` Barrera ciclorruta - pieza aislada A140; `A150` Barrera ciclorruta - pieza de remate A150; `A160` Barrera ciclorruta - pieza rampa A160; `A170` Borde separador verde A170; `A180` A 180 Barrera de seguridad de concreto Tipo A; `BNJM` Barrera Monodireccional (New Jersey); `BNJB` Barrera Bidireccional (New Jersey) | obligatorio |
| `LongitudBarrera` | Longitud | Decimal | Metro (m) | rango 2 a 100 | obligatorio |
| `FechaRegistro` | Fecha de Registro | Fecha | N / A |  | obligatorio |

### Berma

Geometría **polígono**; elementos: Berma.
Fajas comprendidas a los lados de los carriles de circulación. Permiten incrementar la capacidad de las vías al generar la sensación de amplitud en la sección, albergar vehículos averiados de modo que no se interrumpa el flujo continuo, y habilitar zonas de desvío en caso de eventualidades. Sirve de confinamiento lateral de la superficie de rodadura y puede ser empleada para el tránsito de …

Atributos de **Berma**

| Campo | Alias | Tipo | Unidad | Dominio o rango | Marca |
|---|---|---|---|---|---|
| `PK_ID_Berma` | PK_ID_Berma | Entero Largo | N / A |  | obligatorio |
| `CIV` | CIV | Entero Largo | N / A |  | obligatorio |
| `TipoSuperficie` | Tipo de superficie | Entero | N / A | `1` Rígido; `2` Flexible; `3` Mixto; `4` Adoquín Concreto; `5` Adoquín Arcilla; `6` Afirmado; `8` Tierra; `12` Piedra Laja | obligatorio |
| `AnchoBerma` | Ancho | Decimal | Metro (m) | rango 0.3 a 10 | obligatorio |
| `LongitudBerma` | Longitud | Decimal | Metro (m) | rango 1 a 500 | obligatorio |
| `AreaBerma` | Área | Decimal | Metro cuadrado (m2) | rango 1 a 2000 | obligatorio |
| `Confina` | Confinamiento | Texto | N / A | `S` Si; `N` No | obligatorio |
| `FechaRegistro` | Fecha de Registro | Fecha | N / A |  | obligatorio |

### Calzada

Geometría **polígono**; elementos: Calzada.
Zona de la vía, destinada a la circulación de vehículos automotores o peatones. Es una franja física y geométricamente definida mediante un eje en planta, una rasante y un ancho total. Su función es soportar la carga para la que fue diseñada y permitir desplazamientos cómodos y seguros.

Atributos de **Calzada**

| Campo | Alias | Tipo | Unidad | Dominio o rango | Marca |
|---|---|---|---|---|---|
| `PK_ID_Calzada` | PK_ID_Calzada | Entero Largo | N / A |  | obligatorio |
| `CIV` | CIV | Entero Largo | N / A |  | obligatorio |
| `AnchoCalzada` | Ancho Calzada | Decimal (Double) | Metro (m) | rango 0 a 14 | obligatorio |
| `AreaCalzada` | Area Calzada | Decimal (Double) | Metro cuadrado (m2) | rango 0 a 7000 | obligatorio |
| `LongitudHorizontal` | Longitud Horizontal | Decimal (Double) | Metro (m) | rango 0 a 500 | obligatorio |
| `PendienteLongitudinal` | Pendiente Longitudinal | Decimal (Double) | Porcentaje (%) | rango 0 a 25 | obligatorio |
| `NumeroCarriles` | Numero Carriles | Entero Corto | Adimensional | rango 1 a 6 | obligatorio |
| `TipoSuperficie` | Tipo de Superficie | Entero Corto | N / A | `0` Sin dato; `1` Rígido; `2` Flexible; `3` Mixtos; `4` Adoquín concreto; `5` Adoquín arcilla; `6` Afirmado; `8` Tierra; `12` Piedra laja; `13` Placa Huella | obligatorio |
| `TipoFuncionalidad` | Tipo Funcionalidad | Entero Corto | N / A | `1` Vehicular; `2` Peatonal | obligatorio |
| `TramoSeguimiento` | Testigo Seguimiento | Texto | N / A | `C` Convencional; `T` Testigo; `P` Prueba | obligatorio |
| `FechaRegistroIDU` | Fecha Registro | Fecha | N / A |  | obligatorio |

Tabla relacionada **EvaluacionFuncional** (Evaluacion Funcional), de Calzada

| Campo | Alias | Tipo | Unidad | Dominio o rango | Marca |
|---|---|---|---|---|---|
| `PK_ID_Funcional` | PK_ID_Funcional | Entero Largo | N / A |  | obligatorio |
| `FK_ID_Calzada` | FK_ID_Calzada | Entero Largo | N / A |  | obligatorio |
| `MetodologiaIRI` | Metodologia IRI | Entero Corto | N / A | `2` Merlin; `3` Rugosimetro; `4` Calificacion Visual; `1` Romdas; `10` APL | obligatorio |
| `FechaMedicionIRI` | Fecha MedicionIRI | Date (Fecha) | N / A |  | obligatorio |
| `IRITotal` | IRI Total | Decimal (Double) | Metro por kilómetro (m/km) | rango 0 a 12 | obligatorio |
| `MetodologiaAhuellamiento` | Metodologia Ahuellamiento | Entero Corto | N / A | `1` Perfilometro Laser u optico; `2` Perfilometro trasnversal; `3` Reglas graduadas; `4` Perfilometro portatil | según alcance |
| `FechaMedicionAhuellamiento` | Fecha Medicion Ahuellamiento | Date (Fecha) | N / A |  | según alcance |
| `TipoAhuellamiento` | Tipo Ahuellamiento | Texto | Centímetro (cm) | rango 0 a 10; `S` Superficial; `E` Estrctural | según alcance |
| `AhuellamientoTotal` | Ahuellamiento Total | Decimal (Double) | Centímetro (cm) |  | según alcance |
| `CalificacionIRI` | Calificacion IRI | Decimal (Double) | Metro por kilómetro (m/km) | rango 0 a 2.5; `MB` Muy Bueno; `B` Bueno; `R` Regular; `M` Malo |  |
| `CalificacionAhuellamiento` | Calificacion Ahuellamiento | Decimal (Double) | Adimensional |  |  |

Tabla relacionada **IRI** (IRI), de EvaluacionFuncional

| Campo | Alias | Tipo | Unidad | Dominio o rango | Marca |
|---|---|---|---|---|---|
| `PK_ID_IRI` | PK_ID_IRI | Entero Largo | N / A |  | obligatorio |
| `FK_ID_Funcional` | FK_ID_Funcional | Entero Largo | N / A |  | obligatorio |
| `Carril` | Carril | Entero Corto | Adimensional | rango 1 a 6 | obligatorio |
| `AbscisaInicial` | Abscisa Inicial | Decimal (Double) | Metro (m) |  | obligatorio |
| `AbscisaFinal` | Abscisa Final | Decimal (Double) | Metro (m) |  | obligatorio |
| `IRIHuellaIzquierda` | IRI Huella Izquierda | Decimal (Double) | Metro por kilómetro (m/km) |  | obligatorio |
| `IRIHuellaDerecha` | IRI Huella Derecha | Decimal (Double) | Metro por kilómetro (m/km) |  | obligatorio |
| `VelocidadOperacion` | Velocidad Operación | Decimal (Double) | Kilómetro por hora (km/h) |  | obligatorio |
| `IRIPromedio` | IRIPromedio | Decimal (Double) | Metro por kilómetro (m/km) |  | obligatorio |

Tabla relacionada **Ahuellamiento** (Ahuellamiento), de EvaluacionFuncional

| Campo | Alias | Tipo | Unidad | Dominio o rango | Marca |
|---|---|---|---|---|---|
| `PK_ID_Ahuellamiento` | PK_ID_Ahuellamiento | Entero Largo | N / A |  | según alcance |
| `FK_ID_Funcional` | FK_ID_Funcional | Entero Largo | N / A |  | según alcance |
| `Carril` | Carril | Entero Corto | Adimensional |  | según alcance |
| `AbscisaInicial` | Abscisa Inicial | Decimal (Double) | Metro (m) |  | según alcance |
| `AbscisaFinal` | Abscisa Final | Decimal (Double) | Metro (m) |  | según alcance |
| `AhuellamientoIzquierda` | Ahuellamiento Izquierda | Decimal (Double) | Centímetro (cm) |  | según alcance |
| `AhuellamientoPromedio` | AhuellamientoPromedio | Decimal (Double) | Centímetro (cm) |  | según alcance |
| `AhuellamientoDerecha` | Ahuellamiento Derecha | Decimal (Double) | Centímetro (cm) |  | según alcance |
| `MaxAhuellamientoIzquierda` | Maximo Ahuellamiento Izquierda | Decimal (Double) | Centímetro (cm) |  | según alcance |
| `VelocidadOperacion` | Velocidad Operación | Decimal (Double) | Kilómetro por hora (km/h) |  | según alcance |
| `MaxAhuellamientoDerecha` | Maximo Ahuellamiento Derecha | Decimal (Double) | Centímetro (cm) |  | según alcance |

Tabla relacionada **EvaluacionEstructural** (Evaluacion Estructural), de Calzada

| Campo | Alias | Tipo | Unidad | Dominio o rango | Marca |
|---|---|---|---|---|---|
| `PK_ID_Estructural` | PK_ID_Estructural | Entero Largo | N / A |  | obligatorio |
| `FK_ID_Calzada` | FK_ID_Calzada | Entero Largo | N / A |  | obligatorio |
| `INDEstructuralMenor` | Indice Estructural Menor | Decimal (Double) | Adimensional | rango 0 a 5 | según alcance |
| `SN` | SN Efectivo | Decimal (Double) | Adimensional |  | obligatorio |
| `FechaMedicionSN` | Fecha Medicion SN | Date (Fecha) | N / A |  | obligatorio |
| `VidaRemanenteAnos` | Vida Remanente Años | Entero Corto | Año | rango 5 a 30 | según alcance |
| `VidaRemanenteEjes` | Vida Remanente Ejes | Entero Largo | Adimensional |  | según alcance |
| `CBR` | CBR | Decimal (Double) | Porcentaje (%) | rango 0 a 15 | obligatorio |
| `FechaMedicionCBR` | Fecha Medicion CBR | Date (Fecha) | N / A |  | obligatorio |
| `ZonaClima` | Zona Clima | Entero Largo | N / A |  |  |

Tabla relacionada **Espesor** (Espesor), de EvaluacionEstructural

| Campo | Alias | Tipo | Unidad | Dominio o rango | Marca |
|---|---|---|---|---|---|
| `PK_ID_Espesor` | PK_ID_Espesor | Entero Largo | N / A |  |  |
| `FK_ID_Estructural` | FK_ID_Estructural | Entero Largo | N / A |  |  |
| `MetodoEspesores` | Metodo Espesores | Entero Corto | N / A | `1` Georadar; `2` Apique; `3` Asignado Georadar; `4` Asignado Apique; `10` Información Secundaria |  |
| `NumeroCapas` | Numero Capas | Entero Corto | Adimensional |  |  |
| `FechaTomaEspesor` | Fecha Toma Espesor | Date (Fecha) | N / A |  |  |
| `EspesorTotal` | Espesor Total | Decimal (Double) | Centímetro (cm) | rango 2 a 100 |  |

Tabla relacionada **EspesorToma** (Espesor Toma), de Espesor

| Campo | Alias | Tipo | Unidad | Dominio o rango | Marca |
|---|---|---|---|---|---|
| `PK_ID_EspesorMedido` | PK_ID_EspesorMedido | Entero Largo | N / A |  |  |
| `FK_ID_Espesor` | FK_ID_Espesor | Entero Largo | N / A |  |  |
| `Capa` | Capa | Texto | N / A | `TH1` Primera capa a partir de la superficie del pavimento; `TH2` Segunda capa a partir de la superficie del pavimento; `TH3` Tercera capa a partir de la superficie del pavimento; `TH4` Cuarta capa a partir de la superficie del pavimento; `TH5` Quinta capa a partir de la superficie del pavimento; `TH6` Sexta capa a partir de la superficie del pavimento |  |
| `Espesor` | Espesor | Decimal (Double) | Centímetro (cm) | rango 2 a 100 |  |
| `Material` | Material | Texto | N / A |  |  |

Tabla relacionada **Deflectometria** (Deflectometria), de EvaluacionEstructural

| Campo | Alias | Tipo | Unidad | Dominio o rango | Marca |
|---|---|---|---|---|---|
| `PK_ID_Deflexion` | PK_ID_Deflexion | Entero Largo | N / A |  | obligatorio |
| `FK_ID_Estructural` | FK_ID_Estructural | Entero Largo | N / A |  | obligatorio |
| `Equipo` | Equipo Deflectometria | Entero Corto | N / A | `0` Deflectómetro de impacto - FWD o HWD; `1` Deflectómetro de Impacto Portable - LWD | obligatorio |
| `FechaToma` | Fecha Toma Deflexion | Date (Fecha) | N / A |  | obligatorio |
| `Carril` | Carril | Entero Corto | Adimensional | rango 1 a 6 | obligatorio |
| `R` | R | Decimal (Double) | Centímetro (cm) | rango 0 a 180 | obligatorio |
| `MrEscogido` | Mr Escogido | Decimal (Double) | Megapascal (MPa) |  | obligatorio |
| `EpEscogido` | Ep Escogido | Decimal (Double) | Megapascal (MPa) |  | obligatorio |
| `C` | Valor de C | Decimal (Double) | Adimensional |  | obligatorio |
| `MrDiseno` | Mr Diseño | Decimal (Double) | Megapascal (MPa) |  | obligatorio |
| `SN` | SN | Decimal (Double) | Adimensional | rango 0.5 a 15 | obligatorio |
| `VMaxSN` | Valor Maximo SN | Decimal (Double) | Adimensional |  | obligatorio |
| `SNAsignado` | SN Asignado | Decimal (Double) | Adimensional |  | obligatorio |
| `AreaCuenco` | AREA | Decimal (Double) | Pulgadas |  | obligatorio |
| `KEstatico` | K Estatico | Decimal (Double) | Megapascal (MPa) |  | obligatorio |
| `Kdinamico` | K Dinamico | Decimal (Double) | Megapascal (MPa) |  | obligatorio |
| `CoordenadaX` | Coordenada X | Decimal (Double) | Metro (m) |  | obligatorio |
| `CoordenadaY` | Coordenada Y | Decimal (Double) | Metro (m) |  | obligatorio |

Tabla relacionada **DeflexionToma** (Deflexion Toma), de Deflectometría

| Campo | Alias | Tipo | Unidad | Dominio o rango | Marca |
|---|---|---|---|---|---|
| `PK_ID_DeflexionToma` | PK_ID_DeflexionToma | Entero Largo | N / A |  | obligatorio |
| `FK_ID_Deflexion` | FK_ID_Deflexion | Entero Largo | N / A |  | obligatorio |
| `DatosDeflexion` | Datos Deflexion | Entero Corto | Micra (µm) | `1` Original; `2` Corregido Carga; `3` Corregido Temperatura | obligatorio |
| `Carga` | Carga | Decimal (Double) | Kilonewton (kN) |  | obligatorio |
| `Deflexion0` | Deflexion 0 | Decimal (Double) | Micra (µm) | rango 5 a 1500 | obligatorio |
| `Deflexion20` | Deflexion20 | Decimal (Double) | Micra (µm) |  | obligatorio |
| `Deflexion30` | Deflexion 30 | Decimal (Double) | Micra (µm) | rango 5 a 1400 | obligatorio |
| `Deflexion45` | Deflexion45 | Decimal (Double) | Micra (µm) |  | obligatorio |
| `Deflexion60` | Deflexion 60 | Decimal (Double) | Micra (µm) | rango 5 a 1300 | obligatorio |
| `Deflexion90` | Deflexion 90 | Decimal (Double) | Micra (µm) | rango 5 a 1200 | obligatorio |
| `Deflexion120` | Deflexion 120 | Decimal (Double) | Micra (µm) | rango 5 a 1100 | obligatorio |
| `Deflexion150` | Deflexion 150 | Decimal (Double) | Micra (µm) | rango 5 a 1000 | obligatorio |
| `Deflexion180` | Deflexion 180 | Decimal (Double) | Micra (µm) | rango 5 a 900 | obligatorio |

Tabla relacionada **DeflexionTemperatura** (Deflexion Temperatura), de deflectometría

| Campo | Alias | Tipo | Unidad | Dominio o rango | Marca |
|---|---|---|---|---|---|
| `PK_ID_Dtemperatura` | PK_ID_Dtemperatura | Entero Largo | N /A |  | obligatorio |
| `FK_ID_Deflexion` | FK_ID_Deflexion | Entero Largo | N /A |  | obligatorio |
| `Temperatura` | Temperatura | Entero Corto | N /A | `1` Asfalto; `2` Superficie; `3` Aire | obligatorio |
| `Medicion` | Medicion | Decimal (Double) | Grado Celsius (°C) | rango 5 a 40 | obligatorio |

Tabla relacionada **DeflexionCalculo** (Deflexion Calculo), de Deflectometria

| Campo | Alias | Tipo | Unidad | Dominio o rango | Marca |
|---|---|---|---|---|---|
| `PK_ID_DeflexionCalculo` | PK_ID_DeflexionCalculo | Entero Largo | N / A |  | obligatorio |
| `FK_ID_Deflexion` | FK_ID_Deflexion | Entero Largo | N / A |  | obligatorio |
| `Deflexion` | Deflexion | Entero Corto | N / A | `1` Deflexion 0; `2` Deflexion 30; `3` Deflexion 60; `4` Deflexion 90; `5` Deflexion 120; `6` Deflexion 150; `7` Deflexion 180; `8` Deflexion 20; `10` Deflexion 45 | obligatorio |
| `VerificacionR` | Verificacion R | Texto | N / A | `C` Cumple; `N` No Cumple | obligatorio |
| `Mr` | Mr | Decimal (Float) | Megapascal (MPa) |  | obligatorio |
| `Ep` | Ep | Decimal (Float) | Megapascal (MPa) |  | obligatorio |

Tabla relacionada **EvaluacionSuperficial** (Evaluacion Superficial), de Calzada

| Campo | Alias | Tipo | Unidad | Dominio o rango | Marca |
|---|---|---|---|---|---|
| `PK_ID_Superficial` | PK_ID_Superficial | Entero Largo | N / A |  | según alcance |
| `FK ID Calzada` | FK ID Calzada | Entero Largo | N / A |  | según alcance |
| `PCIPonderado` | PCI Ponderado | Entero Corto | Adimensional | rango 0 a 100 | según alcance |
| `FechaCalculoPCI` | Fecha Calculo PCI | Date (Fecha) | N / A |  | según alcance |
| `IS_` | Indice Falla | Decimal (Float) | Adimensional | rango 0 a 100 |  |
| `FechaMedicionIF` | Fecha Medicion IF | Date (Fecha) | N / A |  |  |
| `MDR` | MDR | Decimal (Float) | Adimensional | rango 0 a 100 |  |
| `FechaMedicionMDR` | Fecha Medicion MDR | Date (Fecha) | N / A |  |  |

Tabla relacionada **UnidadMuestreo** (Unidad Muestreo), de Calzada

| Campo | Alias | Tipo | Unidad | Dominio o rango | Marca |
|---|---|---|---|---|---|
| `PK_ID_UnidadMuestreo` | PK_ID_UnidadMuestreo | Entero Largo | N / A |  | según alcance |
| `FK_ID_Calzada` | FK_ID_Calzada | Entero Largo | N / A |  | según alcance |
| `AbcisaInicial` | Abscisa Inicial | Decimal (Double) | Metro (m) |  | según alcance |
| `AbcisaFinal` | Abscisa Final | Decimal (Double) | Metro (m) |  | según alcance |
| `PCIUnidad` | PCI Unidad | Decimal (Float) | Adimensional | rango 0 a 100 | según alcance |
| `AreaUM` | Área | Decimal (Double) | Metro cuadrado (m2) |  | según alcance |
| `ValorDeducidoM` | Valor Deducido Mayor | Decimal (Double) | Adimensional |  | según alcance |
| `NumeroLosas` | Numero Losas | Entero Largo | Adimensional |  | según alcance |

Tabla relacionada **FallaFlexiblePCI** (FallaFlexiblePCI), de UnidadMuestreo

| Campo | Alias | Tipo | Unidad | Dominio o rango | Marca |
|---|---|---|---|---|---|
| `PK_ID_FallaFlexible_PCI` | PK ID FallaFlexible_PCI | Entero Largo | N / A |  | según alcance |
| `FK_ID_UnidadMuestreo` | FK_ID_UnidadMuestreo | Entero Largo | N / A |  | según alcance |
| `FallaFlexible` | Falla Flexible | Entero Corto | N / A | `1` Piel de Cocodrilo; `2` Exudación; `3` Agrietamiento en Bloque; `4` Abultamientos / Hundimientos; `5` Corrugación; `6` Depresión; `7` Grieta de Borde; `8` Grieta por Reflexión de Juntas; `9` Desnivel Carril / Berma; `10` Grietas Longitudinales y Transversales; `11` Parche; `12` Pulimento de Agregados; `13` Huecos; `14` Cruce de Vía Férrea; `15` Ahuellamiento; `16` Desplazamiento; `17` Grieta Parabólica; `18` Hinchamiento; `19` Desprendimiento de Agregados | según alcance |
| `Severidad` | Severidad | Texto | N / A | `A` Alta; `M` Media; `B` Baja | según alcance |
| `Extension` | Extension | Decimal (Double) | Metro cuadrado (m2) |  | según alcance |
| `Densidad` | Densidad | Decimal (Double) | Porcentaje (%) | rango 0 a 100 | según alcance |
| `ValorDeducido` | Valor deducido | Decimal (Double) | Adimensional |  | según alcance |

Tabla relacionada **CalzadaDetalleRigido** (Calzada Detalle Rigido), de Calzada

| Campo | Alias | Tipo | Unidad | Dominio o rango | Marca |
|---|---|---|---|---|---|
| `PK_ID_CalzadaDRigido` | PK_ID_CalzadaDRigido | Entero Largo | N / A |  | obligatorio |
| `FK_ID_Calzada` | FK_ID_Calzada | Entero Largo | N / A |  | obligatorio |
| `NumeroLosa` | Número losa | Entero | N / A |  | obligatorio |
| `TipoSelloJuntas` | Tipo de sello Juntas | Entero | N / A | `0` Sello de Silicona; `1` Sello en caliente Elastometrico; `2` Sello Preformado; `3` Tirilla o cordon de respaldo; `4` Material de Relleno para junta de expansion | obligatorio |
| `SFC` | Coeficiente de rozamiento | Decimal |  |  |  |
| `TD` | Profundidad de la textura | Entero | Milímetros (mm) |  |  |
| `DensidadMDR` | Densidad MDR | Decimal | Porcentaje (%) |  |  |

Tabla relacionada **TransitoPromedioDiario** (Transito Promedio Diario Semanal), de EstacionMaestra

| Campo | Alias | Tipo | Unidad | Dominio o rango | Marca |
|---|---|---|---|---|---|
| `PK_ID_TPD` | PK_ID_TPD | Entero Largo | N / A |  | según alcance |
| `FK_ID_Calzada` | FK_ID_Calzada | Entero Largo | N / A |  | según alcance |
| `FK_ID_Maestra` | FK_ID_Maestra | Entero Largo | N / A |  | según alcance |
| `TipoTPD` | Tipo TPD | Entero | N / A | `0` Diseño; `1` Aforo; `2` Asignación | según alcance |
| `FechaTPD` | Fecha toma TPD | Fecha | N / A |  | según alcance |
| `TPDMotocicletas` | TPDMotocicletas | Entero | Adimensional |  | según alcance |
| `TPDAutomoviles` | TPD automoviles | Entero | Adimensional |  | según alcance |
| `TPDColectivo` | TPDColectivo | Entero | Adimensional |  | según alcance |
| `TPDBus` | TPD buses | Entero | Adimensional |  | según alcance |
| `TPDBuseta` | TPD busetas | Entero | Adimensional |  | según alcance |
| `TPDAlimentador` | TPD alimentadores | Entero | Adimensional |  | según alcance |
| `TPD_C2P` | TPD camiones de 2 ejes | Entero | Adimensional |  | según alcance |
| `TPD_C2G` | TPD camiones grandes de 2 ejes | Entero | Adimensional |  | según alcance |
| `TPD_C3` | TPD camiones de 3 ejes | Entero | Adimensional |  | según alcance |
| `TPD_C4` | TPD camiones de 4 ejes | Entero | Adimensional |  | según alcance |
| `TPD_C5` | TPD camiones de 5 ejes | Entero | Adimensional |  | según alcance |
| `TPD_C6` | TPD camiones de 6 ejes | Entero | Adimensional |  | según alcance |
| `TPD_>C6` | TPD camiones de mas 6 ejes | Entero | Adimensional |  | según alcance |
| `TPDArticulado` | TPD articulados | Entero | Adimensional |  | según alcance |
| `TPDBiarticulado` | TPD biarticulados | Entero | Adimensional |  | según alcance |
| `EjesEquivalentes` | Ejes equivalentes | Entero | Adimensional |  | según alcance |

Tabla relacionada **EstacionMaestra** (Estacion Maestra), de TransitoPromedioDiario

| Campo | Alias | Tipo | Unidad | Dominio o rango | Marca |
|---|---|---|---|---|---|
| `PK_ID_Maestra` | PK_ID_Maestra | Entero Largo | N / A |  | según alcance |
| `NombreEstacion` | NombreEstacion | Texto | N / A |  | según alcance |
| `Fecha` | Fecha | Fecha | N / A |  | según alcance |
| `FactorExpA` | Factor Expansión Autos | Decimal | Porcentaje (%) | rango 0 a 100 | según alcance |
| `FactorExpB` | Factor Expansión Bus | Decimal | Porcentaje (%) | rango 0 a 100 | según alcance |
| `FactorExpC` | Factor Expansión Camion | Decimal | Porcentaje (%) | rango 0 a 100 | según alcance |

Tabla relacionada **TransitoDiseno** (Transito Diseño), de TransitoPromedioDiario

| Campo | Alias | Tipo | Unidad | Dominio o rango | Marca |
|---|---|---|---|---|---|
| `PK_ID_TPDDiseño` | PK_ID_TPDDiseño | Entero Largo | N / A |  |  |
| `FK_ID_TPD` | FK_ID_TPD | Entero Largo | N / A |  |  |
| `Tipo vehiculo` | Tipo vehiculo | Texto | N / A | `L` Automoviles; `C` Colectivos; `BT` Buseta/BuseTon; `B` Buses; `AL` Alimentador; `AT` Articulado; `BA` Biarticulados; `ESP` Vehiculos Servicio; `INT` Transporte Intermunicipal; `C2P` Camiones de 2 ejes pequeños; `C2G` Camiones de 2 ejes; `C3` Camiones de 3 ejes; `C4` Camiones de 4 ejes; `C5` Camiones de 5 ejes; `C6` Camiones de 6 ejes; `>C6` Camiones mas de 6 ejes; `M` Motos; `BIC` Bicicletas |  |
| `FD` | Factor daño | Double | Adimensional | rango 0 a 15 |  |
| `FC` | Factor Carril | Double | Porcentaje (%) | rango 0 a 100 |  |
| `F_D` | Factor direccional | Double | Porcentaje (%) | rango 0 a 100 |  |
| `TasaCrecimiento` | Tasa crecimiento | Float | Porcentaje (%) | rango 0 a 30 |  |
| `AnosProyeccion` | Años de proyección | Entero Corto | Año | rango 0 a 30 |  |

Tabla relacionada **CalzadaDetalleDiagn** (Calzada Detalle Diagnostico), de Calzada

| Campo | Alias | Tipo | Unidad | Dominio o rango | Marca |
|---|---|---|---|---|---|
| `PK_ID_CalzadaDetalleDiag` | PK_ID_CalzadadetalleDiag | Entero Largo | N / A |  |  |
| `FK_ID_Calzada` | FK_ID_Calzada | Entero Largo | N / A |  |  |
| `Curvatura` | Curvatura | Entero | Grado por kilómetro (grado/km) | rango 0 a 10000 |  |
| `IFVP` | IFVP | Decimal | Adimensional |  |  |
| `FechaMedicionIFVP` | Fecha toma IFVP | Fecha | N / A |  |  |

Tabla relacionada **Capas_Estructura** (Capas Estructura), de Calzada

| Campo | Alias | Tipo | Unidad | Dominio o rango | Marca |
|---|---|---|---|---|---|
| `PK_ID_Capa` | PK_ID_Capa |  |  |  |  |
| `Nombre / Granulometria` | Nombre / Granulometria |  |  | `1` Rodadura MD10; `2` Rodadura MD12; `3` Rodadura MS12; `4` Rodadura MD20; `5` Rodadura MS20; `1` No aplica; `1` No aplica; `1` Capa Intermedia MAM20; `2` Capa Intermedia MD12; `3` Capa Intermedia MD20; `4` Capa Intermedia MS20; `5` Capa Intermedia MS25; `1` Base asfáltica MAM20; `2` Base asfáltica MD20; `3` Base asfáltica MG20; `4` Base asfáltica MG25; `5` Base asfáltica MS25; `1` BG-A; `2` BG-B; `3` BG-C; `1` SBG-A; `2` SBG-B; `3` SBG-C; `1` GEC_A_Gr1; `2` GEC_A_Gr2; `3` GEC_B_Gr1; `4` GEC_B_Gr2; `5` GEC_B_Gr3; `6` GEC_C_Gr1; `7` GEC_C_Gr2; `8` MGEA_A; `9` MGEA_B; `10` MGEA_C; `11` GEEA_AGr1; `12` GEEA_AGr2; `13` GEEA_BGr1; `14` GEEA_BGr2; `15` GEEA_CGr1; `16` GEEA_CGr2; `1` GEC_A_Gr1; `2` GEC_A_Gr2; `3` GEC_B_Gr1; `4` GEC_B_Gr2; `5` GEC_B_Gr3; `6` GEC_C_Gr1; `7` GEC_C_Gr2; `8` MGEA_A; `9` MGEA_B; `10` MGEA_C; `11` GEEA_AGr1; `12` GEEA_AGr2; `13` GEEA_BGr1; `14` GEEA_BGr2; `15` GEEA_CGr1; `16` GEEA_CGr2; `1` No aplica; `1` No aplica; `1` No aplica; `1` No aplica |  |
| `Espesor` | Espesor |  |  | `De acuerdo al documento"ConfiguracionCapaEstructura.xls"` |  |
| `Profundidad_Inicial` | Profundidad Inicial |  |  |  |  |
| `Profundidad_Final` | Profundidad Final |  |  |  |  |
| `Granulometria` | Granulometria |  |  | `De acuerdo al documento"ConfiguracionCapaEstructura.xls"` |  |
| `Material_Encontrado` | Material Encontrado |  |  |  |  |
| `Orden_Capa` | Orden Capa |  |  |  |  |
| `FK_ID_Calzada` | FK_ID_Calzada |  |  |  |  |

Tabla relacionada **TransferenciaCarga** (Transferencia de Carga), de Calzada

| Campo | Alias | Tipo | Unidad | Dominio o rango | Marca |
|---|---|---|---|---|---|
| `PK_ID_Transferencia` | PK_ID_Transferencia | Entero Corto | N / A |  |  |
| `FK_ID_Calzada` | FK_ID_Calzada | Entero Largo | N / A |  |  |
| `TransCarga` | Transferencia de Carga | Decimal (Double) |  |  |  |
| `Fecha de Toma` | Fecha de Toma | Date (Fecha) | N / A |  |  |
| `CoordenadaX` | Coordenada X | Decimal (Double) | Metro (m) |  |  |
| `CoordenadaY` | Coordenada Y | Decimal (Double) | Metro (m) |  |  |
| `DeflexionCero` | Deflexion Cero | Decimal (Float) | Micra (µm) |  |  |
| `DeflexionUno` | Deflexion Uno | Decimal (Float) | Micra (µm) |  |  |

Tabla relacionada **FallaRigidoPCI** (Falla Rigido PCI), de UnidadMuestreo

| Campo | Alias | Tipo | Unidad | Dominio o rango | Marca |
|---|---|---|---|---|---|
| `PK_FallaRigido` | PK_FallaRigido | Entero Largo | N / A |  |  |
| `FK_ID_UnidadMuestreo` | FK_ID_UnidadMuestreo | Entero Largo | N / A |  |  |
| `FallaRigido` | Falla Rigido | Entero Corto | N / A | `21` Blowup / Buckling; `22` Grieta de Esquina; `23` Losa Dividida; `24` Grieta de Durabilidad “D”; `25` Escala; `26` Sello de Junta; `27` Desnivel Carril / Berma; `28` Grietas Lineales; `29` Parche grande; `30` Parche pequeño; `31` Pulimento de Agregados; `32` Popouts; `33` Bombeo; `34` Punzonamiento; `35` Cruce de Vía Férrea; `36` Desconchamiento / Mapa de Grietas / Craquelado; `37` Grietas de Retracción; `38` Descascaramiento de Esquina; `39` Descascaramiento de Junta |  |
| `Severidad` | Severidad | Texto | Adimensional | `A` Alta; `M` Media; `B` Baja |  |
| `Extension` | Extension | Decimal (Double) | Adimensional |  |  |
| `Densidad` | Densidad | Decimal (Double) | Porcentaje (%) | rango 0 a 100 |  |
| `ValorDeducido` | Valor deducido | Decimal (Double) | Adimensional |  |  |

Tabla relacionada **FallaFlexibleMDR** (Falla Flexible MDR), de Calzada

| Campo | Alias | Tipo | Unidad | Dominio o rango | Marca |
|---|---|---|---|---|---|
| `PK_ID_FallaFlexibleMDR` | PK_ID_FallaFlexibleMDR | Entero Largo | N / A |  |  |
| `FK_ID_Calzada` | FK_ID_Calzada | Entero Largo | N / A |  |  |
| `FallaFlexibleMDR` | Falla flexible MDR | Entero | N / A | `14` Peladuras; `15` Exudación de asfalto; `16` Baches descubiertos; `17` Desintegración de bordes; `18` Hundimiento; `19` Corrugaciones y desplazamientos; `20` Ahuellamiento; `21` Fisuramiento longitudinal; `22` Fisuramiento transversal; `23` Fisuramiento de borde; `24` Fisuramiento en bloque; `25` Fisuramiento piel de cocodrilo; `26` Fisuramiento por reflexión de juntas |  |
| `Severidad` | Severidad | Texto | N / A | `A` Alta; `M` Media; `B` Baja |  |
| `Extension` | Extension | Decimal |  |  |  |
| `Densidad` | Densidad | Decimal | Porcentaje (%) |  |  |

Tabla relacionada **FallaArticuladoMDR** (Falla Articulado MDR), de Calzada

| Campo | Alias | Tipo | Unidad | Dominio o rango | Marca |
|---|---|---|---|---|---|
| `PK_ID_FallaArticuladoMDR` | PK_ID_FallaArticuladoMDR | Entero Largo | N / A |  |  |
| `FK_ID_Calzada` | FK_ID_Calzada | Entero Largo | N / A |  |  |
| `FallaArticuladoMDR` | Falla Articulado MDR | Entero | N / A | `27` Deterioro del sello de arena; `28` Desintegración del adoquín; `29` Desniveles en la superficie; `30` Hundimientos; `52` Ahuellamiento; `53` Figuración de adoquines |  |
| `Severidad` | Severidad | Texto | N / A | `A` Alta; `M` Media; `B` Baja |  |
| `Extension` | Extension | Decimal |  |  |  |
| `Densidad` | Densidad | Decimal | Porcentaje (%) |  |  |

Tabla relacionada **FallaAfirmadoMDR** (Falla Afirmado MDR), de Calzada

| Campo | Alias | Tipo | Unidad | Dominio o rango | Marca |
|---|---|---|---|---|---|
| `PK_ID_FallaAfirmadoMDR` | PK_ID_FallaAfirmadoMDR | Entero Largo | N / A |  |  |
| `FK_ID_Calzada` | FK_ID_Calzada | Entero Largo | N / A |  |  |
| `FallaAfirmadoMDR` | Falla afirmado MDR | Entero | N / A | `38` Estado superficie Buena; `39` Estado superficie Regular; `40` Estado superficie Mala |  |
| `Severidad` | Severidad | Texto | N / A | `A` Alta; `M` Media; `B` Baja |  |
| `Extension` | Extension | Decimal |  |  |  |
| `Densidad` | Densidad | Decimal | Porcentaje (%) |  |  |

### Defensa

Geometría **línea**; elementos: Defensa.
Obras destinadas a la protección de las márgenes de una vía ante procesos erosivos.

Atributos de **Defensa**

| Campo | Alias | Tipo | Unidad | Dominio o rango | Marca |
|---|---|---|---|---|---|
| `PK_ID_Defensa` | Código Defensa | Entero Largo | N / A |  | obligatorio |
| `CIV` | CIV | Entero Largo | N / A |  | obligatorio |
| `TipoMaterialDefensa` | Tipo material defensa | Entero | N / A | `0` Metálico; `1` Prefabricado en concreto; `2` Fundido in situ | obligatorio |
| `LongitudDefensa` | Longitud | Decimal | Metro (m) | rango 2 a 100 | obligatorio |
| `FechaRegistro` | Fecha de Registro | Fecha | N / A |  | obligatorio |

### Losa

Geometría **polígono**; elementos: Losa.
Elemento de concreto que conforma la superficie de los pavimentos rígidos; su función principal es estructural; dada su alta resistencia mecánica y su gran rigidez soportan las cargas impuestas por los vehículos, trasmitiendo los esfuerzos a la subrasante en magnitudes acordes con su resistencia.

Atributos de **Losa**

| Campo | Alias | Tipo | Unidad | Dominio o rango | Marca |
|---|---|---|---|---|---|
| `PK_ID_Losa` | PK_ID_Losa | Entero Largo | N / A |  | obligatorio |
| `FK_ID_Calzada` | FK_ID_Calzada | Entero Largo | N / A |  | obligatorio |
| `FuncionalidadLosa` | Funcionalidad losa | Texto | N / A | `T` Carril Transmilenio; `M` Carril Mixto; `P` Portal; `G` Patio Garaje | obligatorio |
| `Orden` | Orden | Entero Corto | Adimensional | rango 1 a 6 |  |
| `Fila` | Fila | Entero Corto | Adimensional | rango 1 a 6 |  |
| `Posicion` | Posición | Entero Corto | Adimensional | rango 1 a 200 |  |
| `AnchoLosa` | Ancho | Decimal (Double) | Metro (m) | rango 0.1 a 6 | obligatorio |
| `LongitudLosa` | Longitud | Decimal (Double) | Metro (m) | rango 0.1 a 6 | obligatorio |
| `AreaLosa` | Área | Decimal (Double) | Metro cuadrado (m2) | rango 0.1 a 36 | obligatorio |
| `EspesorLosa` | Espesor | Decimal (Double) | Centímetro (cm) | rango 10 a 50 | obligatorio |
| `TipoRefuerzo` | Tipo de refuerzo | Entero Corto | N / A | `0` Sin Refuerzo; `1` Con Parrilla; `2` Con Doble Parrilla; `3` Continuamente Reforzada | obligatorio |
| `ModuloRotura` | Modulo Rotura | Decimal (Double) | Megapascal (MPa) | rango 4.0 a 5.0 | obligatorio |
| `ElementosEmbebidos` | Elementos embebidos | Texto | N / A | `P` Pozo Alcantarillado; `S` Sumidero; `E` Caja de inspección; `C` Cámara ESP; `I` Instrumentación; `A` Sumidero y Pozo Alcantarillado; `B` Cámara ESP y Pozo Alcantarillado; `N` No contiene | obligatorio |
| `BarrasAmarre` | Barras de amarre | Texto | N / A | `S` Si; `N` No | obligatorio |
| `BarrasPasajuntas` | Barras PasaJuntas | Texto | N / A | `S` Si; `N` No | obligatorio |
| `TransCarga` | Transferencia de cargas | Decimal | Porcentaje (%) | rango 0 a 100 | obligatorio |
| `ConfinamientoExterno` | Confinamiento externo | Texto | N / A | `BE` Berma; `CU` Cuneta; `SA` Sardinel; `LA` Losa Adyacente; `MU` Muro | obligatorio |
| `ControlErosion` | Control erosión | Texto | N / A | `S` Si; `N` No | obligatorio |
| `FechaRegistro` | Fecha de Registro | Fecha | N / A |  | obligatorio |

Tabla relacionada **Seguimiento** (Seguimiento), de Losa

| Campo | Alias | Tipo | Unidad | Dominio o rango | Marca |
|---|---|---|---|---|---|
| `PK_ID_Seguimiento` | PK_ID_Seguimiento | Entero Largo | N / A |  | obligatorio |
| `FK_ID_Elemento` | FK_ID_Elemento | Entero Largo | N / A |  | obligatorio |
| `Contrato` | Número del contrato | Texto | N / A |  | obligatorio |
| `FechaIntervencion` | Fecha de intervención | Fecha | N / A |  | obligatorio |
| `Costo` | Costo de la intervención | Entero | Pesos MCTE ($) |  | obligatorio |
| `TipoIntervencion` | Tipo de intervención | Entero | N / A | `0` Construcción; `1` Mantenimiento Rutinario; `2` Mantenimiento Periodico; `3` Fresado/Sobrecarpeta; `4` Sobrecarpeta; `5` Rehabilitación; `6` Reconstrucción; `7` Limpieza y reposición de juntas; `8` Tratamiento de fisuras y grietas; `9` Reposición a Profundidad Parcial; `10` Reposición a Profundidad Total; `11` Reemplazo Total; `12` Estabilización; `13` Restitución de transferencia de carga; `14` Generación de juntas; `15` Fresado y nivelación | obligatorio |
| `Cantidad` | Cantidad | Decimal | Según el tipo de intrevención realizado |  | obligatorio |
| `Unidad` | Unidad | Texto | Según la unidad definida | `cm` Centimetro; `cm2` Centimetro Cuadrado; `gr` Gramo; `kg` Kilogramo; `kg_cm2` Kilogramo por Centimetro Cuadrado; `m2` Metro Cuadrado; `mm` Milimetro; `mm2` Milimetro Cuadrado; `m` Metro; `Un` Unidades; `µm` Micra | obligatorio |

Tabla relacionada **FallaLosaPCI** (FallaLosaPCI), de Losa

| Campo | Alias | Tipo | Unidad | Dominio o rango | Marca |
|---|---|---|---|---|---|
| `PK_FallaLosa` | PK_FallaLosa | Entero Largo | N / A |  | según alcance |
| `FK_ID_Losa` | FK_ID_Losa | Entero Largo | N / A |  | según alcance |
| `FallaRigido` | Falla Rigido | Entero Corto | N / A | `0` Blowup / Buckling; `1` Bombeo; `2` Cruce de Vía Férrea; `3` Descascaramiento de Esquina; `4` Descascaramiento de Junta; `5` Desconchamiento / Mapa de Grietas / Craquelado; `6` Desnivel Carril / Berma; `7` Escala; `8` Grieta de Durabilidad “D”; `9` Grieta de Esquina; `10` Grietas de Retracción; `11` Grietas Lineales; `12` Losa Dividida; `13` Parche grande; `14` Parche pequeño; `15` Popouts; `16` Pulimento de Agregados; `17` Punzonamiento; `18` Sello de Junta | según alcance |
| `Severidad` | Severidad | Texto | N / A | `A` Alta; `M` Media; `B` Baja | según alcance |
| `Extension` | Extension | Decimal (Double) | Adimensional |  | según alcance |
| `Densidad` | Densidad | Decimal (Double) | Porcentaje (%) |  | según alcance |
| `ValorDeducido` | Valor Deducido | Decimal (Double) | Adimensional |  | según alcance |

Tabla relacionada **FallaRigidoMDR** (Falla Rigido MDR), de Losa

| Campo | Alias | Tipo | Unidad | Dominio o rango | Marca |
|---|---|---|---|---|---|
| `PK_FallaRigidoMDR` | PK_FallaRigidoMDR | Entero Largo | N / A |  |  |
| `FK_ID_Losa` | FK_ID_Losa | Entero | N / A |  |  |
| `FallaLosaMDR` | Falla Losa MDR | Entero | N / A | `1` Peladuras; `2` Pulimento de la superficie; `3` Descascaramiento fisuras capilares; `4` Bache - desintegración total; `5` Hundimiento – Depresión; `6` Dislocamiento; `7` Fisura longitudinal; `8` Fisuramiento transversal; `9` Fisuramiento diagonal y de esquina; `10` Losas subdivididas; `11` Deficiencias de material de sello; `12` Desportillamiento; `13` Levantamiento |  |
| `Severidad` | Severidad | Texto | N / A | `A` Alta; `M` Media; `B` Baja |  |
| `Extension` | Extension | Decimal |  |  |  |
| `Densidad` | Densidad | Decimal | Porcentaje (%) |  |  |

### Sardinel

Geometría **línea**; elementos: Sardinel.
Elemento que separa una calzada del anden o del separador de una vía

Atributos de **Sardinel**

| Campo | Alias | Tipo | Unidad | Dominio o rango | Marca |
|---|---|---|---|---|---|
| `PK_ID_Sardinel` | PK_ID_Sardinel | Entero Largo | N / A |  | obligatorio |
| `CIV` | CIV | Entero Largo | N / A |  | obligatorio |
| `TipoMaterial` | Tipo de sardinel | Texto | N / A | `1` Fundido in situ; `2` A10 Sardinel Prefabricado Tipo A; `3` A15 Sardinel Prefabricado Tipo B | obligatorio |
| `AnchoSardinel` | Longitud | Decimal | Metro (m) | rango 0 a 0.2 | obligatorio |
| `LongitudSardinel` | Longitud | Decimal | Metro (m) | rango 1 a 500 | obligatorio |
| `SardinelAlineado` | Alineación del sardinel | Texto | N / A | `S` Si; `N` No | obligatorio |
| `SardinelAlturaExterna` | Altura externa del sardinel | Decimal | Metro (m) | rango 0.1 a 0.4 | obligatorio |
| `SardinelAlturaInterna` | Altura interna del sardinel | Decimal | Metro (m) | rango 0 a 0.2 | obligatorio |
| `SardinelHomogeneo` | Homogéneo | Entero | Porcentaje (%) | rango 0 a 100 | obligatorio |
| `SardinelHomologado` | Homologado | Entero | Porcentaje (%) | rango 0 a 100 | obligatorio |
| `ICES` | Índice de Condición de Estado de Sardineles | Entero | Porcentaje (%) | rango 0 a 100 | obligatorio |
| `FechaMedicionICES` | Fecha de medicion ICES | Fecha | N / A |  | obligatorio |
| `FechaRegistro` | Fecha de Registro | Fecha | N / A |  | obligatorio |

### Segmento

Geometría **línea**; elementos: Segmento.
El segmento vial es la mínima unidad geográfica del inventario de la malla vial, se representa mediante un vector georreferenciado localizado aproximadamente en el eje de la vía y delimitado por los ejes de la vías que lo intersectan.

Atributos de **Segmento**

| Campo | Alias | Tipo | Unidad | Dominio o rango | Marca |
|---|---|---|---|---|---|
| `CIV` | Código de Identificación Vial | Entero Largo | N / A |  | obligatorio |
| `Nivel` | Nivel | Entero | N / A | `-1` -1; `0` 0; `1` 1; `2` 2; `3` 3 | obligatorio |
| `CodigoUPZ` | CodigoUPZ | Texto | N / A |  | obligatorio |
| `CodigoLocalidad` | Localidad | Texto | N / A | `01` Usaquen; `02` Chapinero; `03` Santa Fe; `04` San Cristóbal; `05` Usme; `06` Tunjuelito; `07` Bosa; `08` Kennedy; `09` Fontibon; `10` Engativa; `11` Suba; `12` Barrios Unidos; `13` Teusaquillo; `14` Los Mártires; `15` Antonio Nariño; `16` Puente Aranda; `17` La Candelaria; `18` Rafael Uribe Uribe; `19` Ciudad Bolívar; `20` Sumapaz | obligatorio |
| `CodigoVia` | CodigoVia | Entero | N / A | `0` Sin Clasificar; `1` Autopista Al Llano; `10` Avenida Callejas (diagonal 127a); `100` Conector Av la Sirena X Av Paseo de los Libertadores; `101` Conector Av Laureano Gomez X Av Pepe Sierra; `102` Conector Av Medellin X Av Boyaca; `103` Conector Av Medellin X Av Ciudad de Cali; `104` Conector Av Medellin X Av del Congraso Eucaristico; `105` Conector Av Medellin X Av España; `106` Conector Av Paseo del Country X Av Carlos Lleras Restrepo; `107` Conector Av Primero de Mayo X Av. Boyaca; `108` Conector Av Primero de Mayo X Av del Congreso Eucaristico; `109` Conector Av Primero de Mayo X Av Ferrocarril del sur; `11` Avenida Camino del Prado; `110` Conector Av Rodrigo Lara Bonilla X Av Paseo de los Libertadores; `111` Conector Carrera 11 X Av Callejas; `112` Glorieta Av Carlos Lleras Res. Av Paseo Country Av Laureano Gomez; `113` Glorieta Av Congreso Eucaristico X Av Jose Celestino Mutis; `114` Glorieta Av de la Constitucion; `115` Glorieta Av Ferrocarril del Sur Av Batallon Caldas Av Montes; `116` Glorieta Av Jose Celestino Mutis X Av Batallon Caldas; `117` Glorieta Av Jose Celestino Mutis X Av la Esmeralda; `118` Glorieta Av la Hortua Av Fucha Av General Santander; `119` Glorieta Av Primero de Mayo X Av Batallon Caldas; `12` Avenida Caracas; `120` Oreja Autonorte X Calle 170; `121` Oreja Av Alberto Lleras Camargo X Av Carlos Lleras Restrepo; `122` Oreja Av Boyaca X Av Centenario; `123` Oreja Av Callejas X Av Paseo de los Libertadores; `124` Oreja Av Centenario X Av Ciudad de Cali; `125` Oreja Av Chile X Av del Congreso Eucaristico; `126` Oreja Av Ciudad de Quito X Av Medellin; `127` Oreja Av Contador X Av Laureano Gomez; `128` Oreja Av Iberia X Av Paseo de los Libertadores; `129` Oreja Av Jorge Eliecer Gaitan X Av Ciudad de Cali; `13` Avenida Castilla; `130` Oreja Av Jose Celestino Mutis X Av Ciudad de Quito; `131` Oreja Av la Sirena X Av Paseo de los Libertadores; `132` Oreja Av Medellin X Av Boyaca; `133` Oreja Av Medellin X Av del Congreso Eucaristico; `134` Oreja Av Medellin X Av España; `135` Oreja Av Paseo de los Libertadores X Av Ciudad de Quito; `136` Oreja Av Primero de Mayo X Av. Boyaca; `137` Puente Av Alfredo d Bateman X Av Medellin; `138` Retorno Av Apaseo de los Libertadores; `139` Retorno Av Callejas; `14` Avenida Centenario; `140` Retorno Av Jose Celestino Mutis; `141` Avenida San Juan Bosco; `142` Via g; `143` Autopista del Sur y Avenida Ferrocarril; `144` Avenida 85; `145` Avenida a Cota; `146` Avenida Alsacia; `147` Avenida Bolivia; `148` Avenida Bosa; `149` Avenida Camino a Pasquilla; `15` Avenida Chile; `150` Avenida Camino de la Horqueta; `151` Avenida Circunvalar del sur; `152` Avenida de Agua; `153` Avenida de la Guacamaya; `154` Avenida de las Mercedes; `155` Avenida de los Alisos; `156` Avenida de los Muiscas; `157` Avenida del Ferrocarril del sur; `158` Avenida del Rio; `159` Avenida del Salitre; `16` Avenida Ciudad de Cali; `160` Avenida del Tabor; `161` Avenida del tam; `162` Avenida del Uval; `163` Avenida el Cortijo; `164` Avenida el Jardin; `165` Avenida el Polo; `166` Avenida el Rincon; `167` Avenida Gonzalo Ariza; `168` Avenida Guaymaral; `169` Avenida Industrial; `17` Avenida Ciudad de Lima; `170` Avenida Jose Asuncion Silva; `171` Avenida la Alameda del sur; `172` Avenida la Conejera; `173` Avenida la Victoria; `174` Avenida las Quintas; `175` Avenida Longitudinal de Occidente; `176` Avenida los Arrayanes; `177` Avenida Low Murtra; `178` Avenida Manuel Cepeda Vargas; `179` Avenida Morisca; `18` Avenida Ciudad de Quito; `180` Avenida Paisajistica de Tunjuelito; `181` Avenida Paramo; `182` Avenida Perimetral de Usme; `183` Avenida Poporo Quimbaya; `184` Avenida Puente Aranda; `185` Avenida San Antonio; `186` Avenida San Bernardino; `187` Avenida San Francisco; `188` Avenida Santa Fe; `189` Avenida Sumapaz; `19` Avenida Ciudad de Villavicencio; `190` Avenida Tibabita; `191` Avenida Tintal; `192` Avenida Tomas Carrasquilla; `193` Avenida Troncal de Juan rey; `194` Avenida Tunjuelito; `195` Avenida Ustminia; `196` Avenida Versalles; `197` Avenida Xue; `198` Carrera 103; `2` Avenida Carlos Lleras Restrepo; `20` Avenida Colombia; `21` Avenida Colon; `22` Avenida Cordoba; `23` Avenida Cundinamarca; `24` Avenida Dario Echandia; `25` Avenida de la Constitucion; `26` Avenida de la Hortua; `27` Avenida de la Sirena; `28` Avenida de las Americas; `29` Avenida de las Orquideas; `3` Avenida Alejandro Obregon; `30` Avenida de las Villas; `31` Avenida de los Cedritos; `32` Avenida de los Cerros; `33` Avenida de los Comuneros; `34` Avenida del Congreso Eucaristico; `35` Avenida del Contador; `36` Avenida del sur; `37` Avenida España; `38` Avenida Fernando Mazuera; `39` Avenida Ferrocarril de Occidente; `4` Avenida Agoberto Mejia Cifuentes; `40` Avenida Fontibon; `41` Avenida Francisco Miranda; `42` Avenida Fucha; `43` Avenida Gabriel Andrade Lleras; `44` Avenida General Santander; `45` Avenida German Arciniegas; `46` Avenida Iberia; `47` Avenida Jimenez de Quesada; `48` Avenida Jorge Eliecer Gaitan; `49` Avenida Jorge Gaitan Cortes; `5` Avenida Alberto Lleras Camargo; `50` Avenida Jorge Uribe Botero; `51` Avenida Jose Celestino Mutis; `52` Avenida la Esmeralda; `53` Avenida la Esperanza; `54` Avenida Laureano Gomez; `55` Avenida Luis Carlos Galan Sarmiento; `56` Avenida Mariscal Sucre; `57` Avenida Medellin; `58` Avenida Montes; `59` Avenida Pablo Vi; `6` Avenida Alfredo d Bateman; `60` Avenida Paseo de los Libertadores ( Autopista Norte); `61` Avenida Paseo del Country (ak 15); `62` Avenida Pedro Leon Trabuchy; `63` Avenida Pepe Sierra; `64` Avenida Primero de Mayo; `65` Avenida Quiroga; `66` Avenida Rodrigo Lara Bonilla; `67` Avenida San Jose; `68` Avenida Santa Barbara; `69` Avenida Santa Lucia; `7` Avenida Batallon Caldas; `70` Avenida Teusaquillo; `71` Avenida Transversal de Suba; `72` Carrera 106; `73` Carrera 11; `74` Conector Autonorte Calle 170; `75` Conector Av Alberto Lleras Camargo X Av Carlos Lleras Restrepo; `76` Conector Av Alberto Lleras Camargo X Av Contador; `77` Conector Av Alberto Lleras Camargo X Av Contador; `78` Conector Av Alberto Lleras Camargo X Av Pepe Sierra; `79` Conector Av Alberto Lleras Camargo X Av Pepe Sierra; `8` Avenida Boyaca; `80` Conector Av Alejandro Obregon X Av Paseo de los Libertadores; `81` Conector Av Alejandro Obregon X Av Paseo de los Libertadores; `82` Conector Av Alfredo d Bateman X Av Medellin; `83` Conector Av Callejas X Av Paseo de los Libertadores; `84` Conector Av Carlos Lleras Restrepo X Av Laureano Gomez; `85` Conector Av Centenario X Av Ciudad de Cali; `86` Conector Av Centenario X Av Colon; `87` Conector Av Centenario X Av del Congreso Eucaristico; `88` Conector Av Chile X Av Ciudad de Cali; `89` Conector Av Chile X Av del Congreso Eucaristico; `9` Avenida Calle 92; `90` Conector Av Ciudad de Quito X Av Alejandro Obregon; `91` Conector Av Ciudad de Quito X Av de los Comuneros; `92` Conector Av Ciudad de Quito X Av Paseo de los Libertadores; `93` Conector Av Contador X Av Laureano Gomez; `94` Conector Av Contador X Av. Paseo de los Libertadores; `95` Conector Av Francisco de Miranda X Av Ciudad de Quito; `96` Conector Av Iberia X Av Paseo de los Libertadores; `97` Conector Av Jorge Eliecer Gaitan X Av Ciudad de Cali; `98` Conector Av Jose Celestino Mutis X Av Ciudad de Quito; `99` Conector Av la Sirena X Av Paseo de los Libertadores; `199` Conector Av Congreso Eucaristico X Av Jose Celestino Mutis; `200` Conector Autopista Al Llano X Av Circunvalar Del Sur; `201` Oreja Av Jorge Eliecer Gaitan X Av Batallon Caldas; `202` Conector Av Jorge Eliecer Gaitan X Av Batallon Caldas; `203` Conector Av Batallon Caldas X Av Pablo VI; `204` Conector Av Boyaca X Av Centenario; `205` Conector Av Boyaca X Av Ciudad De Villavicencio; `206` Oreja Av Boyaca X Av Ciudad De Villavicencio; `207` Conector Av Boyaca X Av Mariscal Sucre; `208` Oreja Av Boyaca X Av Luis Carlos Galan Sarmiento; `209` Conector Av Boyaca X Av Luis Carlos Galan Sarmiento; `210` Conector Avenida Ciudad de Quito X Avenida Fucha; `233` Conector Av Teusaquillo X Av Jorge Eliecer Gaitan; `211` Conector Av De Las Americas X Av Boyaca; `212` Oreja Av De Las Americas X Av Boyaca; `213` Conector Av Del Congreso Eucaristico X Av Ciudad De Quito; `214` Conector Av Del Congreso Eucaristico X Av De Las Americas; `215` Oreja Av Del Congreso Eucaristico X Av De Las Americas; `216` Conector Av Del Sur X Av Ferrocarril Del Sur; `217` Oreja Av Del Sur X Av Boyaca; `218` Conector Av Del Sur X Av Boyaca; `219` Conector Av Batallon Caldas X Av Ciudad De Quito; `220` Glorieta Av Del Sur X Av Ciudad De Villavicencio; `221` Conector Av Del Sur X Av Ciudad De Villavicencio; `222` Oreja Av Ciudad De Quito X Av Pedro Leon Tabuchy; `224` Conector Av Gabriel Andrade Lleras X Av La Esmeralda; `223` Conector Av Ciudad De Quito X Av Pedro Leon Tabuchy; `225` Oreja Av Jorge Eliecer Gaitan X Av Congreso Eucaristico; `226` Conector Av Jorge Eliecer Gaitan X Av Congreso Eucaristico; `227` Conector Av Luis Carlos Galan Sarmiento X Av Congreso Eucaristico; `228` Oreja Av Luis Carlos Galan Sarmiento X Av Congreso Eucaristico; `229` Conector Av Jorge Eliecer Gaitan X Av Fernando Mazuera; `230` Oreja Av Jorge Eliecer Gaitan X Av Fernando Mazuera; `231` Conector Av Manuel Cepeda Vargas X Av Ciudad De Cali; `232` Glorieta Av Manuel Cepeda Vargas X Av Ciudad De Cali; `234` Oreja Av España X Av Paseo De Los Libertadores; `235` Conector Av España X Av Paseo De Los Libertadores; `236` Oreja Av Carlos Lleras Restrepo X Av Paseo De Los Libertadores; `237` Conector Av Carlos Lleras Restrepo X Av Paseo De Los Libertadores; `238` Conector Av Fernando Mazuera X Av Fucha; `239` Conector Av Fucha X Av Caracas; `240` Conector Av Mariscal De Sucre X Av Fucha; `241` Oreja Av Ciudad De Quito X Av Jorge Eliecer Gaitan; `242` Carrera 3 |  |
| `TipoClasificacionSuelo` | Tipo Clasificacion Suelo | Texto | N / A | `U` Urbano; `R` Rural; `E` Expansion |  |
| `SeccionVial` | Seccion Vial | Entero | N / A | `1` V0; `2` V1; `3` V2; `4` V3; `5` V3E; `6` V4; `7` V5; `8` V6; `9` V7; `10` V8; `11` V9 | obligatorio |
| `TipoMalla` | Tipo Malla | Texto | N / A | `AR` Arterial; `IN` Intermedia; `LO` Local; `RU` Rural; `CM` Circuito Movilidad; `EX` Expansion; `FD` Fuera del Distrito |  |
| `LongitudSegmento` | Longitud del segmento | Decimal | Metro (m) | rango 3 a 2000 | obligatorio |

### Separador

Geometría **polígono**; elementos: Separador.
Franja de una vía dispuesta en forma longitudinal y paralela al eje de la misma que separa y canaliza flujos de circulación y en las cuales se quieran establecer jerarquías en la operación de la vía. Pueden ser centrales y laterales o intermedios. Adicionalmente pueden presentarse en piso duro o blando (zona verde).

Atributos de **Separador**

| Campo | Alias | Tipo | Unidad | Dominio o rango | Marca |
|---|---|---|---|---|---|
| `PK_ID_Separador` | PK_ID_Separador | Entero Largo | N / A |  | obligatorio |
| `CIV` | CIV | Entero Largo | N / A |  | obligatorio |
| `TipoMaterialSeparador` | Tipo Material del Separador | Entero | N / A | `1` Concreto; `2` Adoquín; `3` Tableta; `4` Mixto; `6` Tierra; `7` Grama | obligatorio |
| `AnchoSeparador` | Ancho del Separador | Decimal | Metro (m) | rango 0.5 a 15 | obligatorio |
| `LongitudSeparador` | Longitud del Separador | Decimal | Metro (m) | rango 1 a 2000 | obligatorio |
| `AreaSeparador` | Área del Separador | Decimal | Metro cuadrado (m2) | rango 1 a 5000 | obligatorio |
| `FechaRegistro` | Fecha de Registro | Fecha | N / A |  | obligatorio |

Tabla relacionada **DetalleAndenSeparador** (Detalle Andén y Separador), de Separador

| Campo | Alias | Tipo | Unidad | Dominio o rango | Marca |
|---|---|---|---|---|---|
| `PK_ID_DetalleAndenSeparador` | PK_ID_DetalleAndenSeparador | Entero Largo | N / A |  | obligatorio |
| `FK_ID_DetalleAndenSeparador` | FK_ID_DetalleAndenSeparador | Entero Largo | N / A |  | obligatorio |
| `Estado` | Estado de condición | Texto | N / A | `B` Bueno; `R` Regular; `M` Malo | obligatorio |
| `Homogeneo` | Homogeneo | Entero | Porcentaje (%) | rango 0 a 100 | obligatorio |
| `Homologado` | Homologado | Entero | Porcentaje (%) | rango 0 a 100 | obligatorio |
| `Obstaculos` | Obstaculos | Entero | Porcentaje (%) | rango 0 a 100 | obligatorio |
| `CambioNiveles` | Cambio de Niveles | Texto | N / A | `S` Si; `N` No | obligatorio |
| `RedesSubterraneas` | Redes Subterraneas | Texto | N / A | `S` Si; `N` No | obligatorio |
| `ICEASEP` | Índice de Condición de Estado de Andenes y Separadores | Entero | Porcentaje (%) | rango 0 a 100 | obligatorio |
| `FechaMedicionICEASEP` | Fecha medición del ICEA | Fecha | N / A |  | obligatorio |

Tabla relacionada **AccesibilidadAndSep** (Accesibilidad Andén y Separador), de Separador

| Campo | Alias | Tipo | Unidad | Dominio o rango | Marca |
|---|---|---|---|---|---|
| `PK_ID_AccesibilidadAndenSeparador` | PK_ID_AccesibilidadAndenSeparador | Entero Largo | N / A |  | obligatorio |
| `FK_ID_Accesibilidad` | FK_ID_Accesibilidad | Entero Largo | N / A |  | obligatorio |
| `Senalinvidentes` | Señal Invidentes | Texto | N / A | `S` Si; `N` No | obligatorio |
| `Desnivel` | Accesibilidad | Texto | N / A | `S` Si; `N` No | obligatorio |
| `Vados` | Vados | Texto | N / A | `S` Si; `N` No | obligatorio |

Tabla relacionada **FallaAndenSeparador** (Fallas de Andén y Separador), de Separador

| Campo | Alias | Tipo | Unidad | Dominio o rango | Marca |
|---|---|---|---|---|---|
| `PK_ID_FallaAndenSeparador` | PK_ID_FallaAndenSeparador | Entero Largo | N / A |  |  |
| `FK_ID_FallaAndenSeparador` | FK_ID_FallaAndenSeparador | Entero Largo | N / A |  |  |
| `CodigoDano` | Codigo Daño | Texto | N / A | `D1` Abollado; `D2` Hundido; `D3` Fisurado; `D4` Roto; `D5` Partido; `D6` Golpeado; `D7` Inclinado; `D8` Obstaculización; `D9` Maleza; `D10` Perdida de sello; `D11` Grafiteado; `D12` Pintado; `D13` Desportillado; `D14` Faltante; `D15` Mal estado; `D16` Faltante de Pintura; `D17` Enterrado; `D18` No Se Reportan Daños; `D19` Bordeo; `D20` Destrucción de Alcorque |  |
| `AccionCorrectiva` | Accion Correctiva | Entero | N / A | `1` Reemplazar; `2` Retirar; `3` Reinstalar; `4` Reparar; `5` Mantener |  |
| `TipoMantenimiento` | Tipo Mantenimiento | Entero | N / A | `1` Correctivo; `2` Rehabilitación; `3` Rutinario |  |

### SeparadorLineal

Geometría **polígono**; elementos: Separador Lineal.
Espacio estrecho y saliente que independiza dos calzadas de una vía.

Atributos de **SeparadorLineal**

| Campo | Alias | Tipo | Unidad | Dominio o rango | Marca |
|---|---|---|---|---|---|
| `PK_ID_SeparadoLineal` | PK_ID_SeparadorLineal | Entero Largo | N / A |  | obligatorio |
| `CIV` | CIV | Entero Largo | N / A |  | obligatorio |
| `TipoSepLineal` | Tipo de separador lineal | Texto | N / A | `SLC` Separador de carril Transmilenio (Tachón) 18*20*165 cm en concreto; `SLR1` Separador de carril Transmilenio (Tachón) 18*20*165 cm resina o plastico; `SLR2` Separador de carril Transmilenio (Tacha) 15*13*40 cm en resina o plastico; `SLTC` Tachón en concreto 40*15*8 cm; `SLRU` Tacha reflectiva unidireccional; `BNJM` Barrera Monodireccional (New Jersey); `BNJB` Barrera Bidireccional (New Jersey) | obligatorio |
| `LongitudSepLineal` | Longitud | Decimal | Metro (m) | rango 1 a 2000 | obligatorio |
| `FechaRegistro` | Fecha de Registro | Fecha | N / A |  | obligatorio |

## IntervencionInfraestructuraVial

### AreaIntervencion

Geometría **polígono**; elementos: Área de Intervención.
Es la zona real intervenida para cualquier elemento de la sección transversal asociada a la infraestructura vial.

Atributos de **AreaIntervencion**

| Campo | Alias | Tipo | Unidad | Dominio o rango | Marca |
|---|---|---|---|---|---|
| `PK_ID_AreaIntervencion` | PK_ID_AreaIntervencion | Entero Largo | N / A |  | obligatorio |
| `FK_ID_Elemento` | FK_ID_Elemento | Entero Largo | N / A |  | obligatorio |
| `Elemento` | Clase Elemento | Texto | N / A | `ALA` Alameda; `BAH` Bahia; `CAL` Calzada; `CRU` Ciclorruta; `EST` Estación; `LOS` Losa; `MUG` Muro de Gavion; `MUR` Muro de Concreto; `PLZ` Plaza o Plazoleta; `PRT` Portal; `PUP` Puente Peatonal; `PUV` Puente Vehicular; `SEP` Separador; `TAL` Talud; `BCC` Bicicarril; `AND` Anden | obligatorio |
| `Area` | Área Intervención | Decimal | Metro cuadrado (m2) | rango 0.2 a 4000 | obligatorio |
| `Contrato` | Contrato | Entero | N / A |  | obligatorio |
| `FechaRegistro` | Fecha de Registro | Fecha | N / A |  | obligatorio |

Tabla relacionada **DetalleAIntervencionAndSep** (Detalle Área Intervención Andén Separador), de AreaIntervencion

| Campo | Alias | Tipo | Unidad | Dominio o rango | Marca |
|---|---|---|---|---|---|
| `PK_ID_AIAndenSeparador` | PK_ID_AIAndenSeparador | Entero Largo | N / A |  | obligatorio |
| `FK_ID_AreaIntervencion` | FK_ID_AreaIntervencion | Entero Largo | N / A |  | obligatorio |
| `TipoIntervencion / DetalleIntervencion` | Tipo de intervención / Detalle Intervencion | Entero | N / A | `1` A20 Tableta prefabricada 20*20 cms; `2` A30 Loseta rectangular 60*40 cms; `3` A40 Loseta rectangular 60*20 cms; `4` A50 Loseta rectangular 40*40 cms; `5` A55 Loseta táctil alerta 40*40 cms; `6` A56 Loseta táctil guía 40*40 cms; `7` A60 Loseta rectangular 40*20 cms; `8` A65 Loseta rectangular 40*10 cms; `1` A20 Tableta prefabricada 20*20 cms; `2` A30 Loseta rectangular 60*40 cms; `3` A40 Loseta rectangular 60*20 cms; `4` A50 Loseta rectangular 40*40 cms; `5` A55 Loseta táctil alerta 40*40 cms; `6` A56 Loseta táctil guía 40*40 cms; `7` A60 Loseta rectangular 40*20 cms; `8` A65 Loseta rectangular 40*10 cms; `1` A25 Adoquín rectangular 20*10 cms; `2` A26 Adoquín demarcador 20*5 cms; `3` A27 Adoquín rectangular 10*10 cms; `4` A-29 Adoquín en I 21*14,5 cms; `1` A25 Adoquín rectangular 20*10 cms; `2` A26 Adoquín demarcador 20*5 cms; `3` A27 Adoquín rectangular 10*10 cms; `4` A-29 Adoquín en I 21*14,5 cms | obligatorio |
| `FC` | FC | Entero | Kilogramo por centímetro cuadrado (kg/cm2) | rango 150 a 250 | obligatorio |
| `FechaMedicionFC` | Fecha Medición FC | Fecha | N / A |  | obligatorio |

Tabla relacionada **DetalleAreaIntervencionCalzadaCiclorruta** (Detalle Area Intervencion Calzada Ciclorruta), de AreaIntervencion

| Campo | Alias | Tipo | Unidad | Dominio o rango | Marca |
|---|---|---|---|---|---|
| `PK_ID_MallaVial` | PK_ID_MallaVial | Entero Largo | N / A |  | obligatorio |
| `FK_ID_AreaIntervencion` | FK_ID_AreaIntervencion | Entero Largo | N / A |  | obligatorio |
| `EspesorRA` | Espesor Rodadura Asfáltica | Entero Corto | Centímetro (cm) | rango 2 a 20 | obligatorio |
| `GranulometriaRA` | Granulometría Rodadura Asfáltica | Entero Corto | N / A | `1` Rodadura MD10; `2` Rodadura MD12; `3` Rodadura MS12; `4` Rodadura MD20; `5` Rodadura MS20; `7` Rodadura Mezcla Asfáltica con GCR | obligatorio |
| `EspesorCI` | Espesor Capa Intermedia | Entero Corto | Centímetro (cm) | rango 2 a 50 | obligatorio |
| `GranulometriaCI` | Granulometría Capa Intermedia | Entero Corto | N / A | `1` Capa asfáltica intermedia MD20; `2` Capa asfáltica intermedia MS20; `3` Capa asfáltica intermedia MS25; `4` Fresado estabilizado con emulsión; `5` Fresado estabilizado con asfalto espumado; `6` Capa asfática intermedia MAM20; `7` Capa asfática intermedia con GCR; `8` Fresado estabilizado con emulsión y cemento | obligatorio |
| `EspesorBA` | Espesor Base Asfáltica | Entero Corto | Centímetro (cm) | rango 2 a 50 | obligatorio |
| `GranulometriaBA` | Granulometría Base Asfáltica | Entero Corto | N / A | `1` Base asfáltica MD20; `2` Base asfáltica MS25; `3` Base asfáltica MG20; `4` Base asfáltica MG25; `5` Base asfáltica MAM20; `6` Fresado estabilizado con emulsión; `7` Fresado estabilizado con asfalto espumado; `8` Base asfáltica con GCR | obligatorio |
| `EspesorBG` | Espesor Base Granular | Entero Corto | Centímetro (cm) | rango 10 a 50 | obligatorio |
| `GranulometriaBG` | Granulometría Base Granular | Entero Corto | N / A | `1` BG-A; `2` BG-B; `3` BG-C | obligatorio |
| `EspesorBE` | Espesor Base Estabilizada | Entero Corto | Centímetro (cm) | rango 10 a 50 | obligatorio |
| `GranulometriaBE` | Granulometría Base Estabilizada | Entero Corto | N / A | `1` GEC_A_Gr1 CEMENTO; `2` GEC_A_Gr2 CEMENTO; `3` GEC_B_Gr1 CEMENTO; `4` GEC_B_Gr2 CEMENTO; `5` GEC_B_Gr3 CEMENTO; `6` GEC_C_Gr1 CEMENTO; `7` GEC_C_Gr2 CEMENTO; `8` MGEA_A ASFALTO; `9` MGEA_B ASFALTO; `10` MGEA_C ASFALTO; `11` GEEA_AGr1 EMULSIÓN; `12` GEEA_AGr2 EMULSIÓN; `13` GEEA_BGr1 EMULSIÓN; `14` GEEA_BGr2 EMULSIÓN; `15` GEEA_CGr1 EMULSIÓN; `16` GEEA_CGr2 EMULSIÓN | obligatorio |
| `EspesorSBG` | Espesor Subbase Granular | Entero Corto | Centímetro (cm) | rango 10 a 50 | obligatorio |
| `GranulometriaSBG` | Granulometría Subbase Granular | Entero Corto | N / A | `1` SBG-A; `2` SBG-B; `3` SBG-C | obligatorio |
| `EspesorSBE` | Espesor Subbase Estabilizada | Entero Corto | Centímetro (cm) | rango 10 a 50 | obligatorio |
| `GranulometriaSBE` | Granulometría Subbase Estabilizada | Entero Corto | N / A | `1` GEC_A_Gr1 CEMENTO; `2` GEC_A_Gr2 CEMENTO; `3` GEC_B_Gr1 CEMENTO; `4` GEC_B_Gr2 CEMENTO; `5` GEC_B_Gr3 CEMENTO; `6` GEC_C_Gr1 CEMENTO; `7` GEC_C_Gr2 CEMENTO; `8` GEC_D_Gr1 CEMENTO; `9` MGEA_A ASFALTO; `10` MGEA_B ASFALTO; `11` MGEA_C ASFALTO; `12` GEEA_AGr1 EMULSIÓN; `13` GEEA_AGr2 EMULSIÓN; `14` GEEA_BGr1 EMULSIÓN; `15` GEEA_BGr2 EMULSIÓN; `16` GEEA_CGr1 EMULSIÓN; `17` GEEA_CGr2 EMULSIÓN | obligatorio |
| `TipoIntervencion` | Tipo Intervención | Entero Corto | N / A | `1` Bacheo; `3` Fresado y nivelación; `5` Parcheo; `6` Sobrecarpeta; `7` Carpeta Asfaltica; `8` Fresado y Sobrecarpeta; `9` Fresado y reposición de pavimento flexible; `10` Fresado estabilizado con emulsión y sobrecarpeta; `11` Fresado estabilizado con asfalto espumado y sobrecarpeta; `12` Parcheo mecanizado; `13` Tratamiento superficial simple; `14` Microaglomerado en caliente; `15` Fresado estabilizado; `16` Remplazo de Bases | obligatorio |

### Diseno

Geometría **polígono**; elementos: Diseño.
Cobertura informativa, que detalla los elementos con geometría Polígono objeto de los proyectos que contemplan Prefactibilidad, Factibilidad y Diseño reportados a la Dirección Técnica Estratégica - DTE por los distintos actores que intervienen en la infraestructura de los sistemas de movilidad y espacio público

Atributos de **Diseno**

| Campo | Alias | Tipo | Unidad | Dominio o rango | Marca |
|---|---|---|---|---|---|
| `PK_ID_Elemento` | Elemento | Entero Largo | N / A | `N/A` N/A |  |
| `CIV` | CIV | Entero Largo | N / A | `N/A` N/A |  |
| `TipoElemento` | TipoElemento | Texto (Long 3) | N / A | `ALA` Alameda; `AES` Aleta Estribo; `AND` Andén; `BAH` Bahia; `BCC` Bicicarril; `CAB` Cable; `CAI` Caisson; `CAL` Calzada; `CRU` Ciclorruta; `COL` Columna; `DAD` Dado; `ESC` Escalera; `EST` Estación; `ESR` Estribo; `LOS` Losa; `LDA` Losa de Aproximacion; `MUR` Muro de Concreto; `MUG` Muro de Gavion; `PAG` Patio Garaje; `PPA` Pila; `PPO` Pilote; `PLZ` Plaza o Plazoleta; `PRT` Portal; `PUP` Puente Peatonal; `PUV` Puente Vehicular; `RPU` Rampa Puente; `SEG` Segmento; `SEP` Separador; `SPL` SeparadorLineal; `TAB` Tablero; `TAL` Talud; `VIA` Vía; `VIG` Viga |  |
| `Localidad` | Localidad | Entero Corto | N / A | `1` Usaquén; `2` Chapinero; `3` Santa Fe; `4` San Cristóbal; `5` Usme; `6` Tunjuelito; `7` Bosa; `8` Kennedy; `9` Fontibón; `10` Engativá; `11` Suba; `12` Barrios Unidos; `13` Teusaquillo; `14` Los Mártires; `15` Antonio Nariño; `16` Puente Aranda; `17` La Candelaria; `18` Rafael Uribe Uribe; `19` Ciudad Bolívar; `20` Sumapaz |  |
| `Contrato` | Contrato | Texto | N / A | `N/A` N/A |  |
| `Estado` | Estado | Texto | N / A | `RES` Reservado; `EPL` En Pliegos; `ELI` En Licitación; `CON` Contratado; `EJE` En Ejecución; `SUS` Suspendido; `TER` Terminado; `EXC` Excluido |  |
| `Intervencion` | Intervencion | Texto (Long 3) | N / A | `PFA` Pre-Factibilidad; `FAC` Factibilidad; `EYD` Estudios y diseños; `CON` Construcción |  |
| `UnidadPlaneamiento` | Unidad Planeamiento | Texto (Long 7) | N / A | `N/A` N/A |  |
| `TipoMalla` | Tipo Malla | Texto (Long 2) | N / A | `AR` Arterial; `IN` Intermedia; `LO` Local; `RU` Rural; `CM` Circuito Movilidad; `EX` Expansion; `FD` Fuera del Distrito |  |
| `Programa` | Programa | Texto (Long 50) | N / A | `N/A` N/A |  |
| `Comunicacion` | Comunicación | Texto (Long 20) | N / A | `N/A` N/A |  |
| `FechaReporte` | Fecha de Reporte | Fecha | N / A | `N/A` N/A |  |
| `Observacion` | Observacion | Texto (Long 200) | N / A | `N/A` N/A |  |

Tabla relacionada **PRG_ReporteDiseno** (Reporte Diseño), de Diseno

| Campo | Alias | Tipo | Unidad | Dominio o rango | Marca |
|---|---|---|---|---|---|
| `PK_ReporteD` | PK_Reporte Diseño | Entero Largo | N / A | `N/A` N/A |  |
| `FK_ID_Elemento` | FK_ID_ELEMENTO | Entero Largo | N / A | `N/A` N/A |  |
| `FK_ID_BK` | FK_ID_BK | Entero Largo | N / A | `N/A` N/A |  |
| `Estado` | Estado | Texto | N / A | `RES` Reservado; `EPL` En Pliegos; `ELI` En Licitación; `CON` Contratado; `EJE` En Ejecución; `SUS` Suspendido; `TER` Terminado; `EXC` Excluido |  |
| `Comunicación` | Comunicación | Texto (Long 20) | N / A | `N/A` N/A |  |
| `FechaReporte` | Fecha de Reporte | Fecha | N / A | `N/A` N/A |  |
| `Observacion` | Observacion | Texto (Long 200) | N / A | `N/A` N/A |  |

### SeguimientoLinea

Geometría **línea**; elementos: Seguimiento Línea.
Cobertura informativa, que detalla los elementos con geometría Línea objeto de los diferentes proyectos reportados a la DTE por los distintos actores que intervienen en la infraestructura vial.

Atributos de **SeguimientoLinea**

| Campo | Alias | Tipo | Unidad | Dominio o rango | Marca |
|---|---|---|---|---|---|
| `PK_ID_ELEMENTO` | Elemento | Entero Largo | N / A | `N/A` N/A |  |
| `CIV` | CIV | Entero Largo | N / A | `N/A` N/A |  |
| `TIPOELEMENTO` | TipoElemento | Texto (Long 3) | N / A | `ALA` Alameda; `AND` Andén; `BAH` Bahia; `BCA` Banca; `BOL` Bolardo; `CAL` Calzada; `CNC` Caneca; `CRU` Ciclorruta; `EST` Estación; `LOS` Losa; `MON` Monumento; `MUG` Muro de Gavion; `MUR` Muro de Concreto; `PAR` Paradero; `PLZ` Plaza o Plazoleta; `PRT` Portal; `PUP` Puente Peatonal; `PUV` Puente Vehicular; `SEG` Segmento; `SEP` Separador; `TAL` Talud; `BCC` Bicicarril; `POM` Pompeyano; `CLP` CicloEstacion; `RPU` RampaPuente; `SPL` SeparadorLineal; `PAG` PatioGaraje; `CAB` Cable; `PIL` Pileta; `RAM` Rampa; `BAR` Baranda; `CDR` Contenedor Raiz; `PDA` Protector Arbol |  |
| `LOCALIDAD` | Localidad | Entero Corto | N / A | `1` Usaquén; `2` Chapinero; `3` Santa Fe; `4` San Cristóbal; `5` Usme; `6` Tunjuelito; `7` Bosa; `8` Kennedy; `9` Fontibón; `10` Engativá; `11` Suba; `12` Barrios Unidos; `13` Teusaquillo; `14` Los Mártires; `15` Antonio Nariño; `16` Puente Aranda; `17` La Candelaria; `18` Rafael Uribe Uribe; `19` Ciudad Bolívar; `20` Sumapaz |  |
| `CONTRATO` | Contrato | Texto | N / A | `N/A` N/A |  |
| `ESTADO` | Estado | Texto | N / A | `RES` Reservado; `EPL` En Pliegos; `ELI` En Licitación; `CON` Contratado; `EJE` En Ejecución; `SUS` Suspendido; `TER` Terminado; `EXC` Excluido; `FAC` Factibilidad; `PFA` Pre-Factibilidad |  |
| `INTERVENCION` | Intervencion | Texto (Long 3) | N / A | `EYD` Estudios y diseños; `DIA` Diagnostico; `CON` Construcción; `MRU` Mantenimiento Rutinario; `MPE` Mantenimiento Periódico; `REH` Rehabilitación; `FRE` Mejoramiento con Material Fresado; `REC` Reconstrucción; `ADE` Adecuación; `SEN` Señalización; `AMO` Acciones de Movilidad; `PAR` Parcheo; `BAC` Bacheo; `CNS` Conservación |  |
| `UNIDADPLANEAMIENTO` | Unidad Planeamiento | Texto (Long 7) | N / A | `N/A` N/A |  |
| `ENTIDAD` | Entidad | Entero Corto | N / A | `1` FDL USAQUEN; `2` FDL CHAPINERO; `3` FDLSANTA FE; `4` FDL SAN CRISTOBAL; `5` FDL USME; `6` FDL TUNJUELITO; `7` FDL BOSA; `8` FDL KENNEDY; `9` FDL FONTIBON; `10` FDL ENGATIVA; `11` FDL SUBA; `12` FDL BARRIOS UNIDOS; `13` FDL TEUSAQUILLO; `14` FDL LOS MARTIRES; `15` FDL ANTONIO NARIÑO; `16` FDL PUENTE ARANDA; `17` FDL LA CANDELARIA; `18` FDL RAFAEL URIBE URIBE; `19` FDL CIUDAD BOLIVAR; `20` FDL SUMAPAZ; `21` IDU; `22` CVP-CAJA DE VIVIENDA POPULAR; `23` SECRETARIA DEL HABITAT; `24` SECRETARIA DISTRITAL DE MOVILIDAD; `25` EAAB; `26` EMPRESA INMOBILIARIA CUNDINAMARQUESA; `27` IDEPAC; `28` UAERMV |  |
| `TIPOMALLA` | Tipo Malla | Texto (Long 2) | N / A | `AR` Arterial; `IN` Intermedia; `LO` Local; `RU` Rural; `CM` Circuito Movilidad; `EX` Expansion; `FD` Fuera del Distrito |  |
| `PROGRAMA` | Programa | Texto (Long 50) | N / A | `N/A` N/A |  |
| `COMUNICACIÓN` | Comunicación | Texto (Long 20) | N / A | `N/A` N/A |  |
| `FECHAREPORTE` | Comunicación | Fecha | N / A | `N/A` N/A |  |
| `OBSERVACION` | Observacion | Texto (Long 200) | N / A | `N/A` N/A |  |

Tabla relacionada **PRG_ReporteSeguimiento** (Reporte Seguimiento), de SeguimientoLinea

| Campo | Alias | Tipo | Unidad | Dominio o rango | Marca |
|---|---|---|---|---|---|
| `PK_REPORTE` | PK_Reporte | Entero Largo | N / A | `N/A` N/A |  |
| `FK_ID_ELEMENTO` | FK_ID_ELEMENTO | Entero Largo | N / A | `N/A` N/A |  |
| `FK_ID_BK` | FK_ID_BK | Entero Largo | N / A | `N/A` N/A |  |
| `CIV` | CIV | Entero Largo | N / A | `N/A` N/A |  |
| `TIPOELEMENTO` | TipoElemento | Texto (Long 3) | N / A | `ALA` Alameda; `AND` Andén; `BAH` Bahia; `BCA` Banca; `BOL` Bolardo; `CAL` Calzada; `CNC` Caneca; `CRU` Ciclorruta; `EST` Estación; `LOS` Losa; `MON` Monumento; `MUG` Muro de Gavion; `MUR` Muro de Concreto; `PAR` Paradero; `PLZ` Plaza o Plazoleta; `PRT` Portal; `PUP` Puente Peatonal; `PUV` Puente Vehicular; `SEG` Segmento; `SEP` Separador; `TAL` Talud; `BCC` Bicicarril; `POM` Pompeyano; `CLP` CicloEstacion; `RPU` RampaPuente; `SPL` SeparadorLineal; `PAG` PatioGaraje; `CAB` Cable; `PIL` Pileta; `RAM` Rampa; `BAR` Baranda; `CDR` Contenedor Raiz; `PDA` Protector Arbol |  |
| `LOCALIDAD` | Localidad | Entero Corto | N / A | `1` Usaquén; `2` Chapinero; `3` Santa Fe; `4` San Cristóbal; `5` Usme; `6` Tunjuelito; `7` Bosa; `8` Kennedy; `9` Fontibón; `10` Engativá; `11` Suba; `12` Barrios Unidos; `13` Teusaquillo; `14` Los Mártires; `15` Antonio Nariño; `16` Puente Aranda; `17` La Candelaria; `18` Rafael Uribe Uribe; `19` Ciudad Bolívar; `20` Sumapaz |  |
| `CONTRATO` | Contrato | Texto | N / A | `N/A` N/A |  |
| `ESTADO` | Estado | Texto | N / A | `RES` Reservado; `EPL` En Pliegos; `ELI` En Licitación; `CON` Contratado; `EJE` En Ejecución; `SUS` Suspendido; `TER` Terminado; `EXC` Excluido; `FAC` Factibilidad; `PFA` Pre-Factibilidad |  |
| `INTERVENCION` | Intervencion | Texto (Long 3) | N / A | `EYD` Estudios y diseños; `DIA` Diagnostico; `CON` Construcción; `MRU` Mantenimiento Rutinario; `MPE` Mantenimiento Periódico; `REH` Rehabilitación; `FRE` Mejoramiento con Material Fresado; `REC` Reconstrucción; `ADE` Adecuación; `SEN` Señalización; `AMO` Acciones de Movilidad; `PAR` Parcheo; `BAC` Bacheo; `CNS` Conservación |  |
| `UNIDADPLANEAMIENTO` | Unidad Planeamiento | Texto (Long 7) | N / A | `N/A` N/A |  |
| `ENTIDAD` | Entidad | Entero Corto | N / A | `1` FDL USAQUEN; `2` FDL CHAPINERO; `3` FDLSANTA FE; `4` FDL SAN CRISTOBAL; `5` FDL USME; `6` FDL TUNJUELITO; `7` FDL BOSA; `8` FDL KENNEDY; `9` FDL FONTIBON; `10` FDL ENGATIVA; `11` FDL SUBA; `12` FDL BARRIOS UNIDOS; `13` FDL TEUSAQUILLO; `14` FDL LOS MARTIRES; `15` FDL ANTONIO NARIÑO; `16` FDL PUENTE ARANDA; `17` FDL LA CANDELARIA; `18` FDL RAFAEL URIBE URIBE; `19` FDL CIUDAD BOLIVAR; `20` FDL SUMAPAZ; `21` IDU; `22` CVP-CAJA DE VIVIENDA POPULAR; `23` SECRETARIA DEL HABITAT; `24` SECRETARIA DISTRITAL DE MOVILIDAD; `25` EAAB; `26` EMPRESA INMOBILIARIA CUNDINAMARQUESA; `27` IDEPAC; `28` UAERMV |  |
| `TIPOMALLA` | Tipo Malla | Texto (Long 2) | N / A | `AR` Arterial; `IN` Intermedia; `LO` Local; `RU` Rural; `CM` Circuito Movilidad; `EX` Expansion; `FD` Fuera del Distrito |  |
| `PROGRAMA` | Programa | Texto (Long 50) | N / A | `N/A` N/A |  |
| `COMUNICACIÓN` | Comunicación | Texto (Long 20) | N / A | `N/A` N/A |  |
| `FECHAREPORTE` | Comunicación | Fecha | N / A | `N/A` N/A |  |
| `OBSERVACION` | Observacion | Texto (Long 200) | N / A | `N/A` N/A |  |

### SeguimientoPoligono

Geometría **polígono**; elementos: Seguimiento Polígono.
Cobertura informativa, que detalla los elementos con geometría Polígono objeto de los diferentes proyectos reportados a la DTE por los distintos actores que intervienen en la infraestructura vial.

Atributos de **SeguimientoPoligono**

| Campo | Alias | Tipo | Unidad | Dominio o rango | Marca |
|---|---|---|---|---|---|
| `PK_ID_ELEMENTO` | Elemento | Entero Largo | N / A | `N/A` N/A |  |
| `CIV` | CIV | Entero Largo | N / A | `N/A` N/A |  |
| `TIPOELEMENTO` | TipoElemento | Texto (Long 3) | N / A | `ALA` Alameda; `AND` Andén; `BAH` Bahia; `BCA` Banca; `BOL` Bolardo; `CAL` Calzada; `CNC` Caneca; `CRU` Ciclorruta; `EST` Estación; `LOS` Losa; `MON` Monumento; `MUG` Muro de Gavion; `MUR` Muro de Concreto; `PAR` Paradero; `PLZ` Plaza o Plazoleta; `PRT` Portal; `PUP` Puente Peatonal; `PUV` Puente Vehicular; `SEG` Segmento; `SEP` Separador; `TAL` Talud; `BCC` Bicicarril; `POM` Pompeyano; `CLP` CicloEstacion; `RPU` RampaPuente; `SPL` SeparadorLineal; `PAG` PatioGaraje; `CAB` Cable; `PIL` Pileta; `RAM` Rampa; `BAR` Baranda; `CDR` Contenedor Raiz; `PDA` Protector Arbol |  |
| `LOCALIDAD` | Localidad | Entero Corto | N / A | `1` Usaquén; `2` Chapinero; `3` Santa Fe; `4` San Cristóbal; `5` Usme; `6` Tunjuelito; `7` Bosa; `8` Kennedy; `9` Fontibón; `10` Engativá; `11` Suba; `12` Barrios Unidos; `13` Teusaquillo; `14` Los Mártires; `15` Antonio Nariño; `16` Puente Aranda; `17` La Candelaria; `18` Rafael Uribe Uribe; `19` Ciudad Bolívar; `20` Sumapaz |  |
| `CONTRATO` | Contrato | Texto | N / A | `N/A` N/A |  |
| `ESTADO` | Estado | Texto | N / A | `RES` Reservado; `EPL` En Pliegos; `ELI` En Licitación; `CON` Contratado; `EJE` En Ejecución; `SUS` Suspendido; `TER` Terminado; `EXC` Excluido; `FAC` Factibilidad; `PFA` Pre-Factibilidad |  |
| `INTERVENCION` | Intervencion | Texto (Long 3) | N / A | `EYD` Estudios y diseños; `DIA` Diagnostico; `CON` Construcción; `MRU` Mantenimiento Rutinario; `MPE` Mantenimiento Periódico; `REH` Rehabilitación; `FRE` Mejoramiento con Material Fresado; `REC` Reconstrucción; `ADE` Adecuación; `SEN` Señalización; `AMO` Acciones de Movilidad; `PAR` Parcheo; `BAC` Bacheo; `CNS` Conservación |  |
| `UNIDADPLANEAMIENTO` | Unidad Planeamiento | Texto (Long 7) | N / A | `N/A` N/A |  |
| `ENTIDAD` | Entidad | Entero Corto | N / A | `1` FDL USAQUEN; `2` FDL CHAPINERO; `3` FDLSANTA FE; `4` FDL SAN CRISTOBAL; `5` FDL USME; `6` FDL TUNJUELITO; `7` FDL BOSA; `8` FDL KENNEDY; `9` FDL FONTIBON; `10` FDL ENGATIVA; `11` FDL SUBA; `12` FDL BARRIOS UNIDOS; `13` FDL TEUSAQUILLO; `14` FDL LOS MARTIRES; `15` FDL ANTONIO NARIÑO; `16` FDL PUENTE ARANDA; `17` FDL LA CANDELARIA; `18` FDL RAFAEL URIBE URIBE; `19` FDL CIUDAD BOLIVAR; `20` FDL SUMAPAZ; `21` IDU; `22` CVP-CAJA DE VIVIENDA POPULAR; `23` SECRETARIA DEL HABITAT; `24` SECRETARIA DISTRITAL DE MOVILIDAD; `25` EAAB; `26` EMPRESA INMOBILIARIA CUNDINAMARQUESA; `27` IDEPAC; `28` UAERMV; `29` URBANIZADOR |  |
| `TIPOMALLA` | Tipo Malla | Texto (Long 2) | N / A | `AR` Arterial; `IN` Intermedia; `LO` Local; `RU` Rural; `CM` Circuito Movilidad; `EX` Expansion; `FD` Fuera del Distrito |  |
| `PROGRAMA` | Programa | Texto (Long 50) | N / A | `N/A` N/A |  |
| `COMUNICACIÓN` | Comunicación | Texto (Long 20) | N / A | `N/A` N/A |  |
| `FECHAREPORTE` | Comunicación | Fecha | N / A | `N/A` N/A |  |
| `OBSERVACION` | Observacion | Texto (Long 200) | N / A | `N/A` N/A |  |

Tabla relacionada **PRG_ReporteSeguimiento** (Reporte Seguimiento), de SeguimientoPoligono

| Campo | Alias | Tipo | Unidad | Dominio o rango | Marca |
|---|---|---|---|---|---|
| `PK_REPORTE` | PK_Reporte | Entero Largo | N / A | `N/A` N/A | obligatorio (Obligatoriedad) |
| `FK_ID_ELEMENTO` | FK_ID_ELEMENTO | Entero Largo | N / A | `N/A` N/A | obligatorio (Obligatoriedad) |
| `FK_ID_BK` | FK_ID_BK | Entero Largo | N / A | `N/A` N/A | obligatorio (Obligatoriedad) |
| `CIV` | CIV | Entero Largo | N / A | `N/A` N/A | obligatorio (Obligatoriedad) |
| `TIPOELEMENTO` | TipoElemento | Texto (Long 3) | N / A | `ALA` Alameda; `AND` Andén; `BAH` Bahia; `BCA` Banca; `BOL` Bolardo; `CAL` Calzada; `CNC` Caneca; `CRU` Ciclorruta; `EST` Estación; `LOS` Losa; `MON` Monumento; `MUG` Muro de Gavion; `MUR` Muro de Concreto; `PAR` Paradero; `PLZ` Plaza o Plazoleta; `PRT` Portal; `PUP` Puente Peatonal; `PUV` Puente Vehicular; `SEG` Segmento; `SEP` Separador; `TAL` Talud; `BCC` Bicicarril; `POM` Pompeyano; `CLP` CicloEstacion; `RPU` RampaPuente; `SPL` SeparadorLineal; `PAG` PatioGaraje; `CAB` Cable; `PIL` Pileta; `RAM` Rampa; `BAR` Baranda; `CDR` Contenedor Raiz; `PDA` Protector Arbol | obligatorio (Obligatoriedad) |
| `LOCALIDAD` | Localidad | Entero Corto | N / A | `1` Usaquén; `2` Chapinero; `3` Santa Fe; `4` San Cristóbal; `5` Usme; `6` Tunjuelito; `7` Bosa; `8` Kennedy; `9` Fontibón; `10` Engativá; `11` Suba; `12` Barrios Unidos; `13` Teusaquillo; `14` Los Mártires; `15` Antonio Nariño; `16` Puente Aranda; `17` La Candelaria; `18` Rafael Uribe Uribe; `19` Ciudad Bolívar; `20` Sumapaz | obligatorio (Obligatoriedad) |
| `CONTRATO` | Contrato | Texto | N / A | `N/A` N/A | obligatorio (Obligatoriedad) |
| `ESTADO` | Estado | Texto | N / A | `RES` Reservado; `EPL` En Pliegos; `ELI` En Licitación; `CON` Contratado; `EJE` En Ejecución; `SUS` Suspendido; `TER` Terminado; `EXC` Excluido; `FAC` Factibilidad; `PFA` Pre-Factibilidad | obligatorio (Obligatoriedad) |
| `INTERVENCION` | Intervencion | Texto (Long 3) | N / A | `EYD` Estudios y diseños; `DIA` Diagnostico; `CON` Construcción; `MRU` Mantenimiento Rutinario; `MPE` Mantenimiento Periódico; `REH` Rehabilitación; `FRE` Mejoramiento con Material Fresado; `REC` Reconstrucción; `ADE` Adecuación; `SEN` Señalización; `AMO` Acciones de Movilidad; `PAR` Parcheo; `BAC` Bacheo; `CNS` Conservación | obligatorio (Obligatoriedad) |
| `UNIDADPLANEAMIENTO` | Unidad Planeamiento | Texto (Long 7) | N / A | `N/A` N/A | obligatorio (Obligatoriedad) |
| `ENTIDAD` | Entidad | Entero Corto | N / A | `1` FDL USAQUEN; `2` FDL CHAPINERO; `3` FDLSANTA FE; `4` FDL SAN CRISTOBAL; `5` FDL USME; `6` FDL TUNJUELITO; `7` FDL BOSA; `8` FDL KENNEDY; `9` FDL FONTIBON; `10` FDL ENGATIVA; `11` FDL SUBA; `12` FDL BARRIOS UNIDOS; `13` FDL TEUSAQUILLO; `14` FDL LOS MARTIRES; `15` FDL ANTONIO NARIÑO; `16` FDL PUENTE ARANDA; `17` FDL LA CANDELARIA; `18` FDL RAFAEL URIBE URIBE; `19` FDL CIUDAD BOLIVAR; `20` FDL SUMAPAZ; `21` IDU; `22` CVP-CAJA DE VIVIENDA POPULAR; `23` SECRETARIA DEL HABITAT; `24` SECRETARIA DISTRITAL DE MOVILIDAD; `25` EAAB; `26` EMPRESA INMOBILIARIA CUNDINAMARQUESA; `27` IDEPAC; `28` UAERMV | obligatorio (Obligatoriedad) |
| `TIPOMALLA` | Tipo Malla | Texto (Long 2) | N / A | `AR` Arterial; `IN` Intermedia; `LO` Local; `RU` Rural; `CM` Circuito Movilidad; `EX` Expansion; `FD` Fuera del Distrito | obligatorio (Obligatoriedad) |
| `PROGRAMA` | Programa | Texto (Long 50) | N / A | `N/A` N/A | según alcance (Obligatoriedad) |
| `COMUNICACIÓN` | Comunicación | Texto (Long 20) | N / A | `N/A` N/A | obligatorio (Obligatoriedad) |
| `FECHAREPORTE` | Comunicación | Fecha | N / A | `N/A` N/A | obligatorio (Obligatoriedad) |
| `OBSERVACION` | Observacion | Texto (Long 200) | N / A | `N/A` N/A |  |

### SeguimientoPunto

Geometría **punto**; elementos: Seguimiento Punto.
Cobertura informativa, que detalla los elementos con geometría Punto objeto de los diferentes proyectos reportados a la DTE por los distintos actores que intervienen en la infraestructura vial.

Atributos de **SeguimientoPunto**

| Campo | Alias | Tipo | Unidad | Dominio o rango | Marca |
|---|---|---|---|---|---|
| `PK_ID_ELEMENTO` | Elemento | Entero Largo | N / A | `N/A` N/A |  |
| `CIV` | CIV | Entero Largo | N / A | `N/A` N/A |  |
| `TIPOELEMENTO` | TipoElemento | Texto (Long 3) | N / A | `ALA` Alameda; `AND` Andén; `BAH` Bahia; `BCA` Banca; `BOL` Bolardo; `CAL` Calzada; `CNC` Caneca; `CRU` Ciclorruta; `EST` Estación; `LOS` Losa; `MON` Monumento; `MUG` Muro de Gavion; `MUR` Muro de Concreto; `PAR` Paradero; `PLZ` Plaza o Plazoleta; `PRT` Portal; `PUP` Puente Peatonal; `PUV` Puente Vehicular; `SEG` Segmento; `SEP` Separador; `TAL` Talud; `BCC` Bicicarril; `POM` Pompeyano; `CLP` CicloEstacion; `RPU` RampaPuente; `SPL` SeparadorLineal; `PAG` PatioGaraje; `CAB` Cable; `PIL` Pileta; `RAM` Rampa; `BAR` Baranda; `CDR` Contenedor Raiz; `PDA` Protector Arbol |  |
| `LOCALIDAD` | Localidad | Entero Corto | N / A | `1` Usaquén; `2` Chapinero; `3` Santa Fe; `4` San Cristóbal; `5` Usme; `6` Tunjuelito; `7` Bosa; `8` Kennedy; `9` Fontibón; `10` Engativá; `11` Suba; `12` Barrios Unidos; `13` Teusaquillo; `14` Los Mártires; `15` Antonio Nariño; `16` Puente Aranda; `17` La Candelaria; `18` Rafael Uribe Uribe; `19` Ciudad Bolívar; `20` Sumapaz |  |
| `CONTRATO` | Contrato | Texto | N / A | `N/A` N/A |  |
| `ESTADO` | Estado | Texto | N / A | `RES` Reservado; `EPL` En Pliegos; `ELI` En Licitación; `CON` Contratado; `EJE` En Ejecución; `SUS` Suspendido; `TER` Terminado; `EXC` Excluido; `FAC` Factibilidad; `PFA` Pre-Factibilidad |  |
| `INTERVENCION` | Intervencion | Texto (Long 3) | N / A | `EYD` Estudios y diseños; `DIA` Diagnostico; `CON` Construcción; `MRU` Mantenimiento Rutinario; `MPE` Mantenimiento Periódico; `REH` Rehabilitación; `FRE` Mejoramiento con Material Fresado; `REC` Reconstrucción; `ADE` Adecuación; `SEN` Señalización; `AMO` Acciones de Movilidad; `PAR` Parcheo; `BAC` Bacheo; `CNS` Conservación |  |
| `UNIDADPLANEAMIENTO` | Unidad Planeamiento | Texto (Long 7) | N / A | `N/A` N/A |  |
| `ENTIDAD` | Entidad | Entero Corto | N / A | `1` FDL USAQUEN; `2` FDL CHAPINERO; `3` FDLSANTA FE; `4` FDL SAN CRISTOBAL; `5` FDL USME; `6` FDL TUNJUELITO; `7` FDL BOSA; `8` FDL KENNEDY; `9` FDL FONTIBON; `10` FDL ENGATIVA; `11` FDL SUBA; `12` FDL BARRIOS UNIDOS; `13` FDL TEUSAQUILLO; `14` FDL LOS MARTIRES; `15` FDL ANTONIO NARIÑO; `16` FDL PUENTE ARANDA; `17` FDL LA CANDELARIA; `18` FDL RAFAEL URIBE URIBE; `19` FDL CIUDAD BOLIVAR; `20` FDL SUMAPAZ; `21` IDU; `22` CVP-CAJA DE VIVIENDA POPULAR; `23` SECRETARIA DEL HABITAT; `24` SECRETARIA DISTRITAL DE MOVILIDAD; `25` EAAB; `26` EMPRESA INMOBILIARIA CUNDINAMARQUESA; `27` IDEPAC; `28` UAERMV |  |
| `TIPOMALLA` | Tipo Malla | Texto (Long 2) | N / A | `AR` Arterial; `IN` Intermedia; `LO` Local; `RU` Rural; `CM` Circuito Movilidad; `EX` Expansion; `FD` Fuera del Distrito |  |
| `PROGRAMA` | Programa | Texto (Long 50) | N / A | `N/A` N/A |  |
| `COMUNICACIÓN` | Comunicación | Texto (Long 20) | N / A | `N/A` N/A |  |
| `FECHAREPORTE` | Comunicación | Fecha | N / A | `N/A` N/A |  |
| `OBSERVACION` | Observacion | Texto (Long 200) | N / A | `N/A` N/A |  |

Tabla relacionada **PRG_ReporteSeguimiento** (Reporte Seguimiento), de SeguimientoPunto

| Campo | Alias | Tipo | Unidad | Dominio o rango | Marca |
|---|---|---|---|---|---|
| `PK_REPORTE` | PK_Reporte | Entero Largo | N / A | `N/A` N/A |  |
| `FK_ID_ELEMENTO` | FK_ID_ELEMENTO | Entero Largo | N / A | `N/A` N/A |  |
| `FK_ID_BK` | FK_ID_BK | Entero Largo | N / A | `N/A` N/A |  |
| `CIV` | CIV | Entero Largo | N / A | `N/A` N/A |  |
| `TIPOELEMENTO` | TipoElemento | Texto (Long 3) | N / A | `ALA` Alameda; `AND` Andén; `BAH` Bahia; `BCA` Banca; `BOL` Bolardo; `CAL` Calzada; `CNC` Caneca; `CRU` Ciclorruta; `EST` Estación; `LOS` Losa; `MON` Monumento; `MUG` Muro de Gavion; `MUR` Muro de Concreto; `PAR` Paradero; `PLZ` Plaza o Plazoleta; `PRT` Portal; `PUP` Puente Peatonal; `PUV` Puente Vehicular; `SEG` Segmento; `SEP` Separador; `TAL` Talud; `BCC` Bicicarril; `POM` Pompeyano; `CLP` CicloEstacion; `RPU` RampaPuente; `SPL` SeparadorLineal; `PAG` PatioGaraje; `CAB` Cable; `PIL` Pileta; `RAM` Rampa; `BAR` Baranda; `CDR` Contenedor Raiz; `PDA` Protector Arbol |  |
| `LOCALIDAD` | Localidad | Entero Corto | N / A | `1` Usaquén; `2` Chapinero; `3` Santa Fe; `4` San Cristóbal; `5` Usme; `6` Tunjuelito; `7` Bosa; `8` Kennedy; `9` Fontibón; `10` Engativá; `11` Suba; `12` Barrios Unidos; `13` Teusaquillo; `14` Los Mártires; `15` Antonio Nariño; `16` Puente Aranda; `17` La Candelaria; `18` Rafael Uribe Uribe; `19` Ciudad Bolívar; `20` Sumapaz |  |
| `CONTRATO` | Contrato | Texto | N / A | `N/A` N/A |  |
| `ESTADO` | Estado | Texto | N / A | `RES` Reservado; `EPL` En Pliegos; `ELI` En Licitación; `CON` Contratado; `EJE` En Ejecución; `SUS` Suspendido; `TER` Terminado; `EXC` Excluido; `FAC` Factibilidad; `PFA` Pre-Factibilidad |  |
| `INTERVENCION` | Intervencion | Texto (Long 3) | N / A | `EYD` Estudios y diseños; `DIA` Diagnostico; `CON` Construcción; `MRU` Mantenimiento Rutinario; `MPE` Mantenimiento Periódico; `REH` Rehabilitación; `FRE` Mejoramiento con Material Fresado; `REC` Reconstrucción; `ADE` Adecuación; `SEN` Señalización; `AMO` Acciones de Movilidad; `PAR` Parcheo; `BAC` Bacheo; `CNS` Conservación |  |
| `UNIDADPLANEAMIENTO` | Unidad Planeamiento | Texto (Long 7) | N / A | `N/A` N/A |  |
| `ENTIDAD` | Entidad | Entero Corto | N / A | `1` FDL USAQUEN; `2` FDL CHAPINERO; `3` FDLSANTA FE; `4` FDL SAN CRISTOBAL; `5` FDL USME; `6` FDL TUNJUELITO; `7` FDL BOSA; `8` FDL KENNEDY; `9` FDL FONTIBON; `10` FDL ENGATIVA; `11` FDL SUBA; `12` FDL BARRIOS UNIDOS; `13` FDL TEUSAQUILLO; `14` FDL LOS MARTIRES; `15` FDL ANTONIO NARIÑO; `16` FDL PUENTE ARANDA; `17` FDL LA CANDELARIA; `18` FDL RAFAEL URIBE URIBE; `19` FDL CIUDAD BOLIVAR; `20` FDL SUMAPAZ; `21` IDU; `22` CVP-CAJA DE VIVIENDA POPULAR; `23` SECRETARIA DEL HABITAT; `24` SECRETARIA DISTRITAL DE MOVILIDAD; `25` EAAB; `26` EMPRESA INMOBILIARIA CUNDINAMARQUESA; `27` IDEPAC; `28` UAERMV |  |
| `TIPOMALLA` | Tipo Malla | Texto (Long 2) | N / A | `AR` Arterial; `IN` Intermedia; `LO` Local; `RU` Rural; `CM` Circuito Movilidad; `EX` Expansion; `FD` Fuera del Distrito |  |
| `PROGRAMA` | Programa | Texto (Long 50) | N / A | `N/A` N/A |  |
| `COMUNICACIÓN` | Comunicación | Texto (Long 20) | N / A | `N/A` N/A |  |
| `FECHAREPORTE` | Comunicación | Fecha | N / A | `N/A` N/A |  |
| `OBSERVACION` | Observacion | Texto (Long 200) | N / A | `N/A` N/A |  |

## RedInfraestructuraCicloInclusiva

### CicloEstacion

Geometría **punto**; elementos: CicloEstación.
Se define como un módulo cubierto capaz de albergar treinta y seis (36) bicicletas logrando repetir el modulo básico para producir cicloparqueaderos medianos y de gran formato aumentando su longitud y capacidad

Atributos de **CicloEstacion**

| Campo | Alias | Tipo | Unidad | Dominio o rango | Marca |
|---|---|---|---|---|---|
| `PK_ID_CicloEstacion` | PK_ID_CicloEstacion | Entero Largo | N / A |  | obligatorio |
| `Clase` | Clase | Entero Corto | N / A | `1` Cicloestación; `2` Cicloparqueadero | obligatorio |
| `Nombre` | Nombre | Texto | N / A |  | obligatorio |
| `Ubicación` | Ubicación | Texto | N / A |  | obligatorio |
| `Capacidad` | Capacidad | Entero | Adimensional | rango 1 a 250 | obligatorio |
| `FechaRegistro` | Fecha de Registro | Fecha | N / A |  | obligatorio |

### Ciclorruta

Geometría **polígono**; elementos: Ciclorruta.
Calzada destinada de manera permanente a la circulación de bicicletas, ubicada en el andén, el separador o segregada de la calzada vehicular o en otros lugares autorizados, debidamente señalizada y/o delimitada.

Atributos de **Ciclorruta**

| Campo | Alias | Tipo | Unidad | Dominio o rango | Marca |
|---|---|---|---|---|---|
| `PK_ID_Ciclorruta` | PK_ID_Ciclorruta | Entero Largo | N / A |  | obligatorio |
| `CIV` | CIV | Entero | N / A |  | obligatorio |
| `LongitudHorizontal` | Longitud Horizontal de la Ciclorruta | Decimal | Metro (m) |  | obligatorio |
| `AnchoCiclorruta` | Ancho de la Ciclorruta | Decimal | Metro (m) |  | obligatorio |
| `AreaCiclorruta` | Área de la Ciclorruta | Decimal | Metro cuadrado (m2) |  | obligatorio |
| `TipoMaterialCiclorruta` | Tipo de Material de la Ciclorruta | Entero | N / A | `0` Sin dato; `1` Rígido; `2` Flexible; `3` Mixtos; `4` Adoquín concreto; `5` Adoquín arcilla; `6` Afirmado; `8` Tierra; `12` Piedra laja; `13` Placa Huella | obligatorio |
| `Localidad` | Localidad | Entero | N / A |  |  |
| `FechaRegistro` | Fecha de Registro | Fecha | N / A |  | obligatorio |

Tabla relacionada **DetalleCiclorruta** (Detalle de la Ciclorruta), de Ciclorruta

| Campo | Alias | Tipo | Unidad | Dominio o rango | Marca |
|---|---|---|---|---|---|
| `PK_ID_DetalleCiclorruta` | PK_ID_DetalleCiclorruta | Entero Largo | N / A |  |  |
| `FK_ID_Ciclorruta` | FK_ID_Ciclorruta | Entero Largo | N / A |  |  |
| `TH1` | TH1 | Decimal | Centímetro (cm) | rango 2 a 10 |  |
| `TH2` | TH2 | Decimal | Centímetro (cm) | rango 2 a 40 |  |
| `MetodoEspesores` | Metodo Espesores | Entero | N / A | `1` Georadar; `2` Apiques; `3` Asignado Georadar; `4` Asignado Apique; `10` Información Secundaria; `11` Medición en obra |  |
| `TPDBicicletas` | TPD de bicicletas | Entero | Adimensional |  |  |
| `FechadeTPD` | Fecha de TPD | Fecha | N / A |  |  |

Tabla relacionada **DiagnosticoCiclorruta** (Diagnostico de la Ciclorruta), de Ciclorruta

| Campo | Alias | Tipo | Unidad | Dominio o rango | Marca |
|---|---|---|---|---|---|
| `PK_ID_DiagnosticoCiclorruta` | PK_ID_DiagnosticoCiclorruta | Entero Largo | N / A |  | según alcance |
| `FK_ID_Ciclorruta` | FK_ID_Ciclorruta | Entero Largo | N / A |  | según alcance |
| `CBR` | CBR | Entero | Porcentaje (%) | rango 0 a 15 | según alcance |
| `IF` | IF | Entero | Porcentaje (%) | rango 0 a 100 | según alcance |
| `FechaMedicionIF` | Fecha de medición IF | Fecha | N / A |  | según alcance |
| `ICCP` | ICCP | Decimal | Porcentaje (%) | rango 0 a 100 | según alcance |
| `FechaMedicionICCP` | Fecha de medición ICCP | Fecha | N / A |  | según alcance |
| `ICCD` | ICCD | Decimal | Porcentaje (%) | rango 0 a 100 | según alcance |
| `FechaMedicionICCD` | Fecha de medición ICCD | Fecha | N / A |  | según alcance |
| `IRI` | IRI | Entero | Porcentaje (%) | rango 0 a 100 | según alcance |
| `TipoIRI` | TipoIRI | Entero | N / A | `1` Rondas; `2` Melin; `3` Rugosimetro; `4` Calificacion visual; `10` Apl | según alcance |
| `FechaMedicionIRI` | Fecha Medicion IRI | Fecha | N / A |  | según alcance |

Tabla relacionada **DetalleAreaIntervencionCalzadaCiclorruta** (Detalle Area Intervencion Calzada Ciclorruta), de Ciclorruta

| Campo | Alias | Tipo | Unidad | Dominio o rango | Marca |
|---|---|---|---|---|---|
| `PK_ID_MallaVial` | PK_ID_MallaVial | Entero Largo | N / A |  | obligatorio |
| `FK_ID_AreaIntervencion` | FK_ID_AreaIntervencion | Entero Largo | N / A |  | obligatorio |
| `EspesorRA` | Espesor Rodadura Asfáltica | Entero corto | Centímetro (cm) | rango 2 a 20 | obligatorio |
| `GranulometriaRA` | Granulometría Rodadura Asfáltica | Entero Corto | N / A | `1` Rodadura MD10; `2` Rodadura MD12; `3` Rodadura MS12; `4` Rodadura MD20; `5` Rodadura MS20; `7` Rodadura Mezcla Asfáltica con GCR | obligatorio |
| `EspesorCI` | Espesor Capa Intermedia | Entero Corto | Centímetro (cm) | rango 2 a 50 | obligatorio |
| `GranulometriaCI` | Granulometría Capa Intermedia | Entero corto | N / A | `1` Capa asfáltica intermedia MD20; `2` Capa asfáltica intermedia MS20; `3` Capa asfáltica intermedia MS25; `4` Fresado estabilizado con emulsión; `5` Fresado estabilizado con asfalto espumado; `6` Capa asfática intermedia MAM20; `7` Capa asfática intermedia con GCR; `8` Fresado estabilizado con emulsión y cemento | obligatorio |
| `EspesorBA` | Espesor Base Asfáltica | Entero corto | Centímetro (cm) | rango 2 a 50 | obligatorio |
| `GranulometriaBA` | Granulometría Base Asfáltica | Entero Corto | N / A | `1` Base asfáltica MD20; `2` Base asfáltica MS25; `3` Base asfáltica MG20; `4` Base asfáltica MG25; `5` Base asfáltica MAM20; `6` Fresado estabilizado con emulsión; `7` Fresado estabilizado con asfalto espumado; `8` Base asfáltica con GCR | obligatorio |
| `EspesorBG` | Espesor Base Granular | Entero Corto | Centímetro (cm) | rango 10 a 50 | obligatorio |
| `GranulometriaBG` | Granulometría Base Granular | Entero Corto | N / A | `1` BG-A; `2` BG-B; `3` BG-C | obligatorio |
| `EspesorBE` | Espesor Base Estabilizada | Entero Corto | Centímetro (cm) | rango 10 a 50 | obligatorio |
| `GranulometriaBE` | Granulometría Base Estabilizada | Entero corto | N / A | `1` GEC_A_Gr1 CEMENTO; `2` GEC_A_Gr2 CEMENTO; `3` GEC_B_Gr1 CEMENTO; `4` GEC_B_Gr2 CEMENTO; `5` GEC_B_Gr3 CEMENTO; `6` GEC_C_Gr1 CEMENTO; `7` GEC_C_Gr2 CEMENTO; `8` MGEA_A ASFALTO; `9` MGEA_B ASFALTO; `10` MGEA_C ASFALTO; `11` GEEA_AGr1 EMULSIÓN; `12` GEEA_AGr2 EMULSIÓN; `13` GEEA_BGr1 EMULSIÓN; `14` GEEA_BGr2 EMULSIÓN; `15` GEEA_CGr1 EMULSIÓN; `16` GEEA_CGr2 EMULSIÓN | obligatorio |
| `EspesorSBG` | Espesor Subbase Granular | Entero Corto | Centímetro (cm) | rango 10 a 50 | obligatorio |
| `GranulometriaSBG` | Granulometría Subbase Granular | Entero Corto | N / A | `1` SBG-A; `2` SBG-B; `3` SBG-C | obligatorio |
| `EspesorSBE` | Espesor Subbase Estabilizada | Entero Corto | Centímetro (cm) | rango 10 a 50 | obligatorio |
| `GranulometriaSBE` | Granulometría Subbase Estabilizada | Entero Corto | N / A | `1` GEC_A_Gr1 CEMENTO; `2` GEC_A_Gr2 CEMENTO; `3` GEC_B_Gr1 CEMENTO; `4` GEC_B_Gr2 CEMENTO; `5` GEC_B_Gr3 CEMENTO; `6` GEC_C_Gr1 CEMENTO; `7` GEC_C_Gr2 CEMENTO; `8` GEC_D_Gr1 CEMENTO; `9` MGEA_A ASFALTO; `10` MGEA_B ASFALTO; `11` MGEA_C ASFALTO; `12` GEEA_AGr1 EMULSIÓN; `13` GEEA_AGr2 EMULSIÓN; `14` GEEA_BGr1 EMULSIÓN; `15` GEEA_BGr2 EMULSIÓN; `16` GEEA_CGr1 EMULSIÓN; `17` GEEA_CGr2 EMULSIÓN | obligatorio |

### RedCiclorruta

Geometría **línea**; elementos: Red de Ciclorruta.
Eje que articula el sistema de ciclorrutas, conectado de manera lógica, localizado sobre andenes, separadores, alamedas, parques, calzadas y puentes para el tránsito de ciclistas permitiendo su desplazamiento seguro, teniendo como objetivó ofrecer una infraestructura de transporte alterno o recreativo.

Atributos de **RedCiclorruta**

| Campo | Alias | Tipo | Unidad | Dominio o rango | Marca |
|---|---|---|---|---|---|
| `PK_ID_RedCiclorruta` | PK_ID_RedCiclorruta | Entero | N / A |  | obligatorio |
| `CodigoElemento` | Código de elemento localizado | Entero | N / A |  | obligatorio |
| `Localizacion / Clase` | Localización / Clase | Entero | N / A | `1` Espacio Compartido; `2` Ciclorruta; `1` Espacio Compartido; `2` Ciclorruta; `1` Espacio Compartido; `2` Ciclorruta; `3` Bicicarril; `4` Intersección; `5` Carril BusBici; `7` Pompeyano; `12` Ciclobarrio; `13` Vía Compartida; `6` CicloTunel; `1` Espacio Compartido; `2` Ciclorruta; `8` Ciclo-Puente; `9` Ciclo-Peatonal; `10` Peatonal; `11` Vehicular; `1` Espacio Compartido; `2` Ciclorruta | obligatorio |
| `Sentido` | Sentido Circulación | Texto | N / A | `DS` Bidireccional; `US` Unidireccional | obligatorio |
| `Competencia` | Competencia | Texto | N / A | `IDU` Instituto de Desarrollo Urbano; `SDM` Secretaria Distrital de Movilidad; `EAB` Empresa de Acueducto y Alcantarillado de Bogotá; `IDRD` Instituto Distrital de Recreación y Deporte | obligatorio |
| `TipoSuperficie` | Tipo de Superficie |  | N / A | `1` Liso; `2` Corrugado; `3` Particulado; `4` Metálico | obligatorio |
| `Demarcado` | Demarcado | Texto | N / A | `S` Si; `N` No | obligatorio |
| `FechaRegistro` | Fecha de Registro | Fecha | N / A |  | obligatorio |
| `NombreVia` | Tramo | Texto | N / A |  |  |
| `Localidad` | Localidad | Entero | N / A | `1` USAQUEN; `2` CHAPINERO; `3` SANTA FE; `4` SAN CRISTOBAL; `5` USME; `6` TUNJUELITO; `7` BOSA; `8` KENNEDY; `9` FONTIBON; `10` ENGATIVA; `11` SUBA; `12` BARRIOS UNIDOS; `13` TEUSAQUILLO; `14` LOS MARTIRES; `15` ANTONIO NARIÑO; `16` PUENTE ARANDA; `17` CANDELARIA; `18` RAFAEL URIBE URIBE; `19` CIUDAD BOLIVAR; `20` SUMAPAZ |  |
| `Clasificacion` | Clasificación | Entero | N / A | `1` Principal; `2` Secundaria; `3` Complementaria; `4` Ambiental y Recreativa |  |
| `TipoRed` | Tipo Red | Entero | N / A | `1` Ciclorruta; `2` Bicicarril |  |

## RedesAguaAlcantarillado

### Cuneta

Geometría **polígono**; elementos: Cuneta.
Zanjas, revestidas o no, construidas paralelamente a la bermas, destinadas a facilitar el drenaje superficial longitudinal a de la carretera. Su geometría puede variar según las condiciones de la vía y del área que drenan.

Atributos de **Cuneta**

| Campo | Alias | Tipo | Unidad | Dominio o rango | Marca |
|---|---|---|---|---|---|
| `PK_ID_Cuneta` | PK_ID_Cuneta | Entero Largo | N / A |  | obligatorio |
| `CIV` | CIV | Entero Largo | N / A |  | obligatorio |
| `TipoCuneta` | Tipo de cuneta | Entero | N / A | `1` En "v"; `2` Rectangular; `3` Circular; `4` Trapezoidal | obligatorio |
| `TipoMaterialCuneta` | Tipo de material | Entero | N / A | `1` Concreto; `2` Concreto Ciclopeo; `3` Prefabricada | obligatorio |
| `Confina` | Confinamiento | Texto | N / A | `S` Si; `N` No | obligatorio |
| `LongitudCuneta` | Longitud | Decimal | Metro (m) |  | obligatorio |
| `AnchoCuneta` | Ancho | Decimal | Metro (m) |  | obligatorio |
| `AreaCuneta` | Área | Decimal | Metro cuadrado (m2) |  | obligatorio |
| `ProfundidadCuneta` | Profundidad | Decimal | Centímetro (cm) |  | obligatorio |
| `EstadoFuncionalidad` | Estado de funcionalidad | Texto | N / A | `B` Bueno; `M` Malo; `R` Regular | obligatorio |
| `EstadoColmatacion` | Estado de colmatación | Texto | N / A | `B` Bueno; `M` Malo; `R` Regular | obligatorio |
| `FechaRegistro` | Fecha de Registro | Fecha | N / A |  | obligatorio |
