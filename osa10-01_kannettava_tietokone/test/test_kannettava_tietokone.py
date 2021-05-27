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

exercise = 'src.kannettava_tietokone'

def f(attr: list):
    return ",".join([str(x) for x in attr]) 

@points('10.kannettava_tietokone')
class KannettavaTietokoneTest(unittest.TestCase):
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
            from src.kannettava_tietokone import Tietokone
            a = Tietokone("hal", 1)
        except Exception as e:
            self.fail(f'Konstruktorikutsu Tietokone("hal", 1) antoi virheen \n{e}\n' + 
            'Ethän ole muuttanut luokan Tietokone määrittelyä?')

        try:
            from src.kannettava_tietokone import KannettavaTietokone
            a = KannettavaTietokone("hal", 1, 1)
        except Exception as e:
            self.fail(f'Konstruktorikutsu KannettavaTietokone("hal", 1, 1) antoi virheen \n{e}\n' + 
            'Varmista, että luokka on määritelty.')

    def test_2_perinta(self):
        from src.kannettava_tietokone import Tietokone, KannettavaTietokone
        a = KannettavaTietokone("hal", 1, 1)
        self.assertTrue(isinstance(a, Tietokone), f"Luokan KannettavaTietokone pitäisi " +
            'periä luokka Tietokone!')

    def test_3_str_toimii(self):
        from src.kannettava_tietokone import Tietokone, KannettavaTietokone
        test_cases = [("C65",1,10), ("IPM MikroMaija", 128, 4), ("Zony", 1650, 4)]
        for test_case in test_cases:
            kone = KannettavaTietokone(test_case[0], test_case[1], test_case[2])
            val = str(kone)
            corr = f"{test_case[0]}, {test_case[1]} MHz, {test_case[2]} kg"
            self.assertEqual(val, corr, f'Metodin __str__ pitäisi palauttaa\n{corr}\n' + 
                f'mutta nyt metodi palauttaa\n{val}\nkun olio alustettiin näin:\n' + 
                f'KannettavaTietokone("{test_case[0]}", {test_case[1]}, {test_case[2]})')

        

    
if __name__ == '__main__':
    unittest.main()
