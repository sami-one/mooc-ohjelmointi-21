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

exercise = 'src.suodata_kielletyt'

def source_rows(funktio: callable):
    src = inspect.getsource(funktio)
    lines = [line.strip() for line in re.split('\\n|;', src) 
        if len(line.strip()) > 0 and not line.strip().startswith("#")]
    return len(lines)

@points('11.suodata_kielletyt')
class SuodataKielletytTest(unittest.TestCase):
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
            from src.suodata_kielletyt import suodata_kielletyt
        except Exception as e:
            self.fail(f'Ohjelmasta pitäisi löytyä funktio nimeltä suodata_kielletyt.')

    def test_2_paluuarvon_tyyppi(self):
        try:
            from src.suodata_kielletyt import suodata_kielletyt
            val = suodata_kielletyt("abc","a")
        except Exception as e:
            self.assertTrue(False, f"Funktio antoi virheen kun sitä kutsuttiin näin:" + 
                f'\nsuodata_kielletyt("abc","a")\n{e}')
        taip = str(type(val)).replace("<class '","").replace("'>","")
        self.assertTrue(type(val) == str, f"Funktion suodata_kielletyt pitäisi palauttaa arvo, jonka tyyppi on str," +  
            f" nyt se palauttaa arvon {val} joka on tyyppiä {taip}\n kun sitä kutsutaan näin\n" +  
            'suodata_kielletyt("abc","a")')
        

    def test_3_funktion_pituus(self):
        from src.suodata_kielletyt import suodata_kielletyt
        lines = source_rows(suodata_kielletyt)
        max_lines = 3
        self.assertTrue(lines <= max_lines, f'Funktiossa suodata_kielletyt saa tässä tehtävässä olla korkeintaan'+ 
            f' {max_lines} riviä.\n' +
            f'Nyt funktiossa on yhteensä {lines} riviä (poislukien tyhjät rivit ja kommentit.')

    def test_4_testaa_arvoilla1(self):
        test_case = ("abcdefg", "bde")
        corr = "acfg"
        from src.suodata_kielletyt import suodata_kielletyt
        val = suodata_kielletyt(test_case[0], test_case[1])

        self.assertEqual(val, corr, f'Funktion pitäisi palauttaa merkkijono\n{corr}\n' + 
            f'kun sitä kutsutaan parametreilla\n{test_case}\nnyt funktio palauttaa\n' + 
            f'{val}')

    
    def test_5_testaa_arvoilla2(self):
        test_case = ("Vesihiisi sihisi hississä", "sh")
        corr = "Veiiii iii iiä"
        from src.suodata_kielletyt import suodata_kielletyt
        val = suodata_kielletyt(test_case[0], test_case[1])

        self.assertEqual(val, corr, f'Funktion pitäisi palauttaa merkkijono\n{corr}\n' + 
            f'kun sitä kutsutaan parametreilla\n{test_case}\nnyt funktio palauttaa\n' + 
            f'{val}')

    def test_6_testaa_arvoilla3(self):
        test_case = ("appilan pappila apupappi tavaa: abcdefghi", "aeh")
        corr = "ppiln pppil pupppi tv: bcdfgi"
        from src.suodata_kielletyt import suodata_kielletyt
        val = suodata_kielletyt(test_case[0], test_case[1])

        self.assertEqual(val, corr, f'Funktion pitäisi palauttaa merkkijono\n{corr}\n' + 
            f'kun sitä kutsutaan parametreilla\n{test_case}\nnyt funktio palauttaa\n' + 
            f'{val}')



    

   

    








    
if __name__ == '__main__':
    unittest.main()
