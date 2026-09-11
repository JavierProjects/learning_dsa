#!/usr/bin/env python3
"""Genera PDF, guía web, diagramas SVG y programas desde fuentes/contenido.py.

Uso desde cualquier carpeta: python3 ruta/a/herramientas/generar_material.py
Dependencia exclusiva de edición: reportlab. Los scripts del alumno usan
únicamente Python y su biblioteca estándar.
"""

from __future__ import annotations

import html
import json
import math
from pathlib import Path
import re
import runpy

from reportlab.graphics import renderSVG
from reportlab.graphics.shapes import Drawing, Line, Polygon, Rect, String
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    Flowable, Frame, KeepTogether, Paragraph, Preformatted, Spacer, Table,
    TableStyle,
)


ROOT = Path(__file__).resolve().parents[1]
SOURCE = runpy.run_path(str(ROOT / "fuentes" / "contenido.py"))
UNITS = SOURCE["UNIDADES"]
LABS = {p["id"]: p for p in SOURCE["PRACTICAS"]}
SOURCES = SOURCE["FUENTES"]
ANALOGY = SOURCE["ANALOGIA"]
PDF_PATH = ROOT / "output" / "pdf" / "guia_objetos_referencias.pdf"
WIDTH, HEIGHT = letter
LEFT, RIGHT, TOP, BOTTOM = 47, 47, 57, 44
CW = WIDTH - LEFT - RIGHT
CH = HEIGHT - TOP - BOTTOM
INK = colors.HexColor("#182028")
MUTED = colors.HexColor("#4a5158")
LIGHT = colors.HexColor("#f3f4f5")
RULE = colors.HexColor("#bfc5ca")
FONT_DIR = ROOT / "herramientas" / "fuentes_tipograficas"
for alias, filename in [("DsaSans", "DejaVuSans.ttf"),
                         ("DsaSans-Bold", "DejaVuSans-Bold.ttf"),
                         ("DsaMono", "DejaVuSansMono.ttf")]:
    pdfmetrics.registerFont(TTFont(alias, str(FONT_DIR / filename)))
pdfmetrics.registerFontFamily("DsaSans", normal="DsaSans", bold="DsaSans-Bold",
                              italic="DsaSans", boldItalic="DsaSans-Bold")


STYLES = {
    "body": ParagraphStyle("body", fontName="DsaSans", fontSize=10.8,
                           leading=14.8, textColor=INK, spaceAfter=7),
    "small": ParagraphStyle("small", fontName="DsaSans", fontSize=9.3,
                            leading=12.8, textColor=MUTED, spaceAfter=6),
    "tiny": ParagraphStyle("tiny", fontName="DsaSans", fontSize=8.3,
                           leading=11.2, textColor=MUTED, spaceAfter=4),
    "title": ParagraphStyle("title", fontName="DsaSans-Bold", fontSize=20.5,
                            leading=24, textColor=INK, spaceAfter=10),
    "sub": ParagraphStyle("sub", fontName="DsaSans-Bold", fontSize=11.1,
                          leading=14.3, textColor=INK, spaceBefore=7, spaceAfter=5),
    "kicker": ParagraphStyle("kicker", fontName="DsaSans-Bold", fontSize=8.3,
                             leading=10.7, textColor=MUTED, spaceAfter=6),
    "cover": ParagraphStyle("cover", fontName="DsaSans-Bold", fontSize=33,
                            leading=38, textColor=INK, spaceAfter=16),
    "code": ParagraphStyle("code", fontName="DsaMono", fontSize=9.1,
                           leading=12.4, textColor=INK, leftIndent=0,
                           spaceAfter=0),
    "output": ParagraphStyle("output", fontName="DsaMono", fontSize=8.9,
                             leading=12.2, textColor=INK, spaceAfter=4),
}


def rich(text):
    """Escape prose and apply only explicit inline backtick formatting."""
    parts = re.split(r"(`[^`]+`)", text)
    return "".join(
        '<font name="DsaMono" backColor="#e9edf2">' + html.escape(p[1:-1]) + "</font>"
        if p.startswith("`") and p.endswith("`") else html.escape(p)
        for p in parts
    ).replace("\n", "<br/>")


