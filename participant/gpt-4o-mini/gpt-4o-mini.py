import sys
import math
from openai import OpenAI

context_file_path = sys.argv[1]
prompt_file_path = sys.argv[2]

def truncate_prompt_max_tokens(prompt, max_tokens):
    # Estimate of max tokens given how chatgpt defines tokens
    # See https://help.openai.com/en/articles/4936856-what-are-tokens-and-how-to-count-them
    est_max_tokens = math.floor(max_tokens * 0.68)
    tokens = prompt.split(" ")
    print(len(tokens))
    if len(tokens) <= est_max_tokens:
        return prompt
    return ' '.join(tokens[:est_max_tokens]) + '...'

with open(context_file_path, 'r') as file:
    context = file.read()

with open(prompt_file_path, 'r') as file:
    prompt = file.read()

prompt_context = truncate_prompt_max_tokens(prompt + context, 128000)

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
