#Imports
import openai

# API credentials
client = openai.OpenAI(
    api_key="123123",
    base_url="https://api.algion.dev/v1"
)

# Vraag de gebruiker om een vraag
vraag = input("Wat wil je weten? ")

#Stuur HTTP verzoek naar API om antwoord te genereren door AI
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "user", "content": vraag}
    ]
)

#Geef het antwoord van API (de AI chatbot) weer
print(response.choices[0].message.content)