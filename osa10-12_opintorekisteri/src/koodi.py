# Tee ratkaisusi tänne
class Opintorekisteri:
    def __init__(self):
        self.__suoritus = {}

    def lisaa_suoritus(self, nimi, arvosana, op):
        if nimi in self.__suoritus:
             self.__suoritus[nimi].korota_arvosana(arvosana)
        else:
            self.__suoritus[nimi] = Kurssi(nimi, arvosana, op)
             
    def hae_tiedot(self, nimi):
        if nimi not in self.__suoritus:
            return None
        else:
            return self.__suoritus[nimi]

    def suoritukset(self):
        return self.__suoritus

class OpintorekisteriSovellus:
    def __init__(self):
        self.__suoritus = Opintorekisteri()   

    def ohje(self):
        print("komennot: ")        
        print("1 lisää suoritus")
        print("2 hae suoritus")
        print("3 tilastot")
        print("0 lopetus")

    def lisaa_suoritus(self):
        nimi = input("kurssi: ")
        arvosana = input("arvosana: ")
        op = input("opintopisteet: ")
        self.__suoritus.lisaa_suoritus(nimi, arvosana, op)        

    def haku(self):
        nimi = input("nimi: ")
        tiedot = self.__suoritus.hae_tiedot(nimi)
        if tiedot==None:
            print("ei suoritusta")
            return
        print(f"{tiedot.nimi()} ({tiedot.op()} op) arvosana {tiedot.arvosana()}")

    def tilastot(self):  
        tieto = self.__suoritus.suoritukset()        
        op = [tieto[kurssi].op() for kurssi in tieto]
        print(f"suorituksia {len(tieto)} kurssilta, yhteensä {sum(op)} opintopistettä") 
        arvosanat = [tieto[kurssi].arvosana() for kurssi in tieto]  
        ka = f"{sum(arvosanat)/len(arvosanat):.1f}"
        print("keskiarvo", ka)
        print("arvosanajakauma")
        jakauma = {i: arvosanat.count(i)*"x" for i in range(1,6)}
        for rivi in jakauma:
            print(str(rivi) + ": " + str(jakauma[rivi]))
    
    def suorita(self):
        self.ohje()
        while True:
            print("")
            komento = input("komento: ")
            if komento == "0":
                break
            elif komento == "1":
                self.lisaa_suoritus()
            elif komento == "2":
                self.haku()
            elif komento == "3":         
                self.tilastot()
            else:
                self.ohje()

class Kurssi:

    def __init__(self, nimi, arvosana,  op):
        self.__nimi = nimi
        self.__arvosana = arvosana        
        self.__op = op

    def korota_arvosana(self, arvosana):
        if arvosana > self.__arvosana:
            self.__arvosana = arvosana

    def nimi(self):
        return self.__nimi

    def arvosana(self):
        return int(self.__arvosana)

    def op(self):
        return int(self.__op)

# kun testaat, mitään muuta koodia ei saa olla luokkien ulkopuolella kuin seuraavat rivit
sovellus = OpintorekisteriSovellus()
sovellus.suorita()