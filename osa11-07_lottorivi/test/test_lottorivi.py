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

exercise = 'src.lottorivi'

def source_rows(funktio: callable):
    src = inspect.getsource(funktio)
    lines = [line.strip() for line in re.split('\\n|;', src) 
        if len(line.strip()) > 0 and not line.strip().startswith("#")]
    return len(lines)


class LottorivitTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=[AssertionError("Syötteen pyytämistä ei odotettu")]):
           cls.module = load_module(exercise, 'fi')

    @points('11.lottorivi_osa1')
    def test_0a_paaohjelma_kunnossa(self):
        ok, line = check_source(self.module)
        message = """Funktioita testaava koodi tulee sijoittaa lohkon
if __name__ == "__main__":
sisälle. Seuraava rivi tulee siirtää:
"""
        self.assertTrue(ok, message+line)
    
    @points('11.lottorivi_osa1')
    def test_1_luokka_olemassa(self):
        try:
            from src.lottorivi import Lottorivi
        except Exception as e:
            self.fail(f'Tarkista, että luokka Lottorivi on olemassa!')

    @points('11.lottorivi_osa1')  
    def test_2_olion_luonti(self):
        try:
            from src.lottorivi import Lottorivi
            a = Lottorivi(1,[1,2,3,4,5,6,7])
        except Exception as e:
            self.fail(f'Konstruktorikutsu Lottorivi(1,[1,2,3,4,5,6,7]) antoi virheen \n{e}\n' + 
            'Tarkista, että luokasta voi muodostaa olion.')
    
    @points('11.lottorivi_osa1')
    def test_3a_metodi_osumien_maara(self):
        try:
            from src.lottorivi import Lottorivi
            rivi = Lottorivi(1,[1,2,3,4,5,6,7])
            n = rivi.osumien_maara([1,2,3,4,5,6,7])
        except Exception as e:
            self.fail(f'Metodi osumien_maara antoi virheen, kun sitä kutsuttiin seuraavasti:\n' + 
                f'rivi = Lottorivi(1,[1,2,3,4,5,6,7])\n' + 
                f'n = rivi.osumien_maara([1,2,3,4,5,6,7])\n' + 
                f'Virhe oli:\n{e}')

    @points('11.lottorivi_osa1')
    def test_3b_osumien_maara_paluuarvon_tyyppi(self):
        try:
            from src.lottorivi import Lottorivi
            rivi = Lottorivi(1,[1,2,3,4,5,6,7])
            val = rivi.osumien_maara([1,2,3,4,5,6,7])
        except Exception as e:
            self.fail(f'Metodi osumien_maara antoi virheen, kun sitä kutsuttiin seuraavasti:\n' + 
                f'rivi = Lottorivi(1,[1,2,3,4,5,6,7])\n' + 
                f'n = rivi.osumien_maara([1,2,3,4,5,6,7])\n' + 
                f'Virhe oli:\n{e}')
        taip = str(type(val)).replace("<class '","").replace("'>","")
        self.assertTrue(type(val) == int, f"Metodin osumien_maara pitäisi palauttaa arvo, jonka tyyppi on int," +  
            f" nyt se palauttaa arvon {val} joka on tyyppiä {taip}\n kun sitä kutsuttiin näin:\n" +  
            f'rivi = Lottorivi(1,[1,2,3,4,5,6,7])\n' + 
            f'n = rivi.osumien_maara([1,2,3,4,5,6,7])\n')
        
    @points('11.lottorivi_osa1')
    def test_4_metodin_osumien_maara_pituus(self):
        from src.lottorivi import Lottorivi
        lines = source_rows(Lottorivi.osumien_maara)
        max_lines = 2
        self.assertTrue(lines <= max_lines, f'Metodissa osumien_maara saa tässä tehtävässä olla korkeintaan'+ 
            f' {max_lines} riviä.\n' +
            f'Nyt metodissa on yhteensä {lines} riviä (poislukien tyhjät rivit ja kommentit.')

    @points('11.lottorivi_osa1')
    def test_5a_testaa_osumien_maara_arvoilla1(self):
        test_case = [1,2,5,6,9,10,11]
        correct = [1,3,5,7,9,11,13]
        corr = 4
        from src.lottorivi import Lottorivi
        rivi = Lottorivi(1, correct)
        val = rivi.osumien_maara(test_case)

        self.assertEqual(val, corr, f'Metodin osumien_maara pitäisi palauttaa {corr}\n' + 
            f'kun sitä kutsutaan seuraavasti:\n' +
            f'rivi = Lottorivi({correct})\n' + 
            f'n = rivi.osumien_maara({test_case})\n' 
            f'nyt metodi palauttaav{val}')

    @points('11.lottorivi_osa1')
    def test_5b_testaa_osumien_maara_arvoilla2(self):
        test_case = [5,10,15,20,25,30,35]
        correct = [6,7,10,11,12,13,15]
        corr = 2
        from src.lottorivi import Lottorivi
        rivi = Lottorivi(1, correct)
        val = rivi.osumien_maara(test_case)

        self.assertEqual(val, corr, f'Metodin osumien_maara pitäisi palauttaa {corr}\n' + 
            f'kun sitä kutsutaan seuraavasti:\n' +
            f'rivi = Lottorivi({correct})\n' + 
            f'n = rivi.osumien_maara({test_case})\n' 
            f'nyt metodi palauttaav{val}')

    @points('11.lottorivi_osa2')
    def test_6_metodi_osumat_paikoillaan(self):
        try:
            from src.lottorivi import Lottorivi
            rivi = Lottorivi(1,[1,2,3,4,5,6,7])
            n = rivi.osumat_paikoillaan([1,2,3,4,5,6,7])
        except Exception as e:
            self.fail(f'Metodi osumat_paikoillaan( antoi virheen, kun sitä kutsuttiin seuraavasti:\n' + 
                f'rivi = Lottorivi(1,[1,2,3,4,5,6,7])\n' + 
                f'n = rivi.osumat_paikoillaan(([1,2,3,4,5,6,7])\n' + 
                f'Virhe oli:\n{e}')

    @points('11.lottorivi_osa2')
    def test_7_osumat_paikoillaan_paluuarvon_tyyppi(self):
        try:
            from src.lottorivi import Lottorivi
            rivi = Lottorivi(1,[1,2,3,4,5,6,7])
            val = rivi.osumat_paikoillaan([1,2,3,4,5,6,7])
        except Exception as e:
            self.fail(f'Metodi osumat_paikoillaan antoi virheen, kun sitä kutsuttiin seuraavasti:\n' + 
                f'rivi = Lottorivi(1,[1,2,3,4,5,6,7])\n' + 
                f'n = rivi.osumat_paikoillaan([1,2,3,4,5,6,7])\n' + 
                f'Virhe oli:\n{e}')
        taip = str(type(val)).replace("<class '","").replace("'>","")
        self.assertTrue(type(val) == list, f"Metodin osumat_paikoillaan pitäisi palauttaa arvo, jonka tyyppi on list," +  
            f" nyt se palauttaa arvon {val} joka on tyyppiä {taip}\n kun sitä kutsuttiin näin:\n" +  
            f'rivi = Lottorivi(1,[1,2,3,4,5,6,7])\n' + 
            f'n = rivi.osumat_paikoillaan([1,2,3,4,5,6,7])\n')
        
    @points('11.lottorivi_osa2')
    def test_8_metodin_osumat_paikoillaan_pituus(self):
        from src.lottorivi import Lottorivi
        lines = source_rows(Lottorivi.osumat_paikoillaan)
        max_lines = 2
        self.assertTrue(lines <= max_lines, f'Metodissa osumat_paikoillaan saa tässä tehtävässä olla korkeintaan'+ 
            f' {max_lines} riviä.\n' +
            f'Nyt metodissa on yhteensä {lines} riviä (poislukien tyhjät rivit ja kommentit.')

    @points('11.lottorivi_osa2')
    def test_9a_testaa_osumat_paikoillaan_arvoilla1(self):
        test_case = [1,2,5,6,9,10,11]
        correct = [1,3,5,7,9,11,13]
        corr = [1,-1,5,-1,9,-1,11]
        from src.lottorivi import Lottorivi
        rivi = Lottorivi(1, correct)
        val = rivi.osumat_paikoillaan(test_case[:])

        self.assertEqual(val, corr, f'Metodin osumat_paikoillaan pitäisi palauttaa\n{corr}\n' + 
            f'kun sitä kutsutaan seuraavasti:\n' +
            f'rivi = Lottorivi({correct})\n' + 
            f'n = rivi.osumat_paikoillaan({test_case})\n' 
            f'nyt metodi palauttaa\n{val}')

    @points('11.lottorivi_osa2')
    def test_9b_testaa_osumat_paikoillaan_arvoilla2(self):
        test_case = [4,6,8,10,30,32,34]
        correct = [5,6,7,8,32,33,34]
        corr = [-1,6,8,-1,-1,32,34]
        from src.lottorivi import Lottorivi
        rivi = Lottorivi(1, correct)
        val = rivi.osumat_paikoillaan(test_case[:])

        self.assertEqual(val, corr, f'Metodin osumat_paikoillaan pitäisi palauttaa\n{corr}\n' + 
            f'kun sitä kutsutaan seuraavasti:\n' +
            f'rivi = Lottorivi({correct})\n' + 
            f'n = rivi.osumat_paikoillaan({test_case})\n' 
            f'nyt metodi palauttaa\n{val}')
    
if __name__ == '__main__':
    unittest.main()
