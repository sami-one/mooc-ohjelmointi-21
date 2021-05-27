import unittest
from unittest.mock import patch

from tmc import points, reflect
from tmc.utils import load, load_module, reload_module, get_stdout, check_source, sanitize
from functools import reduce
import os
import os.path
import textwrap
from random import choice, randint
from datetime import date, datetime, timedelta

exercise = 'src.koodi'

def f(attr: list):
    return ",".join(attr)

def s(vastaus):
    output = ""
    for n in vastaus:
        output += f"{n}\n"
    return output

class RajatutSuorituksetTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=[AssertionError("Syötteen pyytämistä ei odotettu")]):
           cls.module = load_module(exercise, 'fi')

    def test_00a_paaohjelma_kunnossa(self):
        ok, line = check_source(self.module)
        message = """Funktioita testaava koodi tulee sijoittaa lohkon
if __name__ == "__main__":
sisälle. Seuraava rivi tulee siirtää:
"""
        self.assertTrue(ok, message+line)

    @points('12.rajatut_suoritukset_osa1')
    def test_01_funktio_hyvaksytyt_olemassa(self):
        try:
            from src.koodi import hyvaksytyt
        except:
            self.assertTrue(False, "Ohjelmastasi pitäisi löytyä funktio nimeltä hyvaksytyt(suoritukset: list)")

    @points('12.rajatut_suoritukset_osa1')
    def test_2_hyvaksytyt_paluuarvon_tyyppi(self):
        from src.koodi import hyvaksytyt
        from src.koodi import Suoritus

        koodi = """
s1 = Suoritus("Pekka Python", "Ohjelmoinnin perusteet", 3)
s2 = Suoritus("Olivia Ohjelmoija", "Ohjelmoinnin perusteet", 5)
s3 = Suoritus("Pekka Python", "Ohjelmoinnin jatkokurssi", 0)
hyvaksytyt([s1, s2, s3])
"""

        try:
            s1 = Suoritus("Pekka Python", "Ohjelmoinnin perusteet", 3)
            s2 = Suoritus("Olivia Ohjelmoija", "Ohjelmoinnin perusteet", 5)
            s3 = Suoritus("Pekka Python", "Ohjelmoinnin jatkokurssi", 0)
            vastaus = hyvaksytyt([s1, s2, s3])
        except:
            self.fail(f"Varmista, että seuraavan koodin suoritus onnistuu\n{koodi}")

        m = filter(None, [])
        taip = str(type(vastaus)).replace("<class '","").replace("'>","")
        self.assertTrue(type(vastaus) == type(m) or type(vastaus) == list, f"Funktion suorittajien_nimet(kurssit: list) tulee palauttaa filter tai list, nyt palautettu arvo oli tyypiltään {taip}")
        for alkio in vastaus:
            etaip = str(type(s2)).replace("<class '","").replace("'>","").replace("src.koodi.", "")
            taip = str(type(alkio)).replace("<class '","").replace("'>","")
            self.assertTrue(type(alkio) == type(s2),  f"Kun suoritetaan koodi {koodi}palautettujen alkioiden tulee olla tyypiltään {etaip} nyt niiden tyyppi on {taip}")
             
    @points('12.rajatut_suoritukset_osa1')
    def test_03_hyvaksytyt_toimii_1(self):
        from src.koodi import hyvaksytyt
        from src.koodi import Suoritus

        koodi = """
s1 = Suoritus("Pekka Python", "Ohjelmoinnin perusteet", 3)
s2 = Suoritus("Olivia Ohjelmoija", "Ohjelmoinnin perusteet", 5)
s3 = Suoritus("Pekka Python", "Ohjelmoinnin jatkokurssi", 0)
hyvaksytyt([s1, s2, s3])
"""

        try:
            s1 = Suoritus("Pekka Python", "Ohjelmoinnin perusteet", 3)
            s2 = Suoritus("Olivia Ohjelmoija", "Ohjelmoinnin perusteet", 5)
            s3 = Suoritus("Pekka Python", "Ohjelmoinnin jatkokurssi", 0)
            vastaus = hyvaksytyt([s1, s2, s3])
        except:
            self.fail(f"Varmista, että seuraavan koodin suoritus onnistuu\n{koodi}")

        exp = [ s1, s2 ]

        output = ""
        vast = []
        for n in vastaus:
            output += f"{n}\n"
            vast.append(n)

        def nimi(s):
            return s.kurssi

        self.assertEquals(sorted(vast, key=nimi), sorted(exp,key=nimi),  f"Kun suoritetaan koodi {koodi}pitäisi palauttaa \n{s(exp)}\nfunktio palautti\n{output}")

    @points('12.rajatut_suoritukset_osa1')
    def test_04_hyvaksytyt_filter_kaytossa(self):
        src_file = os.path.join('src', 'koodi.py')
        lines = []
        p = False

        with open(src_file) as f:
            for line in f:
                if "def hyvaksytyt"  in line:
                    p = True
                elif p and ('__name__ == "__main__":' in line or "def suoritus_arvosanalla" in line or "def kurssin_suorittajat" in line):
                    p = False 
                elif p:
                    lines.append(line)

        vaadittu = [
            "filter(",
        ]

        for v in vaadittu:
            on = False
            for line in lines:
                if v in line:
                    on = True              
            self.assertTrue(on, f"Funktio hyvaksytyt(suoritukset: list) on toteutettava filter-funktion avulla")          

    @points('12.rajatut_suoritukset_osa1')
    def test_05_hyvaksytyt_toimii_2(self):
        from src.koodi import hyvaksytyt
        from src.koodi import Suoritus

        koodi = """
s1 = Suoritus("Pekka Python", "Ohjelmoinnin perusteet", 3)
s2 = Suoritus("Olivia Ohjelmoija", "Ohjelmoinnin perusteet", 5)
s3 = Suoritus("Pekka Python", "Ohjelmoinnin jatkokurssi", 0)
s4 = Suoritus("Heikki Helastinen", "Ohjelmoinnin perusteet", 3)
s5 = Suoritus("Lady Gaga", "Ohjelmoinnin perusteet", 0)
s6 = Suoritus("Eila Karkki", "Ohjelmoinnin jatkokurssi", 2)

hyvaksytyt([s1, s2, s3, s4, s5, s6])
"""

        try:
            s1 = Suoritus("Pekka Python", "Ohjelmoinnin perusteet", 3)
            s2 = Suoritus("Olivia Ohjelmoija", "Ohjelmoinnin perusteet", 5)
            s3 = Suoritus("Pekka Python", "Ohjelmoinnin jatkokurssi", 0)
            s4 = Suoritus("Heikki Helastinen", "Ohjelmoinnin perusteet", 3)
            s5 = Suoritus("Lady Gaga", "Ohjelmoinnin perusteet", 0)
            s6 = Suoritus("Eila Karkki", "Ohjelmoinnin jatkokurssi", 2)

            vastaus = hyvaksytyt([s1, s2, s3, s4, s5, s6])
        except:
            self.fail(f"Varmista, että seuraavan koodin suoritus onnistuu\n{koodi}")

        exp = [s1, s2, s4, s6]

        output = ""
        vast = []
        for n in vastaus:
            output += f"{n}\n"
            vast.append(n)

        def nimi(s):
            return s.kurssi

        self.assertEquals(sorted(vast, key=nimi), sorted(exp,key=nimi),  f"Kun suoritetaan koodi {koodi}pitäisi palauttaa \n{s(exp)}\nfunktio palautti\n{output}")

    @points('12.rajatut_suoritukset_osa2')
    def test_06_funktio_suoritus_arvosanalla_olemassa(self):
        try:
            from src.koodi import suoritus_arvosanalla
        except:
            self.assertTrue(False, "Ohjelmastasi pitäisi löytyä funktio nimeltä suoritus_arvosanalla(suoritukset: list, arvosana: int) ")

    @points('12.rajatut_suoritukset_osa2')
    def test_07_suoritus_arvosanalla_tyyppi(self):
        from src.koodi import suoritus_arvosanalla
        from src.koodi import Suoritus

        koodi = """
s1 = Suoritus("Pekka Python", "Ohjelmoinnin perusteet", 3)
s2 = Suoritus("Olivia Ohjelmoija", "Ohjelmoinnin perusteet", 5)
s3 = Suoritus("Pekka Python", "Ohjelmoinnin jatkokurssi", 3)
suoritus_arvosanalla([s1, s2, s3], 3)
"""

        try:
            s1 = Suoritus("Pekka Python", "Ohjelmoinnin perusteet", 3)
            s2 = Suoritus("Olivia Ohjelmoija", "Ohjelmoinnin perusteet", 5)
            s3 = Suoritus("Pekka Python", "Ohjelmoinnin jatkokurssi", 3)
            vastaus = suoritus_arvosanalla([s1, s2, s3], 3)
            
        except:
            self.fail(f"Varmista, että seuraavan koodin suoritus onnistuu\n{koodi}")

        m = filter(None, [])
        taip = str(type(vastaus)).replace("<class '","").replace("'>","")
        self.assertTrue(type(vastaus) == type(m) or type(vastaus) == list, f"Funktion suoritus_arvosanalla(kurssit: list, arvosana: int) tulee palauttaa filter tai list, nyt palautettu arvo oli tyypiltään {taip}")
        for alkio in vastaus:
            etaip = str(type(s2)).replace("<class '","").replace("'>","").replace("src.koodi.", "")
            taip = str(type(alkio)).replace("<class '","").replace("'>","")
            self.assertTrue(type(alkio) == type(s2),  f"Kun suoritetaan koodi {koodi}palautettujen alkioiden tulee olla tyypiltään {etaip} nyt niiden tyyppi on {taip}")
            
    @points('12.rajatut_suoritukset_osa2')
    def test_08_suoritus_arvosanalla_toimii_1(self):
        from src.koodi import suoritus_arvosanalla
        from src.koodi import Suoritus

        koodi = """
s1 = Suoritus("Pekka Python", "Ohjelmoinnin perusteet", 3)
s2 = Suoritus("Olivia Ohjelmoija", "Ohjelmoinnin perusteet", 5)
s3 = Suoritus("Pekka Python", "Ohjelmoinnin jatkokurssi", 3)
suoritus_arvosanalla([s1, s2, s3], 3)
"""

        try:
            s1 = Suoritus("Pekka Python", "Ohjelmoinnin perusteet", 3)
            s2 = Suoritus("Olivia Ohjelmoija", "Ohjelmoinnin perusteet", 5)
            s3 = Suoritus("Pekka Python", "Ohjelmoinnin jatkokurssi", 3)
            vastaus = suoritus_arvosanalla([s1, s2, s3], 3)
            
        except:
            self.fail(f"Varmista, että seuraavan koodin suoritus onnistuu\n{koodi}")

        exp = [ s1, s3 ]

        output = ""
        vast = []
        for n in vastaus:
            output += f"{n}\n"
            vast.append(n)

        def nimi(s):
            return s.kurssi

        self.assertEquals(sorted(vast, key=nimi), sorted(exp,key=nimi),  f"Kun suoritetaan koodi {koodi}pitäisi palauttaa \n{s(exp)}\nfunktio palautti\n{output}")

    @points('12.rajatut_suoritukset_osa2')
    def test_09_suoritus_arvosanalla_filter_kaytossa(self):
        src_file = os.path.join('src', 'koodi.py')
        lines = []
        p = False

        with open(src_file) as f:
            for line in f:
                if "def suoritus_arvosanalla"  in line:
                    p = True
                elif p and ('__name__ == "__main__":' in line or "def hyvaksytyt" in line or "def kurssin_suorittajat" in line): 
                    p = False 
                elif p:
                    lines.append(line)

        vaadittu = [
            "filter(",
        ]

        for v in vaadittu:
            on = False
            for line in lines:
                if v in line:
                    on = True              
            self.assertTrue(on, f"Funktio suoritus_arvosanalla(kurssit: list, arvosana: int) on toteutettava filter-funktion avulla")          

    @points('12.rajatut_suoritukset_osa2')
    def test_10_suoritus_arvosanalla_toimii_2(self):
        from src.koodi import suoritus_arvosanalla
        from src.koodi import Suoritus

        koodi = """
s1 = Suoritus("Pekka Python", "Ohjelmoinnin perusteet", 3)
s2 = Suoritus("Olivia Ohjelmoija", "Ohjelmoinnin perusteet", 5)
s3 = Suoritus("Pekka Python", "Ohjelmoinnin jatkokurssi", 0)
s4 = Suoritus("Heikki Helastinen", "Ohjelmoinnin perusteet", 3)
s5 = Suoritus("Lady Gaga", "Ohjelmoinnin perusteet", 0)
s6 = Suoritus("Eila Karkki", "Ohjelmoinnin jatkokurssi", 3)

suoritus_arvosanalla([s1, s2, s3, s4, s5, s6].)
"""

        try:
            s1 = Suoritus("Pekka Python", "Ohjelmoinnin perusteet", 3)
            s2 = Suoritus("Olivia Ohjelmoija", "Ohjelmoinnin perusteet", 5)
            s3 = Suoritus("Pekka Python", "Ohjelmoinnin jatkokurssi", 0)
            s4 = Suoritus("Heikki Helastinen", "Ohjelmoinnin perusteet", 3)
            s5 = Suoritus("Lady Gaga", "Ohjelmoinnin perusteet", 0)
            s6 = Suoritus("Eila Karkki", "Ohjelmoinnin jatkokurssi", 3)

            vastaus = suoritus_arvosanalla([s1, s2, s3, s4, s5, s6], 3)
        except:
            self.fail(f"Varmista, että seuraavan koodin suoritus onnistuu\n{koodi}")

        exp = [s1, s4, s6]

        output = ""
        vast = []
        for n in vastaus:
            output += f"{n}\n"
            vast.append(n)

        def nimi(s):
            return s.kurssi

        self.assertEquals(sorted(vast, key=nimi), sorted(exp,key=nimi),  f"Kun suoritetaan koodi {koodi}pitäisi palauttaa \n{s(exp)}\nfunktio palautti\n{output}")


    @points('12.rajatut_suoritukset_osa3')
    def test_11_funktio_kurssin_suorittajat_olemassa(self):
        try:
            from src.koodi import kurssin_suorittajat
        except:
            self.assertTrue(False, "Ohjelmastasi pitäisi löytyä funktio nimeltä kurssin_suorittajat(suoritukset: list, kurssi: str) ")

    @points('12.rajatut_suoritukset_osa3')
    def test_12_kurssin_suorittajat_tyyppi(self):
        from src.koodi import kurssin_suorittajat
        from src.koodi import Suoritus

        koodi = """
s1 = Suoritus("Pekka Python", "Ohjelmoinnin perusteet", 3)
s2 = Suoritus("Olivia Ohjelmoija", "Ohjelmoinnin perusteet", 5)
s3 = Suoritus("Pekka Python", "Ohjelmoinnin jatkokurssi", 3)
s4 = Suoritus("Niilo Nörtti", "Tietoliikenteen perusteet", 3)
kurssin_suorittajat([s1, s2, s3, s4], "Ohjelmoinnin perusteet")

"""

        try:
            s1 = Suoritus("Pekka Python", "Ohjelmoinnin perusteet", 3)
            s2 = Suoritus("Olivia Ohjelmoija", "Ohjelmoinnin perusteet", 5)
            s3 = Suoritus("Pekka Python", "Ohjelmoinnin jatkokurssi", 3)
            s4 = Suoritus("Niilo Nörtti", "Tietoliikenteen perusteet", 3)
            vastaus = kurssin_suorittajat([s1, s2, s3, s4], "Ohjelmoinnin perusteet")
            
        except:
            self.fail(f"Varmista, että seuraavan koodin suoritus onnistuu\n{koodi}")

        m = filter(None, [])
        m2 = map(None, [])
        taip = str(type(vastaus)).replace("<class '","").replace("'>","")
        self.assertTrue(type(vastaus) == type(m2) or type(vastaus) == type(m) or type(vastaus) == list, f"Funktion suoritus_arvosanalla(kurssit: list, arvosana: int) tulee palauttaa filter tai list, nyt palautettu arvo oli tyypiltään {taip}")
        for alkio in vastaus:
            etaip = "str"
            taip = str(type(alkio)).replace("<class '","").replace("'>","")
            self.assertTrue(type(alkio) == type(""),  f"Kun suoritetaan koodi {koodi}palautettujen alkioiden tulee olla tyypiltään {etaip} nyt niiden tyyppi on {taip}")
            
    @points('12.rajatut_suoritukset_osa3')
    def test_13_kurssin_suorittajat_toimii_1(self):
        from src.koodi import kurssin_suorittajat
        from src.koodi import Suoritus

        koodi = """
s1 = Suoritus("Pekka Python", "Ohjelmoinnin perusteet", 3)
s2 = Suoritus("Olivia Ohjelmoija", "Ohjelmoinnin perusteet", 5)
s3 = Suoritus("Pekka Python", "Ohjelmoinnin jatkokurssi", 3)
s4 = Suoritus("Niilo Nörtti", "Tietoliikenteen perusteet", 3)
kurssin_suorittajat([s1, s2, s3, s4], "Ohjelmoinnin perusteet")

"""

        try:
            s1 = Suoritus("Pekka Python", "Ohjelmoinnin perusteet", 3)
            s2 = Suoritus("Olivia Ohjelmoija", "Ohjelmoinnin perusteet", 5)
            s3 = Suoritus("Pekka Python", "Ohjelmoinnin jatkokurssi", 3)
            s4 = Suoritus("Niilo Nörtti", "Tietoliikenteen perusteet", 3)
            vastaus = kurssin_suorittajat([s1, s2, s3, s4], "Ohjelmoinnin perusteet")
            
        except:
            self.fail(f"Varmista, että seuraavan koodin suoritus onnistuu\n{koodi}")

        exp = ["Olivia Ohjelmoija", "Pekka Python"]

        output = ""
        vast = []
        for n in vastaus:
            output += f"{n}\n"
            vast.append(n)

        self.assertEquals(vast, exp,  f"Kun suoritetaan koodi {koodi}pitäisi palauttaa \n{s(exp)}\nfunktio palautti\n{output}")

    @points('12.rajatut_suoritukset_osa3')
    def test_14_kurssin_suorittajat_map_ja_filter_kaytossa(self):
        src_file = os.path.join('src', 'koodi.py')
        lines = []
        p = False

        with open(src_file) as f:
            for line in f:
                if "def kurssin_suorittajat"  in line:
                    p = True
                elif p and ('__name__ == "__main__":' in line or "def suoritus_arvosanalla" in line or "def hyvaksytyt" in line):
                    p = False 
                elif p:
                    lines.append(line)

        vaadittu = [
            "filter(",
            "map"
        ]

        for v in vaadittu:
            on = False
            for line in lines:
                if v in line:
                    on = True              
            self.assertTrue(on, f"Funktio kurssin_suorittajat(suoritukset: list, kurssi: str) on toteutettava map- ja filter-funktioiden avulla")          

    @points('12.rajatut_suoritukset_osa3')
    def test_15_kurssin_suorittajat_toimii_2(self):
        from src.koodi import kurssin_suorittajat
        from src.koodi import Suoritus

        koodi = """
s1 = Suoritus("Pekka Python", "Ohjelmoinnin perusteet", 3)
s2 = Suoritus("Yomi Cosa", "Tietoliikenteen perusteet", 5)
s3 = Suoritus("Pekka Python", "Tietorakenteet", 2)
s4 = Suoritus("Olivia Ohjelmoija", "Ohjelmoinnin perusteet", 5)
s5 = Suoritus("Pekka Python", "Ohjelmoinnin jatkokurssi", 3)
s6 = Suoritus("Niilo Nörtti", "Tietoliikenteen perusteet", 3)
s7 = Suoritus("Pekka Python", "Tietoliikenteen perusteet", 0)
kurssin_suorittajat([s1, s2, s3, s4, s5, s6, s7], "Tietoliikenteen perusteet")

"""

        try:
            s1 = Suoritus("Pekka Python", "Ohjelmoinnin perusteet", 3)
            s2 = Suoritus("Yomi Cosa", "Tietoliikenteen perusteet", 5)
            s3 = Suoritus("Pekka Python", "Tietorakenteet", 2)
            s4 = Suoritus("Olivia Ohjelmoija", "Ohjelmoinnin perusteet", 5)
            s5 = Suoritus("Pekka Python", "Ohjelmoinnin jatkokurssi", 3)
            s6 = Suoritus("Niilo Nörtti", "Tietoliikenteen perusteet", 3)
            s7 = Suoritus("Pekka Python", "Tietoliikenteen perusteet", 0)
            vastaus = kurssin_suorittajat([s1, s2, s3, s4, s5, s6, s7], "Tietoliikenteen perusteet")
            
        except:
            self.fail(f"Varmista, että seuraavan koodin suoritus onnistuu\n{koodi}")

        exp = ["Niilo Nörtti", "Yomi Cosa"]

        output = ""
        vast = []
        for n in vastaus:
            output += f"{n}\n"
            vast.append(n)

        self.assertEquals(vast, exp,  f"Kun suoritetaan koodi {koodi}pitäisi palauttaa \n{s(exp)}\nfunktio palautti\n{output}")


if __name__ == '__main__':
    unittest.main()
