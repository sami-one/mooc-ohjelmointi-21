import unittest
from unittest.mock import patch

from tmc import points, reflect
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import os.path
import textwrap
import inspect, re
import types
from random import choice, randint, shuffle

exercise = 'src.satunnaiset_sanat'

def source_rows(funktio: callable):
    src = inspect.getsource(funktio)
    lines = [line.strip() for line in re.split('\\n|;', src) 
        if len(line.strip()) > 0 and not line.strip().startswith("#")]
    return len(lines)

@points('12.satunnaiset_sanat')
class SatunnaisetSanatTest(unittest.TestCase):
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
            from src.satunnaiset_sanat import sanageneraattori
        except Exception as e:
            self.fail(f'Ohjelmasta pitäisi löytyä funktio nimeltä sanageneraattori.')

    def test_2_paluuarvon_tyyppi(self):
        try:
            from src.satunnaiset_sanat import sanageneraattori
            val = sanageneraattori("abc",2,1)
        except Exception as e:
            self.fail(f"Funktio antoi virheen kun sitä kutsuttiin näin:\n"  + 
            'sanageneraattori("abc",2,1)\n' + 
            f'{e}')
        taip = str(type(val)).replace("<class '","").replace("'>","")
        self.assertTrue(type(val) is types.GeneratorType, f"Funktion sanageneraattori pitäisi palauttaa generaattori," +  
            f" nyt se palauttaa arvon {val} joka on tyyppiä {taip}\n kun sitä kutsutaan näin\n" +  
            'sanageneraattori("abc",2,1)')
        

    def test_3_testaa_sanojen_maara(self):
        from src.satunnaiset_sanat import sanageneraattori
    
        test_cases = [("abc",2,3), ("ABCabcDEF",5,10), ("XYZ123456", 4, 7)]
        for test_case in test_cases:
            func = f"satunnaiset_sanat{test_case}"
            corr = test_case[2]
            gen = sanageneraattori(test_case[0], test_case[1], test_case[2])
            val = [i for i in gen]

            self.assertEqual(len(val), corr, f'Generaattorin pitäisi palauttaa {corr} arvoa\n' + 
                f'kun se on alustettu näin:\ngen = {func}\n' +
                f'nyt se palauttaa arvot\n' + 
                f'{val}')

    def test_4_testaa_eri_sanoja(self):
        from src.satunnaiset_sanat import sanageneraattori
    
        test_cases = [("abcdefghijklmnopqrstuvwxyz",3,2), ("ABCabcDEFdefGHIghi",5,3), ("XYZ123456xyz789", 4, 4)]
        for test_case in test_cases:
            func = f"satunnaiset_sanat{test_case}"
            gen = sanageneraattori(test_case[0], test_case[1], test_case[2])
            val = [i for i in gen]
            corr = len(set(val)) != 1

            self.assertTrue(corr, f'Generaattorin pitäisi palauttaa {corr} erilaista arvoa\n' + 
                f'kun se on alustettu näin:\ngen = {func}\n' +
                f'nyt se palauttaa arvot\n' + 
                f'{val}')

    def test_5_testaa_oikeat_kirjaimet(self):
        from src.satunnaiset_sanat import sanageneraattori
    
        test_cases = [("abcdefg",3,2), ("ABCabcDEFdef",5,3), ("XYZ1234", 4, 4)]
        for test_case in test_cases:
            func = f"satunnaiset_sanat{test_case}"
            gen = sanageneraattori(test_case[0], test_case[1], test_case[2])
            val = [i for i in gen]
            c = [[x for x in s if x not in test_case[0]] for s in val]
            corr = reduce(lambda x,y : True and len(y) == 0, c)

            self.assertTrue(corr, f'Generaattorin palauttamien sanojen pitäisi ' + 
                f'sisältää kirjaimia vain jonosta {test_case[0]}\n' +
                f'kun se on alustettu näin:\ngen = {func}\n' +
                f'nyt se palauttaa arvot\n' + 
                f'{val}')



    
if __name__ == '__main__':
    unittest.main()
