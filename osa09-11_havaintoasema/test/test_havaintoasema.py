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

exercise = 'src.havaintoasema'

def f(attr: list):
    return ",".join([str(x) for x in attr]) 

@points('9.havaintoasema')
class HavaintoasemaTest(unittest.TestCase):
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
            from src.havaintoasema import Havaintoasema
            a = Havaintoasema("Kumpula")
        except Exception as e:
            self.fail(f'Konstruktorikutsu Havaintoasema("Kumpula") antoi virheen \n{e}\n' + 
            'Varmista, että luokka on määritelty.')

    def test_2_metodit_olemassa(self):
        from src.havaintoasema import Havaintoasema
        a = Havaintoasema("Kumpula")
        try:
             val = a.havaintojen_maara()
             taip = str(type(val)).replace("<class '","").replace("'>","")
             self.assertTrue(type(val) == int, f'Metodin havaintojen_maara() pitäisi palauttaa kokonaisluku. ' +
                f'Nyt se palauttaa arvon {val} joka on tyyppiä {taip}.')
        except Exception as e:
            self.fail(f'Ohjelma\na=Havaintoasema("Kumpula")\nm=a.havaintojen_maara() antoi virheen \n{e}')

        try:
             val = a.viimeisin_havainto()
             taip = str(type(val)).replace("<class '","").replace("'>","")
             self.assertTrue(type(val) == str, f'Metodin viimeisin_havainto pitäisi palauttaa merkkijono. ' +
                f'Nyt se palauttaa arvon {val} joka on tyyppiä {taip}.')
        except Exception as e:
            self.fail(f'Ohjelma\na=Havaintoasema("Kumpula")\nm=a.viimeisin_havainto() antoi virheen \n{e}')

        try:
             a.lisaa_havainto("x")
        except Exception as e:
            self.fail(f'Ohjelma\na=Havaintoasema("Kumpula")\nm=a.lisaa_havainto("x") antoi virheen \n{e}')

    def test3_testaa_attribuutit(self):
        from src.havaintoasema import Havaintoasema
        a = Havaintoasema("Kumpula")
        ref = reflect.Reflect()
        ref.set_object(a)

        att_list = ["havaintojen_maara", "viimeisin_havainto", "lisaa_havainto"]
        for attribute in att_list:
            self.assertTrue(ref.has_attribute(attribute), f'Luokalla Havaitoasema pitäisi olla attribuutti ' + 
                f'{attribute}.')

        att = ref.list_public_members()
        att.remove("havaintojen_maara")
        att.remove("viimeisin_havainto")
        att.remove("lisaa_havainto")

        self.assertEqual(len(att), 0, f'Luokalla Havaintoasema ei pitäisi olla muita julkisia jäseniä kuin ' +
            f'metodit havaintojen_maara, viimeisin_havainto ja lisaa_havainto.' +  
            f'\nNyt sillä on lisäksi seuraavat julkiset jäsenet:\n'+ f(att))

    def test4_testaa_toiminta(self):     
        from src.havaintoasema import Havaintoasema
        a = Havaintoasema("Kumpula")

        test_cases = ["Sataa","Ukkostaa","Sataa lunta", "Aurinko paistaa", "Sataa"]
        tests = ""
        n = 0
        for test_case in test_cases:
            n += 1
            a.lisaa_havainto(test_case)
            tests += f"\nlisaa_havainto({test_case})"

            self.assertEqual(n, a.havaintojen_maara(), f'Metodin havaintojen_maara pitäisi palauttaa {n} ' + 
                f'kun on kutsuttu seuraavat metodit olion luomisen jälkeen:{tests}\n' + 
                f'Nyt metodi palauttaa {a.havaintojen_maara()}')

            self.assertEqual(test_case, a.viimeisin_havainto(), f'Metodin viimeisin_havainto pitäisi palauttaa {test_case} ' + 
                f'kun on kutsuttu seuraavat metodit olion luomisen jälkeen:{tests}\n' + 
                f'Nyt metodi palauttaa {a.viimeisin_havainto()}')
                

    def test5_testaa_str(self):
        from src.havaintoasema import Havaintoasema

        for nimi in ["Kumpula", "Turku", "Iisalmi"]:
            a = Havaintoasema(nimi)
            test_cases = ["Sataa","Ukkostaa","Sataa lunta", "Aurinko paistaa", "Sataa"]
            tests = ""
            n = 0
            for test_case in test_cases:
                n += 1
                a.lisaa_havainto(test_case)
                tests += f"\nlisaa_havainto({test_case})"
                corr = f"{nimi}, {n} havaintoa"
                var = str(a)

                self.assertEqual(var, corr, f'Olion tulosteen pitäisi olla {corr} ' + 
                    f'kun on kutsuttu seuraavat metodit olion luomisen jälkeen:{tests}\n' + 
                    f'Nyt metodi __str__ palauttaa {var}')


    
   
if __name__ == '__main__':
    unittest.main()
