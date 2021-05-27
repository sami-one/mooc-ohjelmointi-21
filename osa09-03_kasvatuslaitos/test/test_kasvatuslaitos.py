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

exercise = 'src.kasvatuslaitos'

def f(attr: list):
    return ",".join(attr)


class HyvaksytytSuorituksetTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=[AssertionError("Syötteen pyytämistä ei odotettu")]):
           cls.module = load_module(exercise, 'fi')

    @points('9.kasvatuslaitos_osa1')
    def test_0a_paaohjelma_kunnossa(self):
        ok, line = check_source(self.module)
        message = """Funktioita testaava koodi tulee sijoittaa lohkon
if __name__ == "__main__":
sisälle. Seuraava rivi tulee siirtää:
"""
        self.assertTrue(ok, message+line)

    @points('9.kasvatuslaitos_osa1')
    def test_1_luokat_olemassa(self):
        try:
            from src.kasvatuslaitos import Henkilo
            h = Henkilo("Jarmo", 19, 175, 73)
        except Exception as e:
            self.fail(f'Konstruktorikutsu Henkilo("Jarmo", 19, 175, 73) antoi virheen \n{e}\n' +
                'Ethän ole muuttanut luokan Henkilo toteutusta?')
        try:
            from src.kasvatuslaitos import Kasvatuslaitos
            k = Kasvatuslaitos()
        except Exception as e:
            self.fail(f'Konstruktorikutsu Kasvatuslaitos() antoi virheen \n{e}\n' +
                'Onhan luokka toteutettu?')

    @points('9.kasvatuslaitos_osa1')
    def test_2_punnitse_toimii(self):
        test_cases = [("Jarmo", 19, 175, 73), ("Piia", 10, 143, 35), ("Kari", 44, 185, 96), 
            ("Arto", 37, 180, 78), ("Liisa", 17, 176, 68)]
        for test_case in test_cases:
            from src.kasvatuslaitos import Henkilo, Kasvatuslaitos
            laitos = Kasvatuslaitos()
            h = Henkilo(test_case[0], test_case[1], test_case[2], test_case[3])
            val = laitos.punnitse(h)
        
            corr = test_case[3]

            self.assertEqual(val, corr, f'Metodi punnitse() palautti arvon {val}.\nOikea arvo olisi ollut {corr}, ' +
                f'kun olio alustettiin seuraavasti:\nHenkilo{test_case}')
            

    @points('9.kasvatuslaitos_osa2')    
    def test_3_syottaminen_toimii(self):
        test_cases = [("Jarmo", 19, 175, 73, 1), ("Piia", 10, 143, 35, 3), ("Kari", 44, 185, 96, 5), 
            ("Arto", 37, 180, 78, 4), ("Liisa", 17, 176, 68, 2)]
        for test_case in test_cases:
            from src.kasvatuslaitos import Henkilo, Kasvatuslaitos
            laitos = Kasvatuslaitos()
            h = Henkilo(test_case[0], test_case[1], test_case[2], test_case[3])
            for i in range(test_case[4]):
                laitos.syota(h)
            
            val = laitos.punnitse(h)
            corr = test_case[3] + test_case[4]

            self.assertEqual(val, corr, f'Henkilön paino on nyt {val}.\n, vaikka sen pitäisi olla {corr}, ' +
                f'kun olio alustettiin seuraavasti:\nHenkilo{test_case[:-1]}\n' +
                f'ja metodia syota() kutsuttiin {test_case[4]} kertaa.')
    
    @points('9.kasvatuslaitos_osa3')
    def test_4_punnitusten_laskeminen(self):
        test_cases = [("Jarmo", 19, 175, 73, 1), ("Piia", 10, 143, 35, 3), ("Kari", 44, 185, 96, 5), 
            ("Arto", 37, 180, 78, 4), ("Liisa", 17, 176, 68, 2)]
        for i in range(1, len(test_cases)):
            from src.kasvatuslaitos import Henkilo, Kasvatuslaitos
            laitos = Kasvatuslaitos()
            for test_case in test_cases[:i]:
                h = Henkilo(test_case[0], test_case[1], test_case[2], test_case[3])
                laitos.punnitse(h)
            corr = i
            val = laitos.punnitukset()
            
            self.assertEqual(val, corr, f'Metodi punnitukset() palautti {val}.\n, kun oikea arvo olisi ollut {corr}, ' +
                    f'kun metodia punnitse() oli kutsuttu {i} kertaa')
    

                

                
if __name__ == '__main__':
    unittest.main()
