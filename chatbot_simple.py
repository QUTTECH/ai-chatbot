
# importing required libaries
from openai import OpenAI

# 1. Initialize OpenRouter client
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="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",
)

# 2. Call the model with a hardcoded message
response = client.chat.completions.create(
    model="nvidia/nemotron-3-super-120b-a12b:free",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is 2+2 ?"}
    ]
)

# 3. Print the result
print(response.choices[0].message.content)


