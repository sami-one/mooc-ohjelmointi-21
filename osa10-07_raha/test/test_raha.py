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

exercise = 'src.raha'

def f(attr: list):
    return "\n".join([str(x) for x in attr]) 

class RahaTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=[AssertionError("Syötteen pyytämistä ei odotettu")]):
           cls.module = load_module(exercise, 'fi')

    @points('10.raha_osa1')
    def test_0a_paaohjelma_kunnossa(self):
        ok, line = check_source(self.module)
        message = """Funktioita testaava koodi tulee sijoittaa lohkon
if __name__ == "__main__":
sisälle. Seuraava rivi tulee siirtää:
"""
        self.assertTrue(ok, message+line)
    
    @points('10.raha_osa1')
    def test_1_luokka_raha_olemassa(self):
        try:
            from src.raha import Raha
            a = Raha(1,1)
        except Exception as e:
            self.fail(f'Konstruktorikutsu Raha(1,1) antoi virheen \n{e}\n' + 
            'Tarkista, että luokasta voi muodostaa olion.')

    @points('10.raha_osa1')
    def test_2_merkkijonoesitys(self):
        from src.raha import Raha
        test_cases = [(1,50), (2,75), (399,99), (4,1), (5,2), (1243,9)]
        for test_case in test_cases:
            raha = Raha(test_case[0], test_case[1])
            val = str(raha)
            corr = f"{test_case[0]}.{test_case[1]:02d} eur"

            self.assertEqual(val, corr, f'Metodin __str__ pitäisi palauttaa ' +
                f'\n{corr}\nkun raha on alustettu näin:\n' +
                f'Raha({test_case[0]}, {test_case[1]})\nNyt metodi palauttaa\n' + 
                f'{val}')


    @points('10.raha_osa2')
    def test_3_yhtasuuruus(self):
        from src.raha import Raha
        test_cases = [((1,0), (1,0)), ((2,50),(2,50)), ((4,5),(4,5)), ((15,95),(15,95)),
            ((1,0), (2,0)), ((4,50), (4,5)), ((3,95),(3,96)), ((1110,0),(1110,1))]
        for test_case in test_cases:
            tc1,tc2 = test_case
            raha1 = Raha(tc1[0], tc1[1])
            raha2 = Raha(tc2[0], tc2[1])

            corr = tc1 == tc2
            val = (raha1 == raha2)
            stmt = "raha1 == raha2"
            met_name = "__eq__"

            self.assertEqual(val, corr, f'Lausekkeen\nraha1 == raha2\npitäisi olla ' +
                f'{corr},  kun oliot on alustettu seuraavasti:\n'
                f'raha1 = Raha({tc1[0]}, {tc1[1]})\n' + 
                f'raha2 = Raha({tc2[0]}, {tc2[1]})\n' + 
                f'Nyt lauseke palauttaa {val}.\n' + 
                f'Tarkasta metodi {met_name}')

    @points('10.raha_osa3')
    def test_4_pienempi_kuin(self):
        from src.raha import Raha
        test_cases = [((1,0), (2,0)), ((2,50),(3,50)), ((4,5),(4,50)), ((15,95),(15,96)),
            ((2,0), (1,0)), ((4,50), (4,5)), ((3,95),(3,95)), ((1110,10),(1110,1))]
        for test_case in test_cases:
            tc1,tc2 = test_case
            raha1 = Raha(tc1[0], tc1[1])
            raha2 = Raha(tc2[0], tc2[1])

            corr = tc1 < tc2
            val = (raha1 < raha2)
            stmt = "raha1 < raha2"
            met_name = "__lt__"

            self.assertEqual(val, corr, f'Lausekkeen\n{stmt}\npitäisi olla ' +
                f'{corr},  kun oliot on alustettu seuraavasti:\n'
                f'raha1 = Raha({tc1[0]}, {tc1[1]})\n' + 
                f'raha2 = Raha({tc2[0]}, {tc2[1]})\n' + 
                f'Nyt lauseke palauttaa {val}.\n' + 
                f'Tarkasta metodi {met_name}')

    @points('10.raha_osa3')
    def test_5_suurempi_kuin(self):
        from src.raha import Raha
        test_cases = [((1,0), (2,0)), ((2,50),(3,50)), ((4,50),(4,50)), ((15,95),(15,96)),
            ((2,0), (1,0)), ((4,50), (4,5)), ((3,95),(3,90)), ((1110,10),(1110,1))]
        for test_case in test_cases:
            tc1,tc2 = test_case
            raha1 = Raha(tc1[0], tc1[1])
            raha2 = Raha(tc2[0], tc2[1])

            corr = tc1 > tc2
            val = (raha1 > raha2)
            stmt = "raha1 > raha2"
            met_name = "__gt__"

            self.assertEqual(val, corr, f'Lausekkeen\n{stmt}\npitäisi olla ' +
                f'{corr},  kun oliot on alustettu seuraavasti:\n'
                f'raha1 = Raha({tc1[0]}, {tc1[1]})\n' + 
                f'raha2 = Raha({tc2[0]}, {tc2[1]})\n' + 
                f'Nyt lauseke palauttaa {val}.\n' + 
                f'Tarkasta metodi {met_name}')

    @points('10.raha_osa3')
    def test_6_erisuuri_kuin(self):
        from src.raha import Raha
        test_cases = [((1,0), (1,0)), ((2,50),(2,50)), ((4,5),(4,50)), ((15,95),(15,95)),
            ((2,0), (1,0)), ((4,50), (4,5)), ((3,95),(3,90)), ((1110,10),(1110,0))]
        for test_case in test_cases:
            tc1,tc2 = test_case
            raha1 = Raha(tc1[0], tc1[1])
            raha2 = Raha(tc2[0], tc2[1])

            corr = tc1 != tc2
            val = (raha1 != raha2)
            stmt = "raha1 != raha2"
            met_name = "__ne__"

            self.assertEqual(val, corr, f'Lausekkeen\n{stmt}\npitäisi olla ' +
                f'{corr},  kun oliot on alustettu seuraavasti:\n'
                f'raha1 = Raha({tc1[0]}, {tc1[1]})\n' + 
                f'raha2 = Raha({tc2[0]}, {tc2[1]})\n' + 
                f'Nyt lauseke palauttaa {val}.\n' + 
                f'Tarkasta metodi {met_name}')

    @points('10.raha_osa4')
    def test_7_plus(self):
        from src.raha import Raha
        test_cases = [((1,0), (1,0)), ((2,50),(2,50)), ((4,5),(4,50)), ((15,95),(15,95)),
            ((2,0), (1,0)), ((4,50), (4,5)), ((3,95),(3,90)), ((1110,10),(1110,0))]
        for test_case in test_cases:
            tc1,tc2 = test_case
            raha1 = Raha(tc1[0], tc1[1])
            raha2 = Raha(tc2[0], tc2[1])

            e = tc1[0] + tc2[0]
            c = tc1[1] + tc2[1]
            if c >= 100:
                c -= 100
                e += 1
            corr = f"{e}.{c:02d} eur"
            val = str(raha1 + raha2)
            stmt = "print(raha1 + raha2)"
            met_name = "__add__"

            self.assertEqual(val, corr, f'Lausekkeen\n{stmt}\npitäisi tulostaa ' +
                f'{corr}, kun oliot on alustettu seuraavasti:\n'
                f'raha1 = Raha({tc1[0]}, {tc1[1]})\n' + 
                f'raha2 = Raha({tc2[0]}, {tc2[1]})\n' + 
                f'Nyt lauseke tulostaaa {val}.\n' + 
                f'Tarkasta metodi {met_name}')

    @points('10.raha_osa4')
    def test_8a_miinus1(self):
        from src.raha import Raha
        test_cases = [((3,0), (1,0)), ((2,50),(1,50)), ((4,5),(0,50)), ((15,95),(1,55)),
            ((2,0), (1,35)), ((4,30), (2,75)), ((3,95),(3,90)), ((1110,10),(1110,0))]
        for test_case in test_cases:
            tc1,tc2 = test_case
            raha1 = Raha(tc1[0], tc1[1])
            raha2 = Raha(tc2[0], tc2[1])

            e = tc1[0] - tc2[0]
            c = tc1[1] - tc2[1]
            if c < 0:
                c += 100
                e -= 1
            corr = f"{e}.{c:02d} eur"
            val = str(raha1 - raha2)
            stmt = "print(raha1 - raha2)"
            met_name = "__sub__"

            self.assertEqual(val, corr, f'Lausekkeen\n{stmt}\npitäisi tulostaa ' +
                f'{corr}, kun oliot on alustettu seuraavasti:\n'
                f'raha1 = Raha({tc1[0]}, {tc1[1]})\n' + 
                f'raha2 = Raha({tc2[0]}, {tc2[1]})\n' + 
                f'Nyt lauseke tulostaaa {val}.\n' + 
                f'Tarkasta metodi {met_name}')

    @points('10.raha_osa4')
    def test_8b_miinus2(self):
        from src.raha import Raha
        test_cases = [((1,0), (2,0)), ((2,50),(3,50)), ((4,5),(4,6)), ((15,95),(15,96)),
            ((2,0), (2,1)), ((1110,10),(1110,11))]
        for test_case in test_cases:
            tc1,tc2 = test_case
            raha1 = Raha(tc1[0], tc1[1])
            raha2 = Raha(tc2[0], tc2[1])

            
            
            stmt = "print(raha1 - raha2)"
            met_name = "__sub__"

            try:
                str(raha1 - raha2)
                self.fail(f'Lausekkeen\n{stmt}\npitäisi antaa poikkeus ' +
                    f'ValueError, kun oliot on alustettu seuraavasti:\n'
                    f'raha1 = Raha({tc1[0]}, {tc1[1]})\n' + 
                    f'raha2 = Raha({tc2[0]}, {tc2[1]})\n' + 
                    f'Tarkasta metodi {met_name}')
            except ValueError:
                pass

    @points('10.raha_osa5')
    def test_9_kapselointi_1(self):
        from src.raha import Raha
        ref = reflect.Reflect()
        r = Raha(1,50)
        ref.set_object(r)

        attr = ref.list_attributes(True)
        for att in attr:
            if not att.startswith("_"):
                self.fail('Luokalla ei pitäisi olla muita kuin kapseloituja ' +
                    f'attribuutteja. Nyt sillä on julkinen' + 
                    f' attribuutti {att}')

        r.eurot = 1000        
        test = "1000.50 eur"
        self.assertTrue(str(r) != test, f'Lausekkeen raha.eurot = 1000 ei ' + 
        f'pitäisi asettaa olion rahat arvoa, koska arvon pitäisi olla kapseloitu!')

        


    
    
if __name__ == '__main__':
    unittest.main()
