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

exercise = 'src.paras_koetulos'

def source_rows(funktio: callable):
    src = inspect.getsource(funktio)
    lines = [line.strip() for line in re.split('\\n|;', src) 
        if len(line.strip()) > 0 and not line.strip().startswith("#")]
    return len(lines)

@points('11.paras_koetulos')
class ParasKoetulosTest(unittest.TestCase):
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
            from src.paras_koetulos import parhaat_tulokset
        except Exception as e:
            self.fail(f'Ohjelmasta pitäisi löytyä funktio nimeltä parhaat_tulokset.')

    def test_1b_luokka_olemassa(self):
        try:
            from src.paras_koetulos import Koesuoritus
        except Exception as e:
            self.fail(f'Ohjelmasta pitäisi löytyä luokka nimeltä Koesuoritus - ' + 
                'ethän ole muuttanut luokan määrittelyä?')

    def test_2_paluuarvon_tyyppi(self):
        try:
            from src.paras_koetulos import parhaat_tulokset, Koesuoritus
            val = parhaat_tulokset([Koesuoritus("Pekka",1,2,3)])
        except Exception as e:
            self.assertTrue(False, f'Funktio antoi virheen kun sitä kutsuttiin näin:\n' + 
                'parhaat_tulokset([Koesuoritus("Pekka",1,2,3)]):\n{e}')
        taip = str(type(val)).replace("<class '","").replace("'>","")
        self.assertTrue(type(val) == list, f"Funktion parhaat_tulokset pitäisi palauttaa arvo, jonka tyyppi on list," +  
            f" nyt se palauttaa arvon {val} joka on tyyppiä {taip}\n kun sitä kutsutaan parametrilla\n" +  
            "tahtirivit([1])")
        

    def test_3_funktion_pituus(self):
        from src.paras_koetulos import parhaat_tulokset
        lines = source_rows(parhaat_tulokset)
        max_lines = 2
        self.assertTrue(lines <= max_lines, f'Funktiossa parhaat_tulokset saa tässä tehtävässä olla korkeintaan'+ 
            f' {max_lines} riviä.\n' +
            f'Nyt funktiossa on yhteensä {lines} riviä (poislukien tyhjät rivit ja kommentit.')

    def test_4_testaa_arvoilla1(self):
        test_cases = [("Pasi",3,1,2), ("Kimmo",4,5,3), ("Arto",2,3,4)]
        from src.paras_koetulos import parhaat_tulokset, Koesuoritus
        input_values = [Koesuoritus(x[0],x[1],x[2],x[3]) for x in test_cases]
        corr = [max(x[1:]) for x in test_cases]
        val = parhaat_tulokset(input_values)
        test_f = ", ".join([f'Koetulos{x}' for x in test_cases])

        self.assertEqual(val, corr, f'Funktion pitäisi palautta lista\n{corr}\n' + 
            f'kun sitä kutsutaan parametrilla\n{test_f}\nnyt funktio palauttaa\n' + 
            f'{val}')

    def test_5_testaa_arvoilla2(self):
        test_cases = [("Leenu",4,1,2), ("Linnu",1,2,5), ("Tiina",4,4,5), ("Matti",5,1,1), ("Keijo",2,4,2)]
        from src.paras_koetulos import parhaat_tulokset, Koesuoritus
        input_values = [Koesuoritus(x[0],x[1],x[2],x[3]) for x in test_cases]
        corr = [max(x[1:]) for x in test_cases]
        val = parhaat_tulokset(input_values)
        test_f = ", ".join([f'Koetulos{x}' for x in test_cases])

        self.assertEqual(val, corr, f'Funktion pitäisi palautta lista\n{corr}\n' + 
            f'kun sitä kutsutaan parametrilla\n{test_f}\nnyt funktio palauttaa\n' + 
            f'{val}')

   



    
if __name__ == '__main__':
    unittest.main()
