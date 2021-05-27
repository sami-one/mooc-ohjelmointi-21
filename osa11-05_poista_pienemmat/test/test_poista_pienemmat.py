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

exercise = 'src.poista_pienemmat'

def source_rows(funktio: callable):
    src = inspect.getsource(funktio)
    lines = [line.strip() for line in re.split('\\n|;', src) 
        if len(line.strip()) > 0 and not line.strip().startswith("#")]
    return len(lines)

@points('11.poista_pienemmat')
class PoistaPienemmatTest(unittest.TestCase):
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
            from src.poista_pienemmat import poista_pienemmat
        except Exception as e:
            self.fail(f'Ohjelmasta pitäisi löytyä funktio nimeltä poista_pienemmat.')

    def test_2_paluuarvon_tyyppi(self):
        try:
            from src.poista_pienemmat import poista_pienemmat
            val = poista_pienemmat([1,3],2)
        except Exception as e:
            self.assertTrue(False, f"Funktio antoi virheen kun sitä kutsuttiin näin:" + 
                f"\npoista_pienemmat([1,3],2):\n{e}")
        taip = str(type(val)).replace("<class '","").replace("'>","")
        self.assertTrue(type(val) == list, f"Funktion poista_pienemmat pitäisi palauttaa arvo, jonka tyyppi on list," +  
            f" nyt se palauttaa arvon {val} joka on tyyppiä {taip}\n kun sitä kutsutaan parametrilla\n" +  
            "poista_pienemmat([1,3],2)")
        

    def test_3_funktion_pituus(self):
        from src.poista_pienemmat import poista_pienemmat
        lines = source_rows(poista_pienemmat)
        max_lines = 2
        self.assertTrue(lines <= max_lines, f'Funktiossa poista_pienemmat saa tässä tehtävässä olla korkeintaan'+ 
            f' {max_lines} riviä.\n' +
            f'Nyt funktiossa on yhteensä {lines} riviä (poislukien tyhjät rivit ja kommentit.')

    def test_4_testaa_arvoilla1(self):
        test_case = ([1,2,3,4,5,6,7],4)
        corr = [4,5,6,7]
        from src.poista_pienemmat import poista_pienemmat
        val = poista_pienemmat(test_case[0], test_case[1])

        self.assertEqual(val, corr, f'Funktion pitäisi palauttaa lista\n{corr}\n' + 
            f'kun sitä kutsutaan parametrilla\n{test_case}\nnyt funktio palauttaa\n' + 
            f'{val}')

    def test_5_testaa_arvoilla2(self):
        test_case = ([100,101,102,105,106,103,99,98,107],105)
        corr = [105,106,107]
        from src.poista_pienemmat import poista_pienemmat
        val = poista_pienemmat(test_case[0], test_case[1])

        self.assertEqual(val, corr, f'Funktion pitäisi palauttaa lista\n{corr}\n' + 
            f'kun sitä kutsutaan parametrilla\n{test_case}\nnyt funktio palauttaa\n' + 
            f'{val}')

    def test_6_testaa_arvoilla3(self):
        test_case = ([-5,-3,-10,-15,-16,-11,-12,-8],-12)
        corr = [-5,-3,-10,-11,-12,-8]
        from src.poista_pienemmat import poista_pienemmat
        val = poista_pienemmat(test_case[0], test_case[1])

        self.assertEqual(val, corr, f'Funktion pitäisi palauttaa lista\n{corr}\n' + 
            f'kun sitä kutsutaan parametrilla\n{test_case}\nnyt funktio palauttaa\n' + 
            f'{val}')

    








    
if __name__ == '__main__':
    unittest.main()
