import unittest
from unittest.mock import patch

from tmc import points, reflect
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import os.path
import textwrap
from random import choice, randint, shuffle
from datetime import date

exercise = 'src.pelimuseo'

def f(attr: list):
    return "\n".join([str(x) for x in attr]) 

@points('10.pelimuseo')
class PelimuseoTest(unittest.TestCase):
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

    def test_1_luokat_olemassa(self):
        try:
            from src.pelimuseo import Tietokonepeli
            a = Tietokonepeli("Pacman", "Namco", 1980)
        except Exception as e:
            self.fail(f'Konstruktorikutsu Tietokonepeli("Pacman", "Namco", 1980) antoi virheen \n{e}\n' + 
            'Ethän ole muuttanut luokan Tietokonepeli määrittelyä?')

        try:
            from src.pelimuseo import Pelivarasto
            a = Pelivarasto()
        except Exception as e:
            self.fail(f'Konstruktorikutsu Pelivarasto antoi virheen \n{e}\n' + 
            'Ethän ole muuttanut luokan Pelivarasto määrittelyä?')

        try:
            from src.pelimuseo import Pelimuseo
            a = Pelimuseo()
        except Exception as e:
            self.fail(f'Konstruktorikutsu Pelimuseo() antoi virheen \n{e}\n' + 
            'Varmista, että luokka on määritelty.')

    def test_2_perinta(self):
        from src.pelimuseo import Tietokonepeli, Pelivarasto, Pelimuseo
        a = Pelimuseo()
        self.assertTrue(isinstance(a, Pelivarasto), f"Luokan Pelimuseo pitäisi " +
            'periä luokka Pelivarasto!')

    def test_3_metodi_uudelleenmaaritelty(self):
        from src.pelimuseo import Tietokonepeli, Pelivarasto, Pelimuseo
        self.assertTrue(Pelimuseo.anna_pelit is not Pelivarasto.anna_pelit, 
            f'Metodi anna_pelit pitää toteuttaa uudestaan luokassa Pelivarasto!')

    def test_4_metodi_toimii_1(self):
        test_cases = [("Commando","Capcom",1985), ("Super Mario Bros","Nintendo",1985), ("IK+", "System 3", 1987), 
            ("Elite", "Firebird", 1985), ("Star Fox", "Nintendo", 1993)]
        shuffle(test_cases)
        from src.pelimuseo import Tietokonepeli, Pelivarasto, Pelimuseo
        museo = Pelimuseo()
        for test_case in test_cases:
            museo.lisaa_peli(Tietokonepeli(test_case[0], test_case[1], test_case[2]))
        
        corr = sorted([x[0] for x in test_cases if x[2] < 1990])
        val = sorted([p.nimi for p in museo.anna_pelit()])

        test_cases_str = ", ".join([f'Tietokonepeli("{t[0]}","{t[1]}",{t[2]})' for t in test_cases]) 

        self.assertEqual(corr, val, f'Metodin anna_pelit() pitäisi palautta seuraavan nimiset pelit:\n' + 
            f'{f(corr)}\nmutta nyt se palauttaa seuraavat pelit:\n{f(val)}\nkun metodi kutsuttiin seuraavalla ' + 
            f'listalla:\n{test_cases_str}')

    def test_5_metodi_toimii_2(self):
        test_cases = [("IK+", "System 3", 1987), ("Pool of Radiance", "SSI", 1988), ("Great Giana Sisters", "Rainbow Arts", 1987), 
            ("Doom", "ID Software", 1993), ("Sim City 2000", "Maxis", 1993), ("Final Fantasy VII", "Square", 1997)]
        shuffle(test_cases)
        from src.pelimuseo import Tietokonepeli, Pelivarasto, Pelimuseo
        museo = Pelimuseo()
        for test_case in test_cases:
            museo.lisaa_peli(Tietokonepeli(test_case[0], test_case[1], test_case[2]))
        
        corr = sorted([x[0] for x in test_cases if x[2] < 1990])
        val = sorted([p.nimi for p in museo.anna_pelit()])

        test_cases_str = ", ".join([f'Tietokonepeli("{t[0]}","{t[1]}",{t[2]})' for t in test_cases]) 

        self.assertEqual(corr, val, f'Metodin anna_pelit() pitäisi palautta seuraavan nimiset pelit:\n' + 
            f'{f(corr)}\nmutta nyt se palauttaa seuraavat pelit:\n{f(val)}\nkun metodi kutsuttiin seuraavalla ' + 
            f'listalla:\n{test_cases_str}')
    


        

    
if __name__ == '__main__':
    unittest.main()