def para(text, style="body"):
    return Paragraph(rich(text), STYLES[style])


def heading(text):
    return para(text, "sub")


def block(code, *, output=False):
    if output:
        return Preformatted(code.rstrip(), STYLES["output"])
    inner = Preformatted(code.rstrip(), STYLES["code"])
    t = Table([[inner]], colWidths=[CW], hAlign="LEFT")
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), LIGHT),
        ("BOX", (0, 0), (-1, -1), 0.55, RULE),
        ("LEFTPADDING", (0, 0), (-1, -1), 10),
        ("RIGHTPADDING", (0, 0), (-1, -1), 10),
        ("TOPPADDING", (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
    ]))
    return t


def grid(headers, rows, widths=None, *, font="small", row_heights=None):
    widths = widths or [CW / len(headers)] * len(headers)
    data = [[Paragraph("<b>" + rich(h) + "</b>", STYLES[font]) for h in headers]]
    data += [[para(str(v), font) for v in r] for r in rows]
    table = Table(data, colWidths=widths, rowHeights=row_heights, repeatRows=1, hAlign="LEFT")
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), LIGHT),
        ("GRID", (0, 0), (-1, -1), 0.45, RULE),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 7),
        ("RIGHTPADDING", (0, 0), (-1, -1), 7),
        ("TOPPADDING", (0, 0), (-1, -1), 7),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ]))
    return table


class RuledSpace(Flowable):
    def __init__(self, height=42, label="Predicción, dibujo o explicación:"):
        super().__init__()
        self.width, self.height, self.label = CW, height, label

    def draw(self):
        c = self.canv
        c.setFont("DsaSans", 8)
        c.setFillColor(MUTED)
        c.drawString(0, self.height - 10, self.label)
        c.setStrokeColor(RULE)
        c.setLineWidth(0.35)
        y = self.height - 24
        while y >= 2:
            c.line(0, y, self.width, y)
            y -= 16


