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

exercise = 'src.halvempien_hintaero'

def source_rows(funktio: callable):
    src = inspect.getsource(funktio)
    lines = [line.strip() for line in re.split('\\n|;', src) 
        if len(line.strip()) > 0 and not line.strip().startswith("#")]
    return len(lines)

def f(tuplet: list):
    return "\n".join(f'{asunto[0].kuvaus}, {asunto[0].nelioita} neliötä, neliöhinta {asunto[0].neliohinta}, hintaero {asunto[1]}' for asunto in tuplet)

def f2(asunnot: list):
    return "\n".join(f'{asunto.kuvaus}, {asunto.nelioita} neliötä, neliöhinta {asunto.neliohinta}' for asunto in asunnot)

@points('11.halvempien_hintaero')
class HalvempienHintaeroTest(unittest.TestCase):
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
            from src.halvempien_hintaero import halvemmat
        except Exception as e:
            self.fail(f'Ohjelmasta pitäisi löytyä funktio nimeltä halvemmat.')

    def test_1b_luokka_olemassa(self):
        try:
            from src.halvempien_hintaero import Asunto
        except Exception as e:
            self.fail(f'Luokkaa Asunto ei löydy - ethän ole muuttanut sen kuvausta?')

    def test_2_paluuarvon_tyyppi(self):
        try:
            from src.halvempien_hintaero import halvemmat, Asunto
            val = halvemmat([Asunto(1,1,1,"a")], Asunto(1,1,2,"b"))
        except Exception as e:
            self.assertTrue(False, f"Funktio halvemmat antoi virheen kun sitä kutsuttiin näin:" + 
                f'\nhalvemmat([Asunto(1,1,1,"a")], Asunto(1,1,2,"b"))\n{e}')
        taip = str(type(val)).replace("<class '","").replace("'>","")
        self.assertTrue(type(val) == list, f"Funktion halvemmat pitäisi palauttaa arvo, jonka tyyppi on list," +  
            f" nyt se palauttaa arvon {val} joka on tyyppiä {taip}\n kun sitä kutsutaan näin\n" +  
            'halvemmat([Asunto(1,1,1,"a")], Asunto(1,1,2,"b"))')

    def test_2b_paluuarvon_tyyppi2(self):
        from src.halvempien_hintaero import halvemmat, Asunto
        val = halvemmat([Asunto(1,1,1,"a")], Asunto(1,1,2,"b"))
        
        self.assertTrue(len(val) > 0, f"Funktio halvemmat palautti tyhjän listan kun sitä kutsuttiin näin:" + 
            f'\nhalvemmat([Asunto(1,1,1,"a")], Asunto(1,1,2,"b"))')
        
        taip = str(type(val[0])).replace("<class '","").replace("'>","")
        self.assertTrue(type(val[0]) == tuple, f"Funktion halvemmat pitäisi palauttaa alkoita, joiden tyyppi on tuple," +  
            f" nyt se palauttaa arvon {val[0]} joka on tyyppiä {taip}\n kun sitä kutsutaan näin\n" +  
            'halvemmat([Asunto(1,1,1,"a")], Asunto(1,1,2,"b"))')

        taip = str(type(val[0][0])).replace("<class '","").replace("'>","")
        self.assertTrue(type(val[0][0]) == Asunto, f"Funktion halvemmat pitäisi palauttaa lista tupleja, " + 
            f"joiden ensimmäinen alkio on Asunto-tyyppinen.\n" +  
            f"Nyt se palauttaa arvon {val[0][0]} joka on tyyppiä {taip}\n kun sitä kutsutaan näin\n" +  
            'halvemmat([Asunto(1,1,1,"a")], Asunto(1,1,2,"b"))')
        

    def test_3_funktion_pituus(self):
        from src.halvempien_hintaero import halvemmat
        lines = source_rows(halvemmat)
        max_lines = 2
        self.assertTrue(lines <= max_lines, f'Funktiossa halvemmat saa tässä tehtävässä olla korkeintaan'+ 
            f' {max_lines} riviä.\n' +
            f'Nyt funktiossa on yhteensä {lines} riviä (poislukien tyhjät rivit ja kommentit.')

    def test_4_testaa_arvoilla1(self):
        from src.halvempien_hintaero import halvemmat, Asunto
        a1 = Asunto(1, 16, 5500, "Eira yksiö")
        a2 = Asunto(2, 38, 4200, "Kallio kaksio")
        a3 = Asunto(3, 78, 2500, "Jakomäki kolmio")
        a4 = Asunto(6, 215, 500, "Suomussalmi omakotitalo")
        a5 = Asunto(4, 105, 1700, "Kerava 4h ja keittiö")
        a6 = Asunto(25, 1200, 2500, "Haikon kartano")
        test_case = [a1, a2, a3, a4, a5, a6]

        raja = a3

        val = halvemmat(test_case, raja)
        corr = [(a1, 107000), (a2, 35400), (a4, 87500), (a5, 16500)]

        self.assertEqual(val, corr, f'Funktion pitäisi palauttaa seuraavat asunnot\n{f(corr)}\n' + 
            f'kun sille annettin parametriksi seuraavat asunnot:\n' + 
            f'{f2(test_case)}\n' +
            f'ja verrattava asunto oli\n' +
            f'{raja}\n'
            f'nyt funktio palauttaa seuraavat asunnot\n' + 
            f'{f(val)}')

    def test_5_testaa_arvoilla2(self):
        from src.halvempien_hintaero import halvemmat, Asunto
        a1 = Asunto(1, 16, 5500, "Eira yksiö")
        a2 = Asunto(2, 38, 4200, "Kallio kaksio")
        a3 = Asunto(3, 78, 2500, "Jakomäki kolmio")
        a4 = Asunto(6, 215, 500, "Suomussalmi omakotitalo")
        a5 = Asunto(4, 105, 1700, "Kerava 4h ja keittiö")
        a6 = Asunto(25, 1200, 2500, "Haikon kartano")
        test_case = [a1, a2, a3, a4, a5, a6]

        raja = a4

        val = halvemmat(test_case, raja)
        corr = [(a1, 107500 - 88000)]

        self.assertEqual(val, corr, f'Funktion pitäisi palauttaa seuraavat asunnot\n{f(corr)}\n' + 
            f'kun sille annettin parametriksi seuraavat asunnot:\n' + 
            f'{f2(test_case)}\n' +
            f'ja verrattava asunto oli\n' +
            f'{raja}\n'
            f'nyt funktio palauttaa seuraavat asunnot\n' + 
            f'{f(val)}')


 
if __name__ == '__main__':
    unittest.main()
