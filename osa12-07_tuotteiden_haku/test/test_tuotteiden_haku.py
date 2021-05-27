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

exercise = 'src.tuotteiden_haku'

def source_rows(funktio: callable):
    src = inspect.getsource(funktio)
    lines = [line.strip() for line in re.split('\\n|;', src) 
        if len(line.strip()) > 0 and not line.strip().startswith("#")]
    return len(lines)

@points('12.tuotteiden_haku')
class TuotteidenHakuTest(unittest.TestCase):
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
            from src.tuotteiden_haku import hae
        except Exception as e:
            self.fail(f'Ohjelmasta pitäisi löytyä funktio nimeltä hae.')

    def test_2_paluuarvon_tyyppi(self):
        try:
            from src.tuotteiden_haku import hae
            val = hae([("Omena",1,1)], lambda x : True)
        except Exception as e:
            self.fail(f"Funktio antoi virheen kun sitä kutsuttiin näin:\n"  + 
            'hae([("Omena",1,1)], lambda x : True)\n' + 
            f'{e}')
        taip = str(type(val)).replace("<class '","").replace("'>","")
        self.assertTrue(type(val) == list, f"Funktion hae pitäisi palauttaa arvo, jonka tyyppi on list," +  
            f" nyt se palauttaa arvon {val} joka on tyyppiä {taip}\n kun sitä kutsutaan parametrilla\n" +  
            'hae([("Omena",1,1)], lambda x : True)')
        

    def test_3_testaa_arvoilla1(self):
        from src.tuotteiden_haku import hae
    
        test_case = [("Omena",4.0,3), ("Appelsiini",5.95, 5), ("Banaani",2.95,10), ("Ananas", 5.50, 3)]
        test_case_2 = test_case[:]
        func = "lambda tuote: tuote[1] >= 5"
        corr = [("Appelsiini",5.95, 5),("Ananas", 5.50, 3)]
        val = hae(test_case, lambda t: t[1] > 5)

        self.assertEqual(val, corr, f'Funktion pitäisi palauttaa lista\n{corr}\n' + 
            f'kun sitä kutsutaan listalla\n{test_case}\nja funktiolla\n{func}\nnyt funktio palauttaa\n' + 
            f'{val}')

        self.assertEqual(test_case, test_case_2, f"Funktio ei saa muuttaa alkuperäistä listaa!\n" + 
            f'Lista ennen kutsua oli\n{test_case_2}\nja kutsun jälkeen se on\n{test_case}.')

    def test_4_testaa_arvoilla2(self):
        from src.tuotteiden_haku import hae
    
        test_case = [("Omena",4.0,3), ("Appelsiini",5.95, 5), ("Banaani",2.95,10), ("Ananas", 5.50, 3), 
            ("Aprikoosi",6.95,2), ("Mandariini",3.95,4)]
        test_case_2 = test_case[:]
        func = "lambda tuote: tuote[0].startwith('A')"
        corr = [("Appelsiini",5.95, 5),("Ananas", 5.50, 3),("Aprikoosi",6.95,2)]
        val = hae(test_case, lambda t: t[0].startswith("A"))

        self.assertEqual(val, corr, f'Funktion pitäisi palauttaa lista\n{corr}\n' + 
            f'kun sitä kutsutaan listalla\n{test_case}\nja funktiolla\n{func}\nnyt funktio palauttaa\n' + 
            f'{val}')

        self.assertEqual(test_case, test_case_2, f"Funktio ei saa muuttaa alkuperäistä listaa!\n" + 
            f'Lista ennen kutsua oli\n{test_case_2}\nja kutsun jälkeen se on\n{test_case}.')

    def test_5_testaa_arvoilla3(self):
        from src.tuotteiden_haku import hae
    
        test_case = [("Omena",4.0,3), ("Appelsiini",5.95, 5), ("Banaani",2.95,10), ("Ananas", 5.50, 3), 
            ("Aprikoosi",6.95,2), ("Mandariini",3.95,4)]
        test_case_2 = test_case[:]
        func = "lambda tuote: tuote[2] < 5"
        corr = [("Omena",4.0,3), ("Ananas", 5.50, 3), 
            ("Aprikoosi",6.95,2), ("Mandariini",3.95,4)]
        val = hae(test_case, lambda t: t[2] < 5)

        self.assertEqual(val, corr, f'Funktion pitäisi palauttaa lista\n{corr}\n' + 
            f'kun sitä kutsutaan listalla\n{test_case}\nja funktiolla\n{func}\nnyt funktio palauttaa\n' + 
            f'{val}')

        self.assertEqual(test_case, test_case_2, f"Funktio ei saa muuttaa alkuperäistä listaa!\n" + 
            f'Lista ennen kutsua oli\n{test_case_2}\nja kutsun jälkeen se on\n{test_case}.')    

 
    
if __name__ == '__main__':
    unittest.main()