def diagram(key):
    """Diagrams are vectors in the PDF and standalone SVGs for the Markdown."""
    d = Drawing(CW, 112)

    def label(x, y, text, size=8.2, bold=False, anchor="start"):
        d.add(String(x, y, text, fontName="DsaSans-Bold" if bold else "DsaSans",
                     fontSize=size, fillColor=INK, textAnchor=anchor))

    def box(x, y, w, h, lines, *, name=False):
        d.add(Rect(x, y, w, h, strokeColor=RULE if name else INK,
                   fillColor=LIGHT if name else colors.white,
                   strokeWidth=0.65, rx=2, ry=2))
        lines = lines if isinstance(lines, list) else [lines]
        first = y + h / 2 + (len(lines) - 1) * 5 - 3
        for i, line in enumerate(lines):
            label(x + w / 2, first - i * 10, line, size=8, anchor="middle")

    def arrow(x1, y1, x2, y2):
        d.add(Line(x1, y1, x2, y2, strokeColor=INK, strokeWidth=0.8))
        dx, dy = x2 - x1, y2 - y1
        length = math.hypot(dx, dy)
        if not length:
            return
        ux, uy = dx / length, dy / length
        ax, ay = x2 - ux * 5, y2 - uy * 5
        d.add(Polygon([x2, y2, ax - uy * 2.2, ay + ux * 2.2,
                       ax + uy * 2.2, ay - ux * 2.2],
                      fillColor=INK, strokeColor=INK))

    def split(t1, t2):
        label(4, 101, t1, bold=True)
        label(270, 101, t2, bold=True)
        d.add(Line(258, 6, 258, 103, strokeColor=RULE, strokeWidth=0.5))

    def aliases(off, names, contents, separate=False):
        box(off + 8, 62, 48, 22, names[0], name=True)
        box(off + 8, 18, 48, 22, names[1], name=True)
        if separate:
            box(off + 96, 59, 148, 28, contents[0])
            box(off + 96, 15, 148, 28, contents[1])
            arrow(off + 56, 73, off + 96, 73)
            arrow(off + 56, 29, off + 96, 29)
        else:
            box(off + 96, 36, 148, 37, contents[0])
            arrow(off + 56, 73, off + 96, 65)
            arrow(off + 56, 29, off + 96, 44)

    if key == "mutabilidad":
        split("Antes de las operaciones", "Después de las operaciones")
        aliases(0, ["numero", "datos"], ["entero 10", "lista A: [10]"], True)
        aliases(264, ["numero", "datos"], ["entero 11", "lista A: [11]"], True)
    elif key == "alias":
        split("Después de y = x", "Después de y.append(4)")
        aliases(0, ["x", "y"], [["lista A", "[1, 2, 3]"]])
        aliases(264, ["x", "y"], [["misma lista A", "[1, 2, 3, 4]"]])
    elif key == "identidad":
        label(4, 101, "Dos listas distintas; a y b comparten A", bold=True)
        aliases(0, ["a", "b"], [["lista A", "[1, 2]"]])
        box(282, 42, 42, 22, "c", name=True)
        box(361, 35, 147, 37, ["lista B", "[1, 2]"])
        arrow(324, 53, 361, 53)
    elif key == "reasignacion":
        split("Antes de la concatenación", "Después de y = y + [4]")
        aliases(0, ["x", "y"], [["lista A", "[1, 2, 3]"]])
        aliases(264, ["x", "y"], ["A: [1, 2, 3]", "B: [1, 2, 3, 4]"], True)
    elif key == "funciones":
        split("Al entrar en reset_list", "Durante reset_list, tras lst = []")
        aliases(0, ["my_list", "lst"], [["lista A", "['X']"]])
        aliases(264, ["my_list", "lst"], ["A: ['X']", "B: []"], True)
    elif key == "copia_simple":
        split("Después de .copy()", "Después de copia[0] = 99")
        aliases(0, ["original", "copia"], ["A: [1, 2, 'hola', True]", "B: [1, 2, 'hola', True]"], True)
        aliases(264, ["original", "copia"], ["A: [1, 2, 'hola', True]", "B: [99, 2, 'hola', True]"], True)
    elif key == "anidamiento":
        label(4, 101, "Tras c[0][0] = 99: exteriores distintos, una lista interior", bold=True)
        box(8, 57, 130, 36, ["exterior b", "posición 0", "posición 1"])
        box(8, 10, 130, 36, ["exterior c", "posición 0", "posición 1"])
        box(353, 30, 153, 53, ["lista compartida por a", "[99, 2]"])
        for start, end in [(75, 72), (65, 62), (28, 49), (18, 39)]:
            arrow(138, start, 353, end)
    elif key == "matrices":
        split("Con repetición: una fila compartida", "Con filas construidas por separado")
        for off in [0, 264]:
            box(off + 4, 18, 65, 65, ["matrix", "[0]", "[1]", "[2]"])
        box(116, 33, 129, 38, ["fila A", "[1, 0, 0]"])
        for y in [58, 47, 36]:
            arrow(69, y, 116, y)
        for y, val in [(66, "A: [1, 0, 0]"), (38, "B: [0, 0, 0]"), (10, "C: [0, 0, 0]")]:
            box(382, y, 126, 23, val)
        arrow(333, 58, 382, 77)
        arrow(333, 47, 382, 49)
        arrow(333, 36, 382, 21)
    elif key == "profunda":
        split("Original", "Copia profunda, tras cambiar una celda")
        for off, title, vals in [(0, "original", ["B: [1, 2]", "C: [3, 4]"]),
                                  (264, "profunda", ["E: [99, 2]", "F: [3, 4]"])]:
            box(off + 4, 29, 79, 49, [title, "posición 0", "posición 1"])
            box(off + 123, 60, 120, 24, vals[0])
            box(off + 123, 17, 120, 24, vals[1])
            arrow(off + 83, 49, off + 123, 72)
            arrow(off + 83, 37, off + 123, 29)
    elif key == "tupla":
        split("Antes de append(3)", "Después: mismas referencias en T")
        for off, val in [(0, "lista A: [1, 2]"), (264, "lista A: [1, 2, 3]")]:
            box(off + 4, 29, 83, 48, ["tupla T", "posición 0", "posición 1"])
            box(off + 123, 60, 123, 24, val)
            box(off + 123, 17, 123, 24, "str: 'grupo A'")
            arrow(off + 87, 48, off + 123, 72)
            arrow(off + 87, 36, off + 123, 29)
    else:
        raise ValueError(f"Diagrama desconocido: {key}")
    return d


