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

exercise = 'src.lemmikki'

def f(attr: list):
    return ",".join([str(x) for x in attr]) 

@points('9.lemmikki')
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

    def test_1_luokat_olemassa(self):
        try:
            from src.lemmikki import Lemmikki
            l = Lemmikki("Rekku","koira")
        except Exception as e:
            self.fail(f'Konstruktorikutsu Lemmikki("Rekku","koira") antoi virheen \n{e}\n' + 
            'Älä muuta luokkaa Lemmikki')

        try:
            from src.lemmikki import Henkilo
            h = Henkilo("Matti", l)
        except Exception as e:
            self.fail(f'Konstruktorikutsu Henkilo("Matti",Lemmikki("Rekku","koira")) antoi virheen \n{e}\n')

    def test2_str_toimii(self):
        test_cases = [("Arto","Musti","pieni koira"), ("Matti","Hapsu", "kultainen hamsteri"),
                      ("Liisa","Kalervo","veikeä kultakala"), ("Jaakko", "Jarmo", "kiroileva siili")]
        for test_case in test_cases:
            from src.lemmikki import Lemmikki,Henkilo
            lem = Lemmikki(test_case[1], test_case[2])
            hen = Henkilo(test_case[0], lem)
            val = str(hen)

            corr = f"{test_case[0]}, kaverina {test_case[1]}, joka on {test_case[2]}"

            for mjono in test_case:
                self.assertTrue(mjono in val, f'Metodin __str__ tuloksesta pitäisi löytyä merkkijono {mjono}\n' +
                    f'"kun olio on alustettu näin:\n' +
                    f'Henkilo("{test_case[0]}", Lemmikki("{test_case[1]}", "{test_case[2]}"))')

            self.assertEqual(val, corr, f"Metodin __str__ pitäisi palauttaa\n{corr}\n" +
                f"nyt se palauttaa\n{val}\n" +
                f'kun olio on alustettu näin:\n' +
                f'Henkilo("{test_case[0]}", Lemmikki("{test_case[1]}", "{test_case[2]}"))' +
                "\nTarkista, että myös pilkut ja välilyönnit ovat kohdillaan!")
                
if __name__ == '__main__':
    unittest.main()
