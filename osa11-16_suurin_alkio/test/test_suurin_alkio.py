import unittest
from unittest.mock import patch

from tmc import points, reflect
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import os.path
import textwrap
import inspect, re

exercise = 'src.suurin_alkio'

@points('11.suurin_alkio')
class SuurinAlkioTest(unittest.TestCase):
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
            from src.suurin_alkio import suurin_alkio
        except Exception as e:
            self.fail(f'Ohjelmasta pitäisi löytyä funktio nimeltä suurin_alkio.')

    def test_2_paluuarvon_tyyppi(self):
        try:
            from src.suurin_alkio import suurin_alkio, Alkio
            val = suurin_alkio(Alkio(1))
        except Exception as e:
            self.assertTrue(False, f"Funktio antoi virheen kun sitä kutsuttiin näin:" + 
                f'\nsuurin_alkio(Alkio(1))\n{e}')
        taip = str(type(val)).replace("<class '","").replace("'>","")
        self.assertTrue(type(val) == int, f"Funktion suurin_alkio pitäisi palauttaa arvo, jonka tyyppi on int," +  
            f" nyt se palauttaa arvon {val} joka on tyyppiä {taip}\n kun sitä kutsutaan näin\n" +  
            'suurin_alkio(Alkio(1))')
        

    def test_3_onko_rekursiivinen(self):
        from src.suurin_alkio import suurin_alkio, Alkio
        self.assertTrue(reflect.test_recursion(suurin_alkio, Alkio(1, Alkio(2))), 
            f'"Funkton suurin_alkio pitäisi kutsua itseään rekursiivisesti.\n' + 
            f'Nyt kutsu suurin_alkio, Alkio(1, Alkio(2))) ei johda uusiin funktion suurin_alkio kutsuihin.')

    def test_4_testaa_arvoilla1(self):
        from src.suurin_alkio import suurin_alkio, Alkio
        juuri = Alkio(3)
        vasen = Alkio(5,Alkio(7),Alkio(10,Alkio(3),Alkio(13)))
        oikea = Alkio(6,None, Alkio(11))
        test_case = "3, 5, 7, 10, 3, 13, 6, ja 11"
        juuri.vasen_lapsi = vasen
        juuri.oikea_lapsi = oikea

        val = suurin_alkio(juuri)
        corr = 13

        self.assertEqual(val, corr, f'Funktion pitäisi palauttaa arvo\n{corr}\n' + 
            f'kun puussa on arvot\n{test_case}\nnyt funktio palauttaa\n' + 
            f'{val}')

    def test_4_testaa_arvoilla2(self):
        from src.suurin_alkio import suurin_alkio, Alkio
        juuri = Alkio(13)
        vasen = Alkio(15,Alkio(17, Alkio(24)),Alkio(24,Alkio(14),Alkio(9)))
        oikea = Alkio(8,Alkio(29))
        test_case = "13, 15, 17, 24, 14, 9, 8 ja 29"
        juuri.vasen_lapsi = vasen
        juuri.oikea_lapsi = oikea

        val = suurin_alkio(juuri)
        corr = 29

        self.assertEqual(val, corr, f'Funktion pitäisi palauttaa arvo\n{corr}\n' + 
            f'kun puussa on arvot\n{test_case}\nnyt funktio palauttaa\n' + 
            f'{val}')


        
if __name__ == '__main__':
    unittest.main()
