# Tee ratkaisusi tähän:
class Tavara:

    def __init__(self, nimi, paino):
        self.n = nimi
        self.p = paino

    def nimi(self):
        return self.n

    def paino(self):
        return self.p

    
    def __str__(self):
        return f"{self.n} ({self.p} kg)"

class Matkalaukku:

    def __init__(self, maksimipaino):
        self.tavarat = []
        self.maksimipaino = maksimipaino

    def lisaa_tavara(self, tavara: Tavara):
        if self.paino() + tavara.paino() <= self.maksimipaino:
            self.tavarat.append(tavara)

    def tulosta_tavarat(self):
        for t in self.tavarat:
            print(t)

    def paino(self):
        yht = 0
        for t in self.tavarat:
            yht += t.paino()
        return yht

    def raskain_tavara(self):
        s = sorted(self.tavarat, key=lambda t: t.paino())
        return s[-1]
        
    def __str__(self):
        if len(self.tavarat) == 0:
            return f"0 tavaraa ({self.paino()} kg)"
        elif len(self.tavarat) == 1:
            return f"1 tavara ({self.paino()} kg)"
        else:
            return f"{len(self.tavarat)} tavaraa ({self.paino()} kg)"
    
class Lastiruuma:

     def __init__(self, maksimipaino):
        self.matkalaukut = []
        self.maksimipaino = maksimipaino

     def paino(self):
        yht = 0
        for m in self.matkalaukut:
            yht += m.paino()
        return yht
        
     def lisaa_matkalaukku(self, laukku):
        if self.paino() + laukku.paino() <= self.maksimipaino:
         self.matkalaukut.append(laukku)

     def tulosta_tavarat(self):
        for m in self.matkalaukut:
            for t in m.tavarat:
                print(t)

     def __str__(self):
        tilaa = self.maksimipaino - self.paino()
        if len(self.matkalaukut) == 0:
            return f"0 matkalaukkua, tilaa {tilaa} kg"
        elif len(self.matkalaukut) == 1:
            return f"1 matkalaukku, tilaa {tilaa} kg"
        else:
            return f"{len(self.matkalaukut)} matkalaukkua, tilaa {tilaa} kg"


if __name__ == "__main__":

    kirja = Tavara("Aapiskukko", 2)
    puhelin = Tavara("Nokia 3210", 1)
    tiiliskivi = Tavara("Tiiliskivi", 4)

    print("Kirjan nimi", kirja.nimi())
    print("Kirjan paino", kirja.paino())

    print("Kirja:", kirja)
    print("Puhelin:", puhelin)

    matkalaukku = Matkalaukku(5)
    print(matkalaukku)

    matkalaukku.lisaa_tavara(kirja)
    print(matkalaukku)

    matkalaukku.lisaa_tavara(puhelin)
    print(matkalaukku)

    matkalaukku.lisaa_tavara(tiiliskivi)
    print(matkalaukku)

    matkalaukku = Matkalaukku(10)
    matkalaukku.lisaa_tavara(kirja)
    matkalaukku.lisaa_tavara(puhelin)
    matkalaukku.lisaa_tavara(tiiliskivi)

    print("Matkalaukussa on seuraavat tavarat:")
    matkalaukku.tulosta_tavarat()
    paino_yht = matkalaukku.paino()
    print(f"Yhteispaino: {paino_yht} kg")

    raskain = matkalaukku.raskain_tavara()
    print(f"Raskain tavara: {raskain}")

    lastiruuma = Lastiruuma(1000)
    print(lastiruuma)
    
    adan_laukku = Matkalaukku(10)
    adan_laukku.lisaa_tavara(kirja)
    adan_laukku.lisaa_tavara(puhelin)

    pekan_laukku = Matkalaukku(10)
    pekan_laukku.lisaa_tavara(tiiliskivi)


    lastiruuma.lisaa_matkalaukku(adan_laukku)
    lastiruuma.lisaa_matkalaukku(pekan_laukku)


    print("Ruuman matkalaukuissa on seuraavat tavarat:")
    lastiruuma.tulosta_tavarat()