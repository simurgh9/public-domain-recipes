import json
import numpy as np
from pprint import pprint
from matplotlib import pyplot as plt

# data read'aroo
with open('parsed.json', 'r') as fl:
    data = json.load(fl)

# pprint(data[np.random.randint(0, len(data))], sort_dicts=False)

# exploring ingredients
ingredients = []
for recipe in data:
    ingredients += [ingredient['lemma'] for ingredient in recipe['ingredients']]

unique, counts = np.unique(ingredients, return_counts=True)
sort_idx = np.argsort(counts)[::-1]
counts = counts[sort_idx]
unique = unique[sort_idx]

# for count, ingredient in zip(unique, counts[:10]):
#     print(count, ingredient)

# plt.xlabel(r'$i^\text{th}$ ingredient per occurrence')
# plt.ylabel(r'Number of occurences')
# plt.plot(counts)
# plt.tight_layout()
# plt.show()

cut_off = counts > 10
counts = counts[cut_off]
unique = unique[cut_off]

plt.figure(figsize=(16, 12))
plt.bar_label(plt.bar(unique, counts, color='black'), rotation=90, padding=5)
plt.xlabel(r'Ingredient')
plt.ylabel(r'Number of occurences')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

# exploring tags
tags = []
for recipe in data:
    tags += recipe['tags']

unique, counts = np.unique(tags, return_counts=True)
sort_idx = np.argsort(counts)[::-1]
counts = counts[sort_idx]
unique = unique[sort_idx]

# for count, ingredient in zip(unique, counts[:10]):
#     print(count, ingredient)

# plt.xlabel(r'$i^\text{th}$ tag per occurrence')
# plt.ylabel(r'Number of occurences')
# plt.plot(counts)
# plt.tight_layout()
# plt.show()

cut_off = counts > 5
counts = counts[cut_off]
unique = unique[cut_off]

plt.figure(figsize=(16, 12))
plt.bar_label(plt.bar(unique, counts, color='black'), rotation=90, padding=5)
plt.xlabel(r'Tags')
plt.ylabel(r'Number of occurences')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()
