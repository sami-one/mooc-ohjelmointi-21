import unittest
from unittest.mock import patch

from tmc import points, reflect
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import os.path
import textwrap
import inspect, re

exercise = 'src.sulut_tasapainossa'

@points('11.sulut_tasapainossa')
class SulutTasapainossaTest(unittest.TestCase):
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
            from src.sulut_tasapainossa import sulut_tasapainossa
        except Exception as e:
            self.fail(f'Ohjelmasta pitäisi löytyä funktio nimeltä sulut_tasapainossa.')

    def test_2_paluuarvon_tyyppi(self):
        try:
            from src.sulut_tasapainossa import sulut_tasapainossa
            val = sulut_tasapainossa("()")
        except Exception as e:
            self.assertTrue(False, f"Funktio antoi virheen kun sitä kutsuttiin näin:" + 
                f'\nsulut_tasapainossa("()")\n{e}')
        taip = str(type(val)).replace("<class '","").replace("'>","")
        self.assertTrue(type(val) == bool, f"Funktion sulut_tasapainossa pitäisi palauttaa arvo, jonka tyyppi on bool," +  
            f" nyt se palauttaa arvon {val} joka on tyyppiä {taip}\n kun sitä kutsutaan näin\n" +  
            'sulut_tasapainossa("()")')
        

    def test_3_onko_rekursiivinen(self):
        from src.sulut_tasapainossa import sulut_tasapainossa
        self.assertTrue(reflect.test_recursion(sulut_tasapainossa, "()"), 
            f'"Funkton summa pitäisi kutsua itseään rekursiivisesti.\n' + 
            f'Nyt kutsu sulut_tasapainossa("()") ei johda uusiin funktion sulut_tasapainossa kutsuihin.')

    def test_4_testaa_arvoilla1(self):
        from src.sulut_tasapainossa import sulut_tasapainossa
        test_cases = [("()",True), ("(Heippa)", True), ("haka[sulkeet]", True), ("([tupla])", True), 
            ("[eka ja (Toka)]", True), ("(x * (1 + y) / 2)", True), ("((([eka] + toka) * kolmas) - neli)", True)]
        for test_case, corr in test_cases:
            val = sulut_tasapainossa(test_case)
            self.assertEqual(val, corr, f'Funktion pitäisi palauttaa arvo\n{corr}\n' + 
            f'kun sitä kutsutaan parametrilla\n{test_case}\nnyt funktio palauttaa\n' + 
            f'{val}')

    
    def test_5_testaa_arvoilla2(self):
        from src.sulut_tasapainossa import sulut_tasapainossa
        test_cases = [("((x)", False), ("x[[]",False), ("(x)y)", False), ("x[y]z]", False), ("(z]zz", False), ("x[xx)", False), 
            ("([sulut ristissä)]", False), ("[sulut(ristissä])", False)]
        for test_case, corr in test_cases:
            val = sulut_tasapainossa(test_case)
            self.assertEqual(val, corr, f'Funktion pitäisi palauttaa arvo\n{corr}\n' + 
            f'kun sitä kutsutaan parametrilla\n{test_case}\nnyt funktio palauttaa\n' + 
            f'{val}')


        
if __name__ == '__main__':
    unittest.main()
