from pathlib import Path

base = '../data/authors/'
info = []
for i, fl in enumerate(Path(base).iterdir()):
    if not fl.is_file() or fl.name == '_index.md':
        continue
    filename = fl.name
    key = filename.split('.')[0]
    with open(f'{base}{filename}', 'r') as fl:
        info += [f'"{key}": {fl.read().strip()}']

with open('authors.json.new', 'w') as fl:
    fl.write('{\n' + ',\n'.join(info) + '\n}')
