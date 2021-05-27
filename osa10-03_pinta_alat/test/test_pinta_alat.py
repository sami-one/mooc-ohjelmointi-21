import unittest
from unittest.mock import patch

from tmc import points, reflect
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import os.path
import textwrap
from random import choice, randint, shuffle
from datetime import date

exercise = 'src.pinta_alat'

def f(attr: list):
    return "\n".join([str(x) for x in attr])

class PintaalatTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=[AssertionError("Syötteen pyytämistä ei odotettu")]):
           cls.module = load_module(exercise, 'fi')

    @points('10.pinta_alat_osa1')
    def test_0a_paaohjelma_kunnossa(self):
        ok, line = check_source(self.module)
        message = """Funktioita testaava koodi tulee sijoittaa lohkon
if __name__ == "__main__":
sisälle. Seuraava rivi tulee siirtää:
"""
        self.assertTrue(ok, message+line)

    @points('10.pinta_alat_osa1')
    def test_0b_luokka_suorakulmio_olemassa(self):
        try:
            from src.pinta_alat import Suorakulmio
            a = Suorakulmio(1,2)
        except Exception as e:
            self.fail(f'Konstruktorikutsu Suorakulmio(1,2) antoi virheen \n{e}\n' + 
            'Ethän ole muuttanut luokan Suorakulmio määrittelyä?')

    @points('10.pinta_alat_osa1')
    def test_1_luokka_nelio_olemassa(self):
        try:
            from src.pinta_alat import Nelio
            a = Nelio(1)
        except Exception as e:
            self.fail(f'Konstruktorikutsu Nelio(1) antoi virheen \n{e}\n' + 
            'Varmista, että luokka on määritelty.')

    @points('10.pinta_alat_osa1')
    def test_2_nelio_perinta(self):
        from src.pinta_alat import Suorakulmio, Nelio
        a = Nelio(1)
        self.assertTrue(isinstance(a, Suorakulmio), f"Luokan Nelio pitäisi " +
            'periä luokka Suorakulmio!')

    @points('10.pinta_alat_osa1')
    def test_3_nelio_ei_uusia_attribuutteja(self):
        from src.pinta_alat import Suorakulmio, Nelio
        a = Nelio(1)
        b = Suorakulmio(1,2)
        ref = reflect.Reflect()
        ref.set_object(a)
        attr = ref.list_attributes(True)
        self.assertTrue(len(attr) == 3, f"Luokalle Nelio ei saa määritellä " +
            "uusia attribuutteja!")

    @points('10.pinta_alat_osa1')
    def test_4_nelio_str(self):
        from src.pinta_alat import Suorakulmio, Nelio
        test_cases = (1,2,4,6,8)
        for test_case in test_cases:
            nelio = Nelio(test_case)
            val = str(nelio)
            corr = f"neliö {test_case}x{test_case}"
            self.assertEqual(corr, val, f'Metodin __str__ pitäisi palauttaa ' + 
                f'\n{corr}\nmutta nyt se palauttaa\n{val}\nkun olio on ' + 
                f'alustettu näin:\nNelio({test_case})')

    @points('10.pinta_alat_osa1')
    def test_5_nelio_pinta_ala(self):
        from src.pinta_alat import Suorakulmio, Nelio
        test_cases = (1,2,4,6,8)
        for test_case in test_cases:
            nelio = Nelio(test_case)
            val = nelio.pinta_ala()
            corr = test_case ** 2
            self.assertEqual(corr, val, f'Metodin pinta_ala pitäisi palauttaa ' + 
                f'\n{corr}\nmutta nyt se palauttaa\n{val}\nkun olio on ' + 
                f'alustettu näin:\nNelio({test_case})')

if __name__ == '__main__':
    unittest.main()
