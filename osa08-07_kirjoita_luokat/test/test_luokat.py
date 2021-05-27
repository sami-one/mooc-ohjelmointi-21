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

exercise = 'src.kirjoita_luokat'

def f(attr: list):
    return ",".join(attr)

@points('8.kirjoita_luokat')
class LuokatTest(unittest.TestCase):
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

    def test1_luokat_olemassa(self):
        try:
            from src.kirjoita_luokat import Muistilista
        except:
            self.fail("Ohjelmastasi pitäisi löytyä luokka nimeltä Muistilista")

        try:
            from src.kirjoita_luokat import Asiakas
        except:
            self.fail("Ohjelmastasi pitäisi löytyä luokka nimeltä Asiakas")

        try:
            from src.kirjoita_luokat import Kaapeli
        except:
            self.fail("Ohjelmastasi pitäisi löytyä luokka nimeltä Kaapeli")

    def test2_konstruktorit(self):
        try:
            from src.kirjoita_luokat import Muistilista
            val = Muistilista("lista", [])
        except Exception as e:
            self.assertTrue(False, 'Luokan Muistilista konstuktorin kutsuminen arvoilla Muistilista("lista", [])' +
                f' palautti virheen: {e}')
        try:
            from src.kirjoita_luokat import Asiakas
            val = Asiakas("asiakas",1,1.0)
        except Exception as e:
            self.assertTrue(False, 'Luokan Asiakas konstuktorin kutsuminen arvoilla Asiakas("asiakas",1,1.0)' +
                f' palautti virheen: {e}')

        try:
            from src.kirjoita_luokat import Kaapeli
            val = Kaapeli("kaapeli",1.0,1,True)
        except Exception as e:
            self.assertTrue(False, 'Luokan Kaapeli konstuktorin kutsuminen arvoilla Kaapeli("kaapeli",1.0,1.True)' +
                f' palautti virheen: {e}')

    
    def test3_testaa_attribuutit(self):
        with patch('builtins.input', side_effect=[AssertionError("Syötteen pyytämistä ei odotettu")]):
            reload_module(self.module)
            from src.kirjoita_luokat import Muistilista, Asiakas, Kaapeli

            attributes = ("otsikko","merkinnat")
            for attr in attributes:
                ref = reflect.Reflect()
                ref.set_object(Muistilista("lista",[]))

                self.assertTrue(ref.has_attribute(attr), f"Palautetulla oliolla pitäisi olla attribuutti {attr}," +  
                    f'\nnyt attribuutit ovat\n{f(ref.list_attributes(True))}\nkun konstruktoria kutsuttiin parametreilla' + 
                    f'Muistilista("lista",[])')

            attributes = ("tunniste", "saldo", "alennusprosentti")
            for attr in attributes:
                ref = reflect.Reflect()
                ref.set_object(Asiakas("asiakas", 1.0, 1))

                self.assertTrue(ref.has_attribute(attr), f"Palautetulla oliolla pitäisi olla attribuutti {attr}," +  
                    f'\nnyt attribuutit ovat\n{f(ref.list_attributes(True))}\nkun konstruktoria kutsuttiin parametreilla' + 
                    f'Asiakas("asiakas", 1.0, 1)')

            attributes = ("malli", "pituus", "maksiminopeus", "kaksisuuntainen")
            for attr in attributes:
                ref = reflect.Reflect()
                ref.set_object(Kaapeli("kaapeli",1.0,1,True))

                self.assertTrue(ref.has_attribute(attr), f"Palautetulla oliolla pitäisi olla attribuutti {attr}," +  
                    f'\nnyt attribuutit ovat\n{f(ref.list_attributes(True))}\nkun konstruktoria kutsuttiin parametreilla' + 
                    f'Kaapeli("kaapeli",1.0,1,True)')

    
    def test4_testaa_muistikirja(self):
         test_cases = [("Laskut", ["Muista vuokra", "Muista puhelinlasku"]), 
                       ("Kauppalista", ["Maito", "Leipä", "Mehu", "Viili"])]
         
         for test_case in test_cases:
            with patch('builtins.input', side_effect=[AssertionError("Syötteen pyytämistä ei odotettu")]):
                reload_module(self.module)
                from src.kirjoita_luokat import Muistilista

                lista = Muistilista(test_case[0], test_case[1])
                
                attributes = ("otsikko", "merkinnat")
                ref = reflect.Reflect()
                ref.set_object(lista)

                for i in range(len(attributes)):
                    value = ref.get_attribute(attributes[i])
                    self.assertEqual(value, test_case[i], 
                        f'Attribuutin {attributes[i]} arvon pitäisi olla {test_case[i]}, nyt se on {value},\n kun parametrit olivat \n{test_case}')

    def test5_testaa_asiakas(self):
         test_cases = [("Arto Asiakas", 1424.50, 10), ("Anne Asiakas", 550.0, 7), ("Aune Asiakas", 240.25, 15)]
         
         for test_case in test_cases:
            with patch('builtins.input', side_effect=[AssertionError("Syötteen pyytämistä ei odotettu")]):
                reload_module(self.module)
                from src.kirjoita_luokat import Asiakas

                asiakas = Asiakas(test_case[0], test_case[1], test_case[2])
                
                attributes = ("tunniste", "saldo", "alennusprosentti")
                ref = reflect.Reflect()
                ref.set_object(asiakas)

                for i in range(len(attributes)):
                    value = ref.get_attribute(attributes[i])
                    self.assertEqual(value, test_case[i], 
                        f'Attribuutin {attributes[i]} arvon pitäisi olla {test_case[i]}, nyt se on {value},\n kun parametrit olivat \n{test_case}')

    def test6_testaa_kaapeli(self):
         test_cases = [("cat", 5.0, 128, True), ("USB2", 10.0, 24, True), ("BSU3", 25.0, 18, False)]
         
         for test_case in test_cases:
            with patch('builtins.input', side_effect=[AssertionError("Syötteen pyytämistä ei odotettu")]):
                reload_module(self.module)
                from src.kirjoita_luokat import Kaapeli

                kaapeli = Kaapeli(test_case[0], test_case[1], test_case[2], test_case[3])
                
                attributes = ("malli", "pituus", "maksiminopeus", "kaksisuuntainen")
                ref = reflect.Reflect()
                ref.set_object(kaapeli)

                for i in range(len(attributes)):
                    value = ref.get_attribute(attributes[i])
                    self.assertEqual(value, test_case[i], 
                        f'Attribuutin {attributes[i]} arvon pitäisi olla {test_case[i]}, nyt se on {value},\n kun parametrit olivat \n{test_case}')


if __name__ == '__main__':
    unittest.main()
