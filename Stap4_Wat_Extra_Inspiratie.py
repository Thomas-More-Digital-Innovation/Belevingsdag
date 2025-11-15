# Imports
import requests
from bs4 import BeautifulSoup
import openai
from fpdf import FPDF
from gtts import gTTS

# OpenAI client instellen
client = openai.OpenAI(
    api_key="123123",
    base_url="https://api.algion.dev/v1"
)

# URL van het nieuws
url = "https://www.techtarget.com/searchapparchitecture/definition/object-oriented-programming-OOP"

# Haal website op
response = requests.get(url)
if response.status_code != 200:
    print("Kan geen informatie ophalen van de website!")
    exit()

# Parse HTML + haal tekst op
soup = BeautifulSoup(response.content, 'html.parser')
data = soup.text

#laat AI een samenvatting maken
prompt = "Maak een samenvatting van ongeveer 3 minuten leeswerk. Ik wil de samenvatting in het Nederlands ontvangen. Ik wil enkel de samenvatting en geen extra informatie puur samenvatting teruggeven : " + data
response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "user", "content": prompt}
    ]
)

samenvatting = response.choices[0].message.content

# Print samenvatting
print("Samenvatting gemaakt")

# Maak PDF
pdf = FPDF()
pdf.add_page()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.set_font("Arial", size=12)
pdf.multi_cell(0, 10, samenvatting.encode('latin-1', 'replace').decode('latin-1'))
pdf.output("samenvatting_nieuws.pdf")
print("PDF opgeslagen als samenvatting_nieuws.pdf")

# --- Audio genereren (gewoon tekst to speech, dus letterlijk overnemen) ---
tts = gTTS(samenvatting, lang="nl")
tts.save("samenvatting_nieuws.mp3")
print("Audio opgeslagen als samenvatting_nieuws.mp3")