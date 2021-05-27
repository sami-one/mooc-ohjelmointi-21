# Tee ratkaisusi tähän:
class Tehtava:
    id = 1
    def __init__(self, kuvaus, koodari, tyomaara):        
        self.kuvaus = kuvaus
        self.koodari = koodari
        self.tyomaara = tyomaara
        self.valmis = False
        self.id = Tehtava.id
        Tehtava.id += 1 
       
    def on_valmis(self):
        return self.valmis

    def merkkaa_valmiiksi(self):
        self.valmis = True

    def onko_valmis(self):
        if self.valmis:
            return "VALMIS"
        return "EI VALMIS"

    def __str__(self):
        return f"{self.id}: {self.kuvaus} ({self.tyomaara} tuntia), koodari {self.koodari} {self.onko_valmis()}"

class Tilauskirja:

    def __init__(self):
        self.__tilaukset = []

    def lisaa_tilaus(self, kuvaus, koodari, tyomaara):
        t = Tehtava(kuvaus, koodari, tyomaara)
        self.__tilaukset.append(t)

    def kaikki_tilaukset(self):
        return self.__tilaukset

    def koodarit(self):
        return list(set([t.koodari for t in self.__tilaukset]))

    def merkkaa_valmiiksi(self, id: int):        
        loytyi = False
        for t in self.__tilaukset:
            if t.id == id:
                loytyi = True
                tilaus = t
        if loytyi:
            tilaus.merkkaa_valmiiksi()
        else:
            raise ValueError("Ei löydy id:tä") 

    def valmiit_tilaukset(self):
        return [t for t in self.__tilaukset if t.valmis] 

    def ei_valmiit_tilaukset(self):
        return [t for t in self.__tilaukset if t.valmis== False] 

    def koodarin_status(self, koodari: str):
        if len([t for t in self.__tilaukset if t.koodari == koodari]) != 0:
            valmiit = len([t for t in self.__tilaukset if t.valmis and t.koodari == koodari])
            kesken =  len([t for t in self.__tilaukset if not t.valmis and t.koodari == koodari])
            valmiit_tunnit =  sum([t.tyomaara for t in self.__tilaukset if t.valmis and t.koodari == koodari])
            kesken_tunnit = sum([t.tyomaara for t in self.__tilaukset if not t.valmis and t.koodari == koodari])
        else:
            raise ValueError ("Ei löydy koodaria")
        return (valmiit, kesken, valmiit_tunnit, kesken_tunnit)