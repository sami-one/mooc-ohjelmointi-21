import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import os.path
import textwrap
from random import choice, randint

exercise = 'src.pienin_keskiarvo'
function = "pienin_keskiarvo"

def hlo(t: tuple):
    return {"nimi": "Anna", "tulos1": t[0], "tulos2": t[1], "tulos3": t[2]}

def par(t1: tuple, t2: tuple, t3: tuple):
    s = "("
    for t in (t1,t2,t3):
        s += "{" + ",".join([f'"tulos{x}": {t[x-1]}' for x in range(1,4)]) + "}" + ", "
    return s[:-2] + ")"
        

@points('8.pienin_keskiarvo')
class PieninKeskiarvoTest(unittest.TestCase):
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

    def test1_funktio_olemassa(self):
        try:
            from src.pienin_keskiarvo import pienin_keskiarvo
        except:
            self.assertTrue(False, "Ohjelmastasi pitäisi löytyä funktio nimeltä pienin_keskiarvo(h1: dict, h2: dict, h3: dict)")

    def test2_palautusarvon_tyyppi(self):
        try:
            from src.pienin_keskiarvo import pienin_keskiarvo
            val = pienin_keskiarvo(hlo((1,1,1)), hlo((2,2,2)), hlo((3,3,3)))
            taip = str(type(val)).replace("<class '","").replace("'>","")
            self.assertTrue(type(val) == dict, f"Funktion pienin_keskiarvo pitäisi palauttaa arvo, joka on tyyppiä dict," +  
                f" nyt se palauttaa arvon {val} joka on tyyppiä {taip}\n kun sitä kutsutaan parametreilla {par((1,1,1),(2,2,2),(3,3,3))}")
        except:
            self.assertTrue(False, f"Funktio antoi virheen kun sitä kutsuttiin parametrien arvoilla {par((1,1,1),(2,2,2),(3,3,3))}")


    def test3_testaa_arvot(self):
        test_cases = [((1,1,1),(2,2,2),(3,3,3)), ((9,9,9),(7,7,7),(8,8,8)), ((3,3,3),(5,5,5), (1,1,1)), 
                      ((5,3,1),(6,4,2),(2,2,2)), ((9,3,8),(9,4,9),(9,6,8)), ((6,0,0), (5,0,0), (3,3,3)),
                      ((6,4,4),(5,7,7),(4,8,8)), ((4,3,4),(4,2,4),(4,3,4)), ((6,2,2), (5,2,2), (5,2,3))]
        for test_case in test_cases:
            with patch('builtins.input', side_effect=[AssertionError("Syötteen pyytämistä ei odotettu")]):
                reload_module(self.module)
                pienin_keskiarvo = load(exercise, function, 'fi')

                h1 = hlo(test_case[0])
                h2 = hlo(test_case[1])
                h3 = hlo(test_case[2])

                results = [sum(test_case[0]),sum(test_case[1]),sum(test_case[2])]
                results.sort()
                if results[0] == results[1]:
                    self.fail("virhe testeissä: pienin keskiarvo ei ole yksikäsitteinen")

                val = pienin_keskiarvo(h1, h2, h3)

                t1 = hlo(test_case[0])
                t2 = hlo(test_case[1])
                t3 = hlo(test_case[2])
                corr = min((t1,t2,t3), key=lambda x: ((x["tulos1"]+x["tulos2"]+x["tulos3"]) / 3))

                self.assertEqual(val, corr, f"Funktion pitäisi palauttaa \n{corr}\nmutta se palauttaa \n{val}\nkun parametrit ovat\n{par(test_case[0], test_case[1], test_case[2])}")

    

if __name__ == '__main__':
    unittest.main()
