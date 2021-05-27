import unittest
from unittest.mock import patch

from tmc import points, reflect
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import os.path
import textwrap
from random import choice, randint
from datetime import date, datetime, timedelta

exercise = 'src.koodi'

def f(attr: list):
    return ",".join(attr)

def s(l: list):
    return "\n".join(l)

def tt(d, kh, s):
    status = "EI VALMIS" if not s else "VALMIS"
    k, h, *x = kh.split(' ')
    return f"{d} ({h} tuntia), koodari {k} {status}"

@points('12.tilastot_ojennukseen_osa1')
class TilastotOjennukseen1Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=["osa.json", "0"]):
           cls.module = load_module(exercise, 'fi')

    def test_01_pysahtyy(self):
        syote = ["osa.json", "0"]
        with patch('builtins.input', side_effect=syote):
            try:
                reload_module(self.module)
            except:
                self.fail(f"varmista että ohjelma toimii syötteellä\n{s(syote)}")

    def test_02_maara_ja_ohje_tulostetaan(self):
        syote = ["osa.json", "0"]
        with patch('builtins.input', side_effect=syote):
            try:
                reload_module(self.module)
            except:
                self.fail(f"varmista että ohjelma toimii syötteellä\n{s(syote)}")

            output = get_stdout()
            self.assertFalse(len(output)==0,'Koodisi ei tulosta mitään. Eihän se vaan ole if __name__ == "__main__" -lohkon sisällä?')

            exp = """luettiin 14 pelaajan tiedot
komennot:
0 lopeta
1 hae pelaaja
2 joukkueet
3 maat
4 joukkueen pelaajat
5 maan pelaajat
6 eniten pisteitä
7 eniten maaleja
"""
            for rivi in exp.split("\n"):
                if not rivi in output:
                    self.fail(f"Ohjelman pitäisi tulostaa rivi\n{rivi}\nKun ohjelma suoritetaan syötteellä\n{s(syote)}\nTulostus oli\n{output}")   
            
            eiodotettu = "lisätty!"
            self.assertFalse(eiodotettu in output, f"Ohjelmasi tulostuksessa ei saa olla\n{eiodotettu}\nsyötteellä\n{s(syote)}\nTulostus oli\n{output}")   

    def test_03_maara_ja_ohje_tulostetaan_2(self):
        syote = ["kaikki.json", "0"]
        with patch('builtins.input', side_effect=syote):
            try:
                reload_module(self.module)
            except:
                self.fail(f"varmista että ohjelma toimii syötteellä\n{s(syote)}")

            output = get_stdout()

            exp = """luettiin 964 pelaajan tiedot
komennot:
"""
            for rivi in exp.split("\n"):
                if not rivi in output:
                    self.fail(f"Ohjelman pitäisi tulostaa rivi\n{rivi}\nKun ohjelma suoritetaan syötteellä\n{s(syote)}\nTulostus oli\n{output}")   
            
            eiodotettu = "lisätty!"
            self.assertFalse(eiodotettu in output, f"Ohjelmasi tulostuksessa ei saa olla\n{eiodotettu}\nsyötteellä\n{s(syote)}\nTulostus oli\n{output}")   

    def test_04_pelaajan_haku(self):
        syote = ["osa.json", "1", "John Klingberg" ,"0"]
        with patch('builtins.input', side_effect=syote):
            try:
                reload_module(self.module)
            except:
                self.fail(f"varmista että ohjelma toimii syötteellä\n{s(syote)}")

            output = get_stdout()
            self.assertFalse(len(output)==0,'Koodisi ei tulosta mitään. Eihän se vaan ole if __name__ == "__main__" -lohkon sisällä?')

            exp = """John Klingberg       DAL   6 + 26 =  32"""
            for rivi in exp.split("\n"):
                if not rivi in output:
                    self.fail(f"Ohjelman pitäisi tulostaa rivi\n{rivi}\nKun ohjelma suoritetaan syötteellä\n{s(syote)}\nTulostus oli\n{output}")   

    def test_05_joukkueiden_haku(self):
        syote = ["osa.json", "2" ,"0"]
        with patch('builtins.input', side_effect=syote):
            try:
                reload_module(self.module)
            except:
                self.fail(f"varmista että ohjelma toimii syötteellä\n{s(syote)}")

            output = get_stdout()
            self.assertFalse(len(output)==0,'Koodisi ei tulosta mitään. Eihän se vaan ole if __name__ == "__main__" -lohkon sisällä?')

            exp = """BUF
CGY
DAL
NJD
NYI
OTT
PIT
WPG
WSH"""
            for rivi in exp.split("\n"):
                if not rivi in output:
                    self.fail(f"Ohjelman pitäisi tulostaa rivi\n{rivi}\nKun ohjelma suoritetaan syötteellä\n{s(syote)}\nTulostus oli\n{output}")   
            
            output_lines = output.split('\n')
            exp_lines = exp.split("\n")
            n = output_lines.index(exp_lines[0])
            for i in range(len(exp_lines)):
                try:
                    oo = output_lines[n+i]
                except:
                    self.fail(f"Kun ohjelma suoritetaan syötteellä\n{s(syote)}\nTulostus \n{output}\nei ole oikeassa järjestyksessä, sen kuuluisi olla\n{exp}")  
                ee = exp_lines[i]
                self.assertEqual(oo, ee, f"Kun ohjelma suoritetaan syötteellä\n{s(syote)}\nTulostus \n{output}\nei ole oikeassa järjestyksessä, sen kuuluisi olla\n{exp}")  

    def test_06_maiden_haku(self):
        syote = ["osa.json", "3" ,"0"]
        with patch('builtins.input', side_effect=syote):
            try:
                reload_module(self.module)
            except:
                self.fail(f"varmista että ohjelma toimii syötteellä\n{s(syote)}")

            output = get_stdout()
            self.assertFalse(len(output)==0,'Koodisi ei tulosta mitään. Eihän se vaan ole if __name__ == "__main__" -lohkon sisällä?')

            exp = """CAN
CHE
CZE
SWE
USA"""
            for rivi in exp.split("\n"):
                if not rivi in output:
                    self.fail(f"Ohjelman pitäisi tulostaa rivi\n{rivi}\nKun ohjelma suoritetaan syötteellä\n{s(syote)}\nTulostus oli\n{output}")   
            
            output_lines = output.split('\n')
            exp_lines = exp.split("\n")
            n = output_lines.index(exp_lines[0])
            for i in range(len(exp_lines)):
                try:
                    oo = output_lines[n+i]
                except:
                    self.fail(f"Kun ohjelma suoritetaan syötteellä\n{s(syote)}\nTulostus \n{output}\nei ole oikeassa järjestyksessä, sen kuuluisi olla\n{exp}")  
                ee = exp_lines[i]
                self.assertEqual(oo, ee, f"Kun ohjelma suoritetaan syötteellä\n{s(syote)}\nTulostus \n{output}\nei ole oikeassa järjestyksessä, sen kuuluisi olla\n{exp}")  


    def test_07_pelaajan_haku_iso_syote_1(self):
        syote = ["kaikki.json", "1", "Mikko Koivu" ,"0"]
        with patch('builtins.input', side_effect=syote):
            try:
                reload_module(self.module)
            except:
                self.fail(f"varmista että ohjelma toimii syötteellä\n{s(syote)}")

            output = get_stdout()
            self.assertFalse(len(output)==0,'Koodisi ei tulosta mitään. Eihän se vaan ole if __name__ == "__main__" -lohkon sisällä?')

            exp = """Mikko Koivu          MIN   4 + 17 =  21"""
            for rivi in exp.split("\n"):
                if not rivi in output:
                    self.fail(f"Ohjelman pitäisi tulostaa rivi\n{rivi}\nKun ohjelma suoritetaan syötteellä\n{s(syote)}\nTulostus oli\n{output}")   

    def test_08_pelaajan_haku_iso_syote_2(self):
        syote = ["kaikki.json", "1", "Alex Ovechkin" ,"0"]
        with patch('builtins.input', side_effect=syote):
            try:
                reload_module(self.module)
            except:
                self.fail(f"varmista että ohjelma toimii syötteellä\n{s(syote)}")

            output = get_stdout()
            self.assertFalse(len(output)==0,'Koodisi ei tulosta mitään. Eihän se vaan ole if __name__ == "__main__" -lohkon sisällä?')

            exp = """Alex Ovechkin        WSH  48 + 19 =  67"""
            for rivi in exp.split("\n"):
                if not rivi in output:
                    self.fail(f"Ohjelman pitäisi tulostaa rivi\n{rivi}\nKun ohjelma suoritetaan syötteellä\n{s(syote)}\nTulostus oli\n{output}")   



    def test_09_joukkueiden_haku_iso_syota(self):
        syote = ["kaikki.json", "2" ,"0"]
        with patch('builtins.input', side_effect=syote):
            try:
                reload_module(self.module)
            except:
                self.fail(f"varmista että ohjelma toimii syötteellä\n{s(syote)}")

            output = get_stdout()
            self.assertFalse(len(output)==0,'Koodisi ei tulosta mitään. Eihän se vaan ole if __name__ == "__main__" -lohkon sisällä?')

            exp = """ANA
ARI
BOS
BUF
CAR
CBJ
CGY
CHI
COL
DAL
DET
EDM
FLA
LAK
MIN
MTL
NJD
NSH
NYI
NYR
OTT
PHI
PIT
SJS
STL
TBL
TOR
VAN
VGK
WPG
WSH"""
            for rivi in exp.split("\n"):
                if not rivi in output:
                    self.fail(f"Ohjelman pitäisi tulostaa rivi\n{rivi}\nKun ohjelma suoritetaan syötteellä\n{s(syote)}\nTulostus oli\n{output}")   
            
            output_lines = output.split('\n')
            exp_lines = exp.split("\n")
            n = output_lines.index(exp_lines[0])
            for i in range(len(exp_lines)):
                try:
                    oo = output_lines[n+i]
                except:
                    self.fail(f"Kun ohjelma suoritetaan syötteellä\n{s(syote)}\nTulostus \n{output}\nei ole oikeassa järjestyksessä, sen kuuluisi olla\n{exp}")  
                ee = exp_lines[i]
                self.assertEqual(oo, ee, f"Kun ohjelma suoritetaan syötteellä\n{s(syote)}\nTulostus \n{output}\nei ole oikeassa järjestyksessä, sen kuuluisi olla\n{exp}")  

    def test_10_maiden_haku_iso_syote(self):
        syote = ["kaikki.json", "3" ,"0"]
        with patch('builtins.input', side_effect=syote):
            try:
                reload_module(self.module)
            except:
                self.fail(f"varmista että ohjelma toimii syötteellä\n{s(syote)}")

            output = get_stdout()
            self.assertFalse(len(output)==0,'Koodisi ei tulosta mitään. Eihän se vaan ole if __name__ == "__main__" -lohkon sisällä?')

            exp = """AUS
AUT
CAN
CHE
CZE
DEU
DNK
FIN
FRA
GBR
LVA
NLD
NOR
RUS
SVK
SVN
SWE
UKR
USA"""
            for rivi in exp.split("\n"):
                if not rivi in output:
                    self.fail(f"Ohjelman pitäisi tulostaa rivi\n{rivi}\nKun ohjelma suoritetaan syötteellä\n{s(syote)}\nTulostus oli\n{output}")   
            
            output_lines = output.split('\n')
            exp_lines = exp.split("\n")
            n = output_lines.index(exp_lines[0])
            for i in range(len(exp_lines)):
                try:
                    oo = output_lines[n+i]
                except:
                    self.fail(f"Kun ohjelma suoritetaan syötteellä\n{s(syote)}\nTulostus \n{output}\nei ole oikeassa järjestyksessä, sen kuuluisi olla\n{exp}")  
                ee = exp_lines[i]
                self.assertEqual(oo, ee, f"Kun ohjelma suoritetaan syötteellä\n{s(syote)}\nTulostus \n{output}\nei ole oikeassa järjestyksessä, sen kuuluisi olla\n{exp}")  


if __name__ == '__main__':
    unittest.main()