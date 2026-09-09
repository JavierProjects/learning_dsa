#!/usr/bin/env python3
"""Verifica la coherencia de la publicación; no califica a los estudiantes.

Ejecuta cada programa en un proceso nuevo y compara su salida con la salida
declarada en la fuente. Comprueba también que el código publicado coincide con
la fuente usada para producir la guía y que el PDF contiene todos los temas.
"""

import json
from pathlib import Path
import runpy
import subprocess
import sys

from pypdf import PdfReader


ROOT = Path(__file__).resolve().parents[1]


def main():
    source = runpy.run_path(str(ROOT / "fuentes" / "contenido.py"))
    cases = []
    for unit in source["UNIDADES"]:
        cases.append(("ejemplos", unit["example"]))
        cases += [("ejercicios", p) for p in unit["exercises"]]
    for lab in source["PRACTICAS"]:
        cases += [("practicas", lab["initial"]), ("soluciones", lab["solution"])]
    errors = []
    for folder, program in cases:
        p = ROOT / folder / (program["id"] + ".py")
        if not p.exists():
            errors.append(f"Falta {p.relative_to(ROOT)}")
            continue
        if not p.read_text(encoding="utf-8").endswith(program["code"]):
            errors.append(f"Código distinto de la fuente: {p.relative_to(ROOT)}")
        run = subprocess.run([sys.executable, str(p)], cwd=ROOT,
                             capture_output=True, text=True, timeout=10)
        if run.returncode or run.stderr or run.stdout != program["expected"]:
            errors.append(f"{program['id']}: esperado {program['expected']!r}, obtenido {run.stdout!r}; error {run.stderr!r}")
    declared = json.loads((ROOT / "herramientas" / "salidas_esperadas.json").read_text(encoding="utf-8"))
    if len(declared) != len(cases):
        errors.append("El manifiesto de salidas no coincide con el número de programas.")
    for (folder, program), entry in zip(cases, declared):
        if entry != {"path": f"{folder}/{program['id']}.py", "stdout": program["expected"]}:
            errors.append(f"Manifiesto desactualizado: {program['id']}")
    pdf = PdfReader(ROOT / "output" / "pdf" / "guia_objetos_referencias.pdf")
    layout = json.loads((ROOT / "herramientas" / "mapa_paginas.json").read_text(encoding="utf-8"))
    if len(pdf.pages) != layout["total_pages"]:
        errors.append("El número de páginas no coincide con el índice.")
    full_text = "\n".join(page.extract_text() or "" for page in pdf.pages)
    for unit in source["UNIDADES"]:
        index = layout["sections"][unit["number"]] - 1
        if unit["title"] not in (pdf.pages[index].extract_text() or ""):
            errors.append(f"El índice no llega al tema {unit['number']}.")
        for p in [unit["example"], *unit["exercises"]]:
            if p["id"].upper() not in full_text:
                errors.append(f"Falta {p['id']} en el PDF.")
    for lab in source["PRACTICAS"]:
        index = layout["labs"][lab["id"]] - 1
        if lab["title"] not in (pdf.pages[index].extract_text() or ""):
            errors.append(f"El índice no llega a la práctica {lab['id']}.")
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(f"Correcto: {len(cases)} programas ejecutados con salidas verificadas.")
    print(f"Correcto: {len(pdf.pages)} páginas, 10 temas y 4 prácticas presentes en el índice.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
