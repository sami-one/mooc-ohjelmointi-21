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

exercise = 'src.lista_apuri'

def f(attr: list):
    return ",".join([str(x) for x in attr]) 

@points('9.lista_apuri')
class ListaApuriTest(unittest.TestCase):
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
            from src.lista_apuri import ListaApuri
        except Exception as e:
            self.fail(f'Luokkaa ListaApuri ei löydy: \n{e}\n' + 
            'Varmista, ettei luokka ole rikki.')

    def test_2_metodit_olemassa(self):
        from src.lista_apuri import ListaApuri
        try:
            val = ListaApuri.suurin_frekvenssi([1,1,2])
            taip = str(type(val)).replace("<class '","").replace("'>","")
            self.assertTrue(type(val) == int, f'Metodin ListaApuri.suurin_frekvenssi pitäisi ' +
                f'palauttaa arvo, jonka tyyppi on int.\n' + 
                f'Nyt se palauttaa arvon {val} joka on tyyppiä {taip}.\n' + 
                f'Metodia kutsuttiin näin: ListaApuri.suurin_frekvenssi([1,1,2])')
        except Exception as e:
            self.fail(f'Metodikutsu ListaApuri.suurin_frekvenssi([1,1,2]) antoi virheen\n{e}')

        try:
            val = ListaApuri.tuplia([1,1,2])
            taip = str(type(val)).replace("<class '","").replace("'>","")
            self.assertTrue(type(val) == int, f'Metodin ListaApuri.tuplia pitäisi ' +
                f'palauttaa arvo, jonka tyyppi on int.\n' + 
                f'Nyt se palauttaa arvon {val} joka on tyyppiä {taip}.\n' + 
                f'Metodia kutsuttiin näin: ListaApuri.tuplia([1,1,2])')
        except Exception as e:
            self.fail(f'Metodikutsu ListaApuri.tuplia([1,1,2]) antoi virheen\n{e}')

    def test_3_suurin_frekvenssi(self):
        from src.lista_apuri import ListaApuri
        test_cases = [[1,1,1,2,2,3], [3,2,3,2,2,3,2,2,1,1,2], [1,5,4,5,6,7,7,5,7,7,7,], 
                      [1,2,3,1,2,3,1,2,3,4,4,4,3,4,4,3,4,4,3,2,1,4,4,4,4,4,4,4,3,2,1]]
        for test_case in test_cases:
            val = ListaApuri.suurin_frekvenssi(test_case)
            corr = max([(x,test_case.count(x)) for x in test_case], key = lambda y: y[1])[0]

            self.assertEqual(val, corr, f'Metodin ListaApuri.suurin_frekvenssi pitäisi ' + 
                f'palauttaa {corr}, kun lista on\n{test_case}\nMetodi palauttaa kuitenkin {val}.')

    def test_3_tuplia(self):
        from src.lista_apuri import ListaApuri
        test_cases = [[1,1,1,2,2,3], [3,2,3,2,2,3,1,2,4,5,5,6], [1,5,4,5,6,7,7,5,7,7,7,], 
                      [9,8,7,9,8,6,6,5,5,4,3,3]]
        for test_case in test_cases:
            val = ListaApuri.tuplia(test_case)
            corr = len([x for x in set(test_case) if test_case.count(x) > 1])

            self.assertEqual(val, corr, f'Metodin ListaApuri.tuplia pitäisi ' + 
                f'palauttaa {corr}, kun lista on\n{test_case}\nMetodi palauttaa kuitenkin {val}.')

 
   
if __name__ == '__main__':
    unittest.main()
