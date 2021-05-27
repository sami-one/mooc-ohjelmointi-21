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

class OpintopisteettTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=[AssertionError("Syötteen pyytämistä ei odotettu")]):
           cls.module = load_module(exercise, 'fi')

    def test_00_paaohjelma_kunnossa(self):
        ok, line = check_source(self.module)
        message = """Funktioita testaava koodi tulee sijoittaa lohkon
if __name__ == "__main__":
sisälle. Seuraava rivi tulee siirtää:
"""
        self.assertTrue(ok, message+line)

    @points('12.opintopisteet_osa1')
    def test_01_funktio_kaikkien_opintopisteiden_summa_olemassa(self):
        try:
            from src.koodi import kaikkien_opintopisteiden_summa
        except:
            self.assertTrue(False, "Ohjelmastasi pitäisi löytyä funktio nimeltä kaikkien_opintopisteiden_summa(suoritukset: list)")

    @points('12.opintopisteet_osa1')
    def test_02_hkaikkien_opintopisteiden_summa_tyyppi(self):
        from src.koodi import kaikkien_opintopisteiden_summa
        from src.koodi import Suoritus

        koodi = """
s1 = Suoritus("Ohjelmoinnin perusteet", 5, 5)
s2 = Suoritus("Ohjelmoinnin jatkokurssi", 4, 5)
s3 = Suoritus("Tietorakenteet ja algoritmit", 3, 10)
kaikkien_opintopisteiden_summa([s1, s2, s3])
"""

        try:
            s1 = Suoritus("Ohjelmoinnin perusteet", 5, 5)
            s2 = Suoritus("Ohjelmoinnin jatkokurssi", 4, 5)
            s3 = Suoritus("Tietorakenteet ja algoritmit", 3, 10)
            vastaus = kaikkien_opintopisteiden_summa([s1, s2, s3])
        except:
            self.fail(f"Varmista, että seuraavan koodin suoritus onnistuu\n{koodi}")

        taip = str(type(vastaus)).replace("<class '","").replace("'>","")
        self.assertTrue(type(vastaus) == int, f"Funktion kaikkien_opintopisteiden_summa(kurssit: list) tulee palauttaa int, nyt palautettu arvo oli tyypiltään {taip}")

    @points('12.opintopisteet_osa1')
    def test_03_kaikkien_opintopisteiden_summa_toimii_1(self):
        from src.koodi import kaikkien_opintopisteiden_summa
        from src.koodi import Suoritus

        koodi = """
s1 = Suoritus("Ohjelmoinnin perusteet", 5, 5)
s2 = Suoritus("Ohjelmoinnin jatkokurssi", 4, 5)
s3 = Suoritus("Tietorakenteet ja algoritmit", 3, 10)
kaikkien_opintopisteiden_summa([s1, s2, s3])
"""

        try:
            s1 = Suoritus("Ohjelmoinnin perusteet", 5, 5)
            s2 = Suoritus("Ohjelmoinnin jatkokurssi", 4, 5)
            s3 = Suoritus("Tietorakenteet ja algoritmit", 3, 10)
            vastaus = kaikkien_opintopisteiden_summa([s1, s2, s3])
        except:
            self.fail(f"Varmista, että seuraavan koodin suoritus onnistuu\n{koodi}")

        exp = 20

        self.assertEquals(vastaus, exp,  f"Kun suoritetaan koodi {koodi}pitäisi palauttaa\n{exp}\nfunktio palautti\n{vastaus}")

    @points('12.opintopisteet_osa1')
    def test_04_opintopisteiden_summa_reduce_kaytossa(self):
        src_file = os.path.join('src', 'koodi.py')
        lines = []
        p = False

        with open(src_file) as f:
            for line in f:
                if "def kaikkien_opintopisteiden_summa"  in line:
                    p = True
                elif p and ('__name__ == "__main__":' in line or "def hyvaksyttyjen_opintopisteiden_summa" in line or "def keskiarvo" in line):
                    p = False 
                elif p:
                    lines.append(line)

        vaadittu = [
            "reduce(",
        ]

        for v in vaadittu:
            on = False
            for line in lines:
                if v in line:
                    on = True              
            self.assertTrue(on, f"Funktio kaikkien_opintopisteiden_summa(kurssit: list) on toteutettava reduce-funktion avulla")          

    @points('12.opintopisteet_osa1')
    def test_05_kaikkien_opintopisteiden_summa_toimii_2(self):
        from src.koodi import kaikkien_opintopisteiden_summa
        from src.koodi import Suoritus

        koodi = """
s1 = Suoritus("Ohjelmoinnin perusteet", 5, 5)
s2 = Suoritus("Ohjelmoinnin jatkokurssi", 4, 5)
s3 = Suoritus("Tietorakenteet ja algoritmit", 3, 10)
s4 = Suoritus("Full stack -websovelluskehitys", 4, 8)
s5 = Suoritus("DevOps with Docker", 5, 3)
s6 = Suoritus("Toinen kotimainen kieli", 0, 2)
kaikkien_opintopisteiden_summa([s1, s2, s3, s4, s5, s6])
"""

        try:
            s1 = Suoritus("Ohjelmoinnin perusteet", 5, 5)
            s2 = Suoritus("Ohjelmoinnin jatkokurssi", 4, 5)
            s3 = Suoritus("Tietorakenteet ja algoritmit", 3, 10)
            s4 = Suoritus("Full stack -websovelluskehitys", 4, 8)
            s5 = Suoritus("DevOps with Docker", 5, 3)
            s6 = Suoritus("Toinen kotimainen kieli", 0, 2)
            vastaus = kaikkien_opintopisteiden_summa([s1, s2, s3, s4, s5, s6])
        except:
            self.fail(f"Varmista, että seuraavan koodin suoritus onnistuu\n{koodi}")

        exp = 33

        self.assertEquals(vastaus, exp,  f"Kun suoritetaan koodi {koodi}pitäisi palauttaa\n{exp}\nfunktio palautti\n{vastaus}")

    @points('12.opintopisteet_osa2')
    def test_06_funktio_hyvaksyttyjen_opintopisteiden_summa_olemassa(self):
        try:
            from src.koodi import hyvaksyttyjen_opintopisteiden_summa
        except:
            self.assertTrue(False, "Ohjelmastasi pitäisi löytyä funktio nimeltä hyvaksyttyjen_opintopisteiden_summa(suoritukset: list)")

    @points('12.opintopisteet_osa2')
    def test_07_hyvaksyttyjen_opintopisteiden_summa_tyyppi(self):
        from src.koodi import hyvaksyttyjen_opintopisteiden_summa
        from src.koodi import Suoritus

        koodi = """
s1 = Suoritus("Ohjelmoinnin perusteet", 5, 5)
s2 = Suoritus("Ohjelmoinnin jatkokurssi", 4, 5)
s3 = Suoritus("Tietorakenteet ja algoritmit", 3, 0)
kaikkien_opintopisteiden_summa([s1, s2, s3])
"""

        try:
            s1 = Suoritus("Ohjelmoinnin perusteet", 5, 5)
            s2 = Suoritus("Ohjelmoinnin jatkokurssi", 4, 5)
            s3 = Suoritus("Tietorakenteet ja algoritmit", 3, 10)
            vastaus = hyvaksyttyjen_opintopisteiden_summa([s1, s2, s3])
        except:
            self.fail(f"Varmista, että seuraavan koodin suoritus onnistuu\n{koodi}")

        taip = str(type(vastaus)).replace("<class '","").replace("'>","")
        self.assertTrue(type(vastaus) == int, f"Funktion hyvaksyttyjen_opintopisteiden_summa(kurssit: list) tulee palauttaa int, nyt palautettu arvo oli tyypiltään {taip}")

    @points('12.opintopisteet_osa2')
    def test_08_hyvaksyttyjen_opintopisteiden_summa_toimii_1(self):
        from src.koodi import hyvaksyttyjen_opintopisteiden_summa
        from src.koodi import Suoritus

        koodi = """
s1 = Suoritus("Ohjelmoinnin perusteet", 5, 5)
s2 = Suoritus("Ohjelmoinnin jatkokurssi", 4, 5)
s3 = Suoritus("Tietorakenteet ja algoritmit", 0, 10)
hyvaksyttyjen_opintopisteiden_summa([s1, s2, s3])
"""

        try:
            s1 = Suoritus("Ohjelmoinnin perusteet", 5, 5)
            s2 = Suoritus("Ohjelmoinnin jatkokurssi", 4, 5)
            s3 = Suoritus("Tietorakenteet ja algoritmit", 0, 10)
            vastaus = hyvaksyttyjen_opintopisteiden_summa([s1, s2, s3])
        except:
            self.fail(f"Varmista, että seuraavan koodin suoritus onnistuu\n{koodi}")

        exp = 10

        self.assertEquals(vastaus, exp,  f"Kun suoritetaan koodi {koodi}pitäisi palauttaa\n{exp}\nfunktio palautti\n{vastaus}")


    @points('12.opintopisteet_osa2')
    def test_09_opintopisteiden_summa_reduce_kaytossa(self):
        src_file = os.path.join('src', 'koodi.py')
        lines = []
        p = False

        with open(src_file) as f:
            for line in f:
                if "def hyvaksyttyjen_opintopisteiden_summa"  in line:
                    p = True
                elif p and ('__name__ == "__main__":' in line or "def kaikkien_opintopisteiden_summa" in line or "def keskiarvo" in line):
                    p = False 
                elif p:
                    lines.append(line)

        vaadittu = [
            "reduce(",
            "filter"
        ]

        for v in vaadittu:
            on = False
            for line in lines:
                if v in line:
                    on = True              
            self.assertTrue(on, f"Funktio hyvaksyttyjen_opintopisteiden_summa(kurssit: list) on toteutettava filter- ja reduce-funktioiden avulla")          

    @points('12.opintopisteet_osa2')
    def test_10_hyvaksyttyjen_opintopisteiden_summa_toimii_2(self):
        from src.koodi import hyvaksyttyjen_opintopisteiden_summa
        from src.koodi import Suoritus

        koodi = """
s1 = Suoritus("Ohjelmoinnin perusteet", 5, 5)
s2 = Suoritus("Ohjelmoinnin jatkokurssi", 4, 5)
s3 = Suoritus("Tietorakenteet ja algoritmit", 0, 10)
s4 = Suoritus("Full stack -websovelluskehitys", 4, 8)
s5 = Suoritus("DevOps with Docker", 5, 3)
s6 = Suoritus("Toinen kotimainen kieli", 0, 2)
hyvaksyttyjen_opintopisteiden_summa([s1, s2, s3, s4, s5, s6])
"""

        try:
            s1 = Suoritus("Ohjelmoinnin perusteet", 5, 5)
            s2 = Suoritus("Ohjelmoinnin jatkokurssi", 4, 5)
            s3 = Suoritus("Tietorakenteet ja algoritmit", 0, 10)
            s4 = Suoritus("Full stack -websovelluskehitys", 4, 8)
            s5 = Suoritus("DevOps with Docker", 5, 3)
            s6 = Suoritus("Toinen kotimainen kieli", 0, 2)
            vastaus = hyvaksyttyjen_opintopisteiden_summa([s1, s2, s3, s4, s5, s6])
            
        except:
            self.fail(f"Varmista, että seuraavan koodin suoritus onnistuu\n{koodi}")

        exp = 21

        self.assertEquals(vastaus, exp,  f"Kun suoritetaan koodi {koodi}pitäisi palauttaa\n{exp}\nfunktio palautti\n{vastaus}")

    @points('12.opintopisteet_osa3')
    def test_11_funktio_keskiarvo_olemassa(self):
        try:
            from src.koodi import keskiarvo
        except:
            self.assertTrue(False, "Ohjelmastasi pitäisi löytyä funktio nimeltä keskiarvo(suoritukset: list)")

    @points('12.opintopisteet_osa3')
    def test_12_keskiarvo_tyyppi(self):
        from src.koodi import keskiarvo
        from src.koodi import Suoritus

        koodi = """
s1 = Suoritus("Ohjelmoinnin perusteet", 5, 5)
s2 = Suoritus("Ohjelmoinnin jatkokurssi", 4, 5)
s3 = Suoritus("Tietorakenteet ja algoritmit", 3, 0)
keskiarvo([s1, s2, s3])
"""

        try:
            s1 = Suoritus("Ohjelmoinnin perusteet", 5, 5)
            s2 = Suoritus("Ohjelmoinnin jatkokurssi", 4, 5)
            s3 = Suoritus("Tietorakenteet ja algoritmit", 3, 10)
            vastaus = keskiarvo([s1, s2, s3])
        except:
            self.fail(f"Varmista, että seuraavan koodin suoritus onnistuu\n{koodi}")

        taip = str(type(vastaus)).replace("<class '","").replace("'>","")
        self.assertTrue(type(vastaus) == float or type(vastaus) == int, f"Funktion keskiarvo(kurssit: list) tulee palauttaa int tai float, nyt palautettu arvo oli tyypiltään {taip}")

    @points('12.opintopisteet_osa3')
    def test_13_keskiarvo_toimii_1(self):
        from src.koodi import keskiarvo
        from src.koodi import Suoritus

        koodi = """
s1 = Suoritus("Ohjelmoinnin perusteet", 5, 5)
s2 = Suoritus("Ohjelmoinnin jatkokurssi", 4, 5)
s3 = Suoritus("Tietorakenteet ja algoritmit", 3, 10)
keskiarvo([s1, s2, s3])
"""

        try:
            s1 = Suoritus("Ohjelmoinnin perusteet", 5, 5)
            s2 = Suoritus("Ohjelmoinnin jatkokurssi", 4, 5)
            s3 = Suoritus("Tietorakenteet ja algoritmit", 3, 10)
            vastaus = keskiarvo([s1, s2, s3])
        except:
            self.fail(f"Varmista, että seuraavan koodin suoritus onnistuu\n{koodi}")

        exp = 4

        self.assertEquals(vastaus, exp,  f"Kun suoritetaan koodi {koodi}pitäisi palauttaa\n{exp}\nfunktio palautti\n{vastaus}")

    @points('12.opintopisteet_osa3')
    def test_14_opintopisteiden_summa_reduce_kaytossa(self):
        src_file = os.path.join('src', 'koodi.py')
        lines = []
        p = False

        with open(src_file) as f:
            for line in f:
                if "def keskiarvo"  in line:
                    p = True
                elif p and ('__name__ == "__main__":' in line or "def kaikkien_opintopisteiden_summa" in line or "def hyvaksyttyjen_opintopisteiden_summa" in line):
                    p = False 
                elif p:
                    lines.append(line)

        vaadittu = [
            "reduce(",
            "filter"
        ]

        for v in vaadittu:
            on = False
            for line in lines:
                if v in line:
                    on = True              
            self.assertTrue(on, f"Funktio keskiarvo(kurssit: list) on toteutettava filter- ja reduce-funktioiden avulla")          

    @points('12.opintopisteet_osa3')
    def test_15_keskiarvo_toimii_2(self):
        from src.koodi import keskiarvo
        from src.koodi import Suoritus

        koodi = """
s1 = Suoritus("Ohjelmoinnin perusteet", 5, 5)
s2 = Suoritus("Ohjelmoinnin jatkokurssi", 4, 5)
s3 = Suoritus("Tietorakenteet ja algoritmit", 0, 10)
keskiarvo([s1, s2, s3])
"""

        try:
            s1 = Suoritus("Ohjelmoinnin perusteet", 5, 5)
            s2 = Suoritus("Ohjelmoinnin jatkokurssi", 4, 5)
            s3 = Suoritus("Tietorakenteet ja algoritmit", 0, 10)
            vastaus = keskiarvo([s1, s2, s3])
        except:
            self.fail(f"Varmista, että seuraavan koodin suoritus onnistuu\n{koodi}")

        exp = 4.5

        self.assertEquals(vastaus, exp,  f"Kun suoritetaan koodi {koodi}pitäisi palauttaa\n{exp}\nfunktio palautti\n{vastaus}")

    @points('12.opintopisteet_osa3')
    def test_16_keskiarvo_toimii_2(self):
        from src.koodi import keskiarvo
        from src.koodi import Suoritus

        koodi = """
s1 = Suoritus("Ohjelmoinnin perusteet", 5, 5)
s2 = Suoritus("Ohjelmoinnin jatkokurssi", 4, 5)
s3 = Suoritus("Tietorakenteet ja algoritmit", 3, 10)
s4 = Suoritus("Full stack -websovelluskehitys", 4, 8)
s5 = Suoritus("DevOps with Docker", 5, 3)
s6 = Suoritus("Toinen kotimainen kieli", 0, 2)
keskiarvo([s1, s2, s3, s4, s5, s6])
"""

        try:
            s1 = Suoritus("Ohjelmoinnin perusteet", 5, 5)
            s2 = Suoritus("Ohjelmoinnin jatkokurssi", 4, 5)
            s3 = Suoritus("Tietorakenteet ja algoritmit", 3, 10)
            s4 = Suoritus("Full stack -websovelluskehitys", 4, 8)
            s5 = Suoritus("DevOps with Docker", 5, 3)
            s6 = Suoritus("Toinen kotimainen kieli", 0, 2)            
            vastaus = keskiarvo([s1, s2, s3, s4, s5, s6])
        except:
            self.fail(f"Varmista, että seuraavan koodin suoritus onnistuu\n{koodi}")

        exp = 4.2

        self.assertEquals(vastaus, exp,  f"Kun suoritetaan koodi {koodi}pitäisi palauttaa\n{exp}\nfunktio palautti\n{vastaus}")


if __name__ == '__main__':
    unittest.main()
