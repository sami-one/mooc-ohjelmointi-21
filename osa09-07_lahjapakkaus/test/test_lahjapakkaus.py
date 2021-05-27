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

exercise = 'src.lahjapakkaus'

def f(attr: list):
    return ",".join([str(x) for x in attr]) 


class LahjapakkausTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=[AssertionError("Syötteen pyytämistä ei odotettu")]):
           cls.module = load_module(exercise, 'fi')

    @points('9.lahjapakkaus_osa1')
    def test_0a_paaohjelma_kunnossa(self):
        ok, line = check_source(self.module)
        message = """Funktioita testaava koodi tulee sijoittaa lohkon
if __name__ == "__main__":
sisälle. Seuraava rivi tulee siirtää:
"""
        self.assertTrue(ok, message+line)

    @points('9.lahjapakkaus_osa1')
    def test_1_luokka_lahja_olemassa(self):
        try:
            from src.lahjapakkaus import Lahja
            l = Lahja("Pallo", 1)
        except Exception as e:
            self.fail(f'Konstruktorikutsu Lahja("Pallo", 1) antoi virheen \n{e}\n')        

    @points('9.lahjapakkaus_osa1')
    def test_2_lahja_toimii(self):
        test_cases = [("Pallo", 1), ("Leikkijuna",2), ("Polkupyörä", 5), 
                      ("Kitara", 3), ("Auto", 2000)]
        for test_case in test_cases:
            ref = reflect.Reflect()
            from src.lahjapakkaus import Lahja
            lahja = Lahja(test_case[0], test_case[1])
            ref.set_object(lahja)

            for att in ("nimi", "paino"):
                self.assertTrue(ref.has_attribute(att), f'Luokalla Pallo pitäisi olla ' + 
                    f'attribuutti nimeltä {att}')

            self.assertEqual(lahja.nimi, test_case[0], f'Attribuutin nimi arvon pitäisi olla ' +
                f'{test_case[0]}, kun olio on alustettu näin:\n' +
                f'Lahja("{test_case[0]}", {test_case[1]})')

            self.assertEqual(lahja.paino, test_case[1], f'Attribuutin paino arvon pitäisi olla ' +
                f'{test_case[1]}, kun olio on alustettu näin:\n' +
                f'Lahja("{test_case[0]}", {test_case[1]})')

    @points('9.lahjapakkaus_osa2')
    def test_3_luokka_lahjapakkaus_olemassa(self):
        try:
            from src.lahjapakkaus import Pakkaus
            l = Pakkaus()
        except Exception as e:
            self.fail(f'Konstruktorikutsu Pakkaus() antoi virheen \n{e}\n')     

    @points('9.lahjapakkaus_osa2')
    def test_4_lahjapakkaukset_metodit(self):
        from src.lahjapakkaus import Pakkaus, Lahja
        l = Pakkaus()
        try:
            l.lisaa_lahja(Lahja("Pallo",1))
        except Exception as e:
            self.fail(f'Metodikutsu lisaa_lahja(Lahja("Pallo",1)) antoi virheen \n{e}')

        try:
            l.yhteispaino()
        except Exception as e:
            self.fail(f'Metodikutsu yhteispaino() antoi virheen\{e}\n, kun oli lisätty lahja ' +
                'metodikutsulla lisaa_lahja(Lahja("Pallo",1))')

    @points('9.lahjapakkaus_osa2')
    def test_5_lahjapakkaus_toimii(self):
        test_cases = [("Pallo", 1), ("Leikkijuna",2), ("Polkupyörä", 5), 
                      ("Kitara", 3), ("Auto", 2000)]
        corr = 0
        from src.lahjapakkaus import Pakkaus, Lahja
        pakkaus = Pakkaus()
        lahjalista = ""
        for test_case in test_cases:
            lahja = Lahja(test_case[0], test_case[1])
            pakkaus.lisaa_lahja(lahja)
            val = pakkaus.yhteispaino()
            corr += test_case[1]
            lahjalista += f"\n{test_case[0]} (paino {test_case[1]})"

            self.assertEqual(corr, val, f'Pakkauksen yhteispainon pitäisi olla {corr}, kun ' +
                f'pakkaukseen on lisätty seuraavat lahjat:{lahjalista}' + 
                f'\nnyt paino on {val}.')


                
if __name__ == '__main__':
    unittest.main()
