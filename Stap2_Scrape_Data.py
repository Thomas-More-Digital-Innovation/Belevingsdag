#Imports
import requests
from bs4 import BeautifulSoup

# Vraag de gebruiker om een URL
url = input("Voer de URL in van de pagina die je wilt scrapen: ")
# Haal de inhoud van de pagina op
response = requests.get(url)
# Parse de HTML inhoud
soup = BeautifulSoup(response.text, 'html.parser')

# Alle tekst op de pagina
text = soup.get_text()