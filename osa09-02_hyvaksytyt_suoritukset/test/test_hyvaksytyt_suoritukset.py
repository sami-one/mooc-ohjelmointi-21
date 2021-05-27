import unittest
from unittest.mock import patch

from tmc import points, reflect
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import os.path
import textwrap
from random import choice, randint
from datetime import date

exercise = 'src.hyvaksytyt_suoritukset'
function = "hyvaksytyt"

def f(attr: list):
    return ",".join(attr)


@points('9.hyvaksytyt_suoritukset')
class HyvaksytytSuorituksetTest(unittest.TestCase):
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

    def test_0b_konstruktori(self):
        try:
            from src.hyvaksytyt_suoritukset import Koesuoritus
            suoritus = Koesuoritus("Pena", 10)
        except Exception as e:
            self.fail(f'Konstruktorikutsu Koesuoritus("Pena", 10) antoi virheen \n{e}\n' +
                'Ethän ole muuttanut luokan Koesuoritus toteutusta?')


    def test1_funktio_olemassa(self):
        try:
            from src.hyvaksytyt_suoritukset import hyvaksytyt
        except:
            self.assertTrue(False, "Ohjelmastasi pitäisi löytyä funktio " + 
                "nimeltä hyvaksytyt(suoritukset: list, pisteraja: int)")

    def test2_palautusarvon_tyyppi(self):
        from src.hyvaksytyt_suoritukset import hyvaksytyt, Koesuoritus
        val = hyvaksytyt([Koesuoritus("Pena", 10)], 5)
        taip = str(type(val)).replace("<class '","").replace("'>","")
        self.assertTrue(type(val) == list, f"Funktion nopein_auto pitäisi palauttaa arvo, jonka tyyppi on lista," +  
            f' nyt se palauttaa arvon {val} joka on tyyppiä {taip}\n kun sitä kutsutaan parametreilla\n [Auto("Mersu",200), Auto("Lada",100)])')


    def test3_testaa_suoritukset(self):
         test_cases = [[("Arto",10),("Matti",15), 14], [("Pekka", 5), ("Paavo", 3), 4], 
                       [("Paula", 20), ("Pirkko", 18), ("Piia", 13), ("Paavo", 15), 17], 
                       [("Lasse", 24), ("Laura", 14), ("Liisa", 13), ("Lauri", 20), ("Lotta", 19), 15],
                       [("Kari", 29), ("Kake", 26), ("Keijo", 10), ("Kalle", 17), ("Kirsi", 30), ("Kiia", 22), 15],
                       [("Emilia", 10), ("Erkki", 9), 10]]
         
         for test_case in test_cases:
            with patch('builtins.input', side_effect=[AssertionError("Syötteen pyytämistä ei odotettu")]):
                reload_module(self.module)
                hyvaksytyt = load(exercise, function, 'fi')
                from src.hyvaksytyt_suoritukset import Koesuoritus

                testlist = [Koesuoritus(x[0], x[1]) for x in test_case[:-1]]
                val = sorted(hyvaksytyt(testlist, test_case[-1]), key = lambda x : x.suorittaja)    
                corr = sorted([x for x in testlist if x.pisteet >= test_case[-1]], key = lambda x: x.suorittaja)

                self.assertEqual(len(val), len(corr), f"Funktion pitäisi palauttaa {len(corr)} alkiota, mutta se palauttaa {len(val)} alkiota\n" +
                    f'kun syöte on\n{test_case}')
                self.assertEqual(val, corr, f'Funktion pitäisi palauttaa lista \n{corr},\n mutta se palauttaa listan \nn{val}\n kun syöte on \n{test_case}')
                

                
if __name__ == '__main__':
    unittest.main()
