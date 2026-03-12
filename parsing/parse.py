from pathlib import Path
from openai import OpenAI


def generate_prompt(recipe):
    thorn = chr(222)
    with open('prompt.md', 'r') as fl:
        return fl.read().replace(thorn, recipe)


def to_json(prompt, client):
    completion = client.chat.completions.create(
        model='gpt-oss',
        messages=[
            {
                'role':
                'system',
                'content': 'Act as though you are returning an API call that converts a recipe written in a markdown file into a JSON object.'
            },
            {
                'role': 'user',
                'content': prompt,
            },
        ],
    )
    return completion.choices[0].message.content


base = '../content/'
filenames = []
for i, fl in enumerate(Path(base).iterdir()):
    if not fl.is_file() or fl.name == '_index.md':
        continue
    filenames.append(fl.name)

filenames.sort()
prompts = []
for filename in filenames:
    with open(f'{base}/{filename}', 'r') as fl:
        appendage = f'filename: {filename}\n' + fl.read()
        prompts.append(generate_prompt(appendage))

with open('key', 'r') as fl:
    key, api = fl.read().split()

client = OpenAI(api_key=key, base_url=api)
# prompts = prompts[:3]
total = len(prompts)
with open('data.json', 'a') as fl:
    for i, prompt in enumerate(prompts, 1):
        print(f'{i}/{total}', end='\r')
        json = to_json(prompt, client)
        fl.write(json + ',\n')
        fl.flush()
