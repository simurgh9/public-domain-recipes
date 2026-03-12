Act as though you are returning an API call that converts a recipe written in a markdown file into a JSON object. For example, this recipe,

```markdown
filename: aelplermagronen.md
---
title: "Älplermagronen (Alpine macaroni)"
date: 2021-03-11
tags: ['swiss', 'pork', 'potato', 'pasta']
author: alexander-bocken
---

![Älplermagronen](/pix/aelplermagronen.webp)

A swiss favorite, _Älplermagronen_ combines pretty much everything you have at your disposal in your alpine chalet.
It's the definition of comfort food for the Swiss.

- 🍳 Cook time: ~30 minutes
- 🍽️  Servings: 4

## Ingredients

- ~150g (1/3 lb) bacon cubes
- 3 onions (medium size)
- 400g (15 oz) potatoes (firm/waxy)
- 1 - 2L (1/4 - 1/2 gal) milk
- 400g (15 oz) macaroni (dry weight)
- ~150g (1/3 lb) medium soft cheese. Appenzeller works best. Gruyère would be my go-to alternative.
- a jar of apple sauce

Feel free to vary these amounts, it's not like this is anything strict.

## Directions

1. Fry bacon cubes in pot (this pot will be used for everything so choose an appropriately large one).
2. Cut onions into half-rings and let them sweat in the same pot. Add some butter if your bacon was not fatty enough.
3. Peel potatoes and cut them into ~1 cm/half inch cubes.
4. When the onions have become sufficiently cooked, add potatoes.
5. Top everything with milk and let the potatoes cook for about 10 minutes.
7. Add macaroni and the remaining milk to cover everything. Most of the milk will be absorbed by the macaroni.
8. Shred your cheese.
9. A minute or two before the macaroni are done, add the shredded cheese into the pot. It should appear a bit too runny in the pot. While cooling it will increase in viscosity quite a bit. If the final texture is not creamy enough, it is most likely due to using the wrong cheese.
10. Season to taste. (Needs quite a bit of salt). Nutmeg also works well here.
11. Serve with apple sauce. Should be eaten together, not as a dessert.
```

Should be converted to:

```json
{
    "filename": "aelplermagronen.md",
    "date": "2021-03-11",
    "author": "alexander-bocken",
    "title": "Älplermagronen (Alpine macaroni)",
    "tags": ["swiss", "pork", "potato", "pasta"],
    "image_name": "Älplermagronen",
    "image_path": "/pix/aelplermagronen.webp",
    "prep_time": null,
    "cook_time": "30",
    "servings": "4",
    "ingredients": [
        {
            "literal": "~150g (1/3 lb) bacon cubes",
            "base": "bacon cubes",
            "amount": [{"quantity": "150", "unit": "gram"}, {"quantity": "1/3", "unit": "pound"}],
            "lemma": "bacon"
        },
        {
            "literal": "3 onions (medium size)",
            "base": "medium size onions",
            "amount": [{"quantity": "3", "unit": "count"}],
            "lemma": "onion"
        },
        {
            "literal": "400g (15 oz) potatoes (firm/waxy)",
            "base": "firm or waxy potatoes",
            "amount": [{"quantity": "400", "unit": "gram"}, {"quantity": "15", "unit": "ounce"}],
            "lemma": "potato"
        },
        {
            "literal": "1 - 2L (1/4 - 1/2 gal) milk",
            "base": "milk",
            "amount": [{"quantity": ["1", "2"], "unit": "L"}, {"quantity": ["1/4", "1/2"], "unit": "gal"}],
            "lemma": "milk"
        },
        {
            "literal": "400g (15 oz) macaroni (dry weight)",
            "base": "macaroni",
            "amount": [{"quantity": "400", "unit": "gram"}, {"quantity": "15", "unit": "ounce"}],
            "lemma": "macaroni",
            "comment": "weigh when dry"
        },
        {
            "literal": "~150g (1/3 lb) medium soft cheese. Appenzeller works best. Gruyère would be my go-to alternative.",
            "base": "medium soft cheese preferably appenzeller or alternatively gruyère",
            "amount": [{"quantity": "150", "unit": "gram"}, {"quantity": "1/3", "unit": "pound"}],
            "lemma": "cheese"
        },
        {
            "literal": "a jar of apple sauce",
            "base": "jar of apple sauce",
            "amount": [{"quantity": "1", "unit": "count"}],
            "lemma": "apple sauce"
        }
    ],
    "directions": [
        "Fry bacon cubes in pot (this pot will be used for everything so choose an appropriately large one).",
        "Cut onions into half-rings and let them sweat in the same pot. Add some butter if your bacon was not fatty enough.",
        "Peel potatoes and cut them into ~1 cm/half inch cubes.",
        "When the onions have become sufficiently cooked, add potatoes.",
        "Top everything with milk and let the potatoes cook for about 10 minutes.",
        "Add macaroni and the remaining milk to cover everything. Most of the milk will be absorbed by the macaroni.",
        "Shred your cheese.",
        "A minute or two before the macaroni are done, add the shredded cheese into the pot. It should appear a bit too runny in the pot. While cooling it will increase in viscosity quite a bit. If the final texture is not creamy enough, it is most likely due to using the wrong cheese.",
        "Season to taste. (Needs quite a bit of salt). Nutmeg also works well here.",
        "Serve with apple sauce. Should be eaten together, not as a dessert."
    ]
    "comments": [
        "A swiss favorite, _Älplermagronen_ combines pretty much everything you have at your disposal in your alpine chalet. It's the definition of comfort food for the Swiss.",
        "Feel free to vary these amounts, it's not like this is anything strict."
    ]
},

```

Make sure if the time is given in hours and minutes for example, "1 hour" or "1 hour 10 minutes" then you convert it to minutes with `"cook_time": "60",` or `"cook_time": "70",` respectively.

If a certain ingredient is listed without any quantity then use `null` and "to taste" for the unit, i.e., `{"quantity": null, "unit": "to taste"}`.

In general use `null` for missing fields.

Convert the following,

```markdown
Þ
```

and return only the JSON object. Don't wrap it with backticks, e.g., ```json ... ```.
