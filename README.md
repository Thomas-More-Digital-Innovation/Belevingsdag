# Belevingsdag AI

In deze repository vindt u alles voor de **belevingsdag** voor het gedeelte **AI**.

## Wat moet je gaan maken?

Je gaat beginnen met het maken van je eigen **AI-chatbot** met Python.  
Daarna ga je de **inhoud van een website lezen** met Python.  
Als laatste stap ga je jouw **eigen zoekopdracht automatiseren**.  

Vanaf daar ben je vrij om een **AI-automatisering** te maken met Python die jij leuk vindt.

## Tip

Gebruik AI — het is volledig toegestaan 😉

## Stappenplan

### 1. Zorg ervoor dat je een code editor hebt en Python  

*(Indien je dit hebt, mag je deze stap overslaan)*  

**Gebruik Visual Studio Code**  

- Download Visual Studio Code: [https://code.visualstudio.com/download](https://code.visualstudio.com/download)  
- Volg de installer voor het installeren van Visual Studio Code  
- Download een Python versie (liefst een versie vanaf 3.11.x of hoger): [https://www.python.org/downloads/](https://www.python.org/downloads/)  

**Wil je liever niets downloaden? Gebruik deze online code editor**

- Gebruik het Python notebook van Google : [Colab](https://colab.research.google.com/)

### 2. Installeer de nodige libraries

**Wanneer je Visual Studio Code gebruikt:**

- Doe in je CMD (Command Prompt) de volgende commando's om de nodige libraries te installeren:

```bash
py -m pip install requests
py -m pip install bs4
py -m pip install openai
```

**Wanneer je Google Colab gebruikt:**

- Je moet geen lokale pip installs doen, maar je zet bovenaan in je code het volgende om je libraries te installeren:

```bash
!pip install openai
!pip install bs4
!pip install requests
```

### 3. Maak een eigen API Key aan bij GROQ
**Maak een account aan bij GROQ**

Ga naar de website van Groq : [https://console.groq.com/home](https://console.groq.com/home). Maak hier een account aan via email of login via je Google of Github account.

<img width="auto" height="350" alt="image" src="https://github.com/user-attachments/assets/7eae93cc-8b18-4566-bd22-147c466d9a18" />

**Maak nu een API key aan**

Ga via het menu naar API Keys of ga naar de volgende link : [https://console.groq.com/keys](https://console.groq.com/keys). Klik hier op "Create API Key". Kies een display name naar keuze voor je API. De vervaldatum mag je laten staan op geen vervaldatum.
OPGELET : HET TOONT DE API KEY MAAR 1 KEER, SLA DEZE API KEY ERGENS OP!!!

<img width="auto" height="350" alt="image" src="https://github.com/user-attachments/assets/c3df9921-f338-4d33-a875-73bc161ac7af" />

### 4. Maak je eigen chatbot

- Gebruik openai librarie om je AI request te doen. Vergeet niet om je API Key te gebruiken die je in de vorige stap hebt gemaakt.
- Als je vastloopt, kun je kijken naar oplossing 1 op de volgende link: [https://github.com/Thomas-More-Digital-Innovation/Belevingsdag/blob/main/Stap1_Maak_Je_Eigen_Chatbot.py](https://github.com/Thomas-More-Digital-Innovation/Belevingsdag/blob/main/Stap1_Maak_Je_Eigen_Chatbot.py)

### 5. Scrape data

- Gebruik requests om een HTTP request te kunnen doen en gebruik van bs4 de BeatifulSoup om de HTML data mooi te kunnen benaderen.
- Als je vastloopt, kun je kijken naar oplossing 2 op de volgende link: [https://github.com/Thomas-More-Digital-Innovation/Belevingsdag/blob/main/Stap2_Scrape_Data.py](https://github.com/Thomas-More-Digital-Innovation/Belevingsdag/blob/main/Stap2_Scrape_Data.py)

### 6. Automatiseer jouw opzoekwerk

- Gebruik alles wat je hiervoor gebruikt hebt en combineer ze om automatisch jouw gegeven url door AI te laten analyseren.
- Als je vastloopt, kun je kijken naar oplossing 3 op de volgende link: [https://github.com/Thomas-More-Digital-Innovation/Belevingsdag/blob/main/Stap3_Automatiseer_Jouw_Opzoekwerk.py](https://github.com/Thomas-More-Digital-Innovation/Belevingsdag/blob/main/Stap3_Automatiseer_Jouw_Opzoekwerk.py)

### 7. Gebruik je eigen creativiteit

- Maak met alles wat je nu geleerd hebt jouw eigen automatisering. Een goede tip wanneer je vastzit, is dat je AI goed kunt gebruiken met het maken van je script. Heb je geen idee wat je moet maken? Kijk naar het inspiratie script op de volgende link: [https://github.com/Thomas-More-Digital-Innovation/Belevingsdag/blob/main/Stap4_Wat_Extra_Inspiratie.py](https://github.com/Thomas-More-Digital-Innovation/Belevingsdag/blob/main/Stap4_Wat_Extra_Inspiratie.py). Veel succes!!!

## Inhoud

- Presentatie
- Stap 1 : Maak je eigen chatbot (basisoplossing is gegeven)
- Stap 2 : Scrape data van een eigen website naar keuze (basisoplossing is gegeven)
- Stap 3 : Automatiseer jouw eigen opzoekwerk (basisoplossing is gegeven)
- Stap 4 : Wat extra inspiratie (inspiratie is gegeven)
- README.md

<!-- ![SchwartzjAllbetterGIF](https://github.com/user-attachments/assets/c0613ee5-29f9-4aff-8bb2-f9b5237963d3) -->
![IchigiggleGogoGIF](https://github.com/user-attachments/assets/83c41cbf-28d2-4877-b018-b10e24092853)

## Bronnen

- [Groq](https://groq.com/)
- [Google Colab](https://colab.research.google.com/)
- [VS Code](https://code.visualstudio.com/)

Gemaakt door Maurits Groen
