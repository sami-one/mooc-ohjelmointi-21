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

exercise = 'src.lukutilasto'

def f(attr: list):
    return ",".join(attr)

class TilastoTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=["0","-1"]):
           cls.module = load_module(exercise, 'fi')

    def test0a_paaohjelma_kunnossa(self):
        with open("src/lukutilasto.py") as t:
            if "if __name__" in t.read():
                self.assertTrue(False, 'Pääohjelmaa ei saa kirjoittaa lohkon if __name__ == "__main__": sisälle')

    @points('8.lukutilasto_osa1')
    def test1_luokka_olemassa(self):
        with patch('builtins.input', side_effect=["0","-1"]):
            try:
                from src.lukutilasto import Lukutilasto
            except:
                self.assertTrue(False, "Ohjelmastasi pitäisi löytyä luokka nimeltä Lukutilasto")

    @points('8.lukutilasto_osa1')
    def test2_konstruktori(self):
        with patch('builtins.input', side_effect=["0","-1"]):
            try:
                from src.lukutilasto import Lukutilasto
                val = Lukutilasto()
            except Exception as e:
                self.fail('Luokan Lukutilasto konstuktorin Lukutilasto() kutsuminen' +
                    f' palautti virheen: {e}')

    @points('8.lukutilasto_osa1')
    def test2b_testaa_metodit(self):
        from src.lukutilasto import Lukutilasto
        tilasto = Lukutilasto()
        try:
            tilasto.lisaa_luku(1)
        except Exception as e:
            self.fail(f"Metodikutsu lisaa_luku(1) antoi virheen {e}, " +
                "Tarkista että metodi löytyy luokasta!")
        try:
            tilasto.lukujen_maara()
        except Exception as e:
            self.fail(f"Metodikutsu lukujen_maara() antoi virheen {e}, " +
                "Tarkista että metodi löytyy luokasta!")
        

    @points('8.lukutilasto_osa1')
    def test3_testaa_lukujen_maara(self):
        test_cases = ([1], (2,3,4,2), (9,8,7,5,3,2,4,1), (3,3), (5,5,5,5,4,4,4,4,3,3,3,3,4,4,4,4))
        for test_case in test_cases:
            with patch('builtins.input', side_effect=["0","-1"]):    
                try:
                    from src.lukutilasto import Lukutilasto
                    lukutilasto = Lukutilasto()
                    for luku in test_case:
                        lukutilasto.lisaa_luku(luku)
                    corr = len(test_case)
                except Exception as e:
                    self.assertTrue(False, f"Luokkaa käyttäessä tapahtui virhe:\n{e}" +
                        "\nkun tilasto alustettiin kutsulla\n" +
                        f"Lukutilasto()\nja metodia lisaa_luku kutsuttiin arvoilla {test_case}")

                self.assertEqual(lukutilasto.lukujen_maara(), corr, f"Lukujen määrän pitäisi olla {corr}, kun tilasto alustettiin kutsulla\n" +
                    f"Lukutilasto()\nja metodia lisaa_luku kutsuttiin arvoilla {test_case}.\n" +
                    f"Nyt metodi lukujen_maara kuitenkin palauttaa {lukutilasto.lukujen_maara()}.")
                

    @points('8.lukutilasto_osa2')
    def test3_testaa_summa(self):
        from src.lukutilasto import Lukutilasto
        lukutilasto = Lukutilasto()
        lukutilasto.lisaa_luku(1)
        try:
            lukutilasto.summa()
        except Exception as e:
            self.fail(f"Metodikutsu summa() antoi virheen {e}, " +
                "Tarkista että metodi löytyy luokasta!")
       
        test_cases = ([1], (2,3), (5,4,3,4,5), (3,3), (5,5,5,5,4,4,4,4,3,3,3,3,4,4,4,4))
        for test_case in test_cases:
            with patch('builtins.input', side_effect=["0","-1"]):
                lukutilasto = Lukutilasto()
                for luku in test_case:
                    lukutilasto.lisaa_luku(luku)
                corr = sum(test_case)
                val = lukutilasto.summa()

                self.assertEqual(val, corr, f"Lukujen summan pitäisi olla {corr}, kun tilasto alustettiin kutsulla\n" +
                    f"Lukutilasto()\nja metodia lisaa_luku kutsuttiin arvoilla {test_case}.\n" +
                    f"Nyt metodi summa() kuitenkin palauttaa {val}.")

                # Testataan, ettei määrä hajonnut tässä välissä
                self.assertEqual(lukutilasto.lukujen_maara(), len(test_case), f"Lukujen määrän pitäisi olla {len(test_case)}, kun tilasto alustettiin kutsulla\n" +
                    f"Lukutilasto()\nja metodia lisaa_luku kutsuttiin arvoilla {test_case}.\n" +
                        f"Nyt metodi lukujen_maara kuitenkin palauttaa {lukutilasto.lukujen_maara()}.")

    @points('8.lukutilasto_osa2')
    def test3_testaa_keskiarvo(self):
        from src.lukutilasto import Lukutilasto
        lukutilasto = Lukutilasto()
        try:
            lukutilasto.keskiarvo()
        except Exception as e:
            self.fail(f"Metodikutsu keskiarvo() antoi virheen {e}, " +
                "Tarkista että metodi löytyy luokasta!")
        
        test_cases = ([1,1], (2,3), (1,2,3,4), (3,3), (5,5,5,5,4,4,4,4))
        for test_case in test_cases:
            lukutilasto = Lukutilasto()
            with patch('builtins.input', side_effect=["0","-1"]):            
                for luku in test_case:
                    lukutilasto.lisaa_luku(luku)
                corr = sum(test_case) / len(test_case)
                val = lukutilasto.keskiarvo()

                self.assertEqual(val, corr, f"Lukujen keskiarvon pitäisi olla {corr}, kun tilasto alustettiin kutsulla\n" +
                    f"Lukutilasto()\nja metodia lisaa_luku kutsuttiin arvoilla {test_case}.\n" +
                    f"Nyt metodi keskiarvo() kuitenkin palauttaa {val}.")
                
  
    @points('8.lukutilasto_osa3')
    def test3_testaa_input_summa_ja_ka(self):
        test_cases = ([1,-1], (2,3,-1), (5,4,3,4,5,-1), (3,3,-1), (5,5,5,5,4,4,4,4,3,3,3,3,4,4,4,4,-1))
        for test_case in test_cases:
            with patch('builtins.input', side_effect=list([str(x) for x in test_case])):
                reload_module(self.module)

                output = get_stdout()

                summa = sum([x for x in test_case if x != -1])
                ka = summa / (len(test_case) - 1)

                corr1 = f"Summa: {summa}"
                corr2 = f"Keskiarvo: {ka}"

                self.assertTrue(corr1 in output, f"Tulostuksesta pitäisi löytyä rivi\n{corr1}\nkun syöte on \n{test_case}.\nNyt tuloste on \n{output}")
                self.assertTrue(corr2 in output, f"Tulostuksesta pitäisi löytyä rivi\n{corr2}\nkun syöte on \n{test_case}.\nNyt tuloste on \n{output}")

    @points('8.lukutilasto_osa4')
    def test3_testaa_input_parilliset_parittomat(self):
        test_cases = ([1,2,-1], (1,2,3,2,3,2,-1), (5,4,3,4,5,-1), (10,9,8,7,6,5,4,3,2,1,-1))
        for test_case in test_cases:
            with patch('builtins.input', side_effect=list([str(x) for x in test_case])):
                reload_module(self.module)

                output = get_stdout()

                even = sum([x for x in test_case if x % 2 == 0])
                odd = sum([x for x in test_case if x % 2 != 0 and x != -1])

                corr1 = f"Parillisten summa: {even}"
                corr2 = f"Parittomien summa: {odd}"

                self.assertTrue(corr1 in output, f"Tulostuksesta pitäisi löytyä rivi\n{corr1}\nkun syöte on \n{test_case}.\nNyt tuloste on \n{output}")
                self.assertTrue(corr2 in output, f"Tulostuksesta pitäisi löytyä rivi\n{corr2}\nkun syöte on \n{test_case}.\nNyt tuloste on \n{output}")

   

if __name__ == '__main__':
    unittest.main()
