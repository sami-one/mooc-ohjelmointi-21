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
classname = "Kiipeilyreitti"

def f(attr: list):
    return ",".join(attr)

def s(lista):
    return "\n".join(f'{r}' for r in lista)

class KiipeilyreittiTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=[AssertionError("Syötteen pyytämistä ei odotettu")]):
           cls.module = load_module(exercise, 'fi')

    def test_0a_paaohjelma_kunnossa(self):
        ok, line = check_source(self.module)
        message = """Funktioita testaava koodi tulee sijoittaa lohkon
if __name__ == "__main__":
sisälle. Seuraava rivi tulee siirtää:
"""
        self.assertTrue(ok, message+line)

    @points('12.kiipeilyreitti_osa1')
    def test_1_funktio_pituuden_mukaan_olemassa(self):
        try:
            from src.koodi import pituuden_mukaan
        except:
            self.assertTrue(False, "Ohjelmastasi pitäisi löytyä funktio nimeltä pituuden_mukaan(reitit: list)")

    @points('12.kiipeilyreitti_osa1')
    def test_2_pituuden_mukaan_paluuarvon_tyyppi(self):
        from src.koodi import pituuden_mukaan
        from src.koodi import Kiipeilyreitti

        koodi = """
r1 = Kiipeilyreitti("Kantti", 38, "6A+")
r2 = Kiipeilyreitti("Smooth operator", 9, "7A")
r3 = Kiipeilyreitti("Syncro", 14, "8C+")
pituuden_mukaan([r1, r2, r3])

"""

        try:
            r1 = Kiipeilyreitti("Kantti", 38, "6A+")
            r2 = Kiipeilyreitti("Smooth operator", 9, "7A")
            r3 = Kiipeilyreitti("Syncro", 14, "8C+")
            vastaus = pituuden_mukaan([r1, r2, r3])
        except:
            self.fail(f"Varmista, että seuraavan koodin suoritus onnistuu\n{koodi}")

        taip = str(type(vastaus)).replace("<class '","").replace("'>","")
        self.assertTrue(type(vastaus) == list, f"Funktion pituuden_mukaan(reitit: list) tulee palauttaa lista, nyt palautettu arvo oli tyypiltään {taip}")
        self.assertTrue(len(vastaus) == 3, f"Kun suoritetaan koodi {koodi}tulee palauttaa listan jonka pituus on 3, nyt palautetun listan pituus oli {len(vastaus)}")
        taip = str(type(vastaus[0])).replace("<class '","").replace("'>","")
        etaip = str(type(r1)).replace("<class '","").replace("'>","")
        self.assertTrue(type(vastaus[0]) == type(r1),  f"Kun suoritetaan koodi {koodi}palautetun listan alkioiden tulee olla tyypiltään {etaip} nyt niiden tyyppi on {taip}")

    @points('12.kiipeilyreitti_osa1')
    def test_3_pituuden_mukaan_toimii_1(self):
        from src.koodi import pituuden_mukaan
        from src.koodi import Kiipeilyreitti

        koodi = """
r1 = Kiipeilyreitti("Kantti", 38, "6A+")
r2 = Kiipeilyreitti("Smooth operator", 9, "7A")
r3 = Kiipeilyreitti("Syncro", 14, "8C+")
pituuden_mukaan([r1, r2, r3])

"""

        try:
            r1 = Kiipeilyreitti("Kantti", 38, "6A+")
            r2 = Kiipeilyreitti("Smooth operator", 9, "7A")
            r3 = Kiipeilyreitti("Syncro", 14, "8C+")
            vastaus = pituuden_mukaan([r1, r2, r3])
        except:
            self.fail(f"Varmista, että seuraavan koodin suoritus onnistuu\n{koodi}")

        exp = [r1, r3, r2]

        self.assertTrue(vastaus == exp,  f"Kun suoritetaan koodi {koodi}pitäisi palauttaa reitit seuraavassa \n{s(exp)}\nfunktio palautti\n{s(vastaus)}")

    @points('12.kiipeilyreitti_osa1')
    def test_4_pituuden_mukaan_toimii_2(self):
        from src.koodi import pituuden_mukaan
        from src.koodi import Kiipeilyreitti

        koodi = """
r1 = Kiipeilyreitti("Kantti", 38, "6A+")
r2 = Kiipeilyreitti("Smooth operator", 9, "7A")
r3 = Kiipeilyreitti("Syncro", 14, "8C+")
r4 = Kiipeilyreitti("Suuri leikkaus", 36, "6B")
r5 = Kiipeilyreitti("Hedelmätarha", 8, "6A")
r6 = Kiipeilyreitti("Possu ei pidä", 12 , "6B+")
r7 = Kiipeilyreitti("Pieniä askelia", 13, "6A+")
pituuden_mukaan([r1, r2, r3, r4, r5, r6, r7])

"""

        try:
            r1 = Kiipeilyreitti("Kantti", 38, "6A+")
            r2 = Kiipeilyreitti("Smooth operator", 9, "7A")
            r3 = Kiipeilyreitti("Syncro", 14, "8C+")
            r4 = Kiipeilyreitti("Suuri leikkaus", 36, "6B")
            r5 = Kiipeilyreitti("Hedelmätarha", 8, "6A")
            r6 = Kiipeilyreitti("Possu ei pidä", 12 , "6B+")
            r7 = Kiipeilyreitti("Pieniä askelia", 13, "6A+")
            vastaus = pituuden_mukaan([r1, r2, r3, r4, r5, r6, r7])
        except:
            self.fail(f"Varmista, että seuraavan koodin suoritus onnistuu\n{koodi}")

        exp = [r1, r4, r3, r7, r6, r2, r5]

        self.assertTrue(vastaus == exp,  f"Kun suoritetaan koodi {koodi}pitäisi palauttaa reitit seuraavassa \n{s(exp)}\nfunktio palautti\n{s(vastaus)}")

    @points('12.kiipeilyreitti_osa2')
    def test_5_funktio_vaikeuden_mukaan_olemassa(self):
        try:
            from src.koodi import vaikeuden_mukaan
        except:
            self.assertTrue(False, "Ohjelmastasi pitäisi löytyä funktio nimeltä vaikeuden_mukaan(reitit: list)")

    @points('12.kiipeilyreitti_osa2')
    def test_6_vaikeuden_mukaan_paluuarvon_tyyppi(self):
        from src.koodi import vaikeuden_mukaan
        from src.koodi import Kiipeilyreitti

        koodi = """
r1 = Kiipeilyreitti("Kantti", 38, "6A+")
r2 = Kiipeilyreitti("Smooth operator", 9, "7A")
r3 = Kiipeilyreitti("Syncro", 14, "8C+")
vaikeuden_mukaan([r1, r2, r3])

"""

        try:
            r1 = Kiipeilyreitti("Kantti", 38, "6A+")
            r2 = Kiipeilyreitti("Smooth operator", 9, "7A")
            r3 = Kiipeilyreitti("Syncro", 14, "8C+")
            vastaus = vaikeuden_mukaan([r1, r2, r3])
        except:
            self.fail(f"Varmista, että seuraavan koodin suoritus onnistuu\n{koodi}")

        taip = str(type(vastaus)).replace("<class '","").replace("'>","")
        self.assertTrue(type(vastaus) == list, f"Funktion vaikeuden_mukaan(reitit: list) tulee palauttaa lista, nyt palautettu arvo oli tyypiltään {taip}")
        self.assertTrue(len(vastaus) == 3, f"Kun suoritetaan koodi {koodi}tulee palauttaa listan jonka pituus on 3, nyt palautetun listan pituus oli {len(vastaus)}")
        taip = str(type(vastaus[0])).replace("<class '","").replace("'>","")
        etaip = str(type(r1)).replace("<class '","").replace("'>","")
        self.assertTrue(type(vastaus[0]) == type(r1),  f"Kun suoritetaan koodi {koodi}palautetun listan alkioiden tulee olla tyypiltään {etaip} nyt niiden tyyppi on {taip}")

    @points('12.kiipeilyreitti_osa2')
    def test_7_vaikeuden_mukaan_toimii_1(self):
        from src.koodi import vaikeuden_mukaan
        from src.koodi import Kiipeilyreitti

        koodi = """
r1 = Kiipeilyreitti("Kantti", 38, "6A+")
r2 = Kiipeilyreitti("Smooth operator", 9, "7A")
r3 = Kiipeilyreitti("Syncro", 14, "8C+")
vaikeuden_mukaan([r1, r2, r3])

"""

        try:
            r1 = Kiipeilyreitti("Kantti", 38, "6A+")
            r2 = Kiipeilyreitti("Smooth operator", 9, "7A")
            r3 = Kiipeilyreitti("Syncro", 14, "8C+")
            vastaus = vaikeuden_mukaan([r1, r2, r3])
        except:
            self.fail(f"Varmista, että seuraavan koodin suoritus onnistuu\n{koodi}")

        exp = [r3, r2, r1]

        self.assertTrue(vastaus == exp,  f"Kun suoritetaan koodi {koodi}pitäisi palauttaa reitit seuraavassa \n{s(exp)}\nfunktio palautti\n{s(vastaus)}")

    @points('12.kiipeilyreitti_osa2')
    def test_8_vaikeuden_mukaan_toimii_2(self):
        from src.koodi import vaikeuden_mukaan
        from src.koodi import Kiipeilyreitti

        koodi = """
r1 = Kiipeilyreitti("Pieniä askelia", 13, "6A+")
r2 = Kiipeilyreitti("Kantti", 38, "6A+")
r3 = Kiipeilyreitti("Bukowski", 9, "6A+")
vastaus = vaikeuden_mukaan([r1, r2, r3])

"""

        try:
            r1 = Kiipeilyreitti("Pieniä askelia", 13, "6A+")
            r2 = Kiipeilyreitti("Kantti", 38, "6A+")
            r3 = Kiipeilyreitti("Bukowski", 9, "6A+")
            vastaus = vaikeuden_mukaan([r1, r2, r3])
        except:
            self.fail(f"Varmista, että seuraavan koodin suoritus onnistuu\n{koodi}")

        exp = [r2, r1, r3]

        self.assertTrue(vastaus == exp,  f"Kun suoritetaan koodi {koodi}pitäisi palauttaa reitit seuraavassa \n{s(exp)}\nfunktio palautti\n{s(vastaus)}")


    @points('12.kiipeilyreitti_osa2')
    def test_9_vaikeuden_mukaan_toimii_3(self):
        from src.koodi import vaikeuden_mukaan
        from src.koodi import Kiipeilyreitti

        koodi = """
r1 = Kiipeilyreitti("Kantti", 38, "6A+")
r2 = Kiipeilyreitti("Smooth operator", 9, "7A")
r3 = Kiipeilyreitti("Syncro", 14, "8C+")
r4 = Kiipeilyreitti("Suuri leikkaus", 36, "6B")
r5 = Kiipeilyreitti("Hedelmätarha", 8, "6A")
r6 = Kiipeilyreitti("Possu ei pidä", 12 , "6B+")
r7 = Kiipeilyreitti("Pieniä askelia", 13, "6A+")
r8 = Kiipeilyreitti("Ruotsalaisten reitti", 42, "5+")
vaikeuden_mukaan([r1, r2, r3, r4, r5, r6, r7, r8])

"""

        try:
            r1 = Kiipeilyreitti("Kantti", 38, "6A+")
            r2 = Kiipeilyreitti("Smooth operator", 9, "7A")
            r3 = Kiipeilyreitti("Syncro", 14, "8C+")
            r4 = Kiipeilyreitti("Suuri leikkaus", 36, "6B")
            r5 = Kiipeilyreitti("Hedelmätarha", 8, "6A")
            r6 = Kiipeilyreitti("Possu ei pidä", 12 , "6B+")
            r7 = Kiipeilyreitti("Pieniä askelia", 13, "6A+")
            r8 = Kiipeilyreitti("Ruotsalaisten reitti", 42, "5+")
            vastaus = vaikeuden_mukaan([r1, r2, r3, r4, r5, r6, r7, r8])
        except:
            self.fail(f"Varmista, että seuraavan koodin suoritus onnistuu\n{koodi}")

        exp = [r3, r2, r6, r4, r1, r7, r5, r8]

        self.assertTrue(vastaus == exp,  f"Kun suoritetaan koodi {koodi}pitäisi palauttaa reitit seuraavassa \n{s(exp)}\nfunktio palautti\n{s(vastaus)}")


if __name__ == '__main__':
    unittest.main()
