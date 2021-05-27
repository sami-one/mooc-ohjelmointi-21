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

exercise = 'src.palloilijat'

def source_rows(funktio: callable):
    src = inspect.getsource(funktio)
    lines = [line.strip() for line in re.split('\\n|;', src) 
        if len(line.strip()) > 0 and not line.strip().startswith("#")]
    return len(lines)


class PalloilijatTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=[AssertionError("Syötteen pyytämistä ei odotettu")]):
           cls.module = load_module(exercise, 'fi')
    
    @points('12.palloilijat_osa1')
    def test_0a_paaohjelma_kunnossa(self):
        ok, line = check_source(self.module)
        message = """Funktioita testaava koodi tulee sijoittaa lohkon
if __name__ == "__main__":
sisälle. Seuraava rivi tulee siirtää:
"""
        self.assertTrue(ok, message+line)
    
    @points('12.palloilijat_osa1')
    def test1_luokka_olemassa(self):
        try:
            from src.palloilijat import Palloilija 
        except Exception as e:
            self.fail('Ohjelmasta pitäisi löytyä luokka Palloilija - ethän ole muuttanut luokan toteutusta?')
    
    @points('12.palloilijat_osa1')
    def test_2a_funktio_olemassa(self):
        try:
            from src.palloilijat import eniten_maaleja
        except Exception as e:
            self.fail(f'Ohjelmasta pitäisi löytyä funktio nimeltä eniten_maaleja.')

    @points('12.palloilijat_osa1')
    def test_2b_paluuarvon_tyyppi(self):
        try:
            from src.palloilijat import eniten_maaleja, Palloilija
            val = eniten_maaleja([Palloilija("a",2,2,2,2), Palloilija("b",1,1,1,1)])
        except Exception as e:
            self.fail(f"Funktio antoi virheen kun sitä kutsuttiin näin:\n"  + 
            'eniten_maaleja([Palloilija("a",2,2,2,2), Palloilija("b",1,1,1,1)])\n' + 
            f'{e}')
        taip = str(type(val)).replace("<class '","").replace("'>","")
        self.assertTrue(type(val) == str, f"Funktion eniten_maaleja pitäisi palauttaa arvo, jonka tyyppi on str," +  
            f" nyt se palauttaa arvon {val} joka on tyyppiä {taip}\n kun sitä kutsutaan parametrilla\n" +  
            'eniten_maaleja([Palloilija("a",2,2,2,2), Palloilija("b",1,1,1,1)])')
        
    @points('12.palloilijat_osa1')
    def test_2c_testaa_arvoilla1(self):
        from src.palloilijat import eniten_maaleja, Palloilija
    
        tdata = [("Pekka",4,12,6,900), ("Armas",6,14,3,885), ("Jarppi",9,19,2,840), ("Kimmo", 3,11,9,1034)]
        test_case = [Palloilija(tc[0],tc[1],tc[2],tc[3],tc[4]) for tc in tdata]
        shuffle(test_case)
        test_case_2 = test_case[:]
        corr = max(tdata, key=lambda t:t[2])[0]
        val = eniten_maaleja(test_case)

        self.assertEqual(val, corr, f'Funktion eniten_maaleja pitäisi palauttaa merkkijono\n{corr}\n' + 
            f'kun sitä kutsutaan parametrilla\n{test_case}\nnyt funktio palauttaa\n' + 
            f'{val}')

        self.assertEqual(test_case, test_case_2, f"Funktio eniten_maaleja ei saa muuttaa alkuperäistä listaa!\n" + 
            f'Lista ennen kutsua oli\n{test_case_2}\nja kutsun jälkeen se on\n{test_case}.')

    @points('12.palloilijat_osa1')
    def test_2d_testaa_arvoilla2(self):
        from src.palloilijat import eniten_maaleja, Palloilija
    
        tdata = [("Pekka",4,1,6,900), ("Armas",6,4,3,885), ("Jarppi",9,9,2,840), ("Kimmo", 3,13,9,1034)]
        test_case = [Palloilija(tc[0],tc[1],tc[2],tc[3],tc[4]) for tc in tdata]
        shuffle(test_case)
        test_case_2 = test_case[:]
        corr = max(tdata, key=lambda t:t[2])[0]
        val = eniten_maaleja(test_case)

        self.assertEqual(val, corr, f'Funktion eniten_maaleja pitäisi palauttaa merkkijono\n{corr}\n' + 
            f'kun sitä kutsutaan parametrilla\n{test_case}\nnyt funktio palauttaa\n' + 
            f'{val}')

        self.assertEqual(test_case, test_case_2, f"Funktio eniten_maaleja ei saa muuttaa alkuperäistä listaa!\n" + 
            f'Lista ennen kutsua oli\n{test_case_2}\nja kutsun jälkeen se on\n{test_case}.')

    @points('12.palloilijat_osa2')
    def test_3a_funktio_olemassa(self):
        try:
            from src.palloilijat import eniten_pisteita
        except Exception as e:
            self.fail(f'Ohjelmasta pitäisi löytyä funktio nimeltä eniten_pisteita.')

    @points('12.palloilijat_osa2')
    def test_3b_paluuarvon_tyyppi(self):
        try:
            from src.palloilijat import eniten_pisteita, Palloilija
            val = eniten_pisteita([Palloilija("a",2,2,2,2), Palloilija("b",1,1,1,1)])
        except Exception as e:
            self.fail(f"Funktio antoi virheen kun sitä kutsuttiin näin:\n"  + 
            'eniten_pisteita([Palloilija("a",2,2,2,2), Palloilija("b",1,1,1,1)])\n' + 
            f'{e}')
        taip = str(type(val)).replace("<class '","").replace("'>","")
        self.assertTrue(type(val) == tuple, f"Funktion eniten_pisteita pitäisi palauttaa arvo, jonka tyyppi on tuple," +  
            f" nyt se palauttaa arvon {val} joka on tyyppiä {taip}\n kun sitä kutsutaan parametrilla\n" +  
            'eniten_pisteita([Palloilija("a",2,2,2,2), Palloilija("b",1,1,1,1)])')
        
    @points('12.palloilijat_osa2')
    def test_3c_testaa_arvoilla1(self):
        from src.palloilijat import eniten_pisteita, Palloilija
    
        tdata = [("Pekka",4,12,6,900), ("Armas",6,14,11,885), ("Jarppi",9,19,2,840), ("Kimmo", 3,11,9,1034)]
        test_case = [Palloilija(tc[0],tc[1],tc[2],tc[3],tc[4]) for tc in tdata]
        shuffle(test_case)
        test_case_2 = test_case[:]
        c = max(tdata, key=lambda t:t[2]+t[3])
        corr = (c[0],c[1])
        val = eniten_pisteita(test_case)

        self.assertEqual(val, corr, f'Funktion eniten_pisteita pitäisi palauttaa merkkijono\n{corr}\n' + 
            f'kun sitä kutsutaan parametrilla\n{test_case}\nnyt funktio palauttaa\n' + 
            f'{val}')

        self.assertEqual(test_case, test_case_2, f"Funktio eniten_pisteita ei saa muuttaa alkuperäistä listaa!\n" + 
            f'Lista ennen kutsua oli\n{test_case_2}\nja kutsun jälkeen se on\n{test_case}.')

    @points('12.palloilijat_osa2')
    def test_3d_testaa_arvoilla2(self):
        from src.palloilijat import eniten_pisteita, Palloilija
    
        tdata = [("Pekka",4,1,3,900), ("Armas",6,5,5,885), ("Jarppi",9,0,2,840), ("Kimmo", 3,9,0,1034)]
        test_case = [Palloilija(tc[0],tc[1],tc[2],tc[3],tc[4]) for tc in tdata]
        shuffle(test_case)
        test_case_2 = test_case[:]
        c = max(tdata, key=lambda t:t[2]+t[3])
        corr = (c[0],c[1])
        val = eniten_pisteita(test_case)

        self.assertEqual(val, corr, f'Funktion eniten_pisteita pitäisi palauttaa merkkijono\n{corr}\n' + 
            f'kun sitä kutsutaan parametrilla\n{test_case}\nnyt funktio palauttaa\n' + 
            f'{val}')

        self.assertEqual(test_case, test_case_2, f"Funktio eniten_pisteita ei saa muuttaa alkuperäistä listaa!\n" + 
            f'Lista ennen kutsua oli\n{test_case_2}\nja kutsun jälkeen se on\n{test_case}.')

    @points('12.palloilijat_osa3')
    def test_4a_funktio_olemassa(self):
        try:
            from src.palloilijat import vahiten_minuutteja
        except Exception as e:
            self.fail(f'Ohjelmasta pitäisi löytyä funktio nimeltä vahiten_minuutteja.')

    @points('12.palloilijat_osa3')
    def test_4b_paluuarvon_tyyppi(self):
        try:
            from src.palloilijat import vahiten_minuutteja, Palloilija
            val = vahiten_minuutteja([Palloilija("a",2,2,2,2), Palloilija("b",1,1,1,1)])
        except Exception as e:
            self.fail(f"Funktio antoi virheen kun sitä kutsuttiin näin:\n"  + 
            'vahiten_minuutteja([Palloilija("a",2,2,2,2), Palloilija("b",1,1,1,1)])\n' + 
            f'{e}')
        taip = str(type(val)).replace("<class '","").replace("'>","")
        self.assertTrue(type(val) == Palloilija, f"Funktion eniten_pisteita pitäisi palauttaa arvo, jonka tyyppi on Palloilija," +  
            f" nyt se palauttaa arvon {val} joka on tyyppiä {taip}\n kun sitä kutsutaan parametrilla\n" +  
            'vahiten_minuutteja([Palloilija("a",2,2,2,2), Palloilija("b",1,1,1,1)])')
        
    @points('12.palloilijat_osa3')
    def test_4c_testaa_arvoilla1(self):
        from src.palloilijat import vahiten_minuutteja, Palloilija
    
        tdata = [("Pekka",4,12,6,900), ("Armas",6,14,11,885), ("Jarppi",9,19,2,840), ("Kimmo", 3,11,9,1034)]
        test_case = [Palloilija(tc[0],tc[1],tc[2],tc[3],tc[4]) for tc in tdata]
        shuffle(test_case)
        test_case_2 = test_case[:]
        corr = min(test_case, key=lambda p:p.minuutit)
        val = vahiten_minuutteja(test_case)

        self.assertEqual(val, corr, f'Funktion vahiten_minuutteja pitäisi palauttaa Pelaaja\n{corr}\n' + 
            f'kun sitä kutsutaan parametrilla\n{test_case}\nnyt funktio palauttaa\n' + 
            f'{val}')

        self.assertEqual(test_case, test_case_2, f"Funktio vahiten_minuutteja ei saa muuttaa alkuperäistä listaa!\n" + 
            f'Lista ennen kutsua oli\n{test_case_2}\nja kutsun jälkeen se on\n{test_case}.')

    @points('12.palloilijat_osa3')
    def test_4d_testaa_arvoilla2(self):
        from src.palloilijat import vahiten_minuutteja, Palloilija
    
        tdata = [("Pekka",4,12,6,90), ("Armas",6,14,11,88), ("Jarppi",9,19,2,84), ("Kimmo", 3,11,9,134)]
        test_case = [Palloilija(tc[0],tc[1],tc[2],tc[3],tc[4]) for tc in tdata]
        shuffle(test_case)
        test_case_2 = test_case[:]
        corr = min(test_case, key=lambda p:p.minuutit)
        val = vahiten_minuutteja(test_case)

        self.assertEqual(val, corr, f'Funktion vahiten_minuutteja pitäisi palauttaa Pelaaja\n{corr}\n' + 
            f'kun sitä kutsutaan parametrilla\n{test_case}\nnyt funktio palauttaa\n' + 
            f'{val}')

        self.assertEqual(test_case, test_case_2, f"Funktio vahiten_minuutteja ei saa muuttaa alkuperäistä listaa!\n" + 
            f'Lista ennen kutsua oli\n{test_case_2}\nja kutsun jälkeen se on\n{test_case}.')

 
    
if __name__ == '__main__':
    unittest.main()
