#Imports
import requests
from bs4 import BeautifulSoup
import openai

# Vraag de gebruiker om een URL
url = input("Voer de URL in van de pagina waar je een samenvatting van wilt: ")
# Haal de inhoud van de pagina op
response = requests.get(url)
# Parse de HTML inhoud
soup = BeautifulSoup(response.text, 'html.parser')

# Alle tekst op de pagina nemen
text = soup.get_text()

# API credentials
client = openai.OpenAI(
    api_key="123123",
    base_url="https://api.algion.dev/v1"
)

#Stuur HTTP verzoek naar API om samenvatting te genereren door AI
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "user", "content": "Ik wil een mooie gestructureerde samenvatting van de volgende tekst: " + text}
    ]
)

print(response.choices[0].message.content)