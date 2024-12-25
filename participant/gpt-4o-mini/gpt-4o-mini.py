import sys
from openai import OpenAI

context_file_path = sys.argv[1]
prompt_file_path = sys.argv[2]

with open(context_file_path, 'r') as file:
    context = file.read()

with open(prompt_file_path, 'r') as file:
    prompt = file.read()

prompt_context = prompt + context

client = OpenAI()
completion = client.chat.completions.create(
    model="gpt-4o-mini",
    store=True,
    messages=[
        {"role": "user",
         "content": prompt_context}
    ]
)

print(completion.choices[0].message)
