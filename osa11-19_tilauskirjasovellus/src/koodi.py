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
        t = Tehtava(kuvaus, koodari, int(tyomaara))
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
            return "ok"
        else:
            return "ei ok"

    def valmiit_tilaukset(self): 
        return [t for t in self.__tilaukset if t.valmis] 

    def ei_valmiit_tilaukset(self):
        return [t for t in self.__tilaukset if t.valmis== False] 

    def koodarin_status(self, koodari: str):
        if len([t for t in self.__tilaukset if t.koodari == koodari]) != 0:
            valmistuneiden_maara = len([t for t in self.__tilaukset if t.valmis and t.koodari == koodari])
            valmistumattomien_maara =  len([t for t in self.__tilaukset if not t.valmis and t.koodari == koodari])
            valmistuneiden_h =  sum([t.tyomaara for t in self.__tilaukset if t.valmis and t.koodari == koodari])
            valmistumattomien_h = sum([t.tyomaara for t in self.__tilaukset if not t.valmis and t.koodari == koodari])
        else:
            return "ei ok"
        return (valmistuneiden_maara, valmistumattomien_maara, valmistuneiden_h, valmistumattomien_h)

class Sovellus():

    def __init__(self):
        self.__tilaukset = Tilauskirja()

    def valikko(self):
        str = "\nkomennot:\n0 lopetus\n1 lisää tilaus\n2 listaa valmiit\n3 listaa ei valmiit\n4 merkitse tehtävä valmiiksi\n5 koodarit\n6 koodarin status\n"
        print(str)

    def tilauksen_lisays(self):
        kuvaus = input("kuvaus: ")  
        koodari_ja_arvio = input("koodari ja työmääräarvio: ")        
        try:
            koodari, tyomaara = koodari_ja_arvio.split(" ")
            int(tyomaara)
            self.__tilaukset.lisaa_tilaus(kuvaus, koodari, int(tyomaara))
            print("lisätty!")
        except ValueError:
            print("virheellinen syöte")
        

    def listaa_valmiit(self):
        if self.__tilaukset.valmiit_tilaukset() == []:
            print("ei valmiita")
        else:
            for tilaus in self.__tilaukset.valmiit_tilaukset():
                print(tilaus)

    def listaa_ei_valmiit(self):
        if self.__tilaukset.ei_valmiit_tilaukset() == []:
            print("ei keskeneräisiä")
        else:
            for tilaus in self.__tilaukset.ei_valmiit_tilaukset():
                print(tilaus)

    def merkitse_valmiiksi(self):
        tunniste = input("tunniste: ")
        try:
            int(tunniste)
            if self.__tilaukset.merkkaa_valmiiksi(int(tunniste)) == "ok":
                print("merkitty valmiiksi")
            else:
                print("virheellinen syöte")
        except ValueError:
            print("virheellinen syöte")

    def koodarit(self):
        for k in self.__tilaukset.koodarit():
            print(k)
    
    def koodarin_status(self):
        koodari = input("koodari: ")
        if self.__tilaukset.koodarin_status(koodari) == "noup":
            print("virheellinen syöte")
        else:
            valmistuneiden_maara, valmistumattomien_maara, valmistuneiden_h, valmistumattomien_h = self.__tilaukset.koodarin_status(koodari)
            print(f"työt: valmiina {valmistuneiden_maara} ei valmiina {valmistumattomien_maara}, tunteja: tehty {valmistuneiden_h} tekemättä {valmistumattomien_h}")
        
    def kaynnista(self):
        self.valikko()
        while True:
            print("")
            komento = input("komento: ")
            if komento == "0":
                break
            elif komento == "1":
                self.tilauksen_lisays()
            elif komento == "2":
                 self.listaa_valmiit()
            elif komento == "3":         
                 self.listaa_ei_valmiit()
            elif komento == "4":
                self.merkitse_valmiiksi()
            elif komento == "5":
                self.koodarit()
            elif komento == "6":         
                self.koodarin_status()
            else:
                self.valikko()


s = Sovellus()
s.kaynnista()