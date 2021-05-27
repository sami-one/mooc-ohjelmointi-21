import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import os.path
import textwrap
from random import choice, randint
from datetime import date

exercise = 'src.vuodet_listaan'
function = "vuodet_listaan"

def get_corr(m):
    return sorted([x.year for x in m])
        

@points('8.vuodet_listaan')
class VuodetListaanTest(unittest.TestCase):
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

    def test1_funktio_olemassa(self):
        try:
            from src.vuodet_listaan import vuodet_listaan
        except:
            self.assertTrue(False, "Ohjelmastasi pitäisi löytyä funktio nimeltä vuodet_listaan(vuodet: list)")

    def test2_palautusarvon_tyyppi(self):
        try:
            from src.vuodet_listaan import vuodet_listaan
            val = vuodet_listaan([date(1900,1,1)])
            taip = str(type(val)).replace("<class '","").replace("'>","")
            self.assertTrue(type(val) == list, f"Funktion vuodet_listaan pitäisi palauttaa arvo, jonka tyyppi on list," +  
                f" nyt se palauttaa arvon {val} joka on tyyppiä {taip}\n kun sitä kutsutaan parametrilla \n[date(1900,1,1)]")
        except Exception as e:
            self.assertTrue(False, f"Funktio antoi virheen kun sitä kutsuttiin parametrin arvolla [date(1900,1,1)]")


    def test3_testaa_arvot(self):
        d = date
        test_cases = ([d(1900,1,1), d(1950,2,3), d(1979,6,6)], [d(2010,5,11),d(2009,11,1),d(2004,3,3),d(2000,1,23)],
                      [d(1976,8,8), d(1984,12,24), d(1979,2,4), d(1980,9,3)], [d(1763,2,7),d(1454,11,11),d(1133,2,23),d(1755,4,22)])
        for test_case in test_cases:
            with patch('builtins.input', side_effect=[AssertionError("Syötteen pyytämistä ei odotettu")]):
                reload_module(self.module)
                vuodet_listaan = load(exercise, function, 'fi')

                test_case_2 = test_case[:]
               
                val = vuodet_listaan(test_case)
                
                corr = get_corr(test_case_2)

                self.assertEqual(val, corr, f"Funktion pitäisi palauttaa \n{corr}\nmutta se palauttaa \n{val}\nkun parametri on\n{test_case_2}")
                self.assertEqual(test_case, test_case_2, f"Funktio ei saa muuttaa syötteenään saamaansa listaa.\nLista on nyt \n{test_case}, \kun sen pitäisi olla \n{test_case_2}")

    

if __name__ == '__main__':
    unittest.main()
