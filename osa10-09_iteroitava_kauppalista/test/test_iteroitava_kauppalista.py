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

exercise = 'src.iteroitava_kauppalista'

def f(attr: list):
    return "\n".join([str(x) for x in attr]) 

@points('10.iteroitava_kauppalista')
class KauppalistaTest(unittest.TestCase):
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
            from src.iteroitava_kauppalista import Kauppalista
            a = Kauppalista()
        except Exception as e:
            self.fail(f'Konstruktorikutsu Kauppalista() antoi virheen \n{e}\n' + 
            'Tarkista, että luokasta voi muodostaa olion.')

    def test_2_metodit_olemassa(self):
        from src.iteroitava_kauppalista import Kauppalista
        ref = reflect.Reflect()
        lista = Kauppalista()
        ref.set_object(lista)

        if not ref.has_attribute("__getitem__"):    
            self.assertTrue(ref.has_attribute("__iter__"), f'Luokalla Kauppalista ' + 
                'pitäisi olla metodi __iter__, jotta iterointi toimii.')

            self.assertTrue(ref.has_attribute("__next__"), f'Luokalla Kauppalista ' + 
                'pitäisi olla metodi __next__, jotta iterointi toimii.')

    def test_3_iterointi(self):
        from src.iteroitava_kauppalista import Kauppalista
        test_cases = [("Munia",10), ("Maitoa", 2), ("Omenat", 5)]
        lista = Kauppalista()
        for test_case in test_cases:
            lista.lisaa(test_case[0], test_case[1])

        val = []
        for tuote in lista:
            val.append(tuote)

        self.assertEqual(test_cases, val, f'Luokan kauppalista iteroinnin pitäisi ' +
            f'palauttaa järjestyksessä seuraavat alkiot:\n{f(test_cases)}\n' + 
            f'Nyt iterointi palautti seuraavat tuotteet:\n{f(val)}')

    def test_4_iterointi2(self):
        from src.iteroitava_kauppalista import Kauppalista
        test_cases = [("Kurkku",1), ("Tomaatit", 12), 
            ("Kaali", 2), ("Karkkia", 100)]
        lista = Kauppalista()
        for test_case in test_cases:
            lista.lisaa(test_case[0], test_case[1])

        val = []
        for tuote in lista:
            val.append(tuote)

        self.assertEqual(test_cases, val, f'Luokan kauppalista iteroinnin pitäisi ' +
            f'palauttaa järjestyksessä seuraavat alkiot:\n{f(test_cases)}\n' + 
            f'Nyt iterointi palautti seuraavat tuotteet:\n{f(val)}')

    
if __name__ == '__main__':
    unittest.main()
