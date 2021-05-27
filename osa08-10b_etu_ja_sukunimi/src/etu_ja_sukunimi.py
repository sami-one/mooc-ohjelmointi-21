# Tee ratkaisusi tähän:
class Henkilo:

    def __init__(self,nimi:str):
        self.nimi = nimi
        nimi.split(" ")

    def anna_etunimi(self):
        osat = self.nimi.split(' ')
        return osat[0]

    def anna_sukunimi(self):
        osat = self.nimi.split(' ')
        return osat[1]
        
if __name__ == "__main__":
    pekka = Henkilo("Pekka Python")
    print(pekka.anna_etunimi())
    print(pekka.anna_sukunimi())











