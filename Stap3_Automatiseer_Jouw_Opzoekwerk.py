#Imports
import requests
from bs4 import BeautifulSoup
from openai import OpenAI

# Vraag de gebruiker om een URL
url = input("Voer de URL in van de pagina waar je een samenvatting van wilt: ")
# Haal de inhoud van de pagina op
response = requests.get(url)
# Parse de HTML inhoud
soup = BeautifulSoup(response.text, 'html.parser')

# Alle tekst op de pagina nemen
text = soup.get_text()

# API credentials
client = OpenAI(
    api_key="ZET_HIER_JE_GROQ_API_SLEUTEL",
    base_url="https://api.groq.com/openai/v1"
)

# Stuur HTTP verzoek naar API om samenvatting te genereren door AI
response = client.responses.create(
            model="openai/gpt-oss-20b",
            input="Ik wil een mooie gestructureerde samenvatting van de volgende tekst: " + text,
        )

# Toon de samenvatting van de AI
print(response.output_text)
