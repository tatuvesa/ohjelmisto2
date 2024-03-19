class Hissi:

    def __init__(self, alin_kerros, ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.nykyinen_kerros = alin_kerros

    def kerros_ylos(self):
        if self.nykyinen_kerros < self.ylin_kerros:
            self.nykyinen_kerros += 1
        print(f"Hissi on nyt kerroksessa {self.nykyinen_kerros}.")

    def kerros_alas(self):
        if self.nykyinen_kerros > self.alin_kerros:
            self.nykyinen_kerros -= 1
        print(f"Hissi on nyt kerroksessa {self.nykyinen_kerros}.")

    def siirry_kerrokseen(self, kerros):
        while self.nykyinen_kerros < kerros:
            self.kerros_ylos()
        while self.ylin_kerros > kerros:
            self.kerros_alas()

hissi = Hissi(1,10)
hissi.siirry_kerrokseen(5)
hissi.siirry_kerrokseen(1)
