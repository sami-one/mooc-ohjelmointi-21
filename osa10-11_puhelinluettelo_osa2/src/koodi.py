
# Tee ratkaisusi tähän:
class Puhelinluettelo:
    def __init__(self):
        self.__henkilot = {}

    def lisaa_numero(self, nimi: str, numero: str):
        if not nimi in self.__henkilot:
            self.__henkilot[nimi] = Henkilo(nimi)
            self.__henkilot[nimi].lisaa_numero(numero)
        else:
            self.__henkilot[nimi].lisaa_numero(numero)

    def lisaa_osoite(self, nimi, osoite):
        if not nimi in self.__henkilot:
            self.__henkilot[nimi] = Henkilo(nimi)
            self.__henkilot[nimi].lisaa_osoite(osoite)
        else:
            self.__henkilot[nimi].lisaa_osoite(osoite)


    def numerot(self, nimi: str):
        if not nimi in self.__henkilot:
            return None
        return self.__henkilot[nimi].numerot()

    def hae_nimi(self, nro: str):        
        for item in self.__henkilot.items():
            if nro in item[1].numerot():
                return item[1].nimi()
        return None

    def hae_tiedot(self, nimi):
        if nimi not in self.__henkilot:
            return None
        else:
            return self.__henkilot[nimi]

    def kaikki_tiedot(self):
        return self.__henkilot

class PuhelinluetteloSovellus:
    def __init__(self):
        self.__luettelo = Puhelinluettelo()

    def ohje(self):
        print("komennot: ")
        print("0 lopetus")
        print("1 numeron lisäys")
        print("2 haku")
        print("3 osoitteen lisäys")

    def numeron_lisays(self):
        nimi = input("nimi: ")
        numero = input("numero: ")
        self.__luettelo.lisaa_numero(nimi, numero)

    def osoitteen_lisays(self):
        nimi = input("nimi: ")
        osoite = input("osoite: ")
        self.__luettelo.lisaa_osoite(nimi, osoite)

    def haku(self):
        nimi = input("nimi: ")

        tiedot = self.__luettelo.hae_tiedot(nimi)
        if tiedot == None:
            print("numero ei tiedossa")
            print("osoite ei tiedossa")
            return 
        
        numerot = tiedot.numerot()
        if len(numerot)==0:
            print("numero ei tiedossa") 
        else: 
            for numero in numerot:
                print(numero)

        osoite = tiedot.osoite()
        if osoite!=None:
            print(osoite)
        else:
            print("osoite ei tiedossa")

    def suorita(self):
        self.ohje()
        while True:
            print("")
            komento = input("komento: ")
            if komento == "0":
                break
            elif komento == "1":
                self.numeron_lisays()
            elif komento == "2":
                self.haku()
            elif komento == "3":
                self.osoitteen_lisays()
            else:
                self.ohje()
class Henkilo:
    def __init__(self, nimi):
        self.__nimi = nimi
        self.__numerot = []
        self.__osoite = None

    def lisaa_numero(self, nro:str):
        print("Henkilo.lisaa_numero")
        self.__numerot.append(nro)

    def lisaa_osoite(self, os):
        self.__osoite = os

    def nimi(self):
        return self.__nimi
    
    def numerot(self):
        print("Henkilo.numerot")
        return self.__numerot

    def osoite(self):
        return self.__osoite

# kun testaat, mitään muuta koodia ei saa olla luokkien ulkopuolella kuin seuraavat rivit
sovellus = PuhelinluetteloSovellus()
sovellus.suorita()
