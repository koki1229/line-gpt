import openai
import os
from dotenv import load_dotenv

# 環境に追加
load_dotenv('.env')

openai.api_key = os.environ.get("OPEN_AI_KEY")

body = input("質問を入力してください: ")
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": body },
    ]
)
print(response["choices"][0]["message"]["content"])