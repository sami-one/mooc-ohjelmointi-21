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

exercise = 'src.kirja'
classname = "Kirja"

def f(attr: list):
    return ",".join(attr)


@points('8.kirja')
class KirjaTest(unittest.TestCase):
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

    def test1_luokka_olemassa(self):
        try:
            from src.kirja import Kirja
        except:
            self.assertTrue(False, "Ohjelmastasi pitäisi löytyä luokka nimeltä Kirja")

    def test2_konstruktori(self):
        try:
            from src.kirja import Kirja
            val = Kirja("Python 1", "Pekka Python", "Tietokirja", 2010)
            taip = str(type(val)).replace("<class '","").replace("'>","")
            self.assertTrue(True, "")
        except Exception as e:
            self.assertTrue(False, 'Luokan Kirja konstuktorin kutsuminen arvoilla (Kirja("Python 1", "Pekka Python", "Tietokirja", 2010)' +
                f' palautti virheen: {e}')

    
    def test3_testaa_attribuutit(self):
        with patch('builtins.input', side_effect=[AssertionError("Syötteen pyytämistä ei odotettu")]):
            reload_module(self.module)
            from src.kirja import Kirja

            attributes = ("nimi", "kirjoittaja", "genre", "kirjoitusvuosi")

            for attr in attributes:
                ref = reflect.Reflect()
                ref.set_object(Kirja("Python 1", "Pekka Python", "Tietokirja", 2010))

                self.assertTrue(ref.has_attribute(attr), f"Palautetulla oliolla pitäisi olla attribuutti {attr}," +  
                    f'\nnyt attribuutit ovat\n{f(ref.list_attributes(True))}\nkun konstruktoria kutsuttiin parametreilla' + 
                    f'Kirja("Python 1", "Pekka Python", "Tietokirja", 2010)')
    
    def test4_testaa_attribuuttien_tyypit(self):
        with patch('builtins.input', side_effect=[AssertionError("Syötteen pyytämistä ei odotettu")]):
            reload_module(self.module)
            from src.kirja import Kirja

            attributes = (("nimi", str), ("kirjoittaja", str), ("genre", str), ("kirjoitusvuosi", int))

            for attr in attributes:
                ref = reflect.Reflect()
                ref.set_object(Kirja("Python 1", "Pekka Python", "Tietokirja", 2010))
                name,taip = attr

                taip_name = str(taip).replace("<class '", "").replace("'>", "")
                taip2 = str(type(ref.get_attribute(name))).replace("<class '","").replace("'>","")

                self.assertTrue(type(ref.get_attribute(name)) == taip, f"Attribuutin {name} tyypin pitäisi olla {taip_name}, nyt se on {taip2}")

    def test5_testaa_attribuuttien_arvot(self):
         test_cases = [("Seitsemän veljestä", "Aleksis Kivi", "Romaani", 1870), 
                       ("Sinuhe egyptiläinen", "Mika Waltari", "Romaani", 1945),
                       ("Kyberias", "Stanislaw Lem", "Sci-fi", 1965), 
                       ("Kotona maailmankaikkeudessa", "Esko Valtaoja", "Tiede", 2001)]
         
         for test_case in test_cases:
            with patch('builtins.input', side_effect=[AssertionError("Syötteen pyytämistä ei odotettu")]):
                reload_module(self.module)
                from src.kirja import Kirja

                kirja = Kirja(test_case[0], test_case[1], test_case[2], test_case[3])
                
                attributes = ("nimi", "kirjoittaja", "genre", "kirjoitusvuosi")
                ref = reflect.Reflect()
                ref.set_object(kirja)

                for i in range(len(attributes)):
                    value = ref.get_attribute(attributes[i])
                    self.assertEqual(value, test_case[i], 
                        f'Attribuutin {attributes[i]} arvon pitäisi olla {test_case[i]}, nyt se on {value},\n kun parametrit olivat \n{test_case}')


if __name__ == '__main__':
    unittest.main()
