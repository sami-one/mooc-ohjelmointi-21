import unittest
from unittest.mock import patch

from tmc import points, reflect
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import os.path
import textwrap
from random import choice, randint
from datetime import date, datetime, timedelta

exercise = 'src.koodi'

def f(attr: list):
    return ",".join(attr)

def s(l: list):
    return "\n".join(l)

@points('10.puhelinluettelo_osa2_1')
class Puhelinluettelo2_Osa1Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=["0"]):
           cls.module = load_module(exercise, 'fi')

    def test1_henkilo_olemassa(self):
        try:
            from src.koodi import Henkilo
        except:
            self.assertTrue(False, "Ohjelmastasi pitäisi löytyä luokka nimeltä Henkilo")
        try:
            Henkilo("Erkki")
        except Exception as e:
            self.assertTrue(False, 'Luokan Henkilo konstuktorin kutsuminen arvoilla Henkilo("Erkki")' +
                f' palautti virheen: {e}\nVarmista että konstruktori on määritelty oikein')

    def test2_henkilo_toimii(self):
        from src.koodi import Henkilo
        h = Henkilo("Erkki")
        koodi = """
h = Henkilo("Erkki")
h.nimi()
"""
        try:
            p = h.nimi()
        except Exception as e:
            self.assertTrue(False, f'Koodin\n{koodi}\nsuoritus aiheutti virheen\n{e}\nOnhan metodi nimi(self) määritelty?')
        exp = "Erkki"
        self.assertEqual(exp, p,  f'\nKun suoritetaan\n{koodi}\nmetodin pitäsi palauttaa {exp}, paluuarvo oli {p}')

        koodi = """
h = Henkilo("Erkki")
h.mumerot()
"""            
        try:
            p = h.numerot()
        except Exception as e:
            self.assertTrue(False, f'Koodin\n{koodi}\nsuoritus aiheutti virheen\n{e}\nOnhan metodi numerot(self) määritelty?')
        exp = []
        self.assertEqual(exp, p,  f'\nKun suoritetaan\n{koodi}\nmetodin pitäsi palauttaa {exp}, paluuarvo oli {p}')

        koodi = """
h = Henkilo("Erkki")
h.lisaa_numero("040-445566")
"""        
        try:
            h.lisaa_numero("040-445566")
        except Exception as e:
            self.assertTrue(False, f'Koodin\n{koodi}\nsuoritus aiheutti virheen\n{e}\nOnhan metodi lisaa_numero(self, numero: str) määritelty?')           
        
        koodi = """
h = Henkilo("Erkki")
h.lisaa_numero("040-445566")
h.mumerot()
"""    
        try:
            p = h.numerot()
        except Exception as e:
            self.assertTrue(False, f'Koodin\n{koodi}\nsuoritus aiheutti virheen\n{e}\nOnhan metodi numerot(self) määritelty?')
        exp = ["040-445566"]
        self.assertEqual(exp, p,  f'\nKun suoritetaan\n{koodi}\nmetodin pitäsi palauttaa {exp}, paluuarvo oli {p}')

        koodi = """
h = Henkilo("Erkki")
h.lisaa_numero("040-445566")
h.lisaa_numero("02-121212")
h.mumerot()
"""    

        try:
            p = h.numerot()
        except Exception as e:
            self.assertTrue(False, f'Koodin\n{koodi}\nsuoritus aiheutti virheen\n{e}\nOnhan metodi numerot(self) määritelty?')
        exp = ["040-445566"]
        self.assertEqual(sorted(exp), sorted(p), f'\nKun suoritetaan\n{koodi}\nmetodin pitäsi palauttaa {exp}, paluuarvo oli {p}')

        koodi = """
h = Henkilo("Erkki")
h.osoite()
"""            
        try:
            p = h.osoite()
        except Exception as e:
            self.assertTrue(False, f'Koodin\n{koodi}\nsuoritus aiheutti virheen\n{e}\nOnhan metodi numerot(self) määritelty?')
        exp = None
        self.assertEqual(exp, p,  f'\nKun suoritetaan\n{koodi}\nmetodin pitäsi palauttaa {exp}, paluuarvo oli {p}')

        koodi = """
h = Henkilo("Erkki")
h.lisaa_osoite("Linnankatu 1")
"""        
        try:
            h.lisaa_osoite("Linnankatu 1")
        except Exception as e:
            self.assertTrue(False, f'Koodin\n{koodi}\nsuoritus aiheutti virheen\n{e}\nOnhan metodi lisaa_osoite(self, osoite: str) määritelty?')           
        
        koodi = """
h = Henkilo("Erkki")
h.lisaa_osoite("Linnankatu 1")
h.osoite()
"""        
        try:
            p = h.osoite()
        except Exception as e:
            self.assertTrue(False, f'Koodin\n{koodi}\nsuoritus aiheutti virheen\n{e}\nOnhan metodi lisaa_osoite(self, osoite: str) määritelty?')           
        exp = "Linnankatu 1"
        self.assertEqual(exp, p,  f'\nKun suoritetaan\n{koodi}\nmetodin pitäsi palauttaa {exp}, paluuarvo oli {p}')

if __name__ == '__main__':
    unittest.main()

