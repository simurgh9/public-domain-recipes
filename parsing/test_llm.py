from openai import OpenAI

with open('key', 'r') as fl:
    key, api = fl.read().split()

client = OpenAI(api_key=key, base_url=api)

completion = client.chat.completions.create(
    model='gpt-oss',
    messages=[
        {
            'role': 'system',
            'content': 'Talk like a politician.'
        },
        {
            'role': 'user',
            'content': '2+2=?',
        },
    ],
)

print(completion.choices[0].message.content)
