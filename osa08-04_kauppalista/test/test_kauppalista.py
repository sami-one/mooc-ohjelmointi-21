import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import os.path
import textwrap
from random import choice, randint
from datetime import date
from src.kauppalista import Kauppalista

exercise = 'src.kauppalista'
function = "tuotteita_yhteensa"

def get_corr(l):
    return sum(l.maara(i) for i in range(1, l.tuotteita() + 1))

def gen(l: list):
    k = Kauppalista()
    for i in l:
        k.lisaa(i[0],i[1])
    return k

def format(l: list):
    return "\n".join([f"{x[0]}: {x[1]} kpl." for x in l])

        

@points('8.kauppalista')
class KauppalistaTest(unittest.TestCase):
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
            from src.kauppalista import tuotteita_yhteensa
        except:
            self.assertTrue(False, "Ohjelmastasi pitäisi löytyä funktio nimeltä tuotteita_yhteensa(lista: Kauppalista)")

    def test2_palautusarvon_tyyppi(self):
        try:
            from src.kauppalista import tuotteita_yhteensa
            lista = gen([("omena",1)])
            val = tuotteita_yhteensa(lista)
            taip = str(type(val)).replace("<class '","").replace("'>","")
            self.assertTrue(type(val) == int, f"Funktion vuodet_listaan pitäisi palauttaa arvo, jonka tyyppi on int," +  
                f" nyt se palauttaa arvon {val} joka on tyyppiä {taip}\n kun sitä kutsutaan listalla, jolla on yksi tuote")
        except Exception as e:
            self.assertTrue(False, f"Funktio antoi virheen kun sitä kutsuttiin Kauppalista-oliolla, jolla on yksi tuote:\n{e}")


    def test3_testaa_arvot(self):
        d = date
        test_cases = ([("omena",5),("appelsiini",5)], [("omena",4),("appelsiini",5),("banaani",6)],
                      [("marsu", 2), ("hamsteri",8), ("gerbiili", 6)], [("auto",24),("mopo",40),("moottoripyörä",10),("kuorma-auto",5)], 
                      [("ruusu",100),("orvokki",90),("sinivuokko",80),("lilja",70),("valkovuokko",60)])

        for test_case in test_cases:
            with patch('builtins.input', side_effect=[AssertionError("Syötteen pyytämistä ei odotettu")]):
                reload_module(self.module)
                tuotteita_yhteensa = load(exercise, function, 'fi')

                lista = gen(test_case)
               
                val = tuotteita_yhteensa(lista)
                corr = get_corr(lista)

                self.assertEqual(val, corr, f"Funktion pitäisi palauttaa arvo {corr}\nmutta se palauttaa arvon {val}\nkun listassa on tuotteet \n{format(test_case)}")
    

if __name__ == '__main__':
    unittest.main()
