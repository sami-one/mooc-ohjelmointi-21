# TEE RATKAISUSI TÄHÄN:
class Tyontekija:
    def __init__(self, nimi: str):
        self.nimi = nimi
        self.alaiset = []

    def lisaa_alainen(self, tyontekija: 'Tyontekija'):
        self.alaiset.append(tyontekija)

def laske_alaiset(tyontekija: Tyontekija):
    summa = len(tyontekija.alaiset)
    for alainen in tyontekija.alaiset:
        summa +=  laske_alaiset(alainen) 

    return summa