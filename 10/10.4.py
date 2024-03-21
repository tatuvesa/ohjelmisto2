import random


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
        matka = self.nopeus * tunnit
        self.kokomatka += matka


class Kilpailu:
    def __init__(self, nimi, pituus, autot):
        self.nimi = nimi
        self.pituus = pituus
        self.autot = autot

    def tunti_kuluu(self):
        for auto in self.autot:
            auto.kiihdyta(random.randint(-10, 15))
            auto.kulje(1)

    def tulosta_tilanne(self):
        print("|-----------------|--------------|----------------------|----------------|")
        print("| Rekisteritunnus | Huippunopeus | Tämänhetkinen nopeus | Kuljettu matka |")
        print("|-----------------|--------------|----------------------|----------------|")
        for auto in self.autot:
            print(
                f"| {auto.rekisteri:15} | {auto.huippunopeus:7} km/h | {auto.nopeus:15} km/h | {auto.kokomatka:11} km |")

    def kilpailu_ohi(self):
        for auto in self.autot:
            if auto.kokomatka >= self.pituus:
                return True
        return False


autot = [Auto(f"ABC-{i + 1}", random.randint(100, 200)) for i in range(10)]
kilpailu = Kilpailu("Suuri romuralli", 8000, autot)

tunnit = 0
while True:
    kilpailu.tunti_kuluu()
    tunnit += 1
    if tunnit % 10 == 0 or kilpailu.kilpailu_ohi():
        kilpailu.tulosta_tilanne()
    if kilpailu.kilpailu_ohi():
        break
