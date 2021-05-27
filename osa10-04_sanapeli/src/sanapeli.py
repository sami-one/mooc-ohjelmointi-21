# TEE RATKAISUSI TÄHÄN:
import random

class Sanapeli():
    def __init__(self, kierrokset: int):
        self.voitot1 = 0
        self.voitot2 = 0
        self.kierrokset = kierrokset
    def kierroksen_voittaja(self, pelaaja1_sana: str, pelaaja2_sana: str):
        # arvotaan voittaja
        return random.randint(1, 2)
    def pelaa(self):
        print("Sanapeli:")
        for i in range(1, self.kierrokset+1):
            print(f"kierros {i}")
            vastaus1 = input("pelaaja1: ")
            vastaus2 = input("pelaaja2: ")

            if self.kierroksen_voittaja(vastaus1, vastaus2) == 1:
                self.voitot1 += 1
                print("pelaaja 1 voitti")
            elif self.kierroksen_voittaja(vastaus1, vastaus2) == 2:
                self.voitot2 += 1
                print("pelaaja 2 voitti")
            #else:
            #    pass # tasapeli

        print("peli päättyi, voitot:")
        print(f"pelaaja 1: {self.voitot1}")
        print(f"pelaaja 2: {self.voitot2}")

class PisinSana(Sanapeli):    
    def kierroksen_voittaja(self, pelaaja1_sana: str, pelaaja2_sana: str):
        if len(pelaaja1_sana) > len(pelaaja2_sana):
            return 1
        elif len(pelaaja1_sana) < len(pelaaja2_sana):
            return 2
        return -1
    
class EnitenVokaaleja(Sanapeli):    
    def kierroksen_voittaja(self, pelaaja1_sana: str, pelaaja2_sana: str):
        p1 = sum([pelaaja1_sana.count(kirjain)  for kirjain in set(pelaaja1_sana) if kirjain in "aeiouyäöå"])
        p2 = sum([pelaaja2_sana.count(kirjain)  for kirjain in set(pelaaja2_sana) if kirjain in "aeiouyäöå"])
      
        if p1 > p2:
            return 1
        elif p1 < p2:
            return 2
        return -1

class KiviPaperiSakset(Sanapeli):
     def kierroksen_voittaja(self, pelaaja1_sana: str, pelaaja2_sana: str):
         vaihtoehdot = {"kivi":1,  "paperi":2,  "sakset":4}
         if pelaaja1_sana not in vaihtoehdot:
             if pelaaja2_sana not in vaihtoehdot:
                 return -1
             else:
                 return 2
         if pelaaja2_sana not in vaihtoehdot:
            return 1
         if vaihtoehdot[pelaaja1_sana] == vaihtoehdot[pelaaja2_sana] :
             return -1
         if vaihtoehdot[pelaaja1_sana] - vaihtoehdot[pelaaja2_sana] in [-3, 1, 2]:
             return 1
         return 2