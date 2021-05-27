import unittest
from unittest.mock import patch

from tmc import points, reflect
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import os.path
import textwrap
import inspect, re
import types
from random import choice, randint, shuffle

exercise = 'src.alkuluvut'

def source_rows(funktio: callable):
    src = inspect.getsource(funktio)
    lines = [line.strip() for line in re.split('\\n|;', src) 
        if len(line.strip()) > 0 and not line.strip().startswith("#")]
    return len(lines)

@points('12.alkuluvut')
class AlkuluvutTest(unittest.TestCase):
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
            from src.alkuluvut import alkuluvut
        except Exception as e:
            self.fail(f'Ohjelmasta pitäisi löytyä funktio nimeltä alkuluvut.')

    def test_2_paluuarvon_tyyppi(self):
        try:
            from src.alkuluvut import alkuluvut
            val = alkuluvut()
        except Exception as e:
            self.fail(f"Funktio antoi virheen kun sitä kutsuttiin näin:\n"  + 
            'alkuluvut()\n' + 
            f'{e}')
        taip = str(type(val)).replace("<class '","").replace("'>","")
        self.assertTrue(type(val) is types.GeneratorType, f"Funktion alkuluvut pitäisi palauttaa generaattori," +  
            f" nyt se palauttaa arvon {val} joka on tyyppiä {taip}\n kun sitä kutsutaan näin\n" +  
            'alkuluvut()')
        

    def test_3_testaa_arvoilla1(self):
        from src.alkuluvut import alkuluvut
    
        test_cases = (1,3,4,7,9,12)
        al = [2,3,5,7,11,13,17,19,23,29,31,37,41,43]
        for test_case in test_cases:
            corr = al[:test_case]
            gen = alkuluvut()
            val = [next(gen) for i in range(test_case)]

            self.assertEqual(val, corr, f'Generaattorin pitäisi palauttaa arvot\n{corr}\n' + 
                f'kun se on alustettu näin:\ngen = alkuluvut()\n' +
                f'ja kutsutaan {test_case} kertaa funktiota next(gen)\n' +
                f'nyt se palauttaa arvot\n' + 
                f'{val}')

    
if __name__ == '__main__':
    unittest.main()
