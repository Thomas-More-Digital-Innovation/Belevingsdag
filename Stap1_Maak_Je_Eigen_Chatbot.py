#Imports
from openai import OpenAI

# API credentials
client = OpenAI(
    api_key="ZET_HIER_JE_GROQ_API_SLEUTEL",
    base_url="https://api.groq.com/openai/v1"
)

# Vraag de gebruiker om een vraag
vraag = input("Wat wil je weten? ")

#Stuur HTTP verzoek naar API om antwoord te genereren door AI
response = client.responses.create(
            model="openai/gpt-oss-20b",
            input=vraag,
        )

#Geef het antwoord van API (de AI chatbot) weer
print(response.output_text)
