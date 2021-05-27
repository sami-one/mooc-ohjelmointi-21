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

def s(lista):
    return "\n".join(f'{r}' for r in lista)

class KiipeilykalliotTest(unittest.TestCase):
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

    @points('12.kiipeilykalliot_osa1')
    def test_1_funktio_maaran_mukaan_olemassa(self):
        try:
            from src.koodi import reittien_maaran_mukaan
        except:
            self.assertTrue(False, "Ohjelmastasi pitäisi löytyä funktio nimeltä reittien_maaran_mukaan(kalliot: list)")

    @points('12.kiipeilykalliot_osa1')
    def test_2_maaran_mukaan_paluuarvon_tyyppi(self):
        from src.koodi import reittien_maaran_mukaan
        from src.koodi import Kiipeilyreitti, Kiipeilykallio

        koodi = """
k1 = Kiipeilykallio("Olhava")
k1.lisaa_reitti(Kiipeilyreitti("Kantti", 38, "6A+"))
k1.lisaa_reitti(Kiipeilyreitti("Suuri leikkaus", 36, "6B"))
k1.lisaa_reitti(Kiipeilyreitti("Ruotsalaisten reitti", 42, "5+"))

k2 = Kiipeilykallio("Nummi")
k2.lisaa_reitti(Kiipeilyreitti("Syncro", 14, "8C+"))

k3 = Kiipeilykallio("Nalkkilan släbi")
k3.lisaa_reitti(Kiipeilyreitti("Pieniä askelia", 12, "6A+"))
k3.lisaa_reitti(Kiipeilyreitti("Smooth operator", 11, "7A"))
k3.lisaa_reitti(Kiipeilyreitti("Possu ei pidä", 12 , "6B+"))
k3.lisaa_reitti(Kiipeilyreitti("Hedelmätarha", 8, "6A"))

reittien_maaran_mukaan([k1, k2, k3])

"""

        try:
            k1 = Kiipeilykallio("Olhava")
            k1.lisaa_reitti(Kiipeilyreitti("Kantti", 38, "6A+"))
            k1.lisaa_reitti(Kiipeilyreitti("Suuri leikkaus", 36, "6B"))
            k1.lisaa_reitti(Kiipeilyreitti("Ruotsalaisten reitti", 42, "5+"))

            k2 = Kiipeilykallio("Nummi")
            k2.lisaa_reitti(Kiipeilyreitti("Syncro", 14, "8C+"))

            k3 = Kiipeilykallio("Nalkkilan släbi")
            k3.lisaa_reitti(Kiipeilyreitti("Pieniä askelia", 12, "6A+"))
            k3.lisaa_reitti(Kiipeilyreitti("Smooth operator", 11, "7A"))
            k3.lisaa_reitti(Kiipeilyreitti("Possu ei pidä", 12 , "6B+"))
            k3.lisaa_reitti(Kiipeilyreitti("Hedelmätarha", 8, "6A"))

            vastaus = reittien_maaran_mukaan([k1, k2, k3])
        except:
            self.fail(f"Varmista, että seuraavan koodin suoritus onnistuu\n{koodi}")

        taip = str(type(vastaus)).replace("<class '","").replace("'>","")
        self.assertTrue(type(vastaus) == list, f"Funktion reittien_maaran_mukaan(reitit: list) tulee palauttaa lista, nyt palautettu arvo oli tyypiltään {taip}")
        self.assertTrue(len(vastaus) == 3, f"Kun suoritetaan koodi {koodi}tulee palauttaa listan jonka pituus on 3, nyt palautetun listan pituus oli {len(vastaus)}")
        taip = str(type(vastaus[0])).replace("<class '","").replace("'>","")
        etaip = str(type(k1)).replace("<class '","").replace("'>","")
        self.assertTrue(type(vastaus[0]) == type(k1),  f"Kun suoritetaan koodi {koodi}palautetun listan alkioiden tulee olla tyypiltään {etaip} nyt niiden tyyppi on {taip}")

    @points('12.kiipeilykalliot_osa1')
    def test_3_maaran_mukaan_toimii_1(self):
        from src.koodi import reittien_maaran_mukaan
        from src.koodi import Kiipeilyreitti, Kiipeilykallio

        koodi = """
k1 = Kiipeilykallio("Olhava")
k1.lisaa_reitti(Kiipeilyreitti("Kantti", 38, "6A+"))
k1.lisaa_reitti(Kiipeilyreitti("Suuri leikkaus", 36, "6B"))
k1.lisaa_reitti(Kiipeilyreitti("Ruotsalaisten reitti", 42, "5+"))

k2 = Kiipeilykallio("Nummi")
k2.lisaa_reitti(Kiipeilyreitti("Syncro", 14, "8C+"))

k3 = Kiipeilykallio("Nalkkilan släbi")
k3.lisaa_reitti(Kiipeilyreitti("Pieniä askelia", 12, "6A+"))
k3.lisaa_reitti(Kiipeilyreitti("Smooth operator", 11, "7A"))
k3.lisaa_reitti(Kiipeilyreitti("Possu ei pidä", 12 , "6B+"))
k3.lisaa_reitti(Kiipeilyreitti("Hedelmätarha", 8, "6A"))

reittien_maaran_mukaan([k1, k2, k3])

"""

        try:
            k1 = Kiipeilykallio("Olhava")
            k1.lisaa_reitti(Kiipeilyreitti("Kantti", 38, "6A+"))
            k1.lisaa_reitti(Kiipeilyreitti("Suuri leikkaus", 36, "6B"))
            k1.lisaa_reitti(Kiipeilyreitti("Ruotsalaisten reitti", 42, "5+"))

            k2 = Kiipeilykallio("Nummi")
            k2.lisaa_reitti(Kiipeilyreitti("Syncro", 14, "8C+"))

            k3 = Kiipeilykallio("Nalkkilan släbi")
            k3.lisaa_reitti(Kiipeilyreitti("Pieniä askelia", 12, "6A+"))
            k3.lisaa_reitti(Kiipeilyreitti("Smooth operator", 11, "7A"))
            k3.lisaa_reitti(Kiipeilyreitti("Possu ei pidä", 12 , "6B+"))
            k3.lisaa_reitti(Kiipeilyreitti("Hedelmätarha", 8, "6A"))

            vastaus = reittien_maaran_mukaan([k1, k2, k3])
        except:
            self.fail(f"Varmista, että seuraavan koodin suoritus onnistuu\n{koodi}")

        exp = [k2, k1, k3]

        self.assertTrue(vastaus == exp,  f"Kun suoritetaan koodi {koodi}pitäisi palauttaa reitit seuraavassa \n{s(exp)}\nfunktio palautti\n{s(vastaus)}")

    @points('12.kiipeilykalliot_osa1')
    def test_4_maaran_mukaan_toimii_2(self):
        from src.koodi import reittien_maaran_mukaan
        from src.koodi import Kiipeilyreitti, Kiipeilykallio

        koodi = """
k1 = Kiipeilykallio("Olhava")
k1.lisaa_reitti(Kiipeilyreitti("Kantti", 38, "6A+"))
k1.lisaa_reitti(Kiipeilyreitti("Suuri leikkaus", 36, "6B"))
k1.lisaa_reitti(Kiipeilyreitti("Ruotsalaisten reitti", 42, "5+"))

k2 = Kiipeilykallio("Nummi")
k2.lisaa_reitti(Kiipeilyreitti("Syncro", 14, "8C+"))
k2.lisaa_reitti(Kiipeilyreitti("Nummisuutari", 12, "8A"))

k3 = Kiipeilykallio("Nalkkilan släbi")
k3.lisaa_reitti(Kiipeilyreitti("Pieniä askelia", 12, "6A+"))

k4 = Kiipeilykallio("Jaanankallio")
k4.lisaa_reitti(Kiipeilyreitti("Antipatia", 12, "7C"))
k4.lisaa_reitti(Kiipeilyreitti("Vompatti", 14, "6C"))
k4.lisaa_reitti(Kiipeilyreitti("Haliba", 16, "6B"))
k4.lisaa_reitti(Kiipeilyreitti("Old Fart Club", 21, "6A"))

reittien_maaran_mukaan([k1, k2, k3, k4])

"""

        try:
            k1 = Kiipeilykallio("Olhava")
            k1.lisaa_reitti(Kiipeilyreitti("Kantti", 38, "6A+"))
            k1.lisaa_reitti(Kiipeilyreitti("Suuri leikkaus", 36, "6B"))
            k1.lisaa_reitti(Kiipeilyreitti("Ruotsalaisten reitti", 42, "5+"))

            k2 = Kiipeilykallio("Nummi")
            k2.lisaa_reitti(Kiipeilyreitti("Syncro", 14, "8C+"))
            k2.lisaa_reitti(Kiipeilyreitti("Nummisuutari", 12, "8A"))

            k3 = Kiipeilykallio("Nalkkilan släbi")
            k3.lisaa_reitti(Kiipeilyreitti("Pieniä askelia", 12, "6A+"))

            k4 = Kiipeilykallio("Jaanankallio")
            k4.lisaa_reitti(Kiipeilyreitti("Antipatia", 12, "7C"))
            k4.lisaa_reitti(Kiipeilyreitti("Vompatti", 14, "6C"))
            k4.lisaa_reitti(Kiipeilyreitti("Haliba", 16, "6B"))
            k4.lisaa_reitti(Kiipeilyreitti("Old Fart Club", 21, "6A"))

            vastaus = reittien_maaran_mukaan([k1, k2, k3, k4])
        except:
            self.fail(f"Varmista, että seuraavan koodin suoritus onnistuu\n{koodi}")

        exp = [k3, k2, k1, k4]

        self.assertTrue(vastaus == exp,  f"Kun suoritetaan koodi {koodi}pitäisi palauttaa reitit seuraavassa \n{s(exp)}\nfunktio palautti\n{s(vastaus)}")

    @points('12.kiipeilykalliot_osa2')
    def test_5_funktio_vaikeuden_mukaan_olemassa(self):
        try:
            from src.koodi import vaikeimman_reitin_mukaan
        except:
            self.assertTrue(False, "Ohjelmastasi pitäisi löytyä funktio nimeltä vaikeimman_reitin_mukaan(kalliot: list)")

    @points('12.kiipeilykalliot_osa2')
    def test_6_vaikeuden_mukaan_paluuarvon_tyyppi(self):
        from src.koodi import vaikeimman_reitin_mukaan
        from src.koodi import Kiipeilyreitti, Kiipeilykallio

        koodi = """
k1 = Kiipeilykallio("Olhava")
k1.lisaa_reitti(Kiipeilyreitti("Kantti", 38, "6A+"))
k1.lisaa_reitti(Kiipeilyreitti("Suuri leikkaus", 36, "6B"))
k1.lisaa_reitti(Kiipeilyreitti("Ruotsalaisten reitti", 42, "5+"))

k2 = Kiipeilykallio("Nummi")
k2.lisaa_reitti(Kiipeilyreitti("Syncro", 14, "8C+"))

k3 = Kiipeilykallio("Nalkkilan släbi")
k3.lisaa_reitti(Kiipeilyreitti("Pieniä askelia", 12, "6A+"))
k3.lisaa_reitti(Kiipeilyreitti("Smooth operator", 11, "7A"))
k3.lisaa_reitti(Kiipeilyreitti("Possu ei pidä", 12 , "6B+"))
k3.lisaa_reitti(Kiipeilyreitti("Hedelmätarha", 8, "6A"))

vaikeimman_reitin_mukaan([k1, k2, k3])

"""

        try:
            k1 = Kiipeilykallio("Olhava")
            k1.lisaa_reitti(Kiipeilyreitti("Kantti", 38, "6A+"))
            k1.lisaa_reitti(Kiipeilyreitti("Suuri leikkaus", 36, "6B"))
            k1.lisaa_reitti(Kiipeilyreitti("Ruotsalaisten reitti", 42, "5+"))

            k2 = Kiipeilykallio("Nummi")
            k2.lisaa_reitti(Kiipeilyreitti("Syncro", 14, "8C+"))

            k3 = Kiipeilykallio("Nalkkilan släbi")
            k3.lisaa_reitti(Kiipeilyreitti("Pieniä askelia", 12, "6A+"))
            k3.lisaa_reitti(Kiipeilyreitti("Smooth operator", 11, "7A"))
            k3.lisaa_reitti(Kiipeilyreitti("Possu ei pidä", 12 , "6B+"))
            k3.lisaa_reitti(Kiipeilyreitti("Hedelmätarha", 8, "6A"))

            vastaus = vaikeimman_reitin_mukaan([k1, k2, k3])
        except:
            self.fail(f"Varmista, että seuraavan koodin suoritus onnistuu\n{koodi}")

        taip = str(type(vastaus)).replace("<class '","").replace("'>","")
        self.assertTrue(type(vastaus) == list, f"Funktion vaikeimman_reitin_mukaan(reitit: list) tulee palauttaa lista, nyt palautettu arvo oli tyypiltään {taip}")
        self.assertTrue(len(vastaus) == 3, f"Kun suoritetaan koodi {koodi}tulee palauttaa listan jonka pituus on 3, nyt palautetun listan pituus oli {len(vastaus)}")
        taip = str(type(vastaus[0])).replace("<class '","").replace("'>","")
        etaip = str(type(k1)).replace("<class '","").replace("'>","")
        self.assertTrue(type(vastaus[0]) == type(k1),  f"Kun suoritetaan koodi {koodi}palautetun listan alkioiden tulee olla tyypiltään {etaip} nyt niiden tyyppi on {taip}")

    @points('12.kiipeilykalliot_osa2')
    def test_7_vaikeuden_mukaan_toimii_1(self):
        from src.koodi import vaikeimman_reitin_mukaan
        from src.koodi import Kiipeilyreitti, Kiipeilykallio

        koodi = """
k1 = Kiipeilykallio("Olhava")
k1.lisaa_reitti(Kiipeilyreitti("Kantti", 38, "6A+"))
k1.lisaa_reitti(Kiipeilyreitti("Suuri leikkaus", 36, "6B"))
k1.lisaa_reitti(Kiipeilyreitti("Ruotsalaisten reitti", 42, "5+"))

k2 = Kiipeilykallio("Nummi")
k2.lisaa_reitti(Kiipeilyreitti("Syncro", 14, "8C+"))

k3 = Kiipeilykallio("Nalkkilan släbi")
k3.lisaa_reitti(Kiipeilyreitti("Pieniä askelia", 12, "6A+"))
k3.lisaa_reitti(Kiipeilyreitti("Smooth operator", 11, "7A"))
k3.lisaa_reitti(Kiipeilyreitti("Possu ei pidä", 12 , "6B+"))
k3.lisaa_reitti(Kiipeilyreitti("Hedelmätarha", 8, "6A"))

vaikeimman_reitin_mukaan([k1, k2, k3])

"""

        try:
            k1 = Kiipeilykallio("Olhava")
            k1.lisaa_reitti(Kiipeilyreitti("Kantti", 38, "6A+"))
            k1.lisaa_reitti(Kiipeilyreitti("Suuri leikkaus", 36, "6B"))
            k1.lisaa_reitti(Kiipeilyreitti("Ruotsalaisten reitti", 42, "5+"))

            k2 = Kiipeilykallio("Nummi")
            k2.lisaa_reitti(Kiipeilyreitti("Syncro", 14, "8C+"))

            k3 = Kiipeilykallio("Nalkkilan släbi")
            k3.lisaa_reitti(Kiipeilyreitti("Pieniä askelia", 12, "6A+"))
            k3.lisaa_reitti(Kiipeilyreitti("Smooth operator", 11, "7A"))
            k3.lisaa_reitti(Kiipeilyreitti("Possu ei pidä", 12 , "6B+"))
            k3.lisaa_reitti(Kiipeilyreitti("Hedelmätarha", 8, "6A"))

            vastaus = vaikeimman_reitin_mukaan([k1, k2, k3])
        except:
            self.fail(f"Varmista, että seuraavan koodin suoritus onnistuu\n{koodi}")

        exp = [k2, k3, k1]

        self.assertTrue(vastaus == exp,  f"Kun suoritetaan koodi {koodi}pitäisi palauttaa reitit seuraavassa \n{s(exp)}\nfunktio palautti\n{s(vastaus)}")

    @points('12.kiipeilykalliot_osa2')
    def test_8_vaikeuden_mukaan_toimii_2(self):
        from src.koodi import vaikeimman_reitin_mukaan
        from src.koodi import Kiipeilyreitti, Kiipeilykallio

        koodi = """
k1 = Kiipeilykallio("Olhava")
k1.lisaa_reitti(Kiipeilyreitti("Kantti", 38, "6A+"))
k1.lisaa_reitti(Kiipeilyreitti("Suuri leikkaus", 36, "6B"))
k1.lisaa_reitti(Kiipeilyreitti("Ruotsalaisten reitti", 42, "5+"))

k2 = Kiipeilykallio("Nummi")
k2.lisaa_reitti(Kiipeilyreitti("Syncro", 14, "8C+"))
k2.lisaa_reitti(Kiipeilyreitti("Nummisuutari", 12, "8A"))

k3 = Kiipeilykallio("Nalkkilan släbi")
k3.lisaa_reitti(Kiipeilyreitti("Pieniä askelia", 12, "6A+"))

k4 = Kiipeilykallio("Jaanankallio")
k4.lisaa_reitti(Kiipeilyreitti("Antipatia", 12, "7C"))
k4.lisaa_reitti(Kiipeilyreitti("Vompatti", 14, "6C"))
k4.lisaa_reitti(Kiipeilyreitti("Haliba", 16, "6B"))
k4.lisaa_reitti(Kiipeilyreitti("Old Fart Club", 21, "6A"))

vaikeimman_reitin_mukaan([k1, k2, k3, k4])

"""

        try:
            k1 = Kiipeilykallio("Olhava")
            k1.lisaa_reitti(Kiipeilyreitti("Kantti", 38, "6A+"))
            k1.lisaa_reitti(Kiipeilyreitti("Suuri leikkaus", 36, "6B"))
            k1.lisaa_reitti(Kiipeilyreitti("Ruotsalaisten reitti", 42, "5+"))

            k2 = Kiipeilykallio("Nummi")
            k2.lisaa_reitti(Kiipeilyreitti("Syncro", 14, "8C+"))
            k2.lisaa_reitti(Kiipeilyreitti("Nummisuutari", 12, "8A"))

            k3 = Kiipeilykallio("Nalkkilan släbi")
            k3.lisaa_reitti(Kiipeilyreitti("Pieniä askelia", 12, "6A+"))

            k4 = Kiipeilykallio("Jaanankallio")
            k4.lisaa_reitti(Kiipeilyreitti("Antipatia", 12, "7C"))
            k4.lisaa_reitti(Kiipeilyreitti("Vompatti", 14, "6C"))
            k4.lisaa_reitti(Kiipeilyreitti("Haliba", 16, "6B"))
            k4.lisaa_reitti(Kiipeilyreitti("Old Fart Club", 21, "6A"))

            vastaus = vaikeimman_reitin_mukaan([k1, k2, k3, k4])
        except:
            self.fail(f"Varmista, että seuraavan koodin suoritus onnistuu\n{koodi}")

        exp = [k2, k4, k1, k3]

        self.assertTrue(vastaus == exp,  f"Kun suoritetaan koodi {koodi}pitäisi palauttaa reitit seuraavassa \n{s(exp)}\nfunktio palautti\n{s(vastaus)}")


if __name__ == '__main__':
    unittest.main()