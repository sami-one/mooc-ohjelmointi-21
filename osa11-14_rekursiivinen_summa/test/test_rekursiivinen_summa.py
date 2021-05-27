import unittest
from unittest.mock import patch

from tmc import points, reflect
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import os.path
import textwrap
import inspect, re

exercise = 'src.rekursiivinen_summa'

@points('11.rekursiivinen_summa')
class RekursiivinenSummaTest(unittest.TestCase):
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
    
    def test_1_funktio_olemassa(self):
        try:
            from src.rekursiivinen_summa import summa
        except Exception as e:
            self.fail(f'Ohjelmasta pitäisi löytyä funktio nimeltä summa.')

    def test_2_paluuarvon_tyyppi(self):
        try:
            from src.rekursiivinen_summa import summa
            val = summa(1)
        except Exception as e:
            self.assertTrue(False, f"Funktio antoi virheen kun sitä kutsuttiin näin:" + 
                f'\nsumma(1)\n{e}')
        taip = str(type(val)).replace("<class '","").replace("'>","")
        self.assertTrue(type(val) == int, f"Funktion summa pitäisi palauttaa arvo, jonka tyyppi on int," +  
            f" nyt se palauttaa arvon {val} joka on tyyppiä {taip}\n kun sitä kutsutaan näin\n" +  
            'summa(1)')
        

    def test_3_onko_rekursiivinen(self):
        from src.rekursiivinen_summa import summa
        self.assertTrue(reflect.test_recursion(summa, 2), 
            f'"Funkton summa pitäisi kutsua itseään rekursiivisesti.\n' + 
            f'Nyt kutsu summa(2) ei johda uusiin funktion summa kutsuihin.')

    def test_4_testaa_arvoilla(self):
        from src.rekursiivinen_summa import summa
        test_cases = [2,4,6,8,7,5,3]
        for test_case in test_cases:
            val = summa(test_case)
            corr = sum(list(range(test_case + 1)))

            self.assertEqual(val, corr, f'Funktion pitäisi palauttaa arvo\n{corr}\n' + 
            f'kun sitä kutsutaan parametrilla\n{test_case}\nnyt funktio palauttaa\n' + 
            f'{val}')

        
if __name__ == '__main__':
    unittest.main()
