import zipfile

from rag_gdb.dictionary import read_dictionary, render_dictionary

NS = ('xmlns:office="urn:oasis:names:tc:opendocument:xmlns:office:1.0" '
      'xmlns:table="urn:oasis:names:tc:opendocument:xmlns:table:1.0" '
      'xmlns:text="urn:oasis:names:tc:opendocument:xmlns:text:1.0" '
      'xmlns:style="urn:oasis:names:tc:opendocument:xmlns:style:1.0" '
      'xmlns:fo="urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0"')


def _row(*cells):
    out = []
    for cell in cells:
        text, style = cell if isinstance(cell, tuple) else (cell, None)
        attr = f' table:style-name="{style}"' if style else ""
        out.append(f"<table:table-cell{attr}><text:p>{text}</text:p></table:table-cell>")
    return "<table:table-row>" + "".join(out) + "</table:table-row>"


def _sheet(name, *rows):
    return f'<table:table table:name="{name}">' + "".join(rows) + "</table:table>"


def _ods(path, *sheets):
    styles = ('<office:automatic-styles>'
              '<style:style style:name="red"><style:text-properties fo:color="#FF0000"/></style:style>'
              '<style:style style:name="green"><style:text-properties fo:color="#00B050"/></style:style>'
              '</office:automatic-styles>')
    content = (f'<office:document-content {NS}>{styles}<office:body><office:spreadsheet>'
               + "".join(sheets) + "</office:spreadsheet></office:body></office:document-content>")
    with zipfile.ZipFile(path, "w") as archive:
        archive.writestr("content.xml", content)


HEAD = ["Nombre_Campo", "Alias", "Descripción", "Elemento", "Código Dominio", "Etiqueta Dominio",
        "Descripción Dominio", "Rango Mínimo", "Rango Máximo", "Unidad", "Tipo de dato"]


def test_marks_follow_font_color_and_tolerate_header_typos(tmp_path):
    ods = tmp_path / "p.ods"
    catalog = _sheet("CATALOGO_BDG", _row("#", "FEATURE DATASET", "ELEMENTO", "FEATURE CLASS",
                                          "TIPO DE GEOMETRÍA", "DEFINICIÓN"),
                     _row("1", "EspacioPublico", "Rampa", "Rampa", "POLÍGONO", "Acceso sin peldaños"))
    rampa = _sheet("Rampa", _row(*HEAD, "Proyecto: Diseño", "Proyecto: Consrucción", "Contratista"),
                   _row("PK_ID_Rampa", "PK", "", "", "", "", "", "", "", "N / A", "Entero",
                        ("X", "red"), ("X", "red")),
                   _row("Tipo", "Tipo", "", "", "B5", "Peatonal", "", "", "", "N / A", "Texto",
                        "N / A", ("X", "green")),
                   _row("", "", "", "", "B10", "Vehicular"),
                   _row("Notas", "Notas", "", "", "", "", "", "", "", "N / A", "Texto", ("X", "red"), "N / A"))
    explo = _sheet("Exploracion", _row(*HEAD, "Sondeo", "Apique", "Contratista"),
                   _row("Costado", "Costado", "", "", "I", "Izquierdo", "", "", "", "N / A", "Texto",
                        ("X", "red"), ("X", "red")))
    _ods(ods, catalog, rampa, explo)
    data = read_dictionary(ods, "Construcción")
    by_sheet = {c["hoja"]: c for c in data["clases"]}
    fields = {f["campo"]: f for f in by_sheet["Rampa"]["tablas"][0]["campos"]}
    assert by_sheet["Rampa"]["dataset"] == "EspacioPublico"
    assert fields["PK_ID_Rampa"]["marca"] == "obligatorio"
    assert fields["Tipo"]["marca"] == "según alcance"
    assert fields["Tipo"]["dominio"] == [("B5", "Peatonal"), ("B10", "Vehicular")]
    assert fields["Notas"]["marca"] == ""
    costado = by_sheet["Exploracion"]["tablas"][0]["campos"][0]
    assert costado["marca"] == "obligatorio (Sondeo, Apique)"
    text = render_dictionary(data, today="2026-11-19")
    assert "| EspacioPublico | [Rampa](#rampa) | POLÍGONO | 0 | 1 | 1 |" in text
    assert "`B5` Peatonal; `B10` Vehicular" in text
