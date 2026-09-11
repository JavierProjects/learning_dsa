"""Publica la misma fuente en una web estática que también abre sin conexión."""

import hashlib
import json
from pathlib import Path
import runpy
import shutil

ROOT = Path(__file__).resolve().parents[1]
WEB = ROOT.parent / "dist"
CONFIG = runpy.run_path(str(ROOT / "fuentes" / "casos_web.py"))


def options_for(program_id, case, index, other_cases):
    answer = case['expected'].rstrip('\n').split('\n')[index]
    if answer in ('True', 'False'):
        return ['True', 'False']
    candidates = [answer]
    for other in other_cases:
        lines = other['expected'].rstrip('\n').split('\n')
        if index < len(lines):
            candidates.append(lines[index])
    pool = CONFIG['DISTRACTORES'].get(program_id, [])
    # Keep text, numeric and list distractors relevant to the output line.
    def kind(s):
        if s.startswith('['): return 'list'
        if s.startswith('{'): return 'dict'
        if s.lstrip('-').isdigit(): return 'number'
        return 'text'
    candidates += [p for p in pool if kind(p) == kind(answer)]
    candidates += ['None', 'Se produce un error antes de imprimir']
    unique = list(dict.fromkeys(candidates))[:4]
    key = program_id + case['key'] + str(index)
    return sorted(unique, key=lambda value: hashlib.sha256((key + value).encode()).hexdigest())


def build_web(source):
    WEB.mkdir(exist_ok=True)
    units = []
    for unit in source['UNIDADES']:
        item = dict(unit)
        exercises = []
        for exercise in unit['exercises']:
            cases = CONFIG['cases_for'](exercise)
            for case in cases:
                case['prompts'] = [case.pop('prompt')]
                case['options'] = [options_for(exercise['id'], case, i, cases)
                                   for i, _ in enumerate(case['expected'].rstrip('\n').split('\n'))]
            exercises.append({'id': exercise['id'].upper(), 'title': exercise['title'], 'cases': cases})
        item['exercises'] = exercises
        units.append(item)
    labs = []
    for lab in source['PRACTICAS']:
        initial = lab['initial']
        case = {'key': 'inicial', 'label': 'Programa inicial',
                'code': initial['code'], 'expected': initial['expected'], 'change': '',
                'prompts': [
                    'Describe qué objetos se comparten en el programa inicial y explica sus salidas.',
                    'Escribe tu propuesta de código para resolver la práctica. Incluye las variantes solicitadas.',
                    'Explica cómo comprobarías tu propuesta y qué resultados esperas. Si ya ejecutaste el código, registra lo que observaste.',
                ], 'answer': initial['explanation'], 'review': lab['answers'],
                'solution': lab['solution']}
        case['options'] = []
        other = {'expected': lab['solution']['expected']}
        for i, _ in enumerate(initial['expected'].rstrip('\n').split('\n')):
            case['options'].append(options_for(lab['id'], case, i, [case, other]))
        labs.append({'id': lab['id'].upper(), 'section': lab['section'], 'title': lab['title'],
                     'goal': lab['goal'], 'tasks': lab['tasks'], 'cases': [case]})
    payload = {'edition': '1.1', 'units': units, 'labs': labs,
               'analogy': source['ANALOGIA'], 'sources': source['FUENTES']}
    serialized = json.dumps(payload, ensure_ascii=False, indent=2).replace('</', '<\\/')
    (WEB / 'contenido.js').write_text('window.DSA = ' + serialized + ';\n', encoding='utf-8')
    shutil.copyfile(ROOT / 'output/pdf/guia_objetos_referencias.pdf', WEB / 'guia_objetos_referencias.pdf')
    target = WEB / 'diagramas'
    target.mkdir(exist_ok=True)
    for svg in (ROOT / 'diagramas').glob('*.svg'):
        shutil.copyfile(svg, target / svg.name)
    print('Web generada: 20 ejercicios, 20 variaciones y 4 prácticas.')


if __name__ == '__main__':
    build_web(runpy.run_path(str(ROOT / 'fuentes/contenido.py')))
