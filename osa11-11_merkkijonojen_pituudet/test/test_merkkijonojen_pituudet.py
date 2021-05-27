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

exercise = 'src.merkkijonojen_pituudet'

def source_rows(funktio: callable):
    src = inspect.getsource(funktio)
    lines = [line.strip() for line in re.split('\\n|;', src) 
        if len(line.strip()) > 0 and not line.strip().startswith("#")]
    return len(lines)

@points('11.merkkijonojen_pituudet')
class MerkkijonojenPituudetTest(unittest.TestCase):
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
            from src.merkkijonojen_pituudet import pituudet
        except Exception as e:
            self.fail(f'Ohjelmasta pitäisi löytyä funktio nimeltä pituudet.')

    def test_2_paluuarvon_tyyppi(self):
        try:
            from src.merkkijonojen_pituudet import pituudet
            val = pituudet(["a"])
        except Exception as e:
            self.assertTrue(False, f"Funktio antoi virheen kun sitä kutsuttiin näin:" + 
                f'\npituudet(["a"])\n{e}')
        taip = str(type(val)).replace("<class '","").replace("'>","")
        self.assertTrue(type(val) == dict, f"Funktion pituudet pitäisi palauttaa arvo, jonka tyyppi on dict," +  
            f" nyt se palauttaa arvon {val} joka on tyyppiä {taip}\n kun sitä kutsutaan näin\n" +  
            'pituudet(["a"])')
        

    def test_3_funktion_pituus(self):
        from src.merkkijonojen_pituudet import pituudet
        lines = source_rows(pituudet)
        max_lines = 2
        self.assertTrue(lines <= max_lines, f'Funktiossa pituudet saa tässä tehtävässä olla korkeintaan'+ 
            f' {max_lines} riviä.\n' +
            f'Nyt funktiossa on yhteensä {lines} riviä (poislukien tyhjät rivit ja kommentit.')

    def test_4_testaa_arvoilla1(self):
        test_case = ["eka","toka","kolmas"]
        corr = {"eka": 3, "toka": 4, "kolmas": 6}
        from src.merkkijonojen_pituudet import pituudet
        val = pituudet(test_case)

        self.assertEqual(val, corr, f'Funktion pitäisi palauttaa sanakirja\n{corr}\n' + 
            f'kun sitä kutsutaan parametreilla\n{test_case}\nnyt funktio palauttaa\n' + 
            f'{val}')

    def test_5_testaa_arvoilla2(self):
        test_case = ["koira","kissa","marsu","hamsteri","gerbiili","kultakala"]
        corr = {"koira":5, "kissa":5, "marsu":5, "hamsteri":8, "gerbiili":8, "kultakala":9}
        from src.merkkijonojen_pituudet import pituudet
        val = pituudet(test_case)

        self.assertEqual(val, corr, f'Funktion pitäisi palauttaa sanakirja\n{corr}\n' + 
            f'kun sitä kutsutaan parametreilla\n{test_case}\nnyt funktio palauttaa\n' + 
            f'{val}')

    def test_6_testaa_arvoilla3(self):
        test_case = ["commodore", "atari", "amstrad", "msx", "spectrum"]
        corr = {'commodore': 9, 'atari': 5, 'amstrad': 7, 'msx': 3, 'spectrum': 8}
        from src.merkkijonojen_pituudet import pituudet
        val = pituudet(test_case)

        self.assertEqual(val, corr, f'Funktion pitäisi palauttaa sanakirja\n{corr}\n' + 
            f'kun sitä kutsutaan parametreilla\n{test_case}\nnyt funktio palauttaa\n' + 
            f'{val}')

    




    

   

    








    
if __name__ == '__main__':
    unittest.main()
