import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import os.path
import textwrap
from random import choice, randint

exercise = 'src.rivien_summat'
function = "rivien_summat"

def get_corr(m):
    return [r + [sum(r)] for r in m]
        

@points('8.rivien_summat')
class RivienSummatTest(unittest.TestCase):
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

    def test1_funktio_olemassa(self):
        try:
            from src.rivien_summat import rivien_summat
        except:
            self.assertTrue(False, "Ohjelmastasi pitäisi löytyä funktio nimeltä rivien_summat(matriisi: list)")

    def test2_palautusarvon_tyyppi(self):
        try:
            from src.rivien_summat import rivien_summat
            val = rivien_summat([[1,1],[2,2]])
            taip = str(type(val)).replace("<class '","").replace("'>","")
            self.assertTrue(val == None, f"Funktion rivien_summat ei pitäisi palauttaa arvoa," +  
                f" nyt se palauttaa arvon {val} joka on tyyppiä {taip}\n kun sitä kutsutaan parametrilla \n[[1,1],[2,2]]")
        except Exception as e:
            self.assertTrue(False, f"Funktio antoi virheen kun sitä kutsuttiin parametrin arvolla [[1,1],[2,2]]:\n{e}")


    def test3_testaa_arvot(self):
        test_cases = ([[1,1],[2,2]], [[2]*3,[4]*3,[6]*3], [[1,2,3,4],[2,3,4,5],[3,4,5,6]], [[5,6],[4,1],[10,20],[6,9],[11,22]],
                      [[1,3,5,7,9],[2,4,6,8,10],[-1,-3,-5,-7,-9]])
        for test_case in test_cases:
            with patch('builtins.input', side_effect=[AssertionError("Syötteen pyytämistä ei odotettu")]):
                reload_module(self.module)
                rivien_summat = load(exercise, function, 'fi')

                test_case_2 = [m[:] for m in test_case[:]]
                rivien_summat(test_case)
                
                corr = get_corr(test_case_2)

                self.assertEqual(test_case, corr, f"Funktion suorituksen jälkeen matriisin pitäisi olla \n{corr}\nmutta se on \n{test_case}\nkun parametri on\n{test_case_2}")

    

if __name__ == '__main__':
    unittest.main()
