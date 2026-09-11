"""Comprueba las salidas de la web, la fuente común y sus archivos locales."""

from html.parser import HTMLParser
import json
from pathlib import Path
import re
import runpy
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
WEB = ROOT.parent / 'dist'


def main():
    source = runpy.run_path(str(ROOT / 'fuentes/contenido.py'))
    config = runpy.run_path(str(ROOT / 'fuentes/casos_web.py'))
    raw = (WEB / 'contenido.js').read_text()
    payload = json.loads(raw.removeprefix('window.DSA = ').rstrip().removesuffix(';').replace('<\\/', '</'))
    assert len(payload['units']) == 10 and len(payload['labs']) == 4
    count = 0
    for unit, rendered in zip(source['UNIDADES'], payload['units']):
        for key in ('number', 'title', 'goal', 'question', 'concepts', 'pitfall', 'checkpoint'):
            assert unit[key] == rendered[key], (unit['number'], key)
        for exercise, web_exercise in zip(unit['exercises'], rendered['exercises']):
            assert web_exercise['id'] == exercise['id'].upper()
            declared = config['cases_for'](exercise)
            for expected_case, case in zip(declared, web_exercise['cases']):
                assert case['code'] == expected_case['code']
                assert case['expected'] == expected_case['expected']
                check_run(case['code'], case['expected'], web_exercise['id'] + ':' + case['key'])
                count += 1
                check_options(case)
    for lab, rendered in zip(source['PRACTICAS'], payload['labs']):
        case = rendered['cases'][0]
        assert case['code'] == lab['initial']['code']
        assert case['solution'] == lab['solution']
        assert case['review'] == lab['answers']
        check_run(case['code'], case['expected'], rendered['id'])
        check_options(case)
        assert len(case['prompts']) == 3
        count += 1
    assert payload['analogy'] == source['ANALOGIA']
    check_run(payload['analogy']['code'], payload['analogy']['expected'], 'Analogía')
    assert (WEB / 'guia_objetos_referencias.pdf').read_bytes() == (ROOT / 'output/pdf/guia_objetos_referencias.pdf').read_bytes()
    for unit in source['UNIDADES']:
        name = unit['diagram'] + '.svg'
        assert (WEB / 'diagramas' / name).read_bytes() == (ROOT / 'diagramas' / name).read_bytes()
    parser = AssetParser()
    parser.feed((WEB / 'index.html').read_text())
    for ref in parser.references:
        if not ref.startswith(('http:', 'https:', 'data:', '#')):
            assert (WEB / ref).is_file(), f'Falta el archivo local {ref}'
    assert not (ROOT / 'guia_objetos_referencias.md').exists()
    for path in (ROOT.parent / 'README.md', ROOT / 'README.md'):
        assert 'guia_objetos_referencias.md)' not in path.read_text()
    # Program references in prose use uppercase; paths and internal IDs are excluded.
    for unit in source['UNIDADES']:
        texts = [unit[key] for key in ('question', 'pitfall', 'variation', 'variation_answer', 'checkpoint')]
        texts += unit['concepts']
        for p in [unit['example'], *unit['exercises']]:
            texts += [p['explanation'], *p['questions']]
        assert not any(re.search(r'\b[edps]\d{2}\b', text) for text in texts), unit['number']
    print(f'Correcto: {count} casos web y la analogía ejecutados; opciones, fuentes, PDF y recursos sincronizados.')


def check_run(code, expected, label):
    run = subprocess.run([sys.executable, '-c', code], capture_output=True, text=True, timeout=10)
    assert run.returncode == 0 and run.stderr == '' and run.stdout == expected, (label, run.stdout, expected, run.stderr)


def check_options(case):
    lines = case['expected'].rstrip('\n').split('\n')
    assert len(case['options']) == len(lines)
    for line, options in zip(lines, case['options']):
        assert len(options) >= 2 and len(options) == len(set(options)) and options.count(line) == 1
    assert case['prompts'] and all(p.strip() for p in case['prompts'])


class AssetParser(HTMLParser):
    references = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag in ('script', 'img') and attrs.get('src'):
            self.references.append(attrs['src'])
        if tag == 'link' and attrs.get('href'):
            self.references.append(attrs['href'])


if __name__ == '__main__':
    main()
