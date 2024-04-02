import requests


def hae_saa(paikkakunta):
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={paikkakunta}&appid={key}&units=metric"
        vastaus = requests.get(url)
        data = vastaus.json()

        lampotila = data['main']['temp']


        saa_tila = data['weather'][0]['description']

        print(f"Säätila paikkakunnalla {paikkakunta} on: {saa_tila}")
        print(f"Lämpötila on: {lampotila:.1f} °C")
    except Exception as e:
        print("Ei toimi")


paikkakunta = input("Anna paikkakunnan nimi: ")
key = "c17cc257b1538954c91ed1a3e38570f6"

hae_saa(paikkakunta)
