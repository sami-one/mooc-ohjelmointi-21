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

exercise = 'src.auto'

def f(attr: list):
    return ",".join([str(x) for x in attr]) 

@points('9.auto')
class AutoTest(unittest.TestCase):
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
            from src.auto import Auto
            a = Auto()
        except Exception as e:
            self.fail(f'Konstruktorikutsu Auto() antoi virheen \n{e}\n' + 
            'Varmista, että luokka on määritelty.')

    def test_2_metodit_olemassa(self):
        from src.auto import Auto
        a = Auto()
        try:
             a.aja(10)
        except Exception as e:
            self.fail(f"Metodikutsu aja(10) antoi virheen \n{e}")

        try:
            a.tankkaa()
        except Exception as e:
            self.fail(f"Metodikutsu tankkaa() antoi virheen \n{e}")

    def test3_testaa_attribuutit(self):
        from src.auto import Auto
        a = Auto()
        ref = reflect.Reflect()
        ref.set_object(a)

        att = ref.list_public_members()
        if "aja" in att: att.remove("aja")
        if "tankkaa" in att: att.remove("tankkaa")

        self.assertEqual(len(att), 0, f'Luokalla Auto ei pitäisi olla muita julkisia jäseniä kuin ' +
            f'metodit aja ja tankkaa. Nyt sillä on lisäksi seuraavat julkiset jäsenet:\n'+ f(att))

    def test4_testaa_str(self):
        from src.auto import Auto
        a = Auto()
        try:
            output = str(a)
        except Exception as e:
            self.fail(f"Auton __str__-metodin kutsuminen aiheuttaa virheen {e}.")

        self.assertTrue("0 km" in output and "0 litraa" in output, f'Auton __str__-metodin pitäisi palauttaa ' +
            f'merkkijono "Auto: ajettu 0 km, bensaa 0 litraa", nyt se palauttaa\n{output}')
        

    def test5_testaa_tankkaus(self):
        from src.auto import Auto
        a = Auto()

        a.tankkaa()
        output = str(a)

        self.assertTrue("60 litraa" in output, f"Auton bensamäärän pitäisi olla 60 litraa tankkauksen jälkeen, nyt " +
            f"__str__-metodi palauttaa\n{output}")

    def test6_testaa_ajo_ja_tankkaus(self):
        from src.auto import Auto
        a = Auto()
        a.tankkaa()

        test_cases = [10, 20, 10, 20, 5]
        bensaa = 60
        km = 0
        tests = ""
        for test_case in test_cases:
            a.aja(test_case)
            if test_case <= bensaa:
                bensaa -= test_case
                km += test_case
            tests += f"\naja({test_case})"

            output = str(a)

            self.assertTrue(str(bensaa) + " litraa" in output and str(km) + " km" in output, f'Auton tulostuksessa pitäisi ilmoittaa ' +
                f'bensamääräksi {bensaa} litraa ja kilometrimääräksi {km} kun alustuksen ' +
                f'jälkeen on kutsuttu seuraavat metodit:\n{tests}' +
                f'\nNyt tulostus on\n{output}')

        a.tankkaa()
        tests += "\ntankkaa()"
        test_cases = [10, 30, 20]
        bensaa = 60
        for test_case in test_cases:
            a.aja(test_case)
            if test_case <= bensaa:
                bensaa -= test_case
                km += test_case
            tests += f"\naja({test_case})"

            output = str(a)

            self.assertTrue(str(bensaa) + " litraa" in output and str(km) + " km" in output, f'Auton tulostuksessa pitäisi ilmoittaa ' +
                f'bensamääräksi {bensaa} litraa ja kilometrimääräksi {km} kun alustuksen ' +
                f'jälkeen on kutsuttu seuraavat metodit:\n{tests}' +
                f'\nNyt tulostus on\n{output}')

if __name__ == '__main__':
    unittest.main()
