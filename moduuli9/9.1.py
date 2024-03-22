class auto:

    def __init__(self, rekisteri, huippunopeus):
        self.rekisteri = rekisteri
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0

    def ominaisuudet(self):
        print(f"Rekisteritunnus: {self.rekisteri}\n"
              f"Huippunopeus   : {self.huippunopeus}\n"
              f"Nopeus         : {self.nopeus}\n"
              f"Matka          : {self.matka}")


hamburger = auto("ABC-123", 142)
hamburger.ominaisuudet()
