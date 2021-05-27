# TEE RATKAISUSI TÄHÄN:

class Maksukortti:
    def __init__(self, saldo: float):
        self.saldo = saldo

    def lataa_rahaa(self, lisays: float):
        self.saldo += lisays

    def ota_rahaa(self, maara: float):
        if self.saldo >= maara:
            self.saldo -= maara
            return True
        else:
            return False
        # Toteuta metodi siten, että se ottaa kortilta rahaa vain, jos saldoa riittää
        # Onnistuessaan metodi palauttaa True ja muuten False

class Kassapaate:

    maukkaan_hinta = 4.3
    edullisen_hinta = 2.5
    
    def __init__(self):
        # kassassa on aluksi 1000 euroa rahaa
        self.rahaa = 1000
        self.edulliset = 0
        self.maukkaat = 0

    def syo_edullisesti(self, maksu: float):
        # Edullinen lounas maksaa 2.50 euroa
        # Kasvatetaan kassan rahamäärää edullisen lounaan hinnalla ja palautetaan vaihtorahat
        # Jos parametrina annettu maksu ei ole riittävän suuri, ei lounasta myydä ja metodi palauttaa koko summan
        if maksu >= self.edullisen_hinta:
            self.edulliset += 1
            self.rahaa += self.edullisen_hinta
            return maksu - self.edullisen_hinta
        else:
            return float(maksu)

    def syo_maukkaasti(self, maksu: float):
        # Maukas lounas maksaa 4.30 euroa
        # Kasvatetaan kassan rahamäärää maukkaan lounaan hinnalla ja palautetaan vaihtorahat
        # Jos parametrina annettu maksu ei ole riittävän suuri, ei lounasta myydä ja metodi palauttaa koko summan      
        if maksu >= 4.3:
            self.maukkaat += 1
            self.rahaa += self.maukkaan_hinta
            return maksu - self.maukkaan_hinta
        else:
            return float(maksu)

    def syo_edullisesti_kortilla(self, kortti:Maksukortti):
        # Edullinen lounas maksaa 2.50 euroa
        # Jos kortilla on tarpeeksi rahaa, vähennetään hinta kortilta ja palautetaan True
        # Muuten palautetaan False
        if kortti.saldo >= self.edullisen_hinta:
            kortti.saldo -= self.edullisen_hinta
            self.edulliset += 1
            return True
        else:
            return False

    def syo_maukkaasti_kortilla(self, kortti:Maksukortti):
        # Maukas lounas maksaa 4.30 euroa
        # Jos kortilla on tarpeeksi rahaa, vähennetään hinta kortilta ja palautetaan True
        # Muuten palautetaan False
        if kortti.saldo >= self.maukkaan_hinta:
            kortti.saldo -= self.maukkaan_hinta
            self.maukkaat += 1
            return True
        else:
            return False

    def lataa_rahaa_kortille(self, kortti: Maksukortti, summa: float):
        self.rahaa += summa
        kortti.lataa_rahaa(summa) 

    def __repr__(self):
        return f"kassassa rahaa {self.rahaa} edullisia lounaita myyty {self.edulliset} maukkaita lounaita myyty {self.maukkaat}"



if __name__ == "__main__":

    exactum = Kassapaate()
    print(exactum)

    antin_kortti = Maksukortti(2)

    print(f"kortilla rahaa {antin_kortti.saldo} euroa")

    onnistuiko = exactum.syo_maukkaasti_kortilla(antin_kortti)
    print("riittikö raha:", onnistuiko)

    exactum.lataa_rahaa_kortille(antin_kortti, 100)

    onnistuiko = exactum.syo_maukkaasti_kortilla(antin_kortti)
    print("riittikö raha:", onnistuiko)

    print(f"kortilla rahaa {antin_kortti.saldo} euroa")

    print(exactum)