import sys
from openai import OpenAI

context_file_path = sys.argv[1]
with open(context_file_path, 'r') as file:
    context = file.read()

prompt = """Write code that adds two numbers and
multiplies the result by a third number. Respond with the code only.
Reuse existing code where appropriate. Existing code: """ + context

print(prompt)

client = OpenAI()
completion = client.chat.completions.create(
    model="gpt-4o-mini",
    store=True,
    messages=[
        {"role": "user",
         "content": prompt}
    ]
)

print(completion.choices[0].message)
