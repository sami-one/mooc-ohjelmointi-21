import unittest
from unittest.mock import patch

from tmc import points, reflect
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import os.path
import textwrap
from random import choice, randint
from datetime import date

exercise = 'src.postinumerot'

def f(attr: list):
    return ",".join([str(x) for x in attr]) 

@points('9.postinumerot')
class PostinumeroTest(unittest.TestCase):
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

    def test_1_luokka_olemassa(self):
        try:
            from src.postinumerot import Kaupunki
            a = Kaupunki("Helsinki", 500000)
        except Exception as e:
            self.fail(f'Konstruktorikutsu Kaupunki("Helsinki", 500000) antoi virheen \n{e}\n' + 
            'Varmista, ettei luokka ole rikki.')

    def test_2_muuttuja_olemassa(self):
        from src.postinumerot import Kaupunki
        val = Kaupunki.postinumerot
        taip = str(type(val)).replace("<class '","").replace("'>","")
        self.assertTrue(type(val) == dict, f'Luokkamuuttujan Kaupunki.postinumerot pitäisi viitata sanakirjaan (dict). ' +
            f'Nyt sen arvo on {val} joka on tyyppiä {taip}.')


    def test_3_arvot(self):
        from src.postinumerot import Kaupunki
        test_cases = [("Helsinki", "00100"), 
                    ("Turku", "20100"),
                    ("Tampere", "33100"),
                    ("Jyväskylä", "40100"),
                    ("Oulu", "90100")]
        val = Kaupunki.postinumerot

        for test_case in test_cases:
            if test_case[0] not in val or val[test_case[0]] != test_case[1]:
                    self.fail(f'Sanakirjasta Kaupunki.postinumerot pitäisi löytyä avain-arvo-pari\n' + 
                        f'{test_case[0]}: {test_case[1]}')
            
   
if __name__ == '__main__':
    unittest.main()
