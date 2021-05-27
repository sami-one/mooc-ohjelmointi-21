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

exercise = 'src.parilliset'

def source_rows(funktio: callable):
    src = inspect.getsource(funktio)
    lines = [line.strip() for line in re.split('\\n|;', src) 
        if len(line.strip()) > 0 and not line.strip().startswith("#")]
    return len(lines)

@points('12.parilliset')
class ParillisetTest(unittest.TestCase):
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
            from src.parilliset import parilliset
        except Exception as e:
            self.fail(f'Ohjelmasta pitäisi löytyä funktio nimeltä parilliset.')

    def test_2_paluuarvon_tyyppi(self):
        try:
            from src.parilliset import parilliset
            val = parilliset(2,4)
        except Exception as e:
            self.fail(f"Funktio antoi virheen kun sitä kutsuttiin näin:\n"  + 
            'parilliset(2,4)\n' + 
            f'{e}')
        taip = str(type(val)).replace("<class '","").replace("'>","")
        self.assertTrue(type(val) is types.GeneratorType, f"Funktion parilliset pitäisi palauttaa generaattori," +  
            f" nyt se palauttaa arvon {val} joka on tyyppiä {taip}\n kun sitä kutsutaan parametrilla\n" +  
            'parilliset(2,4)')
        

    def test_3_testaa_arvoilla(self):
        from src.parilliset import parilliset
    
        test_cases = [(2,6), (4,11), (7,12), (20,22), (1,19)]
        for test_case in test_cases:
            func = f"parilliset {test_case}"
            corr = [x for x in range(test_case[0] 
                if test_case[0] % 2 == 0 else test_case [0] + 1, 
                test_case[1] + 1 if test_case[1] % 2 == 0 else test_case[1], 2)]
            gen = parilliset(test_case[0], test_case[1])
            val = [x for x in gen]

            self.assertEqual(val, corr, f'Generaattorin pitäisi palauttaa arvot\n{corr}\n' + 
                f'kun se on alustettu näin:\n{func}\nnyt se palauttaa arvot\n' + 
                f'{val}')

    
if __name__ == '__main__':
    unittest.main()
