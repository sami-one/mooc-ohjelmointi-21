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

exercise = 'src.saannolliset_lausekkeet'

def source_rows(funktio: callable):
    src = inspect.getsource(funktio)
    lines = [line.strip() for line in re.split('\\n|;', src) 
        if len(line.strip()) > 0 and not line.strip().startswith("#")]
    return len(lines)


class SaannollisetLausekkeetTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=[AssertionError("Syötteen pyytämistä ei odotettu")]):
           cls.module = load_module(exercise, 'fi')
    
    @points('12.saannolliset_lausekkeet_osa1')
    def test_0a_paaohjelma_kunnossa(self):
        ok, line = check_source(self.module)
        message = """Funktioita testaava koodi tulee sijoittaa lohkon
if __name__ == "__main__":
sisälle. Seuraava rivi tulee siirtää:
"""
        self.assertTrue(ok, message+line)
    
    @points('12.saannolliset_lausekkeet_osa1')
    def test_2a_funktio_olemassa(self):
        try:
            from src.saannolliset_lausekkeet import on_viikonpaiva
        except Exception as e:
            self.fail(f'Ohjelmasta pitäisi löytyä funktio nimeltä on_viikonpaiva.')

    @points('12.saannolliset_lausekkeet_osa1')
    def test_2b_paluuarvon_tyyppi(self):
        try:
            from src.saannolliset_lausekkeet import on_viikonpaiva
            val = on_viikonpaiva("ma")
        except Exception as e:
            self.fail(f"Funktio antoi virheen kun sitä kutsuttiin näin:\n"  + 
            'on_viikonpaiva("ma")\n' + 
            f'{e}')
        taip = str(type(val)).replace("<class '","").replace("'>","")
        self.assertTrue(type(val) == bool, f"Funktion on_viikonpaiva pitäisi palauttaa arvo, jonka tyyppi on bool," +  
            f" nyt se palauttaa arvon {val} joka on tyyppiä {taip}\n kun sitä kutsutaan parametrilla\n" +  
            'on_viikonpaiva("ma")')
        
    @points('12.saannolliset_lausekkeet_osa1')
    def test_2c_testaa_arvoilla(self):
        from src.saannolliset_lausekkeet import on_viikonpaiva
        test_cases = "ma ti ke to pe la su am it ek ok lördag smunnuntai tu ko po my".split()
        for test_case in test_cases:
            corr = test_case in "ma ti ke to pe la su".split()
            val = on_viikonpaiva(test_case)

            self.assertEqual(val, corr, f'Funktion on_viikonpaiva pitäisi palauttaa {corr}\n' + 
                f'kun sitä kutsutaan parametrilla\n{test_case}\nnyt funktio palauttaa\n' + 
                f'{val}')

    @points('12.saannolliset_lausekkeet_osa2')
    def test_3a_funktio_olemassa(self):
        try:
            from src.saannolliset_lausekkeet import kaikki_vokaaleja
        except Exception as e:
            self.fail(f'Ohjelmasta pitäisi löytyä funktio nimeltä kaikki_vokaaleja.')

    @points('12.saannolliset_lausekkeet_osa2')
    def test_3b_paluuarvon_tyyppi(self):
        try:
            from src.saannolliset_lausekkeet import kaikki_vokaaleja
            val = kaikki_vokaaleja("aa")
        except Exception as e:
            self.fail(f"Funktio kaikki_vokaaleja antoi virheen kun sitä kutsuttiin näin:\n"  + 
            'kaikki_vokaaleja("aa")\n' + 
            f'{e}')
        taip = str(type(val)).replace("<class '","").replace("'>","")
        self.assertTrue(type(val) == bool, f"Funktion kaikki_vokaaleja pitäisi palauttaa arvo, jonka tyyppi on bool," +  
            f" nyt se palauttaa arvon {val} joka on tyyppiä {taip}\n kun sitä kutsutaan parametrilla\n" +  
            'kaikki_vokaaleja("aa")')
        
    @points('12.saannolliset_lausekkeet_osa2')
    def test_3c_testaa_arvoilla(self):
        from src.saannolliset_lausekkeet import kaikki_vokaaleja
        test_cases = "aaa eee iii oo uu yy åå ää öö aeee ioioi aioioä oyoyuaå aab aec ooooaeoip åååååbo".split()
        for test_case in test_cases:
            corr = len([x for x in test_case if x not in "aeiouyåäö"]) == 0
            val = kaikki_vokaaleja(test_case)

            self.assertEqual(val, corr, f'Funktion kaikki_vokaaleja pitäisi palauttaa {corr}\n' + 
                f'kun sitä kutsutaan parametrilla\n{test_case}\nnyt funktio palauttaa\n' + 
                f'{val}')

    @points('12.saannolliset_lausekkeet_osa3')
    def test_4a_funktio_olemassa(self):
        try:
            from src.saannolliset_lausekkeet import kellonaika
        except Exception as e:
            self.fail(f'Ohjelmasta pitäisi löytyä funktio nimeltä kellonaika.')

    @points('12.saannolliset_lausekkeet_osa3')
    def test_4b_paluuarvon_tyyppi(self):
        try:
            from src.saannolliset_lausekkeet import kellonaika
            val = kellonaika("11:11:11")
        except Exception as e:
            self.fail(f"Funktio kellonaika antoi virheen kun sitä kutsuttiin näin:\n"  + 
            'kellonaika("11:11:11")\n' + 
            f'{e}')
        taip = str(type(val)).replace("<class '","").replace("'>","")
        self.assertTrue(type(val) == bool, f"Funktion kellonaika pitäisi palauttaa arvo, jonka tyyppi on bool," +  
            f" nyt se palauttaa arvon {val} joka on tyyppiä {taip}\n kun sitä kutsutaan parametrilla\n" +  
            'kellonaika("11:11:11")')
        
    @points('12.saannolliset_lausekkeet_osa3')
    def test_4c_testaa_arvoilla(self):
        from src.saannolliset_lausekkeet import kellonaika
        test_cases = ("12:12:12 16:34:56 23:55:59 19:00:00 20:10:30 " + 
            "ab:20:20 23:15:xx 19:zz:04 " + 
            "25:13:01 39:23:20 11:66:03 17:34:87").split()
        cor = (True,True,True,True,True,False,False,False,False,False,False,False)
        for test_case,corr in zip(test_cases,cor):
            val = kellonaika(test_case)

            self.assertEqual(val, corr, f'Funktion kellonaika pitäisi palauttaa {corr}\n' + 
                f'kun sitä kutsutaan parametrilla\n{test_case}\nnyt funktio palauttaa\n' + 
                f'{val}')

    
if __name__ == '__main__':
    unittest.main()
