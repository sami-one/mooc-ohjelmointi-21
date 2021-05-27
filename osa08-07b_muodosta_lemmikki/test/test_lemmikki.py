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

exercise = 'src.muodosta_lemmikki'
function = "uusi_lemmikki"

def f(attr: list):
    return ",".join(attr)


@points('8.muodosta_lemmikki')
class LemmikkiTest(unittest.TestCase):
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
            from src.muodosta_lemmikki import Lemmikki
            musti = Lemmikki("Musti","Koira",2014)
        except Exception as e:
            self.fail(f'Konstruktorikutsu Lemmikki("Musti","Koira",2014) antoi virheen \n{e}')


    def test1_funktio_olemassa(self):
        try:
            from src.muodosta_lemmikki import uusi_lemmikki
        except:
            self.assertTrue(False, "Ohjelmastasi pitäisi löytyä funktio " + 
                "nimeltä uusi_lemmikki(nimi: str, laji: str, syntymavuosi: int)")

    def test2_palautusarvon_tyyppi(self):
        try:
            from src.muodosta_lemmikki import uusi_lemmikki
            val = uusi_lemmikki("Musti","koira",1970)
        except Exception as e:
            self.fail('Funktio antoi virheen kun sitä kutsuttiin parametreilla uusi_lemmikki("Musti","koira",1970)')
        taip = str(type(val)).replace("<class '","").replace("'>","")
        self.assertTrue("Lemmikki" in str(type(val)), f"Funktion uusi_lemmikki pitäisi palauttaa arvo, jonka tyyppi on Lemmikki," +  
            f' nyt se palauttaa arvon {val} joka on tyyppiä {taip}\n kun sitä kutsutaan parametreilla uusi_lemmikki("Musti","koira",1970)')
        


    def test3_testaa_attribuutit(self):
        with patch('builtins.input', side_effect=[AssertionError("Syötteen pyytämistä ei odotettu")]):
            reload_module(self.module)
            uusi_lemmikki = load(exercise, function, 'fi')

            attributes = ("nimi", "laji", "syntymavuosi")

            for attr in attributes:
                ref = reflect.Reflect()
                ref.set_object(uusi_lemmikki("Musti","koira",1970))

                self.assertTrue(ref.has_attribute(attr), f"Palautetulla Lemmikki-oliolla pitäisi olla attribuutti {attr}," +  
                    f'\nnyt attribuutit ovat\n{f(ref.list_attributes(True))}\nkun funktiota kutsuttiin parametreilla ("Musti","koira",1970)')
    
    def test4_testaa_attribuuttien_tyypit(self):
        with patch('builtins.input', side_effect=[AssertionError("Syötteen pyytämistä ei odotettu")]):
            reload_module(self.module)
            uusi_lemmikki = load(exercise, function, 'fi')

            attributes = (("nimi", str), ("laji", str), ("syntymavuosi", int))

            for attr in attributes:
                ref = reflect.Reflect()
                ref.set_object(uusi_lemmikki("Musti","koira",1970))
                name,taip = attr

                taip2 = str(type(ref.get_attribute(name))).replace("<class '","").replace("'>","")

                self.assertTrue(type(ref.get_attribute(name)) == taip, f"Attribuutin {name} tyypin pitäisi olla {taip}, nyt se on {taip2}")

    def test5_testaa_attribuuttien_arvot(self):
         test_cases = [("Musti","koira",1970), ("Viiru","kissa",1986), ("Tiku","orava",1999),("Dumbo","norsu",1963)]
         
         for test_case in test_cases:
            with patch('builtins.input', side_effect=[AssertionError("Syötteen pyytämistä ei odotettu")]):
                reload_module(self.module)
                uusi_lemmikki = load(exercise, function, 'fi')

                val = uusi_lemmikki(test_case[0], test_case[1], test_case[2])
                
                attributes = ("nimi", "laji", "syntymavuosi")
                ref = reflect.Reflect()
                ref.set_object(val)

                for i in range(len(attributes)):
                    value = ref.get_attribute(attributes[i])
                    self.assertEqual(value, test_case[i], 
                        f'Attribuutin {attributes[i]} arvon pitäisi olla {test_case[i]}, nyt se on {value},\n kun parametrit olivat {test_case}')
if __name__ == '__main__':
    unittest.main()
