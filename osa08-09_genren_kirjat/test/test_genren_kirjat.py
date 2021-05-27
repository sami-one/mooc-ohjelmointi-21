import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import os.path
import textwrap
from random import choice, randint

exercise = 'src.genren_kirjat'
function = "genren_kirjat"


@points('8.genren_kirjat')
class GenrenKirjatTest(unittest.TestCase):
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
            from src.genren_kirjat import genren_kirjat
        except:
            self.assertTrue(False, "Ohjelmastasi pitäisi löytyä funktio nimeltä vanhempi_kirja(kirja1: Kirja, kirja2: Kirja)")

    def test1b_luokkamaarittely_olemassa(self):
        try:
            from src.genren_kirjat import Kirja
        except:
            self.assertTrue(False, "Ohjelmassa pitää olla määriteltynä luokka Kirja!")

    def test2_palautusarvon_tyyppi(self):
        try:
            from src.genren_kirjat import genren_kirjat
            from src.genren_kirjat import Kirja
            
            val = genren_kirjat([Kirja("Python","P. Python", "tieto", 2000), Kirja("Java", "J.Java", "tieto", 2001)], "tieto")
            taip = str(type(val)).replace("<class '","").replace("'>","")
            self.assertTrue(type(val) == list, f"Funktion genren_kirjat pitäisi palauttaa lista," +  
                f" nyt se palauttaa arvon {val} joka on tyyppiä {taip}\n kun sitä kutsutaan parametreilla\n" + 
                'genren_kirjat([Kirja("Python","P. Python", "tieto", 2000), Kirja("Java", "J.Java", "tieto", 2001)])')
        except Exception as e:
            self.assertTrue(False, f"Funktio antoi virheen kun sitä kutsuttiin parametrin arvolla\n" +
                f'genren_kirjat([Kirja("Python","P. Python", "tieto", 2000), Kirja("Java", "J.Java", "tieto", 2001)])\n{e}')


    def test3_testaa_lista1(self):
        test_case = [("Seitsemän veljestä", "Aleksis Kivi", "Romaani", 1870), 
                       ("Sinuhe egyptiläinen", "Mika Waltari", "Romaani", 1945),
                       ("Kyberias", "Stanislaw Lem", "Sci-fi", 1965), 
                       ("Kotona maailmankaikkeudessa", "Esko Valtaoja", "Tiede", 2001)]
        genre = "Romaani"
        
        with patch('builtins.input', side_effect=[AssertionError("Syötteen pyytämistä ei odotettu")]):
            reload_module(self.module)
            genren_kirjat = load(exercise, function, 'fi')
            from src.genren_kirjat import Kirja

            lista = [Kirja(x[0],x[1],x[2],x[3]) for x in test_case]
            corr = sorted([x for x in lista if x.genre == genre], key = lambda x: x.nimi)
            val = sorted(genren_kirjat(lista, genre), key = lambda x: x.nimi)
            
            self.assertEqual(corr, val, f"Funktion tulisi palauttaa listassa arvot\n{corr}\n,nyt se palauttaa listan\n{val}\nkun kirjat olivat\n{test_case}")

    def test4_testaa_lista2(self):
        test_case = [("Seitsemän veljestä", "Aleksis Kivi", "Romaani", 1870), 
                       ("Sinuhe egyptiläinen", "Mika Waltari", "Romaani", 1945),
                       ("Kyberias", "Stanislaw Lem", "Sci-fi", 1965), 
                       ("Kotona maailmankaikkeudessa", "Esko Valtaoja", "Tiede", 2001),
                       ("Avaruusseikkalu 2001", "Arthur C. Clarke", "Sci-fi", 1968)]
        genre = "Sci-fi"
        
        with patch('builtins.input', side_effect=[AssertionError("Syötteen pyytämistä ei odotettu")]):
            reload_module(self.module)
            genren_kirjat = load(exercise, function, 'fi')
            from src.genren_kirjat import Kirja

            lista = [Kirja(x[0],x[1],x[2],x[3]) for x in test_case]
            corr = sorted([x for x in lista if x.genre == genre], key = lambda x: x.nimi)
            val = sorted(genren_kirjat(lista, genre), key = lambda x: x.nimi)
            
            self.assertEqual(corr, val, f"Funktion tulisi palauttaa listassa arvot\n{corr}\n,nyt se palauttaa listan\n{val}\nkun kirjat olivat\n{test_case}")

                
    

if __name__ == '__main__':
    unittest.main()
