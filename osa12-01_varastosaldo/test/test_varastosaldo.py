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

exercise = 'src.varastosaldo'

def source_rows(funktio: callable):
    src = inspect.getsource(funktio)
    lines = [line.strip() for line in re.split('\\n|;', src) 
        if len(line.strip()) > 0 and not line.strip().startswith("#")]
    return len(lines)

@points('12.varastosaldo')
class VarastosaldoTest(unittest.TestCase):
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
            from src.varastosaldo import jarjesta_varastosaldon_mukaan
        except Exception as e:
            self.fail(f'Ohjelmasta pitäisi löytyä funktio nimeltä jarjesta_varastosaldon_mukaan.')

    def test_2_paluuarvon_tyyppi(self):
        try:
            from src.varastosaldo import jarjesta_varastosaldon_mukaan
            val = jarjesta_varastosaldon_mukaan([("omena",1,1),("ananas",2,2)])
        except Exception as e:
            self.fail(f"Funktio antoi virheen kun sitä kutsuttiin näin:\n"  + 
            f'jarjesta_varastosaldon_mukaan([("omena",1,1),("ananas",2,2)]):\n{e}')
        taip = str(type(val)).replace("<class '","").replace("'>","")
        self.assertTrue(type(val) == list, f"Funktion jarjesta_varastosaldon_mukaan pitäisi palauttaa arvo, jonka tyyppi on list," +  
            f" nyt se palauttaa arvon {val} joka on tyyppiä {taip}\n kun sitä kutsutaan parametrilla\n" +  
            'jarjesta_varastosaldon_mukaan([("omena",1,1),("ananas",2,2)])')
        

    def test_3_testaa_arvoilla1(self):
        from src.varastosaldo import jarjesta_varastosaldon_mukaan
        test_case = [("omena",5,3), ("appelsiini",10,2), ("ananas",8,6), ("luumu",11,5)]
        test_case_2 = test_case[:]
        corr = [("appelsiini",10,2), ("omena",5,3), ("luumu",11,5), ("ananas",8,6)]
        val = jarjesta_varastosaldon_mukaan(test_case)

        self.assertEqual(val, corr, f'Funktion pitäisi palauttaa lista\n{corr}\n' + 
            f'kun sitä kutsutaan parametrilla\n{test_case}\nnyt funktio palauttaa\n' + 
            f'{val}')

        self.assertEqual(test_case, test_case_2, f"Funktio ei saa muuttaa alkuperäistä listaa!\n" + 
            f'Lista ennen kutsua oli\n{test_case_2}\nja kutsun jälkeen se on\n{test_case}.')

    def test_4_testaa_arvoilla2(self):
        from src.varastosaldo import jarjesta_varastosaldon_mukaan
        test_case = [("auto",5,13), ("mopo",10,12), ("vene",11,4), ("rullalauta",11,9), ("skootteri",11,10)]
        test_case_2 = test_case[:]
        corr = [("vene",11,4), ("rullalauta",11,9), ("skootteri",11,10), ("mopo",10,12), ("auto",5,13)]
        val = jarjesta_varastosaldon_mukaan(test_case)

        self.assertEqual(val, corr, f'Funktion pitäisi palauttaa lista\n{corr}\n' + 
            f'kun sitä kutsutaan parametrilla\n{test_case}\nnyt funktio palauttaa\n' + 
            f'{val}')

        self.assertEqual(test_case, test_case_2, f"Funktio ei saa muuttaa alkuperäistä listaa!\n" + 
            f'Lista ennen kutsua oli\n{test_case_2}\nja kutsun jälkeen se on\n{test_case}.')
    
if __name__ == '__main__':
    unittest.main()
