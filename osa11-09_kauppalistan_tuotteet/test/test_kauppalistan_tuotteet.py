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

exercise = 'src.kauppalistan_tuotteet'

def source_rows(funktio: callable):
    src = inspect.getsource(funktio)
    lines = [line.strip() for line in re.split('\\n|;', src) 
        if len(line.strip()) > 0 and not line.strip().startswith("#")]
    return len(lines)

@points('11.kauppalistan_tuotteet')
class KauppalistanTuotteetTest(unittest.TestCase):
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
            from src.kauppalistan_tuotteet import kauppalistan_tuotteet
        except Exception as e:
            self.fail(f'Ohjelmasta pitäisi löytyä funktio nimeltä kauppalistan_tuotteet.')

    def test_2_paluuarvon_tyyppi(self):
        try:
            from src.kauppalistan_tuotteet import kauppalistan_tuotteet
            val = kauppalistan_tuotteet([("omena",2)],1)
        except Exception as e:
            self.assertTrue(False, f"Funktio antoi virheen kun sitä kutsuttiin näin:" + 
                f'\nkauppalistan_tuotteet([("omena",2)],1)\n{e}')
        taip = str(type(val)).replace("<class '","").replace("'>","")
        self.assertTrue(type(val) == list, f"Funktion kauppalistan_tuotteet pitäisi palauttaa arvo, jonka tyyppi on list," +  
            f" nyt se palauttaa arvon {val} joka on tyyppiä {taip}\n kun sitä kutsutaan näin\n" +  
            'kauppalistan_tuotteet([("omena",2)],1)')
        

    def test_3_funktion_pituus(self):
        from src.kauppalistan_tuotteet import kauppalistan_tuotteet
        lines = source_rows(kauppalistan_tuotteet)
        max_lines = 2
        self.assertTrue(lines <= max_lines, f'Funktiossa suodata_kielletyt saa tässä tehtävässä olla korkeintaan'+ 
            f' {max_lines} riviä.\n' +
            f'Nyt funktiossa on yhteensä {lines} riviä (poislukien tyhjät rivit ja kommentit.')

    def test_4_testaa_arvoilla1(self):
        test_case = [("Omena",10),("Appelsiini",6),("Banaani",8),("Ananas",4),("Luumu",9)]
        corr = ["Omena","Banaani","Luumu"]
        raja = 7
        from src.kauppalistan_tuotteet import kauppalistan_tuotteet
        val = kauppalistan_tuotteet(test_case, raja)

        self.assertEqual(val, corr, f'Funktion pitäisi palauttaa lista\n{corr}\n' + 
            f'kun sitä kutsutaan näin:\n' + 
            f'kauppalistan_tuotteet({test_case}, {raja})\n' +
            f'nyt funktio palauttaa\n' + 
            f'{val}')

    def test_5_testaa_arvoilla2(self):
        test_case = [("Purkka",5),("Suklaa",4),("Tikkari",5),("Sipsit",4)]
        corr = ["Purkka","Tikkari"]
        raja = 5
        from src.kauppalistan_tuotteet import kauppalistan_tuotteet
        val = kauppalistan_tuotteet(test_case, raja)

        self.assertEqual(val, corr, f'Funktion pitäisi palauttaa lista\n{corr}\n' + 
            f'kun sitä kutsutaan näin:\n' + 
            f'kauppalistan_tuotteet({test_case}, {raja})\n' +
            f'nyt funktio palauttaa\n' + 
            f'{val}')

    def test_6_testaa_arvoilla3(self):
        test_case = [("Vihko",12),("Kynä",14),("Terotin",9),("Viivotin",7)]
        corr = ["Kynä"]
        raja = 13
        from src.kauppalistan_tuotteet import kauppalistan_tuotteet
        val = kauppalistan_tuotteet(test_case, raja)

        self.assertEqual(val, corr, f'Funktion pitäisi palauttaa lista\n{corr}\n' + 
            f'kun sitä kutsutaan näin:\n' + 
            f'kauppalistan_tuotteet({test_case}, {raja})\n' +
            f'nyt funktio palauttaa\n' + 
            f'{val}')

 
if __name__ == '__main__':
    unittest.main()
