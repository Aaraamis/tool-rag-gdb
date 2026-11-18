"""CLI del primer hito de tool-rag-gdb."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from .checklist import write_checklist
from .consolidation import consolidate, ollama_embed
from .classification import apply_manual_reviews, classify_manifest, write_classification
from .extraction import page_texts, validate_dir
from .inventory import build_manifest, write_json
from .normative import write_normative
from .normative_links import propose_links, register_groups, review_links
from .pipeline import convert_selected, profile_manifest
from .proposal import ollama_ask, propose_selected
from .reports import write_informe, write_matriz


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
    propose_cmd = sub.add_parser("proponer", help="Candidatos de observación con un modelo local (Ollama)")
    propose_cmd.add_argument("--seleccion", type=Path, required=True,
                             help="TXT con una ruta relativa del manifiesto por línea")
    propose_cmd.add_argument("--modelo", default="qwen3.5:9b-q4_K_M")
    propose_cmd.add_argument("--url", default="http://localhost:11434")
    propose_cmd.add_argument("--prompt", type=Path, default=Path("prompts/proponer-observaciones.md"))
    propose_cmd.add_argument("--manifiesto", type=Path, default=Path("datos/01_inventario/manifiesto.json"))
    propose_cmd.add_argument("--salida-dir", type=Path, default=Path("datos/03_candidatos"))
    merge = sub.add_parser("consolidar", help="Agrupa observaciones repetidas (RF8) con embeddings locales")
    merge.add_argument("--extraido-dir", type=Path, default=Path("datos/03_extraido"))
    merge.add_argument("--salida-dir", type=Path, default=Path("datos/04_consolidado"))
    merge.add_argument("--decisiones", type=Path, default=Path("config/consolidacion-pares.csv"))
    merge.add_argument("--modelo", default="bge-m3")
    merge.add_argument("--url", default="http://localhost:11434")
    merge.add_argument("--temas", type=Path, default=Path("config/temas.csv"))
    merge.add_argument("--temas-manuales", type=Path, default=Path("config/temas-asignacion.csv"))
    check = sub.add_parser("checklist", help="Borrador de checklist-gdb.md desde los grupos consolidados")
    check.add_argument("--grupos", type=Path, default=Path("datos/04_consolidado/grupos.json"))
    check.add_argument("--salida", type=Path, default=Path("datos/04_entregables/checklist-gdb.md"))
    check.add_argument("--enlaces", type=Path, default=Path("config/normativa-enlaces.csv"))
    check.add_argument("--catalogo", type=Path,
                       default=Path("datos/04_consolidado/catalogo-normativa.json"))
    check.add_argument("--registro", type=Path, default=Path("config/grupos-registro.csv"))
    registry = sub.add_parser("registrar-grupos",
                              help="Registra los miembros de los grupos actuales para trasladar decisiones")
    registry.add_argument("--grupos", type=Path, default=Path("datos/04_consolidado/grupos.json"))
    registry.add_argument("--registro", type=Path, default=Path("config/grupos-registro.csv"))
    matrix = sub.add_parser("matriz", help="matriz-observaciones.md desde los grupos consolidados")
    matrix.add_argument("--grupos", type=Path, default=Path("datos/04_consolidado/grupos.json"))
    matrix.add_argument("--salida", type=Path, default=Path("datos/04_entregables/matriz-observaciones.md"))
    matrix.add_argument("--contratos", type=Path, default=Path("config/contratos-documentos.csv"))
    report = sub.add_parser("informe", help="informe-corpus.md: estado de cada archivo del manifiesto")
    report.add_argument("--manifiesto", type=Path, default=Path("datos/01_inventario/manifiesto.json"))
    report.add_argument("--perfiles", type=Path, default=Path("datos/01_inventario/perfiles.json"))
    report.add_argument("--clasificacion", type=Path, default=Path("datos/01_inventario/clasificacion.csv"))
    report.add_argument("--convertidos", type=Path, default=Path("datos/02_convertidos/estado.json"))
    report.add_argument("--extraido-dir", type=Path, default=Path("datos/03_extraido"))
    report.add_argument("--salida", type=Path, default=Path("datos/04_entregables/informe-corpus.md"))
    normative = sub.add_parser("normativa", help="Verifica el alistamiento y genera el catálogo normativo (RF7)")
    normative.add_argument("--raiz", type=Path, required=True,
                           help="Raíz del paquete de alistamiento IDU 2020")
    normative.add_argument("--registro", type=Path, default=Path("config/normativa.csv"))
    normative.add_argument("--catalogo", type=Path,
                           default=Path("datos/04_consolidado/catalogo-normativa.json"))
    normative.add_argument("--salida", type=Path,
                           default=Path("datos/04_entregables/normativa-vigente.md"))
    normative.add_argument("--proyecto", default="contrato IDU 348 — construcción (récord)")
    links = sub.add_parser("enlazar-normativa",
                           help="Propone enlaces entre grupos y requisitos normativos para revisión")
    links.add_argument("--grupos", type=Path, default=Path("datos/04_consolidado/grupos.json"))
    links.add_argument("--catalogo", type=Path,
                       default=Path("datos/04_consolidado/catalogo-normativa.json"))
    links.add_argument("--salida", type=Path,
                       default=Path("datos/04_consolidado/normativa-enlaces-revisar.csv"))
    links.add_argument("--cache", type=Path,
                       default=Path("datos/04_consolidado/normativa-embeddings.json"))
    links.add_argument("--modelo", default="bge-m3")
    links.add_argument("--url", default="http://localhost:11434")
    links.add_argument("--candidatos", type=int, default=5)
    review_links_cmd = sub.add_parser("revisar-enlaces-normativa",
                                      help="Pide una segunda opinión local sobre candidatos normativos")
    review_links_cmd.add_argument("--candidatos", type=Path,
                                  default=Path("datos/04_consolidado/normativa-enlaces-revisar.csv"))
    review_links_cmd.add_argument("--salida", type=Path,
                                  default=Path("datos/04_consolidado/normativa-enlaces-modelo.csv"))
    review_links_cmd.add_argument("--estado", type=Path,
                                  default=Path("datos/04_consolidado/normativa-enlaces-modelo.json"))
    review_links_cmd.add_argument("--prompt", type=Path,
                                  default=Path("prompts/revisar-enlaces-normativos.md"))
    review_links_cmd.add_argument("--modelo", default="qwen3.5:9b-q4_K_M")
    review_links_cmd.add_argument("--url", default="http://localhost:11434")
    review_links_cmd.add_argument("--lote", type=int, default=5)
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
    elif args.command == "consolidar":
        print(json.dumps(consolidate(args.extraido_dir, args.salida_dir, args.decisiones,
                                     ollama_embed(args.modelo, args.url), args.modelo,
                                     themes_path=args.temas, overrides_path=args.temas_manuales)))
    elif args.command == "checklist":
        print(json.dumps(write_checklist(args.grupos, args.salida, args.enlaces, args.catalogo,
                                         args.registro)))
    elif args.command == "registrar-grupos":
        print(json.dumps(register_groups(args.grupos, args.registro)))
    elif args.command == "matriz":
        print(json.dumps(write_matriz(args.grupos, args.salida, args.contratos)))
    elif args.command == "informe":
        print(json.dumps(write_informe(args.manifiesto, args.perfiles, args.clasificacion,
                                       args.convertidos, args.extraido_dir, args.salida)))
    elif args.command == "normativa":
        print(json.dumps(write_normative(args.registro, args.raiz, args.catalogo,
                                         args.salida, args.proyecto), ensure_ascii=False))
    elif args.command == "enlazar-normativa":
        print(json.dumps(propose_links(args.grupos, args.catalogo, args.salida, args.cache,
                                       ollama_embed(args.modelo, args.url), args.modelo,
                                       args.candidatos), ensure_ascii=False))
    elif args.command == "revisar-enlaces-normativa":
        print(json.dumps(review_links(args.candidatos, args.salida, args.estado,
                                      args.prompt.read_text(encoding="utf-8"),
                                      ollama_ask(args.modelo, args.url), args.modelo, args.lote),
                         ensure_ascii=False))
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
            if args.command == "proponer":
                result = propose_selected(manifest, pdf_dir, args.salida_dir, selected,
                                          args.prompt.read_text(encoding="utf-8"), args.modelo,
                                          ollama_ask(args.modelo, args.url))
            else:
                result = convert_selected(manifest, pdf_dir, args.salida_dir, selected)
        errors = sum(x["estado"] == "error" for x in result["documentos"].values())
        print(json.dumps({"documentos": len(result["documentos"]), "errores": errors}))
        return 1 if errors else 0
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
