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

exercise = 'src.yleisimmat_sanat'

def source_rows(funktio: callable):
    src = inspect.getsource(funktio)
    lines = [line.strip() for line in re.split('\\n|;', src) 
        if len(line.strip()) > 0 and not line.strip().startswith("#")]
    return len(lines)

@points('11.yleisimmat_sanat')
class YleisimmatSanatTest(unittest.TestCase):
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
            from src.yleisimmat_sanat import yleisimmat_sanat
        except Exception as e:
            self.fail(f'Ohjelmasta pitäisi löytyä funktio nimeltä yleisimmat_sanat.')

    def test_2_paluuarvon_tyyppi(self):
        try:
            from src.yleisimmat_sanat import yleisimmat_sanat
            val = yleisimmat_sanat("comprehensions.txt", 3)
        except Exception as e:
            self.assertTrue(False, f"Funktio antoi virheen kun sitä kutsuttiin näin:" + 
                f'\nyleisimmat_sanat("comprehensions.txt", 3)\n{e}')
        taip = str(type(val)).replace("<class '","").replace("'>","")
        self.assertTrue(type(val) == dict, f"Funktion yleisimmat_sanat pitäisi palauttaa arvo, jonka tyyppi on dict," +  
            f" nyt se palauttaa arvon {val} joka on tyyppiä {taip}\n kun sitä kutsutaan näin\n" +  
            'yleisimmat_sanat("comprehensions.txt", 3))')


    def test_3_testaa_tiedosto1(self):
        fname = "comprehensions.txt"
        from src.yleisimmat_sanat import yleisimmat_sanat
        limit = 3
        val = yleisimmat_sanat(fname, limit)
        corr = {'comprehension': 4, 'is': 3, 'and': 3, 'for': 3, 'list': 4, 'in': 3}

        self.assertEqual(val, corr, f'Funktion pitäisi palauttaa sanakirja\n' + 
            f'{corr}\nkun luetaan tiedostoa {fname} ja raja on {limit}.\n' + 
            f'Nyt funktio palauttaa sanakirjan\n{val}')

    def test_4_testaa_tiedosto2(self):
        fname = "programming.txt"
        from src.yleisimmat_sanat import yleisimmat_sanat
        limit = 6
        val = yleisimmat_sanat(fname, limit)
        corr = {'and': 7, 'of': 6, 'programming': 9}

        self.assertEqual(val, corr, f'Funktion pitäisi palauttaa sanakirja\n' + 
            f'{corr}\nkun luetaan tiedostoa {fname} ja raja on {limit}.\n' + 
            f'Nyt funktio palauttaa sanakirjan\n{val}')

    def test_5_testaa_tiedosto3(self):
        fname = "comprehensions.txt"
        from src.yleisimmat_sanat import yleisimmat_sanat
        limit = 4
        val = yleisimmat_sanat(fname, limit)
        corr = {'comprehension': 4, 'list': 4}

        self.assertEqual(val, corr, f'Funktion pitäisi palauttaa sanakirja\n' + 
            f'{corr}\nkun luetaan tiedostoa {fname} ja raja on {limit}.\n' + 
            f'Nyt funktio palauttaa sanakirjan\n{val}')

    def test_6_testaa_tiedosto4(self):
        fname = "programming.txt"
        from src.yleisimmat_sanat import yleisimmat_sanat
        limit = 4
        val = yleisimmat_sanat(fname, limit)
        corr = {'is': 5, 'and': 7, 'the': 5, 'of': 6, 'in': 4, 'programming': 9, 'languages': 5}
        
        self.assertEqual(val, corr, f'Funktion pitäisi palauttaa sanakirja\n' + 
            f'{corr}\nkun luetaan tiedostoa {fname} ja raja on {limit}.\n' + 
            f'Nyt funktio palauttaa sanakirjan\n{val}')






    

   

    








    
if __name__ == '__main__':
    unittest.main()
