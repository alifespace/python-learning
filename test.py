from openai import OpenAI

client = OpenAI(api_key="sk-94c3efc401af4b87be01a4ecce532bcc", base_url="https://api.deepseek.com")

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "如何做炸酱面"},
    ],
    stream=False
)

print(response.choices[0].message.content)
