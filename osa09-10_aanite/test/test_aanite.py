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

exercise = 'src.aanite'

def f(attr: list):
    return ",".join([str(x) for x in attr]) 

@points('9.aanite')
class AaniteTest(unittest.TestCase):
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
            from src.aanite import Aanite
            a = Aanite(1)
        except Exception as e:
            self.fail(f'Konstruktorikutsu Aanite(1) antoi virheen \n{e}\n' + 
            'Varmista, että luokka on määritelty.')

    def test_2_metodit_olemassa(self):
        from src.aanite import Aanite
        a = Aanite(1)
        try:
             val = a.pituus
             taip = str(type(val)).replace("<class '","").replace("'>","")
             self.assertTrue(type(val) == int, f'Havainnointimetodin pituus pitäisi palauttaa kokonaisluku. ' +
                f'Nyt se palauttaa arvon {val} joka on tyyppiä {taip}.')
        except Exception as e:
            self.fail(f"Ohjelma\na = Aanite(1)\narvo = a.pituus\n antoi virheen \n{e}")

        try:
             a.pituus = 3
        except Exception as e:
            self.fail(f"Ohjelma\na = Aanite(1)\na.pituus = 3\n antoi virheen \n{e}")

    def test3_testaa_attribuutit(self):
        from src.aanite import Aanite
        a = Aanite(1)
        ref = reflect.Reflect()
        ref.set_object(a)

        att = ref.list_public_members()

        self.assertTrue(ref.has_attribute("pituus"), f'Luokalla aanite pitäisi olla julkinen havainnointimetodi pituus')

        att.remove("pituus")

        self.assertEqual(len(att), 0, f'Luokalla Aanite ei pitäisi olla muita julkisia jäseniä kuin ' +
            f'asetus- ja havainnointimetodit pituudelle. Nyt sillä on lisäksi seuraavat julkiset jäsenet:\n'+ f(att))
    
    def test4_testaa_lailliset(self):
        from src.aanite import Aanite
        test_cases = [(1,10), (5,50), (100,10)]
        for test_case in test_cases:
            a = Aanite(test_case[0])
            self.assertEqual(a.pituus, test_case[0], f'Pituuden pitäisi olla {test_case[0]} kun olio on alustettu näin:\n' +
                f'Aanite({test_case[0]})\nNyt pituus kuitenkin on {a.pituus}')

            a.pituus = test_case[1]
            self.assertEqual(a.pituus, test_case[1], f'Pituuden pitäisi olla {test_case[1]} kun on suoritettu rivit:\n' +
                f'a = Aanite({test_case[0]})\na.pituus = {test_case[1]}\n' + 
                f'Nyt pituus kuitenkin on {a.pituus}')

    def test5_testaa_laittomat(self):
        from src.aanite import Aanite

        for i in [-1,-5,-1000]:
            try:
                a = Aanite(i)
                self.fail(f'Luokan pitäisi antaa ValueError-tyyppinen virhe, kun se alustetaan näin:\nAanite({i})')
            except Exception as ve:
                if type(ve) is not ValueError:
                    taip = str(type(ve)).replace("<class '","").replace("'>","")
                    self.fail(f'Luokan pitäisi antaa ValueError-tyyppinen virhe, kun se alustetaan näin:\nAanite({i})\n')

        for i in [-1,-5,-1000]:
            try:
                a = Aanite(1)
                a.pituus = i
                self.fail(f'Luokan pitäisi antaa ValueError-tyyppinen virhe, kun asetusmetodia kutsutaan arvolla {i}')
            except Exception as ve:
                if type(ve) is not ValueError:
                    taip = str(type(ve)).replace("<class '","").replace("'>","")
                    self.fail(f'Luokan pitäisi antaa ValueError-tyyppinen virhe, kun asetusmetodia kutsutaan arvolla {i}\n')
    
if __name__ == '__main__':
    unittest.main()
