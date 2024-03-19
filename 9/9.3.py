import random

class auto:

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
        matka = self.nopeus * tunnit
        self.kokomatka += matka

    def ominaisuudet(self):
        print(f"Rekisteritunnus: {self.rekisteri}\n"
              f"Huippunopeus   : {self.huippunopeus} km/h\n"
              f"Nopeus         : {self.nopeus} km/h\n"
              f"Matka          : {self.kokomatka} km")


hamburger = auto("ABC-123", 142)
hamburger.kiihdyta(30)
hamburger.kiihdyta(70)
hamburger.kiihdyta(50)
print(f"Auton nopeus kiihdytuksen jälkeen: ")
hamburger.ominaisuudet()
hamburger.kiihdyta(-200)
print(f"\nAuton nopeus hätäjarrutuksen jälkeen: ")
hamburger.ominaisuudet()
hamburger.kiihdyta(60)
hamburger.kulje(1.5)
print("\nMatka kuljettu 1.5 tunnin jälkeen: ")
hamburger.ominaisuudet()