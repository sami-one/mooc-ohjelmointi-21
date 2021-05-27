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

exercise = 'src.asuntovertailu'

def f(attr: list):
    return ",".join([str(x) for x in attr]) 


class AsuntovertailuTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=[AssertionError("Syötteen pyytämistä ei odotettu")]):
           cls.module = load_module(exercise, 'fi')

    @points('9.asuntovertailu_osa1')
    def test_0a_paaohjelma_kunnossa(self):
        ok, line = check_source(self.module)
        message = """Funktioita testaava koodi tulee sijoittaa lohkon
if __name__ == "__main__":
sisälle. Seuraava rivi tulee siirtää:
"""
        self.assertTrue(ok, message+line)

    @points('9.asuntovertailu_osa1')
    def test_1_luokka_olemassa(self):
        try:
            from src.asuntovertailu import Asunto
            h = Asunto(1,1,1)
        except Exception as e:
            self.fail(f'Konstruktorikutsu Asunto(1,1,1) antoi virheen \n{e}\n' + 
            'Älä muuta luokan konstruktoria!')        

    @points('9.asuntovertailu_osa1')
    def test_2_onko_suurempi(self):
        from src.asuntovertailu import Asunto 
        a1 = Asunto(1,1,1)
        a2 = Asunto(2,2,2)
        a1.suurempi(a2)

        test_cases = [((1,24,2500), (2,48,3200)), ((2,43,4200), (1,52,3900)), 
                      ((3,67,3000), (3,69,3000)), ((4,100,5000), (4,99,5010))]
        for test_case in test_cases:
            d1,d2 = test_case
            a1 = Asunto(d1[0],d1[1],d1[2])
            a2 = Asunto(d2[0],d2[1],d2[2])

            val = a1.suurempi(a2)
            corr = d1[1] > d2[1]

            self.assertEqual(val, corr, f'Metodikutsun asunto1.suurempi(asunto2) pitäisi ' +
                f'palauttaa {corr}, kun oliot on alustettu seuraavasti:\n' +
                f'asunto1 = Asunto({d1[0]},{d1[1]},{d1[2]})\n' + 
                f'asunto2 = Asunto({d2[0]},{d2[1]},{d2[2]})\n' +
                f'Nyt metodi palautti {val}.')
    
    @points('9.asuntovertailu_osa2')
    def test_3_hintaero(self):
        from src.asuntovertailu import Asunto 
        a1 = Asunto(1,1,1)
        a2 = Asunto(2,2,2)
        a1.hintaero(a2)

        test_cases = [((1,24,2500), (2,48,3200)), ((2,43,4200), (1,32,3900)), 
                      ((3,67,3000), (3,69,3000)), ((4,100,5000), (4,99,5000))]
        for test_case in test_cases:
            d1,d2 = test_case
            a1 = Asunto(d1[0],d1[1],d1[2])
            a2 = Asunto(d2[0],d2[1],d2[2])

            val = a1.hintaero(a2)
            corr = abs((d1[1] * d1[2]) - (d2[1] * d2[2]))

            self.assertEqual(val, corr, f'Metodikutsun asunto1.hintaero(asunto2) pitäisi ' +
                f'palauttaa {corr}, kun oliot on alustettu seuraavasti:\n' +
                f'asunto1 = Asunto({d1[0]},{d1[1]},{d1[2]})\n' + 
                f'asunto2 = Asunto({d2[0]},{d2[1]},{d2[2]})\n' +
                f'Nyt metodi palautti {val}.')

    @points('9.asuntovertailu_osa3')
    def test_4_onko_kalliimpi(self):
        from src.asuntovertailu import Asunto 
        a1 = Asunto(1,1,1)
        a2 = Asunto(2,2,2)
        a1.kalliimpi(a2)

        test_cases = [((1,24,2500), (2,48,3200)), ((2,43,4200), (1,32,3900)), 
                      ((3,67,3000), (3,69,3000)), ((4,100,5000), (4,99,5000))]
        for test_case in test_cases:
            d1,d2 = test_case
            a1 = Asunto(d1[0],d1[1],d1[2])
            a2 = Asunto(d2[0],d2[1],d2[2])

            val = a1.kalliimpi(a2)
            corr = (d1[1] * d1[2]) > (d2[1] * d2[2])

            self.assertEqual(val, corr, f'Metodikutsun asunto1.kalliimpi(asunto2) pitäisi ' +
                f'palauttaa {corr}, kun oliot on alustettu seuraavasti:\n' +
                f'asunto1 = Asunto({d1[0]},{d1[1]},{d1[2]})\n' + 
                f'asunto2 = Asunto({d2[0]},{d2[1]},{d2[2]})\n' +
                f'Nyt metodi palautti {val}.')
                


                
if __name__ == '__main__':
    unittest.main()
