import unittest
from unittest.mock import patch

from tmc import points, reflect
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import os.path
import textwrap
import inspect, re
from random import choice, randint, shuffle

exercise = 'src.pisteiden_mukaan'

def source_rows(funktio: callable):
    src = inspect.getsource(funktio)
    lines = [line.strip() for line in re.split('\\n|;', src) 
        if len(line.strip()) > 0 and not line.strip().startswith("#")]
    return len(lines)

@points('12.pisteiden_mukaan')
class PisteidenMukaanTest(unittest.TestCase):
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
    
    def test_1_funktio_olemassa(self):
        try:
            from src.pisteiden_mukaan import jarjesta_pisteiden_mukaan
        except Exception as e:
            self.fail(f'Ohjelmasta pitäisi löytyä funktio nimeltä jarjesta_pisteiden_mukaan.')

    def test_2_paluuarvon_tyyppi(self):
        try:
            from src.pisteiden_mukaan import jarjesta_pisteiden_mukaan
            val = jarjesta_pisteiden_mukaan([{ "nimi": "Dexter", "pisteet" : 8.6, "kausia":9 }, 
                { "nimi": "Friends", "pisteet" : 8.9, "kausia":10 }])
        except Exception as e:
            self.fail(f"Funktio antoi virheen kun sitä kutsuttiin näin:\n"  + 
            'jarjesta_pisteiden_mukaan([{ "nimi": "Dexter", "pisteet" : 8.6, "kausia":9 }, { "nimi": "Friends", "pisteet" : 8.9, "kausia":10 }]):\n' + 
            f'{e}')
        taip = str(type(val)).replace("<class '","").replace("'>","")
        self.assertTrue(type(val) == list, f"Funktion jarjesta_pisteiden_mukaan pitäisi palauttaa arvo, jonka tyyppi on list," +  
            f" nyt se palauttaa arvon {val} joka on tyyppiä {taip}\n kun sitä kutsutaan parametrilla\n" +  
            'jarjesta_pisteiden_mukaan([{ "nimi": "Dexter", "pisteet" : 8.6, "kausia":9 }, { "nimi": "Friends", "pisteet" : 8.9, "kausia":10 }])')
        

    def test_3_testaa_arvoilla1(self):
        from src.pisteiden_mukaan import jarjesta_pisteiden_mukaan
    
        tdata = [("Dexter",8.8, 9), ("Simpsons",8.6,30), ("Friends",8.9,10), ("Oz",8.7,6)]
        test_case = [{"nimi":tc[0], "pisteet":tc[1], "kausia":tc[2]} for tc in tdata]
        test_case_2 = test_case[:]
        corr = sorted(test_case, key=lambda t:t["pisteet"], reverse=True)
        val = jarjesta_pisteiden_mukaan(test_case)

        self.assertEqual(val, corr, f'Funktion pitäisi palauttaa lista\n{corr}\n' + 
            f'kun sitä kutsutaan parametrilla\n{test_case}\nnyt funktio palauttaa\n' + 
            f'{val}')

        self.assertEqual(test_case, test_case_2, f"Funktio ei saa muuttaa alkuperäistä listaa!\n" + 
            f'Lista ennen kutsua oli\n{test_case_2}\nja kutsun jälkeen se on\n{test_case}.')

    def test_4_testaa_arvoilla1(self):
        from src.pisteiden_mukaan import jarjesta_pisteiden_mukaan
    
        tdata = [("The Wire",9.3, 5), ("Game of Thrones",9.2,8), ("Band of Brothers",9.5,1), ("Sopranos",9.4,6), ("Sherlock",9.1,4)]
        test_case = [{"nimi":tc[0], "pisteet":tc[1], "kausia":tc[2]} for tc in tdata]
        test_case_2 = test_case[:]
        corr = sorted(test_case, key=lambda t:t["pisteet"], reverse=True)
        val = jarjesta_pisteiden_mukaan(test_case)

        self.assertEqual(val, corr, f'Funktion pitäisi palauttaa lista\n{corr}\n' + 
            f'kun sitä kutsutaan parametrilla\n{test_case}\nnyt funktio palauttaa\n' + 
            f'{val}')

        self.assertEqual(test_case, test_case_2, f"Funktio ei saa muuttaa alkuperäistä listaa!\n" + 
            f'Lista ennen kutsua oli\n{test_case_2}\nja kutsun jälkeen se on\n{test_case}.')

 
    
if __name__ == '__main__':
    unittest.main()
