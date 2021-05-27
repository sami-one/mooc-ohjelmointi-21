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

exercise = 'src.kello'
classname = "Kello"

def f(attr: list):
    return ",".join(attr)

@points('8.kello')
class KelloTest(unittest.TestCase):
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

    
    def test1_luokka_olemassa(self):
        try:
            from src.kello import Kello
        except:
            self.assertTrue(False, "Ohjelmastasi pitäisi löytyä luokka nimeltä Kello")

    def test2_konstruktori(self):
        try:
            from src.kello import Kello
            kello = Kello(12,0,0)
            self.assertTrue(True, "")
        except Exception as e:
            self.assertTrue(False, 'Luokan Kello konstuktorin kutsuminen arvoilla Kello(12,0,0)' +
                f' palautti virheen: {e}')

    def test3_testaa_str(self):
        test_cases = ((23,30,0), (10,10,10), (15,10,5), (23,5,15), (4,24,28), (3,4,5))
        for test_case in test_cases:
            try:
                from src.kello import Kello
                h,m,s = test_case
                kello = Kello(h,m,s)

                corr = (datetime(2000,1,1,h,m,s)).strftime("%H:%M:%S")
                val = str(kello)

                self.assertEqual(corr, val, f"Metodin __str__ pitäisi palauttaa merkkijono {corr}\nkun olio luotiin kutsulla\n" + 
                    f"Kello({h}:{m}:{s}).\nNyt metodi palauttaa merkkijonon {val}.")

            except Exception as e:
                self.assertTrue(False, 'Metodin __str__ kutsuminen' +
                    f' palautti virheen: {e}\nkun kello alustettiin kutsullla Kello({h},{m},{s})')

    def test4_testaa_tikitys(self):
        test_cases = ((10,10,58,3),(23,59,55,6),(0,0,0,30),(23,58,30,31))
        for test_case in test_cases:
            try:
                from src.kello import Kello
                h,m,s,t = test_case
                kello = Kello(h,m,s)
                for i in range(t):
                    kello.tick()

                corr = (datetime(2000,1,1,h,m,s) + timedelta(seconds=t)).strftime("%H:%M:%S")
                val = str(kello)

                self.assertEqual(corr, val, f"Metodin __str__ pitäisi palauttaa merkkijono {corr}\nkun olio luotiin kutsulla\n" + 
                    f"Kello({h}:{m}:{s}) ja metodia tick() kutsuttiin {t} kertaa.\nNyt metodi palauttaa merkkijonon {val}.")

            except Exception as e:
                self.assertTrue(False, 'Metodin tick() kutsuminen' +
                    f' palautti virheen: {e}\nkun kello alustettiin kutsullla Kello({h},{m},{s})')

    def test5_testaa_ajan_asetus(self):
        test_cases = ((10,10,58,15,15),(23,59,55,11,0),(0,0,0,12,0),(23,58,10,11,34))
        for test_case in test_cases:
            try:
                from src.kello import Kello
                h,m,s,h2,m2 = test_case
                kello = Kello(h,m,s)
                kello.aseta(h2,m2)

                corr = (datetime(2000,1,1,h2,m2,0)).strftime("%H:%M:00")
                val = str(kello)

                self.assertEqual(corr, val, f"Metodin __str__ pitäisi palauttaa merkkijono {corr}\nkun olio luotiin kutsulla\n" + 
                    f"Kello({h}:{m}:{s}) ja sen jälkeen kutsuttiin aseta({h2}:{m2}).\nNyt metodi __str__ palauttaa merkkijonon {val}.")

            except Exception as e:
                self.assertTrue(False, f'Metodin aseta({h2},{m2}) kutsuminen' +
                    f' palautti virheen: {e}\nkun kello alustettiin kutsullla Kello({h},{m},{s})')

if __name__ == '__main__':
    unittest.main()
