import requests

def hae_saa(paikkakunta):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={paikkakunta}&appid=c17cc257b1538954c91ed1a3e38570f6"
    vastaus = requests.get(url)
    data = vastaus.json()

    lampotila_kelvin = data['main']['temp']
    lampotila_celsius = lampotila_kelvin - 273.15

    saa_tila = data['weather'][0]['description']

    print(f"Säätila paikkakunnalla {paikkakunta} on: {saa_tila}")
    print(f"Lämpötila on: {lampotila_celsius:.1f} °C")

paikkakunta = input("Anna paikkakunnan nimi: ")

hae_saa(paikkakunta)
