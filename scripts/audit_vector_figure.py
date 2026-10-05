"""Audit SVG/PDF structure and final-width fonts; not a semantic/visual review."""
from __future__ import annotations

import argparse
import collections
import json
from pathlib import Path
import sys
import xml.etree.ElementTree as ET


def normalized(value):
    return " ".join(value.split())


def audit_svg(path, required, allow_raster):
    root = ET.parse(path).getroot()
    tag = lambda element: element.tag.rsplit("}", 1)[-1]
    elements = list(root.iter())
    text_nodes = [e for e in elements if tag(e) == "text"]
    labels = [normalized("".join(e.itertext())) for e in text_nodes]
    labels = [value for value in labels if value]
    images = [e for e in elements if tag(e) == "image"]
    foreign = [e for e in elements if tag(e) == "foreignObject"]
    ids = collections.Counter(e.attrib["id"] for e in elements if "id" in e.attrib)
    duplicates = sorted(key for key, count in ids.items() if count > 1)
    native = sum(tag(e) in {"path", "rect", "circle", "ellipse", "line", "polyline", "polygon"} for e in elements)
    issues = []
    if tag(root) != "svg":
        issues.append("Source root is not SVG.")
    if not labels:
        issues.append("SVG has no nonempty live text labels.")
    if not native:
        issues.append("SVG has no native shapes or paths.")
    for element in images:
        href = element.get('href') or element.get('{http://www.w3.org/1999/xlink}href')
        if not href:
            issues.append("SVG image element has no href dependency.")
        elif not href.startswith(('data:', '#', 'http://', 'https://')) and not (path.parent / href).is_file():
            issues.append("SVG image dependency missing: " + href)
    if images and not allow_raster:
        issues.append("SVG contains image elements (possibly raster or embedded SVG); inspect or declare intentional insets.")
    if foreign:
        issues.append("SVG uses foreignObject; use portable native labels/shapes or review separately.")
    if duplicates:
        issues.append("SVG has duplicate object IDs.")
    for label in required:
        if normalized(label) not in labels:
            issues.append(f"Required editable SVG label missing: {label}")
    return {"path": str(path.resolve()), "live_text_count": len(labels),
            "native_shape_count": native, "image_count": len(images),
            "foreign_object_count": len(foreign), "duplicate_ids": duplicates,
            "viewBox": root.attrib.get("viewBox"), "issues": issues}


def audit_pdf(path, required, allow_raster, column_width, min_font):
    try:
        import pymupdf
    except ImportError as exc:
        raise RuntimeError("PDF audit requires PyMuPDF in the selected Python runtime.") from exc
    pages, issues, all_text = [], [], []
    with pymupdf.open(path) as document:
        if len(document) != 1:
            issues.append("Expected a one-page figure export; audit manuscript pages separately.")
        for index, page in enumerate(document):
            scale = column_width / page.rect.width if column_width else 1.0
            spans = [s for b in page.get_text("dict")["blocks"]
                     for line in b.get("lines", []) for s in line["spans"]
                     if s["text"].strip()]
            sizes = [s["size"] * scale for s in spans]
            images = page.get_image_info()
            drawings = page.get_drawings()
            all_text.append(page.get_text())
            if not spans:
                issues.append(f"Page {index + 1} has no selectable text.")
            if not drawings:
                issues.append(f"Page {index + 1} has no vector drawing paths.")
            if images and not allow_raster:
                issues.append(f"Page {index + 1} contains image content.")
            if sizes and min(sizes) + 0.01 < min_font:
                issues.append(f"Page {index + 1} minimum printed font is {min(sizes):.2f} pt, below {min_font:g} pt.")
            pages.append({"page": index + 1, "export_size_pt": [page.rect.width, page.rect.height],
                          "printed_size_pt": [page.rect.width * scale, page.rect.height * scale],
                          "min_printed_font_pt": min(sizes) if sizes else None,
                          "image_count": len(images), "vector_path_count": len(drawings),
                          "text_span_count": len(spans)})
    corpus = normalized(" ".join(all_text))
    for label in required:
        if normalized(label) not in corpus:
            issues.append(f"Required selectable PDF label missing: {label}")
    return {"path": str(path.resolve()), "pages": pages, "issues": issues}


def positive(value):
    number = float(value)
    if number <= 0:
        raise argparse.ArgumentTypeError("must be positive")
    return number


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--svg", type=Path)
    parser.add_argument("--pdf", type=Path)
    parser.add_argument("--column-width-pt", type=positive)
    parser.add_argument("--min-font-pt", type=positive, default=8)
    parser.add_argument("--require-label", action="append", default=[])
    parser.add_argument("--allow-raster-assets", action="store_true")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    if not args.svg and not args.pdf:
        parser.error("provide --svg, --pdf, or both")
    result = {"scope": "Structure and font evidence only; does not establish semantic, visual or editor-round-trip correctness.",
              "printed_font_basis": "specified column width" if args.column_width_pt else "native PDF export width",
              "issues": []}
    try:
        if args.svg:
            result["svg"] = audit_svg(args.svg, args.require_label, args.allow_raster_assets)
            result["issues"].extend(result["svg"]["issues"])
        if args.pdf:
            result["pdf"] = audit_pdf(args.pdf, args.require_label, args.allow_raster_assets,
                                      args.column_width_pt, args.min_font_pt)
            result["issues"].extend(result["pdf"]["issues"])
    except (OSError, ET.ParseError, RuntimeError, ValueError) as exc:
        result["issues"].append(str(exc))
    result["structure_checks_passed"] = not result["issues"]
    result["unverified"] = ["semantics", "visual quality", "edge attachment", "editor round-trip", "paper integration"]
    output = json.dumps(result, indent=2, ensure_ascii=False) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(output)
    print(output, end="")
    return 0 if result["structure_checks_passed"] else 1


if __name__ == "__main__":
    sys.exit(main())
