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
        output += n + "\n"
    return output

class SuorituksetTest(unittest.TestCase):
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

    @points('12.suoritukset_osa1')
    def test_01_funktio_suorittajien_nimet_olemassa(self):
        try:
            from src.koodi import suorittajien_nimet
        except:
            self.assertTrue(False, "Ohjelmastasi pitäisi löytyä funktio nimeltä suorittajien_nimet(suoritukset: list)")

    @points('12.suoritukset_osa1')
    def test_02_suorittajien_nimet_paluuarvon_tyyppi(self):
        from src.koodi import suorittajien_nimet
        from src.koodi import Suoritus

        koodi = """
s1 = Suoritus("Pekka Python", "Ohjelmoinnin perusteet", 3)
s2 = Suoritus("Olivia Ohjelmoija", "Ohjelmoinnin perusteet", 5)
s3 = Suoritus("Pekka Python", "Ohjelmoinnin jatkokurssi", 2)
suorittajien_nimet([s1, s2, s3])
"""

        try:
            s1 = Suoritus("Pekka Python", "Ohjelmoinnin perusteet", 3)
            s2 = Suoritus("Olivia Ohjelmoija", "Ohjelmoinnin perusteet", 5)
            s3 = Suoritus("Pekka Python", "Ohjelmoinnin jatkokurssi", 2)
            vastaus = suorittajien_nimet([s1, s2, s3])
        except:
            self.fail(f"Varmista, että seuraavan koodin suoritus onnistuu\n{koodi}")

        m = map(None, [])
        taip = str(type(vastaus)).replace("<class '","").replace("'>","")
        self.assertTrue(type(vastaus) == type(m) or type(vastaus) == list, f"Funktion suorittajien_nimet(kurssit: list) tulee palauttaa map tai list, nyt palautettu arvo oli tyypiltään {taip}")
        for alkio in vastaus:
            etaip = str(type("")).replace("<class '","").replace("'>","")
            taip = str(type(alkio)).replace("<class '","").replace("'>","")
            self.assertTrue(type(alkio) == type(""),  f"Kun suoritetaan koodi {koodi}palautettujen alkioiden tulee olla tyypiltään {etaip} nyt niiden tyyppi on {taip}")
             
    @points('12.suoritukset_osa1')
    def test_03_suorittajien_nimet_toimii_1(self):
        from src.koodi import suorittajien_nimet
        from src.koodi import Suoritus

        koodi = """
s1 = Suoritus("Pekka Python", "Ohjelmoinnin perusteet", 3)
s2 = Suoritus("Olivia Ohjelmoija", "Ohjelmoinnin perusteet", 5)
s3 = Suoritus("Pekka Python", "Ohjelmoinnin jatkokurssi", 2)
suorittajien_nimet([s1, s2, s3])
"""

        try:
            s1 = Suoritus("Pekka Python", "Ohjelmoinnin perusteet", 3)
            s2 = Suoritus("Olivia Ohjelmoija", "Ohjelmoinnin perusteet", 5)
            s3 = Suoritus("Pekka Python", "Ohjelmoinnin jatkokurssi", 2)
            vastaus = suorittajien_nimet([s1, s2, s3])
        except:
            self.fail(f"Varmista, että seuraavan koodin suoritus onnistuu\n{koodi}")

        exp = [ s.opiskelijan_nimi for s in [s1, s2, s3]]

        output = ""
        vast = []
        for n in vastaus:
            output += n + "\n"
            vast.append(n)

        self.assertEquals(sorted(vast), sorted(exp),  f"Kun suoritetaan koodi {koodi}pitäisi palauttaa nimet \n{s(exp)}\nfunktio palautti\n{output}")

    @points('12.suoritukset_osa1')
    def test_04_suorittajien_nimet_map_kaytossa(self):
        src_file = os.path.join('src', 'koodi.py')
        lines = []
        p = False

        with open(src_file) as f:
            for line in f:
                if "def suorittajien_nimet"  in line:
                    p = True
                elif p and ('__name__ == "__main__":' in line or "def kurssien_nimet" in line):
                    p = False 
                elif p:
                    lines.append(line)

        on = False
        for line in lines:
            if "map" in line:
                on = True              
        self.assertTrue(on, f"Funktio suorittajien_nimet(suoritukset: list) on toteutettava map-funktion avulla")   

    @points('12.suoritukset_osa1')
    def test_05_suorittajien_nimet_toimii_2(self):
        from src.koodi import suorittajien_nimet
        from src.koodi import Suoritus

        koodi = """
s1 = Suoritus("Pekka Python", "Ohjelmoinnin perusteet", 3)
s2 = Suoritus("Olivia Ohjelmoija", "Ohjelmoinnin perusteet", 5)
s3 = Suoritus("Pekka Python", "Ohjelmoinnin jatkokurssi", 2)
s4 = Suoritus("Heikki Helastinen", "Ohjelmoinnin perusteet", 3)
s5 = Suoritus("Lady Gaga", "Ohjelmoinnin perusteet", 5)
s6 = Suoritus("Eila Karkki", "Ohjelmoinnin jatkokurssi", 2)

suorittajien_nimet([s1, s2, s3, s4, s5, s6])
"""

        try:
            s1 = Suoritus("Pekka Python", "Ohjelmoinnin perusteet", 3)
            s2 = Suoritus("Olivia Ohjelmoija", "Ohjelmoinnin perusteet", 5)
            s3 = Suoritus("Pekka Python", "Ohjelmoinnin jatkokurssi", 2)
            s4 = Suoritus("Heikki Helastinen", "Ohjelmoinnin perusteet", 3)
            s5 = Suoritus("Lady Gaga", "Ohjelmoinnin perusteet", 5)
            s6 = Suoritus("Eila Karkki", "Ohjelmoinnin jatkokurssi", 2)

            vastaus = suorittajien_nimet([s1, s2, s3, s4, s5, s6])
        except:
            self.fail(f"Varmista, että seuraavan koodin suoritus onnistuu\n{koodi}")

        exp = [ s.opiskelijan_nimi for s in [s1, s2, s3, s4, s5, s6]]

        output = ""
        vast = []
        for n in vastaus:
            output += n + "\n"
            vast.append(n)

        self.assertEquals(sorted(vast), sorted(exp),  f"Kun suoritetaan koodi {koodi}pitäisi palauttaa nimet \n{s(exp)}\nfunktio palautti\n{output}")

    @points('12.suoritukset_osa2')
    def test_06_funktio_kurssien_nimet_olemassa(self):
        try:
            from src.koodi import kurssien_nimet
        except:
            self.assertTrue(False, "Ohjelmastasi pitäisi löytyä funktio nimeltä kurssien_nimet(suoritukset: list)")

    @points('12.suoritukset_osa2')
    def test_07_kurssien_nimet_paluuarvon_tyyppi(self):
        from src.koodi import kurssien_nimet
        from src.koodi import Suoritus

        koodi = """
s1 = Suoritus("Pekka Python", "Ohjelmoinnin perusteet", 3)
s2 = Suoritus("Olivia Ohjelmoija", "Ohjelmoinnin perusteet", 5)
s3 = Suoritus("Pekka Python", "Ohjelmoinnin jatkokurssi", 2)
kurssien_nimet([s1, s2, s3])
"""

        try:
            s1 = Suoritus("Pekka Python", "Ohjelmoinnin perusteet", 3)
            s2 = Suoritus("Olivia Ohjelmoija", "Ohjelmoinnin perusteet", 5)
            s3 = Suoritus("Pekka Python", "Ohjelmoinnin jatkokurssi", 2)
            vastaus = kurssien_nimet([s1, s2, s3])
        except:
            self.fail(f"Varmista, että seuraavan koodin suoritus onnistuu\n{koodi}")

        m = map(None, [])
        taip = str(type(vastaus)).replace("<class '","").replace("'>","")
        self.assertTrue(type(vastaus) == type(m) or type(vastaus) == list or type(vastaus) == set, f"Funktion kurssien_nimet(kurssit: list) tulee palauttaa map tai list, nyt palautettu arvo oli tyypiltään {taip}")
        for alkio in vastaus:
            etaip = str(type("")).replace("<class '","").replace("'>","")
            taip = str(type(alkio)).replace("<class '","").replace("'>","")
            self.assertTrue(type(alkio) == type(""),  f"Kun suoritetaan koodi {koodi}palautettujen alkioiden tulee olla tyypiltään {etaip} nyt niiden tyyppi on {taip}")
     
    @points('12.suoritukset_osa2')
    def test_08_kurssien_nimet_toimii_1(self):
        from src.koodi import kurssien_nimet
        from src.koodi import Suoritus

        koodi = """
s1 = Suoritus("Pekka Python", "Ohjelmoinnin perusteet", 3)
s2 = Suoritus("Olivia Ohjelmoija", "Ohjelmoinnin perusteet", 5)
s3 = Suoritus("Pekka Python", "Ohjelmoinnin jatkokurssi", 2)
kurssien_nimet([s1, s2, s3])
"""

        try:
            s1 = Suoritus("Pekka Python", "Ohjelmoinnin perusteet", 3)
            s2 = Suoritus("Olivia Ohjelmoija", "Ohjelmoinnin perusteet", 5)
            s3 = Suoritus("Pekka Python", "Ohjelmoinnin jatkokurssi", 2)
            vastaus = kurssien_nimet([s1, s2, s3])
        except:
            self.fail(f"Varmista, että seuraavan koodin suoritus onnistuu\n{koodi}")

        m = map(None, [])
        taip = str(type(vastaus)).replace("<class '","").replace("'>","")
        self.assertTrue(type(vastaus) == type(m) or type(vastaus) == list or type(vastaus) == set, f"Funktion kurssien_nimet(kurssit: list) tulee palauttaa map tai list, nyt palautettu arvo oli tyypiltään {taip}")
        
        vastaus = list(vastaus)

        for alkio in vastaus:
            etaip = str(type("")).replace("<class '","").replace("'>","")
            taip = str(type(alkio)).replace("<class '","").replace("'>","")
            self.assertTrue(type(alkio) == type(""),  f"Kun suoritetaan koodi {koodi}palautettujen alkioiden tulee olla tyypiltään {etaip} nyt niiden tyyppi on {taip}")
     
        exp = sorted(set( s.kurssi for s in [s1, s2, s3]))

        output = ""
        vast = []
        for n in vastaus:
            output += n + "\n"
            vast.append(n)

        self.assertTrue(sorted(vast) == sorted(exp),  f"Kun suoritetaan koodi {koodi}pitäisi palauttaa kurssit \n{s(exp)}\nfunktio palautti\n{output}")

    @points('12.suoritukset_osa2')
    def test_09_kurssin_nimet_map_kaytossa(self):
        src_file = os.path.join('src', 'koodi.py')
        lines = []
        p = False

        with open(src_file) as f:
            for line in f:
                if "def kurssien_nimet"  in line:
                    p = True
                elif p and ('__name__ == "__main__":' in line or "def suorittajien_nimet" in line):
                    p = False 
                elif p:
                    lines.append(line)

        on = False
        for line in lines:
            if "map" in line:
                on = True              
        self.assertTrue(on, f"Funktio kurssien_nimet(suoritukset: list) on toteutettava map-funktion avulla")   

    @points('12.suoritukset_osa2')
    def test_10_kurssien_nimet_toimii_2(self):
        from src.koodi import kurssien_nimet
        from src.koodi import Suoritus

        koodi = """
s1 = Suoritus("Pekka Python", "Ohjelmoinnin perusteet", 3)
s2 = Suoritus("Olivia Ohjelmoija", "Ohjelmoinnin perusteet", 5)
s3 = Suoritus("Pekka Python", "Tietorakenteet", 2)
s4 = Suoritus("Heikki Helastinen", "Full stack -websovelluskehitys", 3)
s5 = Suoritus("Lady Gaga", "Ohjelmoinnin jatkokurssi", 5)
s6 = Suoritus("Eila Karkki", "Tietoliikenne 1", 2)

kurssien_nimet([s1, s2, s3, s4, s5, s6])
"""

        try:
            s1 = Suoritus("Pekka Python", "Ohjelmoinnin perusteet", 3)
            s2 = Suoritus("Olivia Ohjelmoija", "Ohjelmoinnin perusteet", 5)
            s3 = Suoritus("Pekka Python", "Tietorakenteet", 2)
            s4 = Suoritus("Heikki Helastinen", "Full stack -websovelluskehitys", 3)
            s5 = Suoritus("Lady Gaga", "Ohjelmoinnin jatkokurssi", 5)
            s6 = Suoritus("Eila Karkki", "Tietoliikenne 1", 2)

            vastaus = kurssien_nimet([s1, s2, s3, s4, s5, s6])
        except:
            self.fail(f"Varmista, että seuraavan koodin suoritus onnistuu\n{koodi}")

        exp = sorted(set( s.kurssi for s in [s1, s2, s3, s4, s5, s6]))

        output = ""
        vast = []
        for n in vastaus:
            output += n + "\n"
            vast.append(n)

        self.assertEquals(sorted(vast), sorted(exp),  f"Kun suoritetaan koodi {koodi}pitäisi palauttaa kurssit\n{s(exp)}\nfunktio palautti\n{output}")


if __name__ == '__main__':
    unittest.main()
