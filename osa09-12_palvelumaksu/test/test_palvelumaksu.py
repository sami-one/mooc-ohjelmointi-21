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

exercise = 'src.palvelumaksu'

def f(attr: list):
    return ",".join([str(x) for x in attr]) 

@points('9.palvelumaksu')
class PalvelumaksuTest(unittest.TestCase):
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
            from src.palvelumaksu import Pankkitili
            a = Pankkitili("Testi","12345",1.0)
        except Exception as e:
            self.fail(f'Konstruktorikutsu Pankkitili("Testi","12345",1.0) antoi virheen \n{e}\n' + 
            'Varmista, että luokka on määritelty.')

    def test_2_metodit_olemassa(self):
        from src.palvelumaksu import Pankkitili
        a = Pankkitili("Testi","12345",1.0)
        try:
             val = a.saldo
             taip = str(type(val)).replace("<class '","").replace("'>","")
             self.assertTrue(type(val) == float, f'Havainnointimetodin saldo pitäisi palauttaa kokonaisluku. ' +
                f'Nyt se palauttaa arvon {val} joka on tyyppiä {taip}.')
        except Exception as e:
            self.fail(f'Ohjelma\nPankkitili("Testi","12345",1.0)\ns = a.saldo\n antoi virheen \n{e}')

        try:
             a.talleta(1.0)       
        except Exception as e:
            self.fail(f'Ohjelma\nPankkitili("Testi","12345",1.0)\na.talleta(1.0)\n antoi virheen \n{e}')

        try:
             a.nosta(1.0)       
        except Exception as e:
            self.fail(f'Ohjelma\nPankkitili("Testi","12345",1.0)\na.nosta(1.0)\n antoi virheen \n{e}')


    def test3_testaa_attribuutit(self):
        from src.palvelumaksu import Pankkitili
        a = Pankkitili("Testi","12345",1.0)
        ref = reflect.Reflect()
        ref.set_object(a)

        att_list = ["saldo","talleta","nosta"]
        for attribute in att_list:
            self.assertTrue(ref.has_attribute(attribute), f'Luokalla Havaitoasema pitäisi olla attribuutti ' + 
                f'{attribute}.')

        att = ref.list_public_members()
        att.remove("saldo")
        att.remove("talleta")
        att.remove("nosta")

        self.assertEqual(len(att), 0, f'Luokalla Havaintoasema ei pitäisi olla muita julkisia jäseniä kuin ' +
            f'metodit saldo, talleta ja nosta.' +  
            f'\nNyt sillä on lisäksi seuraavat julkiset jäsenet:\n'+ f(att))

        self.assertTrue(ref.has_attribute("_Pankkitili__palvelumaksu"), f'Luokalla pitäisi olla yksityinen metodi ' +
            f'__palvelumaksu(self)')

    def test4_testaa_talletukset(self):
        from src.palvelumaksu import Pankkitili
        a = Pankkitili("Testi","12345",0)
        test_cases = [10, 10, 20]
        tests = ""
        corr = 0
        for test_case in test_cases:
            a.talleta(test_case)
            corr += test_case
            corr *= 0.99
            tests += f"\ntalleta({test_case})"

            self.assertAlmostEqual(a.saldo, corr, 2, f'Saldon pitäisi olla {corr} kun on alustettu luokka seuraavasti:\n' +
                f'Pankkitili("Testi","12345",0)' + 
                f'\nja kutsuttu metodia talleta ' + 
                f'seuraavasti:\n{tests}\nNyt saldo on {a.saldo}')

    def test5_testaa_nostot(self):
        from src.palvelumaksu import Pankkitili
        a = Pankkitili("Testi","12345",100)
        test_cases = [5, 10, 10]
        tests = ""
        corr = 100
        for test_case in test_cases:
            a.nosta(test_case)
            corr -= test_case
            corr *= 0.99
            tests += f"\nnosta({test_case})"

            self.assertAlmostEqual(a.saldo, corr, 2, f'Saldon pitäisi olla {corr} kun on alustettu luokka seuraavasti:\n' +
                f'Pankkitili("Testi","12345",0)' + 
                f'\nja kutsuttu metodia nosta ' + 
                f'seuraavasti:\n{tests}\nNyt saldo on {a.saldo}')

        

   
if __name__ == '__main__':
    unittest.main()
