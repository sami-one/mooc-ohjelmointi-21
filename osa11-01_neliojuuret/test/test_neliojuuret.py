import unittest
from unittest.mock import patch

from tmc import points, reflect
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import os.path
import textwrap
import inspect, re
from random import choice, randint, shuffle
from math import sqrt

exercise = 'src.neliojuuret'

def source_rows(funktio: callable):
    src = inspect.getsource(funktio)
    lines = [line.strip() for line in re.split('\\n|;', src) 
        if len(line.strip()) > 0 and not line.strip().startswith("#")]
    return len(lines)

@points('11.neliojuuret')
class NeliojuuretTest(unittest.TestCase):
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
            from src.neliojuuret import neliojuuret
        except Exception as e:
            self.fail(f'Ohjelmasta pitäisi löytyä funktio nimeltä neliojuuret.')

    def test_2_paluuarvon_tyyppi(self):
        try:
            from src.neliojuuret import neliojuuret
            val = neliojuuret([1])
        except Exception as e:
            self.assertTrue(False, f"Funktio antoi virheen kun sitä kutsuttiin näin:\nneliojuuret([1]):\n{e}")
        taip = str(type(val)).replace("<class '","").replace("'>","")
        self.assertTrue(type(val) == list, f"Funktion neliojuuret pitäisi palauttaa arvo, jonka tyyppi on list," +  
            f" nyt se palauttaa arvon {val} joka on tyyppiä {taip}\n kun sitä kutsutaan parametrilla" +  
            "\nneliojuuret([1])")
    

    def test_3_funktion_pituus(self):
        from src.neliojuuret import neliojuuret
        lines = source_rows(neliojuuret)
        max_lines = 2
        self.assertTrue(lines <= max_lines, f'Funktiossa neliojuuret saa tässä tehtävässä olla korkeintaan'+ 
            f' {max_lines} riviä.\n' +
            f'Nyt funktiossa on yhteensä {lines} riviä (poislukien tyhjät rivit ja kommentit.')

    def test_4_testaa_arvoilla1(self):
        test_case = [1,4,9,16,100]
        corr = [1.0, 2.0, 3.0, 4.0, 10.0]
        from src.neliojuuret import neliojuuret
        val = neliojuuret(test_case)

        self.assertEqual(val, corr, f'Funktion pitäisi palautta lista\n{corr}\n' + 
            f'kun sitä kutsutaan parametrilla\n{test_case}\nnyt funktio palauttaa\n' + 
            f'{val}')

    def test_5_testaa_arvoilla2(self):
        test_case = [25,36,49,64,81,10000,400]
        corr = [5.0,6.0,7.0,8.0,9.0,100.0,20.0]
        from src.neliojuuret import neliojuuret
        val = neliojuuret(test_case)

        self.assertEqual(val, corr, f'Funktion pitäisi palautta lista\n{corr}\n' + 
            f'kun sitä kutsutaan parametrilla\n{test_case}\nnyt funktio palauttaa\n' + 
            f'{val}')
    
if __name__ == '__main__':
    unittest.main()
