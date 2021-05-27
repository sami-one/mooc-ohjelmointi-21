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

exercise = 'src.etu_ja_sukunimi'

def f(attr: list):
    return ",".join(attr)

@points('8.etu_ja_sukunimi')
class EtuJaSukunimiTest(unittest.TestCase):
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
            from src.etu_ja_sukunimi import Henkilo
        except:
            self.assertTrue(False, "Ohjelmastasi pitäisi löytyä luokka nimeltä Henkilo")


    def test2_konstruktori(self):
        try:
            from src.etu_ja_sukunimi import Henkilo
            val = Henkilo("Pekka Python")
            self.assertTrue(True, "")
        except Exception as e:
            self.assertTrue(False, 'Luokan Henkilo konstuktorin kutsuminen arvoilla Henkilo("Pekka Python")' +
                f' palautti virheen: {e}')

    def test3_testaa_etunimi(self):
        test_cases = ("Pekka Python", "Paula Pascal", "Jarmo Java", "Heikki Haskell", "Benjamin Basic", "Carlos Ceesharp")
        for test_case in test_cases:
            try:
                from src.etu_ja_sukunimi import Henkilo
                hlo = Henkilo(test_case)
                val = hlo.anna_etunimi()
                corr = test_case.split(" ")[0]

                self.assertEqual(val, corr, f"Metodin anna_etunimi pitäisi palauttaa {corr}, kun laskuri alustettiin kutsulla\n" +
                    f"Henkilo('{test_case}')\nNyt metodi palauttaa\n{val}")
                    
            except Exception as e:
                self.assertTrue(False, f"Metodia anna_etunimi kutsuessa tapahtui virhe:\n{e}" +
                    f"kun olio alustettiin kutsulla Henkilo{(test_case)}")

    def test4_testaa_sukunimi(self):
        test_cases = ("Pekka Python", "Paula Pascal", "Jarmo Java", "Heikki Haskell", "Benjamin Basic", "Carlos Ceesharp")
        for test_case in test_cases:
            try:
                from src.etu_ja_sukunimi import Henkilo
                hlo = Henkilo(test_case)
                val = hlo.anna_sukunimi()
                corr = test_case.split(" ")[-1]

                self.assertEqual(val, corr, f"Metodin anna_sukunimi pitäisi palauttaa {corr}, kun laskuri alustettiin kutsulla\n" +
                    f"Henkilo('{test_case}')\nNyt metodi palauttaa\n{val}")
                    
            except Exception as e:
                self.assertTrue(False, f"Metodia anna_sukunimi kutsuessa tapahtui virhe:\n{e}" +
                    f"kun olio alustettiin kutsulla Henkilo{(test_case)}")

    def test5_testaa_attribuutit(self):
        try:
            from src.etu_ja_sukunimi import Henkilo
            hlo = Henkilo("Eka Vekara")
            en = hlo.anna_etunimi()
            sn = hlo.anna_sukunimi()

            
        except Exception as e:
            self.fail(f"Tapahtui virhe:\n{e}" +
                    f"kun olio alustettiin kutsulla Henkilo('Eka Vekara')\n" + 
                    "ja kutsuttiin metodeja anna_etunimi() ja anna_sukunimi()")

        ref = reflect.Reflect(hlo)
        ref.set_object(hlo)
        att_list = ref.attributes_only()
        

        self.assertTrue(len(att_list) == 1, f"Luokalla Henkilo saa olla vain yksi attribuutti, nyt niitä on {len(att_list)}\n" + 
            f"Varmista, ettet käytä turhaan self-määrittelyä luodessasi paikallisen muuttujan!\n" + 
            f"Luokassa on nyt seuraavat attribuutit:\n{att_list}")



    

if __name__ == '__main__':
    unittest.main()
