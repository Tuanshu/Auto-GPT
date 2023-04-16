import json
import os

import openai
import requests

# Set your API key
api_key = "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"

# Test the API key by sending a simple request
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}",
}

data = {
    "model": "gpt-3.5-turbo",
    "messages": [{"role": "user", "content": "Say this is a test!"}],
    "temperature": 0.7,
}

response = requests.post(
    "https://api.openai.com/v1/chat/completions", headers=headers, data=json.dumps(data)
)

if response.status_code == 200:
    result = response.json()
    print("API key is working!")
    print("Result:")
    print(result["choices"][0]["message"]["content"])
else:
    print("Error:", response.status_code, response.text)

# try:
#     print(openai.Model.list())
# except Exception as e:
#     print(f"Error: {e}")
