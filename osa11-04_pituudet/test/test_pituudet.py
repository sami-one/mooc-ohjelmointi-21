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

exercise = 'src.pituudet'

def source_rows(funktio: callable):
    src = inspect.getsource(funktio)
    lines = [line.strip() for line in re.split('\\n|;', src) 
        if len(line.strip()) > 0 and not line.strip().startswith("#")]
    return len(lines)

@points('11.pituudet')
class PItuudetTest(unittest.TestCase):
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
            from src.pituudet import pituudet
        except Exception as e:
            self.fail(f'Ohjelmasta pitäisi löytyä funktio nimeltä pituudet.')

    def test_2_paluuarvon_tyyppi(self):
        try:
            from src.pituudet import pituudet
            val = pituudet([[1]])
        except Exception as e:
            self.assertTrue(False, f"Funktio antoi virheen kun sitä kutsuttiin näin:\npituudet([[1]]):\n{e}")
        taip = str(type(val)).replace("<class '","").replace("'>","")
        self.assertTrue(type(val) == list, f"Funktion pituudet pitäisi palauttaa arvo, jonka tyyppi on list," +  
            f" nyt se palauttaa arvon {val} joka on tyyppiä {taip}\n kun sitä kutsutaan parametrilla\n" +  
            "pituudet([[1]])")
        

    def test_3_funktion_pituus(self):
        from src.pituudet import pituudet
        lines = source_rows(pituudet)
        max_lines = 2
        self.assertTrue(lines <= max_lines, f'Funktiossa pituudet saa tässä tehtävässä olla korkeintaan'+ 
            f' {max_lines} riviä.\n' +
            f'Nyt funktiossa on yhteensä {lines} riviä (poislukien tyhjät rivit ja kommentit.')

    def test_4_testaa_arvoilla1(self):
        test_case = [[1,2],[3,4]]
        corr = [2,2]
        from src.pituudet import pituudet
        val = pituudet(test_case)

        self.assertEqual(val, corr, f'Funktion pitäisi palauttaa lista\n{corr}\n' + 
            f'kun sitä kutsutaan parametrilla\n{test_case}\nnyt funktio palauttaa\n' + 
            f'{val}')

    def test_5_testaa_arvoilla2(self):
        test_case = [[1,2,3],[4,3,2,1],[1,2,1,2,1,2]]
        corr = [3,4,6]
        from src.pituudet import pituudet
        val = pituudet(test_case)

        self.assertEqual(val, corr, f'Funktion pitäisi palauttaa lista\n{corr}\n' + 
            f'kun sitä kutsutaan parametrilla\n{test_case}\nnyt funktio palauttaa\n' + 
            f'{val}')

    def test_6_testaa_arvoilla2(self):
        test_case = [[1,2,3,1,2,3],[1,2,3,4,5,4,3,2,1],[1],[1]]
        corr = [6,9,1,1]
        from src.pituudet import pituudet
        val = pituudet(test_case)

        self.assertEqual(val, corr, f'Funktion pitäisi palauttaa lista\n{corr}\n' + 
            f'kun sitä kutsutaan parametrilla\n{test_case}\nnyt funktio palauttaa\n' + 
            f'{val}')






    
if __name__ == '__main__':
    unittest.main()
