import unittest
from unittest.mock import patch

from tmc import points, reflect
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import os.path
import textwrap
import inspect, re

exercise = 'src.pomot_ja_alaiset'

@points('11.pomot_ja_alaiset')
class PomotJaAlaisetTest(unittest.TestCase):
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

    def test_1_funktio_olemassa(self):
        try:
            from src.pomot_ja_alaiset import laske_alaiset
        except Exception as e:
            self.fail(f'Ohjelmasta pitäisi löytyä funktio nimeltä laske_alaiset.')

    def test_2_paluuarvon_tyyppi(self):
        try:
            from src.pomot_ja_alaiset import laske_alaiset, Tyontekija
            val = laske_alaiset(Tyontekija("Make"))
        except Exception as e:
            self.assertTrue(False, f"Funktio antoi virheen kun sitä kutsuttiin näin:" + 
                f'\nlaske_alaiset(Tyontekija(\"Make\"))\n{e}')
        taip = str(type(val)).replace("<class '","").replace("'>","")
        self.assertTrue(type(val) == int, f"Funktion laske_alaiset pitäisi palauttaa arvo, jonka tyyppi on int," +  
            f" nyt se palauttaa arvon {val} joka on tyyppiä {taip}\n kun sitä kutsutaan näin\n" +  
            'laske_alaiset(Tyontekija(\"Make\"))')

    def test_3_toimiiko(self):
        from src.pomot_ja_alaiset import laske_alaiset, Tyontekija

        t1 = Tyontekija("Sasu")
        t2 = Tyontekija("Matti")
        t3 = Tyontekija("Erkki")
        t4 = Tyontekija("Antti")
        t5 = Tyontekija("Emilia")
        t6 = Tyontekija("Kjell")
        t7 = Tyontekija("Jyrki")
        t8 = Tyontekija("Tiina")
        t9 = Tyontekija("Teemu")
        t10 = Tyontekija("Arto")
        t11 = Tyontekija("Esko")
        t12 = Tyontekija("Lea")
        t1.lisaa_alainen(t3)
        t1.lisaa_alainen(t4)
        t1.lisaa_alainen(t7)
        t3.lisaa_alainen(t8)
        t3.lisaa_alainen(t9)
        t3.lisaa_alainen(t10)
        t3.lisaa_alainen(t12)
        t9.lisaa_alainen(t2)
        t2.lisaa_alainen(t5)
        t2.lisaa_alainen(t11)
        t5.lisaa_alainen(t6)

        tests = [(t1,11),(t2,3),(t3,8),(t4,0),(t5,1),(t6,0),(t7,0),(t8,0),(t9,4),(t10,0),(t11,0),(t12,0)]
        for test in tests:
            result = laske_alaiset(test[0])
            self.assertEqual(result, test[1], f"Tyontekijällä {test[0].nimi} tulisi olla {test[1]} alaista mutta funktiosi antaa {result} alaista "+
                                               "(voit katsoa testeistä henkilöstörakenteen)")

if __name__ == '__main__':
    unittest.main()
