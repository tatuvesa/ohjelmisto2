class Auto:
    def __init__(self, rekisteri, huippunopeus):
        self.rekisteri = rekisteri
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kokomatka = 0

    def kiihdyta(self, nopeudenmuutos):
        uusnopeus = self.nopeus + nopeudenmuutos
        if uusnopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif uusnopeus < 0:
            self.nopeus = 0
        else:
            self.nopeus = uusnopeus

    def kulje(self, tunnit):
        self.kokomatka += round(self.nopeus * tunnit)

    def ominaisuudet(self):
        print(f"Rekisteritunnus: {self.rekisteri}\n"
              f"Huippunopeus   : {self.huippunopeus} km/h\n"
              f"Nopeus         : {self.nopeus} km/h\n"
              f"Matka          : {self.kokomatka} km")

class Sähköauto(Auto):
    def __init__(self, rekisteri, huippunopeus, akkukapasiteetti):
        super().__init__(rekisteri, huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti

class Polttomoottoriauto(Auto):
    def __init__(self, rekisteri, huippunopeus, bensatankin_koko):
        super().__init__(rekisteri, huippunopeus)
        self.bensatankin_koko = bensatankin_koko

sähköauto = Sähköauto("ABC-15", 180, 52.5)
polttomoottoriauto = Polttomoottoriauto("ACD-123", 165, 32.3)

sähköauto.kiihdyta(60)
sähköauto.kiihdyta(60)
sähköauto.kiihdyta(60)
polttomoottoriauto.kiihdyta(60)
polttomoottoriauto.kiihdyta(60)
polttomoottoriauto.kiihdyta(60)

while True:
    try:
        kulkusähkö = int(input("Montako tuntia haluat sähkäauton kulkevan?: "))
        break
    except ValueError:
        print("Syötä kokonaisluku.")

while True:
    try:
        kulkupoltto = int(input("Montako tuntia haluat polttomoottorillisen auton kulkevan?: "))
        break
    except ValueError:
        print("Syötä kokonaisluku.")

sähköauto.kulje(kulkusähkö)
polttomoottoriauto.kulje(kulkupoltto)

print(f"\nSähköauton kulkema matka {kulkusähkö} tunnin jälkeen:\n")
print("        Sähköauto")
print("-------------------------")
sähköauto.ominaisuudet()
print(f"\nPolttomoottoriauton matka {kulkupoltto} tunnin jälkeen:\n")
print("      Polttomoottori")
print("--------------------------")
polttomoottoriauto.ominaisuudet()
