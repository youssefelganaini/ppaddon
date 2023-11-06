import openai

openai.api_key = open("key.txt", "r").read()

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages= [
        {"role": "user", "content": "Wer bist du?"}
    ]
)

print(response["choices"][0]["message"]["content"])