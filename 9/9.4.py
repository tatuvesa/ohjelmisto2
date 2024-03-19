import random


class Auto:

    def __init__(self, rekisteri, huippunopeus):
        self.rekisteri = rekisteri
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kokomatka = 2000

    def kiihdyta(self, nopeudenmuutos):
        uusnopeus = self.nopeus + nopeudenmuutos
        if uusnopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif uusnopeus < 0:
            self.nopeus = 0
        else:
            self.nopeus = uusnopeus

    def kulje(self, tunnit):
        # tunnit = float(input("Tunnit: "))
        matka = self.nopeus * tunnit
        self.kokomatka += matka


autot = [Auto(f"ABC-{i + 1}", random.randint(100, 200)) for i in range(10)]

while True:
    for auto in autot:
        auto.kiihdyta(random.randint(-10, 15))
        auto.kulje(1)
        if auto.kokomatka >= 10000:
            break
    else:
        continue
    break

# Tulostetaan autot
print("| Rekisteritunnus | Huippunopeus | Tämänhetkinen nopeus | Kuljettu matka |")
print("|-----------------|--------------|----------------------|----------------|")
for auto in autot:
    print(f"| {auto.rekisteri:15} | {auto.huippunopeus:7} km/h | {auto.nopeus:15} km/h | {auto.kokomatka:11} km |")
