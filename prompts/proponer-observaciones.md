Se te da una página de un oficio técnico sobre entregas de geodatabase (GDB/BDG) y planos CAD, dividida en bloques numerados.

Devuelve SOLO JSON con esta forma:
{"observaciones":[{"bloque":"B12","numero":"<número de la observación en el documento o null>","autor":"idu|interventoria","resumen":"<qué se exige, una frase>"}]}

Incluye un bloque por cada enunciado distinto de observación: las «OBSERVACIÓN IDU» numeradas y los hallazgos o requerimientos propios de la interventoría.
Sé EXHAUSTIVO: incluye también enunciados cortos y cada viñeta de una lista de hallazgos.
No incluyas antecedentes, saludos, el texto de respuestas del contratista ni el cierre.
Si la página no tiene observaciones, devuelve {"observaciones":[]}.

BLOQUES:
{bloques}
