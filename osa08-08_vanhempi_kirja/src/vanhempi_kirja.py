# ÄLÄ MUUTA ALLA OLEVAA LUOKKAA Kirja
# Kirjoita ratkaisui Kirja-luokan jälkeen

class Kirja:
    def __init__(self, nimi: str, kirjoittaja: str, genre: str, kirjoitusvuosi: int):
        self.nimi = nimi
        self.kirjoittaja = kirjoittaja
        self.genre = genre
        self.kirjoitusvuosi = kirjoitusvuosi

# -----------------------------
# tee ratkaisu tänne

def vanhempi_kirja(kirja1: Kirja, kirja2: Kirja):
        if kirja1.kirjoitusvuosi == kirja2.kirjoitusvuosi:
            print(f"{kirja1.nimi} ja {kirja2.nimi} kirjoitettiin {kirja1.kirjoitusvuosi}")
        elif kirja1.kirjoitusvuosi < kirja2.kirjoitusvuosi:
            print(f"{kirja1.nimi} on vanhempi, se kirjoitettiin {kirja1.kirjoitusvuosi}")
        else:
            print(f"{kirja2.nimi} on vanhempi, se kirjoitettiin {kirja2.kirjoitusvuosi}")