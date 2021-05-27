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

exercise = 'src.nopein_auto'
function = "nopein_auto"

def f(attr: list):
    return ",".join(attr)


@points('9.nopein_auto')
class NopeinAutoTest(unittest.TestCase):
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

    def test_0b_konstruktori(self):
        try:
            from src.nopein_auto import Auto
            Lada = Auto("Lada", 110)
        except Exception as e:
            self.fail(f'Konstruktorikutsu Lada = Auto("Lada", 110) antoi virheen \n{e}')


    def test1_funktio_olemassa(self):
        try:
            from src.nopein_auto import nopein_auto
        except:
            self.assertTrue(False, "Ohjelmastasi pitäisi löytyä funktio " + 
                "nimeltä nopein_auto(autot: list)")

    def test2_palautusarvon_tyyppi(self):
        from src.nopein_auto import nopein_auto, Auto
        val = nopein_auto([Auto("Mersu",200), Auto("Lada",100)])
        taip = str(type(val)).replace("<class '","").replace("'>","")
        self.assertTrue(type(val) == str, f"Funktion nopein_auto pitäisi palauttaa arvo, jonka tyyppi on merkkijono (str)," +
            f' nyt se palauttaa arvon {val} joka on tyyppiä {taip}\n kun sitä kutsutaan parametreilla\n [Auto("Mersu",200), Auto("Lada",100)])')


    def test3_testaa_listat(self):
        test_cases = [[("Mersu",200),("Volvo",180)], [("Opel", 175), ("Mazda", 185)], [("Lada", 170), ("Mersu", 155), ("Volvo", 175)],
                      [("Ferrari", 300), ("Bugatti", 350), ("Lamborghini", 330)],
                      [("Trabant", 100), ("Lada", 110), ("Skoda", 105), ("Mosse", 95)]]
        for test_case in test_cases:
            nopeus, maara = -1, 0
            for x in test_case:
                if x[1] > nopeus:
                    nopeus = x[1]
                    maara = 1
                elif x[1] == nopeus:
                    maara += 1
            self.assertEqual(maara, 1, "Virhe testissä: nopein auto ei ole yksikäsitteinen")
            with patch('builtins.input', side_effect=[AssertionError("Syötteen pyytämistä ei odotettu")]):
                reload_module(self.module)
                nopein_auto = load(exercise, function, 'fi')
                from src.nopein_auto import Auto

                testlist = [Auto(x[0], x[1]) for x in test_case]
                val = nopein_auto(testlist)
                corr = max(testlist, key = lambda x : x.huippunopeus).merkki

                self.assertEqual(val, corr, f'Funktion pitäisi palauttaa {corr}, mutta se palauttaa {val} kun testilista on \n{testlist}')
                

                
if __name__ == '__main__':
    unittest.main()
