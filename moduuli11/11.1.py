class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi


class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivumaara):
        self.kirjoittaja = kirjoittaja
        self.sivumaara = sivumaara
        super().__init__(nimi)

    def tulosta_tiedot(self):
        print(f"Kirjan nimi  : {self.nimi}")
        print(f"Kirjoittaja  : {self.kirjoittaja}")
        print(f"Sivumäärä    : {self.sivumaara}")


class Lehti(Julkaisu):
    def __init__(self, nimi, paatoimittaja):
        self.paatoimittaja = paatoimittaja
        super().__init__(nimi)

    def tulosta_tiedot(self):
        print(f"Lehden nimi  : {self.nimi}")
        print(f"Päätoimittaja: {self.paatoimittaja}")


lehti = Lehti("Aku Ankka", "Aki Hyyppä\n")
kirja = Kirja("Hytti n:o 6", "Rosa Liksom", 200)

lehti.tulosta_tiedot()
kirja.tulosta_tiedot()
print("Amogus")