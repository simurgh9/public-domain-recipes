import json
import numpy as np
from textwrap import fill


def rgb_print(text, r=240, g=128, b=128):
    return print(f'\x1B[38;2;{r};{g};{b}m{text}\x1B[m')


def print_recipe(recipe, idx):
    keys = {
        'title': 'Title',
        'author': 'Author',
        'prep_time': 'Prep. Time (min.)',
        'cook_time': 'Cook Time (min.)',
        'servings': 'Servings',
        'date': 'Date'
    }

    rgb_print('~ ABOUT')
    for k in keys:
        if recipe[k] is not None:
            print(f'  {keys[k]:18s} {recipe[k]}')

    print()
    rgb_print('~ INGREDIENTS')
    width = max([len(e['base']) for e in recipe['ingredients']])

    for i, e in enumerate(recipe['ingredients'], 1):
        quantity = e['amount'][0]['quantity']
        quantity = '' if quantity == None else quantity
        quantity = '--'.join(quantity) if type(quantity) is list else quantity
        unit = e['amount'][0]['unit'].lower()
        print(f'{i:3}. {e["base"]:{width}s} {quantity:>7} {unit}')

    print()
    rgb_print('~ DIRECTIONS')
    for i, e in enumerate(recipe['directions'], 1):
        suffix = f'{i:>3}. '
        print(
            fill(e,
                 width=70,
                 initial_indent=suffix,
                 subsequent_indent=(' ' * len(suffix))))

    if recipe['comments']:
        print()
        rgb_print('~ COMMENTS')
        for e in recipe['comments']:
            print(
                fill(e,
                     width=70,
                     initial_indent=(' ' * len(suffix)),
                     subsequent_indent=(' ' * len(suffix))))

    if recipe['tags']:
        print()
        rgb_print('~ TAGS')
        print(
            fill(', '.join(['#' + t.lower() for t in recipe['tags']]),
                 width=70,
                 initial_indent=(' ' * len(suffix)),
                 subsequent_indent=(' ' * len(suffix))))

    print()
    rgb_print(f'~ INDEX')
    print(f'     {idx}')


with open('parsed.json', 'r') as fl:
    data = json.load(fl)

while (i := input('>>> ')) != 'q':
    print_recipe(data[int(i)], int(i))
