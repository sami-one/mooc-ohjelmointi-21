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

exercise = 'src.vaheneva_laskuri'
classname = "VahenevaLaskuri"

def f(attr: list):
    return ",".join(attr)



class KirjaTest(unittest.TestCase):
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

    @points('8.vaheneva_laskuri_osa1')
    def test1_luokka_olemassa(self):
        try:
            from src.vaheneva_laskuri import VahenevaLaskuri
        except:
            self.assertTrue(False, "Ohjelmastasi pitäisi löytyä luokka nimeltä VahenevaLaskuri")

    @points('8.vaheneva_laskuri_osa1')
    def test2_konstruktori(self):
        try:
            from src.vaheneva_laskuri import VahenevaLaskuri
            val = VahenevaLaskuri(1)
            self.assertTrue(True, "")
        except Exception as e:
            self.assertTrue(False, 'Luokan VahenevaLaskuri konstuktorin kutsuminen arvoilla (VahenevaLaskuri(1)' +
                f' palautti virheen: {e}')

    @points('8.vaheneva_laskuri_osa1')
    def test3_testaa_vahenna(self):
        test_cases = ((5,1), (9,4), (100,10), (1,1))
        for test_case in test_cases:
            try:
                from src.vaheneva_laskuri import VahenevaLaskuri
                laskuri = VahenevaLaskuri(test_case[0])
                for i in range(test_case[1]):
                    laskuri.vahenna()
                corr = test_case[0] - test_case[1]

                self.assertEqual(laskuri.arvo, corr, f"Laskurin arvon pitäisi olla {corr}, kun laskuri alustettiin kutsulla\n" +
                    f"VahenevaLaskuri({test_case[0]})\nja metodia vahenna kutsuttiin {test_case[1]} kertaa.\n" +
                    f"Nyt laskurin arvo on {laskuri.arvo}.")
            except Exception as e:
                self.assertTrue(False, f"Metodia vahenna kutsuessa tapahtui virhe:\n{e}" +
                    f"kun olio alustettiin kutsulla VahenevaLaskuri{(test_case[0])}")

    @points('8.vaheneva_laskuri_osa2')
    def test4_testaa_negatiivinen(self):
        test_cases = ((1,2), (3,6), (100,101), (1,10))
        for test_case in test_cases:
            try:
                from src.vaheneva_laskuri import VahenevaLaskuri
                laskuri = VahenevaLaskuri(test_case[0])
                for i in range(test_case[1]):
                    laskuri.vahenna()
                corr = 0

                self.assertEqual(laskuri.arvo, corr, f"Laskurin arvon pitäisi olla {corr}, kun laskuri alustettiin kutsulla\n" +
                    f"VahenevaLaskuri({test_case[0]})\nja metodia vahenna kutsuttiin {test_case[1]} kertaa.\n" +
                    f"Nyt laskurin arvo on {laskuri.arvo}.\nLaskurin arvo ei saa mennä negatiiviseksi!")
            except Exception as e:
                self.assertTrue(False, f"Metodia vahenna kutsuessa tapahtui virhe:\n{e}" + 
                    f"kun olio alustettiin kutsulla VahenevaLaskuri{(test_case[0])}")

    @points('8.vaheneva_laskuri_osa3')
    def test5_testaa_nollaus(self):
        test_cases = ((1,0), (3,0), (100,10))
        for test_case in test_cases:
            try:
                from src.vaheneva_laskuri import VahenevaLaskuri
                laskuri = VahenevaLaskuri(test_case[0])
                for i in range(test_case[1]):
                    laskuri.vahenna()
                laskuri.nollaa()
                corr = 0

                self.assertEqual(laskuri.arvo, corr, f"Laskurin arvon pitäisi olla {corr}, kun laskuri alustettiin kutsulla\n" +
                    f"VahenevaLaskuri({test_case[0]}),\nmetodia vahenna kutsuttiin {test_case[1]} kertaa,\n" +
                    f"ja sen jälkeen kutsuttiin metodia nollaa().\n" + 
                    f"Nyt laskurin arvo on {laskuri.arvo}.")
            except Exception as e:
                self.assertTrue(False, f"Tapahtui virhe:\n{e}"
                    f"kun olio alustettiin kutsulla VahenevaLaskuri{(test_case[0])}" +
                    "\nmetodia vahenna kutsuttiin {test_case[1]} kertaa,\n" +
                    f"ja sen jälkeen kutsuttiin metodia nollaa().")

    @points('8.vaheneva_laskuri_osa4')
    def test6_testaa_palautus(self):
        test_cases = ((2,1), (3,3), (100,20), (5,10))
        for test_case in test_cases:
            try:
                from src.vaheneva_laskuri import VahenevaLaskuri
                laskuri = VahenevaLaskuri(test_case[0])
                for i in range(test_case[1]):
                    laskuri.vahenna()
                laskuri.palauta_alkuperainen_arvo()
                corr = test_case[0]

                self.assertEqual(laskuri.arvo, corr, f"Laskurin arvon pitäisi olla {corr}, kun laskuri alustettiin kutsulla\n" +
                    f"VahenevaLaskuri({test_case[0]}),\nmetodia vahenna kutsuttiin {test_case[1]} kertaa,\n" +
                    f"ja sen jälkeen kutsuttiin metodia palauta_alkuperainen_arvo().\n" + 
                    f"Nyt laskurin arvo on {laskuri.arvo}.")
            except Exception as e:
                self.assertTrue(False, f"Tapahtui virhe:\n{e}"
                    f"kun olio alustettiin kutsulla VahenevaLaskuri{(test_case[0])}" +
                    "\nmetodia vahenna kutsuttiin {test_case[1]} kertaa,\n" +
                    f"ja sen jälkeen kutsuttiin metodia palauta_alkuperainen_arvo().")

    

if __name__ == '__main__':
    unittest.main()