def all_programs():
    for unit in UNITS:
        yield "ejemplos", unit["example"]
        for exercise in unit["exercises"]:
            yield "ejercicios", exercise
    for lab in LABS.values():
        yield "practicas", lab["initial"]
        yield "soluciones", lab["solution"]


def write_programs():
    expectations = []
    for folder, program in all_programs():
        target = ROOT / folder / (program["id"] + ".py")
        target.parent.mkdir(parents=True, exist_ok=True)
        note = "Lee la consigna y escribe tu predicción en la guía antes de ejecutar."
        if folder == "soluciones":
            note = "Consulta después de intentar la práctica y justificar tu propuesta."
        target.write_text(
            '# -*- coding: utf-8 -*-\n'
            f'"""{program["id"].upper()}: {program["title"]}.\n\n{note}\n"""\n\n'
            + program["code"], encoding="utf-8"
        )
        expectations.append({"path": str(target.relative_to(ROOT)),
                             "stdout": program["expected"]})
    target = ROOT / "herramientas" / "salidas_esperadas.json"
    target.write_text(json.dumps(expectations, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def export_diagrams():
    target = ROOT / "diagramas"
    target.mkdir(exist_ok=True)
    for unit in UNITS:
        path = target / (unit["diagram"] + ".svg")
        renderSVG.drawToFile(diagram(unit["diagram"]), str(path))
        svg = path.read_text(encoding="utf-8")
        svg = svg.replace("font-family: DsaSans-Bold", "font-family: DejaVu Sans, sans-serif; font-weight: bold")
        svg = svg.replace("font-family: DsaSans", "font-family: DejaVu Sans, sans-serif")
        path.write_text(svg, encoding="utf-8")


def page_title(number, title, kind):
    return [para(kind.upper(), "kicker"), para(f"{number}  {title}", "title")]


def read_page(unit):
    example = unit["example"]
    parts = page_title(unit["number"], unit["title"], "Lectura y razonamiento")
    parts += [para("Meta: " + unit["goal"], "small"),
              para(unit["question"], "sub")]
    parts += [para(p) for p in unit["concepts"]]
    if "table" in unit:
        parts += [grid(unit["table"]["headers"], unit["table"]["rows"], font="tiny"), Spacer(1, 6)]
    parts += [heading(f"Ejemplo resuelto {example['id'].upper()}"),
              block(example["code"]), Spacer(1, 6),
              para("Salida", "kicker"), block(example["expected"], output=True),
              para(example["explanation"], "small"), diagram(unit["diagram"]),
              para("Observa: " + unit["pitfall"], "small")]
    return parts


def exercise_page(unit):
    parts = page_title(unit["number"], "Predice y explica", "Resuelve en papel")
    parts += [para("Escribe la salida antes de ejecutar. Conserva tu primera respuesta y usa cajas y flechas para justificarla. Los programas se reinician de forma independiente.", "small")]
    for exercise in unit["exercises"]:
        parts += [heading(exercise["id"].upper() + " | " + exercise["title"]),
                  block(exercise["code"]), Spacer(1, 5)]
        for n, question in enumerate(exercise["questions"], 1):
            parts.append(para(f"{n}. {question}", "small"))
        parts.append(RuledSpace(62))
    parts += [heading("Una variación"), para(unit["variation"], "small"),
              RuledSpace(38, "Predicción de la variación y motivo:")]
    return parts


def answer_page(unit):
    parts = page_title(unit["number"], "Comprueba tu razonamiento", "Respuestas razonadas | después del intento")
    parts += [para("Compara tus respuestas con las explicaciones. Si te equivocaste, conserva tu predicción inicial e identifica qué objeto o referencia interpretaste de otra manera.")]
    for exercise in unit["exercises"]:
        parts += [heading(exercise["id"].upper() + " | Salida esperada"),
                  block(exercise["expected"], output=True),
                  para(exercise["explanation"])]
    parts += [heading("La variación"), para(unit["variation_answer"]),
              heading("Antes de avanzar"), para(unit["checkpoint"]),
              para("Marca tu situación:  [ ] Puedo justificarlo.   [ ] Necesito revisar un ejemplo.", "small"),
              RuledSpace(92, "Mi corrección o explicación con mis propias palabras:")]
    if unit["number"] != "1.10":
        parts.append(para("Si la explicación aún no es clara, vuelve al diagrama del tema y sigue cada flecha desde la instrucción que produce el cambio.", "small"))
    return parts


def lab_page(lab):
    parts = page_title(lab["id"].upper(), lab["title"], "Comprueba en Python | práctica de laboratorio")
    parts += [para("Meta: " + lab["goal"], "small"),
              para(f"Archivo: `practicas/{lab['id']}.py`. Abre la carpeta `etapa_01_objetos_referencias`.", "small"),
              heading("Programa inicial: primero predice"), block(lab["initial"]["code"]),
              Spacer(1, 6)]
    for n, task in enumerate(lab["tasks"], 1):
        parts.append(para(f"{n}. {task}", "small"))
    parts += [heading("Registro de comprobación"),
              para("Puedes ampliar este registro en tu cuaderno. Cada variante se ejecuta desde el estado inicial.", "small"),
              grid(["Caso", "Predicción", "Observación y explicación"],
                   [["Inicial", "\n\n", "\n\n"],
                    ["Variante / corrección", "\n\n", "\n\n"]], widths=[95, 160, CW - 255],
                   row_heights=[29, 47, 55]),
              Spacer(1, 6),
              para("Para ejecutar: `python3 practicas/" + lab["id"] + ".py`  |  En Windows: `py practicas/" + lab["id"] + ".py`", "tiny")]
    return parts


def lab_answer_page(lab):
    parts = page_title(lab["id"].upper(), "Revisión de la práctica", "Solución de referencia | después del intento")
    for answer in lab["answers"]:
        parts.append(para(answer, "small"))
    parts += [heading(lab["solution"]["title"]), block(lab["solution"]["code"]),
              Spacer(1, 6), para("Salida", "kicker"),
              block(lab["solution"]["expected"], output=True),
              para(lab["solution"]["explanation"], "small"),
              para(f"Archivo de referencia: `soluciones/{lab['solution']['id']}.py`.", "small"),
              RuledSpace(56, "¿Qué cambié y qué evidencia demuestra que mi solución cumple la consigna?")]
    return parts


def cover():
    return [
        Spacer(1, 20),
        para("ESTRUCTURA Y ORGANIZACIÓN DE DATOS", "kicker"),
        Spacer(1, 23),
        para("Objetos y referencias en memoria", "cover"),
        para("Python | Etapa 1", "title"),
        para("Guía de aprendizaje autónomo", "sub"),
        Spacer(1, 12),
        para("Comprende qué cambia cuando ejecutas una instrucción: el estado de un objeto, una referencia o ambos. Aprende a predecir esos cambios, explicarlos y comprobarlos."),
        Spacer(1, 20),
        grid(["Lee y razona", "Comprueba y corrige"],
             [["10 temas progresivos\n20 ejercicios de predicción\n10 variaciones", "10 ejemplos resueltos\n4 prácticas de laboratorio\nRespuestas razonadas"]]),
        Spacer(1, 24),
        para("Papel primero", "sub"),
        para("Lee, predice y dibuja antes de abrir el intérprete. En las prácticas señaladas, ejecuta el código y compara el resultado con tu explicación. Conserva tus errores iniciales: te ayudan a localizar qué debes revisar."),
        Spacer(1, 20),
        RuledSpace(67, "Nombre:                                             Grupo:                      Fecha:"),
        Spacer(1, 13),
        para("Edición 1.1 | Septiembre de 2026", "small"),
        para("Formato carta, preparado para impresión en blanco y negro. Los programas del estudiante funcionan con Python 3.10 o posterior y su biblioteca estándar.", "small"),
    ]


def navigation(start_pages, lab_pages, end_pages):
    parts = [para("TU RECORRIDO", "kicker"), para("Avanza por comprensión", "title"),
             para("Sigue el orden. Avanza cuando puedas explicar el ejemplo y resolver una variación. Si una predicción falla, revisa las referencias antes de continuar."),
             grid(["Tema", "Página"], [[f"{u['number']}  {u['title']}", str(start_pages[u["number"]])] for u in UNITS], [CW - 56, 56]),
             Spacer(1, 14), heading("Momentos de ejecución"),
             grid(["Práctica", "Después de", "Página"],
                  [[f"{p['id'].upper()}  {p['title']}", p["section"], str(lab_pages[p["id"]])] for p in LABS.values()],
                  [CW - 116, 63, 53]),
             Spacer(1, 12),
             para(f"Cierre y autoevaluación: página {end_pages['closure']}. Glosario y fuentes: página {end_pages['sources']}.", "small"),
             heading("Cómo leer los diagramas"),
             para("Las cajas representan objetos o nombres, según su etiqueta. Las flechas representan referencias. A, B y C son etiquetas simbólicas, nunca direcciones reales. Los valores dentro de las cajas de listas se abrevian; el dibujo no representa posiciones físicas contiguas de memoria.", "small"),
             ]
    return parts


def method():
    return [para("ANTES DE EMPEZAR", "kicker"), para("Cómo trabajar con la guía", "title"),
            para("Para empezar, necesitas reconocer variables, índices, claves de diccionarios, ciclos sencillos y la sintaxis de una función. Aquí tienes un recordatorio para consultar mientras trabajas."),
            grid(["Acción", "Qué haces"], [
                ["1. Leer", "Estudia el concepto, el ejemplo resuelto y su diagrama."],
                ["2. Predecir", "Escribe la salida y justifica qué objeto o referencia cambia."],
                ["3. Comprobar", "En las prácticas señaladas, ejecuta y registra el resultado real."],
                ["4. Investigar", "Sigue las flechas y corrige la explicación, conservando tu predicción."],
                ["5. Modificar", "Cambia una sola condición y predice otra vez antes de ejecutar."],
            ], [86, CW - 86]),
            heading("Recordatorio de sintaxis"),
            grid(["Expresión", "Lectura"], [
                ["`datos[0]`", "Primer elemento de una lista. Los índices empiezan en 0."],
                ['`alumno["edad"]`', 'Valor asociado a la clave `"edad"` de un diccionario.'],
                ["`lista.append(x)`", "Agrega un elemento al final de la misma lista."],
                ["`lista[:]`", "Crea una copia superficial de la lista."],
                ["`def f(datos):`", "Define la función `f()` con el parámetro local `datos`."],
                ["`return resultado`", "Entrega un objeto al código que llamó a la función."],
                ["`range(3)`", "Permite recorrer los valores `0`, `1` y `2` en un ciclo."],
                ["`None`", "Objeto que representa la ausencia de un resultado útil en estos ejemplos."],
            ], [144, CW - 144], font="tiny"),
            heading("Preparación para el laboratorio"),
            para("Abre la carpeta `etapa_01_objetos_referencias`. Ejecuta cada archivo completo, desde el inicio. En macOS o Linux: `python3 ejercicios/e05.py`. En Windows: `py ejercicios/e05.py`. También puedes usar tu editor.", "small"),
            para("No se necesitan servicios en línea ni paquetes adicionales. Mantén la guía impresa abierta y utiliza el intérprete para comprobar tus predicciones. En un cuaderno interactivo, reinicia el entorno antes de cada ejemplo para evitar estados anteriores.", "small"),
            para("Compara las identidades con respuestas `True` o `False`. No necesitas memorizar números de `id()` ni direcciones de memoria.", "small")]


def analogy_page():
    a = ANALOGY
    return page_title("1.1", a["title"], "Una analogía para seguir las referencias") + [
        para(a["intro"]), para(a["labels"]),
        grid(a["table"]["headers"], a["table"]["rows"], [95, CW - 95], font="tiny"),
        heading("Asignar puede llevarnos a la misma tarjeta o a otra"),
        para(a["same"], "small"), para(a["other"], "small"),
        block(a["code"]), Spacer(1, 6),
        para("Salida: `True` y después `False`.", "small"),
        para(a["conclusion"], "small"),
    ]


def closure():
    return [para("CIERRE DE LA ETAPA", "kicker"), para("Demuestra tu comprensión", "title"),
            para("Vuelve a un ejercicio que inicialmente resolviste mal. Sin mirar su respuesta, explica ahora el recorrido de sus referencias y el objeto afectado por cada instrucción."),
            grid(["Puedo...", "Sí / Revisar"], [
                ["Distinguir objetos mutables e inmutables y explicar una reasignación.", ""],
                ["Anticipar coincidencias de identidad sin usar direcciones fijas.", ""],
                ["Separar la mutación de una lista de la reasignación de un nombre.", ""],
                ["Explicar los efectos de una función sobre el objeto recibido.", ""],
                ["Seguir referencias por varios niveles de contenedores.", ""],
                ["Construir filas independientes y comprobarlo.", ""],
                ["Elegir una copia superficial o profunda según el cambio previsto.", ""],
                ["Explicar una lista mutable dentro de una tupla inmutable.", ""],
            ], [CW - 82, 82]),
            heading("Una explicación completa contiene"),
            para("1. Los objetos relevantes y los nombres o posiciones que llegan a ellos.\n2. La instrucción que produce el cambio.\n3. El objeto o referencia que se modifica.\n4. El motivo por el que el resultado coincide o difiere de la predicción."),
            heading("Transferencia"),
            para("Elige la práctica P03 o P04. Explica qué cambiarías si el problema necesitara compartir ciertos objetos de manera intencional. Especifica cuáles compartirías y qué modificaciones serían observables desde cada referencia."),
            RuledSpace(124, "Mi explicación y mi decisión de diseño:"),
            para("Puedes necesitar varios intentos. Escribe por qué tu respuesta cambió y pide apoyo señalando la instrucción o flecha que no logras explicar. El número de aciertos por sí solo no describe tu comprensión.", "small"),
            para("Conserva la guía como referencia para las siguientes etapas del curso. Esta etapa se centra en los objetos incorporados de Python y sus referencias.", "small")]


def sources_page():
    parts = [para("CONSULTA", "kicker"), para("Glosario y fuentes", "title"),
             grid(["Término", "Significado en esta guía"], [
                 ["Objeto", "Dato con tipo, valor e identidad."],
                 ["Referencia", "Relación que permite llegar a un objeto desde un nombre o un contenedor."],
                 ["Alias", "Otro nombre o referencia que llega al mismo objeto."],
                 ["Mutación", "Cambio del estado de un objeto existente."],
                 ["Asignación", "Indicar qué objeto señala un nombre; puede ser el mismo que antes u otro."],
                 ["Reasignación", "Volver a asignar un nombre; en los ejemplos puede pasar a señalar otro objeto."],
                 ["Identidad", "Lo que distingue a un objeto concreto. Se compara con `is` y permanece mientras el objeto existe."],
                 ["Copia superficial", "Nuevo contenedor exterior que reutiliza referencias a sus elementos."],
                 ["Copia profunda", "Copia recursiva que puede conservar alias internos y reutilizar inmutables."],
             ], [105, CW - 105], font="tiny"),
             heading("Documentación para ampliar")]
    for n, (title, url, note) in enumerate(SOURCES, 1):
        parts.append(Paragraph(f'<b>{n}. <link href="{html.escape(url, quote=True)}" color="#182028">{html.escape(title)}</link></b>', STYLES["small"]))
        parts.append(para(note, "tiny"))
        parts.append(Paragraph('<link href="' + html.escape(url, quote=True) + '">' + html.escape(url) + '</link>', STYLES["tiny"]))
    parts += [Spacer(1, 5),
              para("Selección y adaptación: los casos de listas, funciones, matrices, copias y equipos parten del material de referencia aportado para este curso. Las explicaciones, la progresión, los ejercicios adicionales y los diagramas se elaboraron para esta guía. Las referencias externas son de consulta; no necesitas abrirlas para realizar las actividades.", "tiny")]
    return parts


def pages():
    # First reserve navigation; page numbers are computed from the actual sequence.
    result = [("Portada", cover()), ("Recorrido", []), ("Cómo trabajar", method())]
    start_pages, lab_pages = {}, {}
    for unit in UNITS:
        start_pages[unit["number"]] = len(result) + 1
        result.append((unit["number"] + " " + unit["title"], read_page(unit)))
        if unit["number"] == "1.1":
            result.append(("1.1 Tarjetas, etiquetas y flechas", analogy_page()))
        result.append((unit["number"] + " Ejercicios", exercise_page(unit)))
        if "lab" in unit:
            lab = LABS[unit["lab"]]
            lab_pages[lab["id"]] = len(result) + 1
            result.append((lab["id"].upper() + " Práctica", lab_page(lab)))
        result.append((unit["number"] + " Respuestas", answer_page(unit)))
        if "lab" in unit:
            result.append((unit["lab"].upper() + " Revisión", lab_answer_page(LABS[unit["lab"]])))
    end_pages = {"closure": len(result) + 1, "sources": len(result) + 2}
    result += [("Cierre", closure()), ("Glosario y fuentes", sources_page())]
    result[1] = ("Recorrido", navigation(start_pages, lab_pages, end_pages))
    return result, start_pages, lab_pages


def build_pdf():
    PDF_PATH.parent.mkdir(parents=True, exist_ok=True)
    document_pages, start_pages, lab_pages = pages()
    c = canvas.Canvas(str(PDF_PATH), pagesize=letter, pageCompression=1, invariant=1)
    c.setTitle("Objetos y referencias en memoria - Python - Etapa 1")
    c.setAuthor("Curso Estructura y Organización de Datos")
    c.setSubject("Guía imprimible con ejercicios, prácticas y respuestas razonadas")
    c.setCreator("learning_dsa | herramientas/generar_material.py")
    log = []
    overflows = []
    for n, (title, content) in enumerate(document_pages, 1):
        if n > 1:
            c.setFont("DsaSans", 8)
            c.setFillColor(MUTED)
            c.drawString(LEFT, HEIGHT - 29, "ESTRUCTURA Y ORGANIZACIÓN DE DATOS")
            c.drawRightString(WIDTH - RIGHT, HEIGHT - 29, "ETAPA 1 | PYTHON")
            c.setStrokeColor(RULE)
            c.setLineWidth(0.4)
            c.line(LEFT, HEIGHT - 36, WIDTH - RIGHT, HEIGHT - 36)
        c.setFont("DsaSans", 8)
        c.setFillColor(MUTED)
        c.drawString(LEFT, 25, "Objetos y referencias en memoria")
        c.drawRightString(WIDTH - RIGHT, 25, f"{n} / {len(document_pages)}")
        key = "page" + str(n)
        c.bookmarkPage(key)
        c.addOutlineEntry(title, key, level=0, closed=False)
        frame = Frame(LEFT, BOTTOM, CW, CH, leftPadding=0, rightPadding=0,
                      topPadding=0, bottomPadding=0, showBoundary=0)
        remaining = list(content)
        frame.addFromList(remaining, c)
        if remaining:
            consumed = len(content) - len(remaining)
            overflows.append(f"Página {n} ({title}): {consumed}/{len(content)} elementos; siguiente: {type(remaining[0]).__name__}.")
        log.append({"page": n, "title": title, "remaining_height": round(frame._y - BOTTOM, 1)})
        c.showPage()
    c.save()
    if overflows:
        raise RuntimeError("Hay páginas con contenido excedente:\n" + "\n".join(overflows))
    (ROOT / "herramientas" / "mapa_paginas.json").write_text(
        json.dumps({"total_pages": len(document_pages), "sections": start_pages,
                    "labs": lab_pages, "pages": log}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return len(document_pages)


def main():
    write_programs()
    export_diagrams()
    n = build_pdf()
    from generar_web import build_web
    build_web(SOURCE)
    print(f"Generados: {n} páginas, {len(list(all_programs()))} programas y {len(UNITS)} diagramas.")
    print(PDF_PATH)


if __name__ == "__main__":
    main()
