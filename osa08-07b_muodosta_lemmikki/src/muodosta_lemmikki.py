# Tee ratkaisusi tähän:
class Lemmikki:

    def __init__(self, nimi: str, laji: str, vuosi: int):
        self.nimi = nimi
        self.laji = laji
        self.syntymavuosi = vuosi

def uusi_lemmikki(nimi: str, laji: str, vuosi: int):
        return Lemmikki(nimi, laji, vuosi)