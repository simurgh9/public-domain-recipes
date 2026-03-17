import json
import csv
import numpy as np

with open('version/parsed_v3.json', 'r') as fl:
    data = json.load(fl)

with open('unit_map.csv', 'r') as fl:
    unit_map = dict(csv.reader(fl))

units = []
for recipe in data:
    for ingredient in recipe['ingredients']:
        for amount in ingredient['amount']:
            if amount['unit'] not in unit_map:
                raise ValueError(f'{amount["unit"]} has no unit mapping.')
            amount['unit'] = unit_map[amount['unit']]
            units.append(amount['unit'])

unique, counts = np.unique(units, return_counts=True)
sort_idx = np.argsort(counts)[::-1]
counts = counts[sort_idx]
unique = unique[sort_idx]

# for unit, freq in zip(unique, counts):
#     print(unit)
    
print(f'\nThere are a total of {len(unique)} units.')

if input('Write Out? <y/n>  ') == 'y':
    with open('version/parsed_v?.json', 'w') as fl:
        fl.write(json.dumps(data, indent=2))
