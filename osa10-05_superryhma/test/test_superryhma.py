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

exercise = 'src.superryhma'

def f(attr: list):
    return "\n".join([str(x) for x in attr]) 

@points('10.superryhma')
class SuperryhmaTest(unittest.TestCase):
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

    def test_1_luokka_supersankari_olemassa(self):
        try:
            from src.superryhma import SuperSankari
            a = SuperSankari("Bulk","ilkeys")
        except Exception as e:
            self.fail(f'Konstruktorikutsu SuperSankari("Bulk","ilkeys") antoi virheen \n{e}\n' + 
            'Ethän ole muuttanut luokan SuperSankari määrittelyä?')

    def test_2_luokka_superryhma_olemassa(self):
        try:
            from src.superryhma import SuperSankari, SuperRyhma
            a = SuperRyhma("Ryhmä", "Helsinki")
        except Exception as e:
            self.fail(f'Konstruktorikutsu SuperRyhma("Ryhmä", "Helsinki") antoi virheen \n{e}\n' + 
            'Varmista, että luokka on olemassa ja että siitä voi luoda olion.')

    def test_3_attribuutit_suojattu(self):
        from src.superryhma import SuperSankari, SuperRyhma
        ref = reflect.Reflect()
        ryhma = SuperRyhma("Ryhmä", "Helsinki")
        ref.set_object(ryhma)
        ryhma_attr = ref.list_attributes(True)

        attr_list = ("_nimi", "_kotipaikka", "_jasenet")
        for attr in attr_list:
            self.assertTrue(attr in ryhma_attr, f'Luokalla SuperRyhma pitäisi olla ' +
                f'suojattu attribuutti {attr}.\nVarmista, että attribuutti ' +
                'on määritelty.')


    def test_4_havainnointimetodit(self):
        from src.superryhma import SuperSankari, SuperRyhma
        ref = reflect.Reflect()
        ryhma = SuperRyhma("Ryhmä", "Helsinki")
        ref.set_object(ryhma)
        ryhma_attr = ref.list_attributes(True)

        attr_list = ("nimi", "kotipaikka")
        for attr in attr_list:
            self.assertTrue(attr in ryhma_attr, f'Luokalla SuperRyhma pitäisi olla ' +
                f'havainnointimetodi {attr}!\nVarmista, että attribuutti ' +
                'on määritelty.')

    def test_5_lisays_tulostus1(self):
        from src.superryhma import SuperSankari, SuperRyhma
        test_cases = [("Bulk","Superilkeys"), ("Flush", "Superhuuhtelu"), 
            ("Spam Man", "Roskapostitus")]
        ryhma = SuperRyhma("Karskit Korstot", "Ulvila")
        corr = "Karskit Korstot, Ulvila\nJäsenet:"
        test_str = ""
        for test_case in test_cases:
            ryhma.lisaa_jasen(SuperSankari(test_case[0], test_case[1]))
            corr += "\n" + test_case[0] + ", superkyvyt: " + test_case[1]
            test_str += f'SuperSankari("{test_case[0]}", "{test_case[1]}")'

        ryhma.tulosta_ryhma()
        output = "\n".join([x.strip() for x in get_stdout().split("\n") if len(x.strip()) > 0])

        self.assertEqual(output, corr, f'Metodin tulosta_ryhma() pitäisi tulostaa\n' + 
            f'{corr}\n, mutta se tulostaa\n{output}\nkun ryhmään lisättiin jäsenet:\n' +
            test_str)

    def test_6_lisays_tulostus2(self):
        from src.superryhma import SuperSankari, SuperRyhma
        test_cases = [("Super-Super","Metasankaruus"), ("Vihreä Lyhde", "Superekoilu"), 
            ("Taika-Jam", "Tekee superhyvää hilloa")]
        ryhma = SuperRyhma("Vimmaiset Viikingit", "Oslo")
        corr = "Vimmaiset Viikingit, Oslo\nJäsenet:"
        test_str = ""
        for test_case in test_cases:
            ryhma.lisaa_jasen(SuperSankari(test_case[0], test_case[1]))
            corr += "\n" + test_case[0] + ", superkyvyt: " + test_case[1]
            test_str += f'SuperSankari("{test_case[0]}", "{test_case[1]}")'

        ryhma.tulosta_ryhma()
        output = "\n".join([x.strip() for x in get_stdout().split("\n") if len(x.strip()) > 0])

        self.assertEqual(output, corr, f'Metodin tulosta_ryhma() pitäisi tulostaa\n' + 
            f'{corr}\n, mutta se tulostaa\n{output}\nkun ryhmään lisättiin jäsenet:\n' +
            test_str)



    
if __name__ == '__main__':
    unittest.main()
