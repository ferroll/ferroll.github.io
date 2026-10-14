#!/usr/bin/env python3
"""Checks that every translation has the same shape and placeholders as en.py."""
import importlib.util, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
PH = re.compile(r'\{(IG|SUPPORT|IOS|AND|EN)\}')


def load(name):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, 'strings', name + '.py'))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m.S


def walk(a, b, path, errs):
    if isinstance(a, dict):
        if set(a) != set(b): errs.append(f'{path}: keys {sorted(set(a) ^ set(b))}')
        for k in a:
            if k in b: walk(a[k], b[k], f'{path}.{k}', errs)
    elif isinstance(a, (list, tuple)):
        if not isinstance(b, (list, tuple)) or len(a) != len(b): errs.append(f'{path}: length {len(a)} vs {len(b) if isinstance(b, (list, tuple)) else type(b).__name__}')
        else:
            for i, (x, y) in enumerate(zip(a, b)): walk(x, y, f'{path}[{i}]', errs)
    elif isinstance(a, str):
        if not isinstance(b, str): errs.append(f'{path}: not a string'); return
        if path.endswith('translation_note'): return
        if sorted(PH.findall(a)) != sorted(PH.findall(b)): errs.append(f'{path}: placeholders {PH.findall(a)} vs {PH.findall(b)}')
        if a.count('<a ') != b.count('<a ') or a.count('<strong>') != b.count('<strong>'):
            errs.append(f'{path}: markup differs (<a> {a.count("<a ")}/{b.count("<a ")}, <strong> {a.count("<strong>")}/{b.count("<strong>")})')
    elif a is None and b is not None and not path.endswith('translation_note'):
        errs.append(f'{path}: expected None')


en = load('en'); bad = 0
for f in sorted(os.listdir(os.path.join(HERE, 'strings'))):
    name = f[:-3]
    if not f.endswith('.py') or name == 'en': continue
    errs = []; walk(en, load(name), name, errs)
    print(f'{name:8} ' + ('OK' if not errs else f'{len(errs)} problems'))
    for e in errs[:15]: print('   ', e)
    bad += len(errs)
sys.exit(1 if bad else 0)
