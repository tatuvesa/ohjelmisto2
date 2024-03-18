class auto:

    def __init__(self, rekisteri, huippunopeus):
        self.rekisteri = rekisteri
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0

    def kiihdyta(self, nopeudenmuutos):
        uusnopeus = self.nopeus + nopeudenmuutos
        if uusnopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif uusnopeus < 0:
            self.nopeus = 0
        else:
            self.nopeus = uusnopeus

    def ominaisuudet(self):
        print(f"Rekisteritunnus: {self.rekisteri}\n"
              f"Huippunopeus   : {self.huippunopeus} km/h\n"
              f"Nopeus         : {self.nopeus} km/h\n"
              f"Matka          : {self.matka} km")


hamburger = auto("ABC-123", 142)
hamburger.kiihdyta(30)
hamburger.kiihdyta(70)
hamburger.kiihdyta(50)
print(f"Auton nopeus kiihdytuksen jälkeen: ")
hamburger.ominaisuudet()
hamburger.kiihdyta(-200)
print(f"\nAuton nopeus hätäjarrutuksen jälkeen: ")
hamburger.ominaisuudet()
