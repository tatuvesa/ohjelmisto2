class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissien_lkm):
        self.hissit = [Hissi(alin_kerros, ylin_kerros) for _ in range(hissien_lkm)]

    def aja_hissia(self, hissi_numero, kohde_kerros):
        if hissi_numero < len(self.hissit):
            self.hissit[hissi_numero].siirry_kerrokseen(kohde_kerros)
        else:
            print("Annettua hissin numeroa ei ole olemassa.")


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
        while self.nykyinen_kerros > kerros:
            self.kerros_alas()


talo = Talo(1, 10, 3)
print(f"Ensimmäinen hissi: ")
talo.aja_hissia(0, 5)
print(f"Toinen hissi: ")
talo.aja_hissia(1, 3)
print(f"Kolmas hissi: ")
talo.aja_hissia(2, 7)
