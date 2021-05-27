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

exercise = 'src.tahtirivit'

def source_rows(funktio: callable):
    src = inspect.getsource(funktio)
    lines = [line.strip() for line in re.split('\\n|;', src) 
        if len(line.strip()) > 0 and not line.strip().startswith("#")]
    return len(lines)

@points('11.tahtirivit')
class TahtirivitTest(unittest.TestCase):
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
            from src.tahtirivit import tahtirivit
        except Exception as e:
            self.fail(f'Ohjelmasta pitäisi löytyä funktio nimeltä tahtirivit.')

    def test_2_paluuarvon_tyyppi(self):
        try:
            from src.tahtirivit import tahtirivit
            val = tahtirivit([1])
        except Exception as e:
            self.assertTrue(False, f"Funktio antoi virheen kun sitä kutsuttiin näin:\ntahtirivit([1]):\n{e}")
        taip = str(type(val)).replace("<class '","").replace("'>","")
        self.assertTrue(type(val) == list, f"Funktion tahtirivit pitäisi palauttaa arvo, jonka tyyppi on list," +  
            f" nyt se palauttaa arvon {val} joka on tyyppiä {taip}\n kun sitä kutsutaan parametrilla\n" +  
            "tahtirivit([1])")
        

    def test_3_funktion_pituus(self):
        from src.tahtirivit import tahtirivit
        lines = source_rows(tahtirivit)
        max_lines = 2
        self.assertTrue(lines <= max_lines, f'Funktiossa tahtirivit saa tässä tehtävässä olla korkeintaan'+ 
            f' {max_lines} riviä.\n' +
            f'Nyt funktiossa on yhteensä {lines} riviä (poislukien tyhjät rivit ja kommentit.')

    def test_4_testaa_arvoilla1(self):
        test_case = [1,2,3]
        corr = ["*","**","***"]
        from src.tahtirivit import tahtirivit
        val = tahtirivit(test_case)

        self.assertEqual(val, corr, f'Funktion pitäisi palautta lista\n{corr}\n' + 
            f'kun sitä kutsutaan parametrilla\n{test_case}\nnyt funktio palauttaa\n' + 
            f'{val}')

    def test_5_testaa_arvoilla2(self):
        test_case = [4,3,2,3,4]
        corr = ["****","***","**","***","****"]
        from src.tahtirivit import tahtirivit
        val = tahtirivit(test_case)

        self.assertEqual(val, corr, f'Funktion pitäisi palautta lista\n{corr}\n' + 
            f'kun sitä kutsutaan parametrilla\n{test_case}\nnyt funktio palauttaa\n' + 
            f'{val}')

    def test_5_testaa_arvoilla3(self):
        test_case = [6,4,2,10]
        corr = ["******","****","**","**********"]
        from src.tahtirivit import tahtirivit
        val = tahtirivit(test_case)

        self.assertEqual(val, corr, f'Funktion pitäisi palautta lista\n{corr}\n' + 
            f'kun sitä kutsutaan parametrilla\n{test_case}\nnyt funktio palauttaa\n' + 
            f'{val}')



    
if __name__ == '__main__':
    unittest.main()
