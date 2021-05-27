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

exercise = 'src.paivays'

def f(attr: list):
    return "\n".join([str(x) for x in attr]) 

class PaivaysTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=[AssertionError("Syötteen pyytämistä ei odotettu")]):
           cls.module = load_module(exercise, 'fi')

    @points('10.paivays_osa1')
    def test_0a_paaohjelma_kunnossa(self):
        ok, line = check_source(self.module)
        message = """Funktioita testaava koodi tulee sijoittaa lohkon
if __name__ == "__main__":
sisälle. Seuraava rivi tulee siirtää:
"""
        self.assertTrue(ok, message+line)
    
    @points('10.paivays_osa1')
    def test_1_luokka_olemassa(self):
        try:
            from src.paivays import Paivays
            a = Paivays(1,1,1900)
        except Exception as e:
            self.fail(f'Konstruktorikutsu Paivays(1,1,1900) antoi virheen \n{e}\n' + 
            'Tarkista, että luokasta voi muodostaa olion.')

    @points('10.paivays_osa1')
    def test_2_merkkijonoesitys(self):
        from src.paivays import Paivays
        test_cases = [(1,1,1900),(2,4,1984),(9,9,1976),(10,11,2015),(24,11,1299)]
        for test_case in test_cases:
            pvm = Paivays(test_case[0], test_case[1], test_case[2])
            val = str(pvm)
            corr = f"{test_case[0]}.{test_case[1]}.{test_case[2]}"

            self.assertEqual(val, corr, f'Metodin __str__ pitäisi palauttaa ' +
                f'\n{corr}\nkun päiväys on alustettu näin:\n' +
                f'Paivays({test_case[0]}, {test_case[1]}, {test_case[2]})\n' + 
                f'Nyt metodi palauttaa\n{val}')


    @points('10.paivays_osa1')
    def test_3_yhtasuuruus(self):
        from src.paivays import Paivays
        test_cases = [((1,1,1900),(1,1,1900)),((5,6,1876),(5,6,1876)),
            ((9,9,1976),(9,9,1976)), ((1,4,1800),(2,4,1800)), 
            ((1,7,1999),(1,8,1999)),((25,5,1943),(25,5,1944))]
        for test_case in test_cases:
            tc1,tc2 = test_case
            pv1 = Paivays(tc1[0], tc1[1], tc1[2])
            pv2 = Paivays(tc2[0], tc2[1], tc2[2])

            corr = (tc1 == tc2)
            val = (pv1 == pv2)
            stmt = "pv1 == pv2"
            met_name = "__eq__"

            self.assertEqual(val, corr, f'Lausekkeen\n{stmt}\npitäisi olla ' +
                f'{corr},  kun oliot on alustettu seuraavasti:\n'
                f'pv1 = Paivays({tc1[0]}, {tc1[1]}, {tc1[2]})\n' + 
                f'pv2 = Paivays({tc2[0]}, {tc2[1]}, {tc2[2]})\n' + 
                f'Nyt lauseke palauttaa {val}.\n' + 
                f'Tarkasta metodi {met_name}')

    @points('10.paivays_osa1')
    def test_4_pienempi_kuin(self):
        from src.paivays import Paivays
        test_cases = [((1,1,1900),(1,1,1901)),((5,6,1876),(6,6,1876)),
            ((9,9,1976),(9,10,1976)), ((2,4,1800),(1,4,1800)), 
            ((1,8,1999),(1,7,1999)),((25,5,1944),(25,5,1943)), 
            ((1,3,1900),(2,4,1889))]
        for test_case in test_cases:
            tc1,tc2 = test_case
            pv1 = Paivays(tc1[0], tc1[1], tc1[2])
            pv2 = Paivays(tc2[0], tc2[1], tc2[2])

            tv1 = tc1[2] * 360 + tc1[1] * 30 + tc1[0]
            tv2 = tc2[2] * 360 + tc2[1] * 30 + tc2[0]
            corr = (tv1 < tv2)
            val = (pv1 < pv2)
            stmt = "pv1 < pv2"
            met_name = "__lt__"

            self.assertEqual(val, corr, f'Lausekkeen\n{stmt}\npitäisi olla ' +
                f'{corr},  kun oliot on alustettu seuraavasti:\n'
                f'pv1 = Paivays({tc1[0]}, {tc1[1]}, {tc1[2]})\n' + 
                f'pv2 = Paivays({tc2[0]}, {tc2[1]}, {tc2[2]})\n' + 
                f'Nyt lauseke palauttaa {val}.\n' + 
                f'Tarkasta metodi {met_name}')

    @points('10.paivays_osa1')
    def test_5_suurempi_kuin(self):
        from src.paivays import Paivays
        test_cases = [((1,1,1900),(1,1,1901)),((5,6,1876),(6,6,1876)),
            ((9,9,1976),(9,10,1976)), ((2,4,1800),(1,4,1800)), 
            ((1,8,1999),(1,7,1999)),((25,5,1944),(25,5,1943)), 
            ((9,9,1900),(8,8,1901))]
        for test_case in test_cases:
            tc1,tc2 = test_case
            pv1 = Paivays(tc1[0], tc1[1], tc1[2])
            pv2 = Paivays(tc2[0], tc2[1], tc2[2])

            tv1 = tc1[2] * 360 + tc1[1] * 30 + tc1[0]
            tv2 = tc2[2] * 360 + tc2[1] * 30 + tc2[0]
            corr = (tv1 > tv2)
            val = (pv1 > pv2)
            stmt = "pv1 > pv2"
            met_name = "__lt__"

            self.assertEqual(val, corr, f'Lausekkeen\n{stmt}\npitäisi olla ' +
                f'{corr},  kun oliot on alustettu seuraavasti:\n'
                f'pv1 = Paivays({tc1[0]}, {tc1[1]}, {tc1[2]})\n' + 
                f'pv2 = Paivays({tc2[0]}, {tc2[1]}, {tc2[2]})\n' + 
                f'Nyt lauseke palauttaa {val}.\n' + 
                f'Tarkasta metodi {met_name}')

    @points('10.paivays_osa1')
    def test_6_erisuuri_kuin(self):
        from src.paivays import Paivays
        test_cases = [((1,1,1900),(1,1,1900)),((5,6,1876),(5,6,1876)),
            ((9,9,1976),(9,9,1976)), ((1,4,1800),(2,4,1800)), 
            ((1,7,1999),(1,8,1999)),((25,5,1943),(25,5,1944))]
        for test_case in test_cases:
            tc1,tc2 = test_case
            pv1 = Paivays(tc1[0], tc1[1], tc1[2])
            pv2 = Paivays(tc2[0], tc2[1], tc2[2])

            corr = (tc1 != tc2)
            val = (pv1 != pv2)
            stmt = "pv1 != pv2"
            met_name = "__ne__"

            self.assertEqual(val, corr, f'Lausekkeen\n{stmt}\npitäisi olla ' +
                f'{corr},  kun oliot on alustettu seuraavasti:\n'
                f'pv1 = Paivays({tc1[0]}, {tc1[1]}, {tc1[2]})\n' + 
                f'pv2 = Paivays({tc2[0]}, {tc2[1]}, {tc2[2]})\n' + 
                f'Nyt lauseke palauttaa {val}.\n' + 
                f'Tarkasta metodi {met_name}')

    @points('10.paivays_osa2')
    def test_7_plus(self):
        from src.paivays import Paivays
        test_cases = [(1,1,1900,1),(5,5,1900,20),(1,5,1878,30),(23,5,1999,45), 
            (1,12,1999,150),(29,12,1999,790)]
        for test_case in test_cases:
            pvm = Paivays(test_case[0], test_case[1], test_case[2])
            
            d,m,y = test_case[:-1]
            d += test_case[-1]
            while d > 30:
                d -= 30
                m += 1
            while m> 12:
                m -= 12
                y += 1
            corr = f"{d}.{m}.{y}"
            val = str(pvm + test_case[-1])
            stmt = f"print(pvm + {test_case[-1]})"
            met_name = "__add__"

            self.assertEqual(val, corr, f'Lausekkeen\n{stmt}\npitäisi tulostaa ' +
                f'{corr},  kun olio on alustettu seuraavasti:\n'
                f'pvm = Paivays({test_case[0]}, {test_case[1]}, {test_case[2]})\n' + 
                f'Nyt lauseke tulostaa {val}.\n' + 
                f'Tarkasta metodi {met_name}')

    @points('10.paivays_osa3')
    def test_8_miinus(self):
        from src.paivays import Paivays
        test_cases = [((2,1,1900),(1,1,1900)),((5,6,1876),(4,6,1876)),
            ((9,9,1976),(9,10,1976)), ((1,4,1800),(1,5,1800)), 
            ((1,7,1999),(1,8,1998)),((25,5,1943),(25,5,1942)), 
            ((9,9,1976),(9,10,1966)), ((1,4,1800),(3,5,1842)),
            ((1,7,1999),(1,8,1998)),((25,5,1943),(25,5,1942))]

        for test_case in test_cases:
            tc1,tc2 = test_case
            pv1 = Paivays(tc1[0], tc1[1], tc1[2])
            pv2 = Paivays(tc2[0], tc2[1], tc2[2])

            tv1 = tc1[2] * 360 + tc1[1] * 30 + tc1[0]
            tv2 = tc2[2] * 360 + tc2[1] * 30 + tc2[0]

            corr = abs(tv1 - tv2)
            val = (pv1 - pv2)
            stmt = "pv1 - pv2"
            met_name = "__sub__"

            self.assertEqual(val, corr, f'Lausekkeen\n{stmt}\narvon pitäisi olla ' +
                f'{corr},  kun oliot on alustettu seuraavasti:\n'
                f'pv1 = Paivays({tc1[0]}, {tc1[1]}, {tc1[2]})\n' + 
                f'pv2 = Paivays({tc2[0]}, {tc2[1]}, {tc2[2]})\n' + 
                f'Nyt lauseke palauttaa {val}.\n' + 
                f'Tarkasta metodi {met_name}')

 
    
if __name__ == '__main__':
    unittest.main()
