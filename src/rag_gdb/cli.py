"""CLI del primer hito de tool-rag-gdb."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from .classification import apply_manual_reviews, classify_manifest, write_classification
from .extraction import page_texts, validate_dir
from .inventory import build_manifest, write_json
from .pipeline import convert_selected, profile_manifest


def main() -> int:
    parser = argparse.ArgumentParser(prog="rag-gdb")
    sub = parser.add_subparsers(dest="command", required=True)
    inv = sub.add_parser("inventariar")
    inv.add_argument("--pdf-dir", type=Path, required=True)
    inv.add_argument("--ods", type=Path, required=True)
    inv.add_argument("--reglas", type=Path, help="JSON con patrones regex de remitentes y asuntos a excluir")
    inv.add_argument("--salida", type=Path, default=Path("datos/01_inventario/manifiesto.json"))
    profile = sub.add_parser("perfilar")
    profile.add_argument("--manifiesto", type=Path, default=Path("datos/01_inventario/manifiesto.json"))
    profile.add_argument("--salida", type=Path, default=Path("datos/01_inventario/perfiles.json"))
    convert = sub.add_parser("convertir")
    convert.add_argument("--manifiesto", type=Path, default=Path("datos/01_inventario/manifiesto.json"))
    convert.add_argument("--salida-dir", type=Path, default=Path("datos/02_convertidos"))
    convert.add_argument("--seleccion", type=Path, required=True,
                         help="TXT con una ruta relativa del manifiesto por línea")
    classify = sub.add_parser("clasificar")
    classify.add_argument("--manifiesto", type=Path, default=Path("datos/01_inventario/manifiesto.json"))
    classify.add_argument("--salida", type=Path, default=Path("datos/01_inventario/clasificacion.csv"))
    classify.add_argument("--leer-texto", action="store_true",
                          help="Busca señales GDB en texto PDF; conserva los casos sin señal para revisión")
    classify.add_argument("--revisiones", type=Path, default=Path("config/clasificacion-manual.csv"))
    validate = sub.add_parser("validar", help="Valida las observaciones extraídas contra esquema, hash y PDF")
    validate.add_argument("--manifiesto", type=Path, default=Path("datos/01_inventario/manifiesto.json"))
    validate.add_argument("--extraido-dir", type=Path, default=Path("datos/03_extraido"))
    pages = sub.add_parser("paginas", help="Imprime el texto de un PDF con marcas de página")
    pages.add_argument("ruta", help="Ruta relativa del PDF tal como aparece en el manifiesto")
    pages.add_argument("--manifiesto", type=Path, default=Path("datos/01_inventario/manifiesto.json"))
    args = parser.parse_args()
    if args.command == "inventariar":
        rules = json.loads(args.reglas.read_text()) if args.reglas else None
        result = build_manifest(args.pdf_dir, args.ods, rules)
        write_json(args.salida, result)
        print(json.dumps(result["resumen"], ensure_ascii=False))
    elif args.command == "clasificar":
        manifest = json.loads(args.manifiesto.read_text())
        pdf_dir = Path(manifest["directorio_pdf"]) if args.leer_texto else None
        result = classify_manifest(manifest, Path(manifest["inventario_ods"]), pdf_dir)
        apply_manual_reviews(result, args.revisiones)
        print(json.dumps(write_classification(args.salida, result), ensure_ascii=False))
    elif args.command == "validar":
        manifest = json.loads(args.manifiesto.read_text())
        results = validate_dir(args.extraido_dir, manifest, Path(manifest["directorio_pdf"]))
        for name, errors in results.items():
            for error in errors:
                print(f"{name}: {error}")
        invalid = sum(bool(errors) for errors in results.values())
        print(json.dumps({"archivos": len(results), "invalidos": invalid}))
        return 1 if invalid else 0
    elif args.command == "paginas":
        manifest = json.loads(args.manifiesto.read_text())
        if args.ruta not in {item["ruta"] for item in manifest["archivos"]}:
            raise SystemExit(f"PDF no encontrado en el manifiesto: {args.ruta}")
        for number, text in enumerate(page_texts(Path(manifest["directorio_pdf"]) / args.ruta), 1):
            print(f"===== página {number} =====\n{text}")
    else:
        manifest = json.loads(args.manifiesto.read_text())
        pdf_dir = Path(manifest["directorio_pdf"])
        if args.command == "perfilar":
            result = profile_manifest(manifest, pdf_dir, args.salida)
        else:
            selected = [line.strip() for line in args.seleccion.read_text().splitlines()
                        if line.strip() and not line.lstrip().startswith("#")]
            result = convert_selected(manifest, pdf_dir, args.salida_dir, selected)
        errors = sum(x["estado"] == "error" for x in result["documentos"].values())
        print(json.dumps({"documentos": len(result["documentos"]), "errores": errors}))
        return 1 if errors else 0
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
