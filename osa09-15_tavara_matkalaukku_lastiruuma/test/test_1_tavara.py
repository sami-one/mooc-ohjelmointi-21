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

@points('8.tavara_matkalaukku_lastiruuma_osa1')
class TavaraTest(unittest.TestCase):
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

    def test1_tavara_olemassa(self):
        try:
            from src.koodi import Tavara
        except:
            self.assertTrue(False, "Ohjelmastasi pitäisi löytyä luokka nimeltä Tavara")

    def test2_tavara_konstruktori(self):
        try:
            from src.koodi import Tavara
            tavara = Tavara("Aapiskukko", 2)
        except Exception as e:
            self.assertTrue(False, 'Luokan Tavara konstuktorin kutsuminen arvoilla Tavara("Aapiskukko", 2)' +
                f' palautti virheen: {e}\nVarmista että konstruktori on määritelty oikein')

    def test3_tavara_str(self):
        test_cases = [("Aapiskukko", 2), ("Moukari", 8), ("Kalajapullo", 1)]
        for test_case in test_cases:
            from src.koodi import Tavara
            tavara = Tavara(test_case[0], test_case[1])

            corr = f'{test_case[0]} ({test_case[1]} kg)'
            val = str(tavara)

            self.assertEqual(corr, val, f"Metodin __str__ pitäisi palauttaa merkkijono\n{corr}\nkun olio luotiin kutsulla\n" + 
                f'Tavara("{test_case[0]}", {test_case[1]})\nNyt metodi palauttaa merkkijonon\n{val}')

    def test4_aatribuutit_piilossa(self):
        from src.koodi import Tavara
        koodi = """
tavara = Tavara("Aapiskukko", 2)
print(tavara.paino)
"""

        ok = False
        tavara = Tavara("Aapiskukko", 2)
        try:
            v = tavara.paino
        except Exception as e:
            ok = True
        
        if not ok:
            self.assertFalse(type(v) ==  type(2), f'Koodin\n{koodi}\nsuorituksen ei pitäisi tulostaa tuotteen painoa. Tuotteen painon tulee olla kapseloitu')
        
        koodi = """
tavara = Tavara("Aapiskukko", 2)
print(tavara.nimi)
"""

        ok = False
        tavara = Tavara("Aapiskukko", 2)
        try:
            v = tavara.paino
        except Exception as e:
            ok = True
        
        if not ok:
            self.assertFalse(type(v) == type("LOL"), f'Koodin\n{koodi}\nsuorituksen ei pitäisi tulostaa tuotteen nimeä. Tuotteen nimen tulee olla kapseloitu')
         
    def test5_tavara_paino(self):
        try:
            from src.koodi import Tavara
            koodi = """
tavara = Tavara("Aapiskukko", 2)
tavara.paino()
"""

            tavara = Tavara("Aapiskukko", 2)
            p = tavara.paino()

        except Exception as e:
            self.assertTrue(False, f'Koodin\n{koodi}\nsuoritus aiheutti virheen\n{e}\nOnhan metodi paino(self) määritelty?')
                
        self.assertTrue(p == 2, f'Kun suoritetaan\n{koodi}\n, metodin pitäsi palauttaa 2, paluuarvo oli {p}')

    @points('8.tavara_matkalaukku_lastiruuma_osa1')
    def test6_tavara_nimi(self):
        try:
            from src.koodi import Tavara
            koodi = """
tavara = Tavara("Aapiskukko", 2)
tavara.nimi()
"""

            tavara = Tavara("Aapiskukko", 2)
            p = tavara.nimi()

        except Exception as e:
            self.assertTrue(False, f'Koodin\n{koodi}\nsuoritus aiheutti virheen\n{e}\nOnhan metodi nimi(self) määritelty?')
                
        self.assertTrue(p == "Aapiskukko", f'Kun suoritetaan\n{koodi}\n, metodin pitäsi palauttaa Aapiskukko, paluuarvo oli {p}')

    def test7_tavara_paino_2(self):
        try:
            from src.koodi import Tavara
            koodi = """
tavara = Tavara("Aapiskukko", 5)
tavara.paino()
"""

            tavara = Tavara("Aapiskukko", 5)
            p = tavara.paino()

        except Exception as e:
            self.assertTrue(False, f'Koodin\n{koodi}\nsuoritus aiheutti virheen\n{e}\nOnhan metodi paino(self) määritelty?')
                
        self.assertTrue(p == 5, f'Kun suoritetaan\n{koodi}\n, metodin pitäsi palauttaa 5, paluuarvo oli {p}')

    @points('8.tavara_matkalaukku_lastiruuma_osa1')
    def test7_tavara_nimi_2(self):
        try:
            from src.koodi import Tavara
            koodi = """
tavara = Tavara("Kukko", 2)
tavara.nimi()
"""

            tavara = Tavara("Kukko", 2)
            p = tavara.nimi()

        except Exception as e:
            self.assertTrue(False, f'Koodin\n{koodi}\nsuoritus aiheutti virheen\n{e}\nOnhan metodi nimi(self) määritelty?')
                
        self.assertTrue(p == "Kukko", f'Kun suoritetaan\n{koodi}\n, metodin pitäsi palauttaa Kukko, paluuarvo oli {p}')


if __name__ == '__main__':
    unittest.main()

