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

exercise = 'src.listaan_lukuja'

@points('11.listaan_lukuja')
class ListaanLukujaTest(unittest.TestCase):
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
            from src.listaan_lukuja import listaan_lukuja
        except Exception as e:
            self.fail(f'Ohjelmasta pitäisi löytyä funktio nimeltä listaan_lukuja.')

    def test_2_paluuarvon_tyyppi(self):
        try:
            from src.listaan_lukuja import listaan_lukuja
            val = listaan_lukuja([1,2,3,4])
        except Exception as e:
            self.assertTrue(False, f"Funktio antoi virheen kun sitä kutsuttiin näin:" + 
                f'\nlistaan_lukuja([1,2,3,4])\n{e}')
        taip = str(type(val)).replace("<class '","").replace("'>","")
        self.assertTrue(val == None, f"Funktion listaan_lukuja ei pitäisi palauttaa mitään arvoa," +  
            f" nyt se palauttaa arvon {val} joka on tyyppiä {taip}\n kun sitä kutsutaan näin\n" +  
            'listaan_lukuja([1,2,3,4])')
        

    def test_3_onko_rekursiivinen(self):
        from src.listaan_lukuja import listaan_lukuja
        self.assertTrue(reflect.test_recursion(listaan_lukuja, [1,2]), 
            f'"Funkton listaan_lukuja pitäisi kutsua itseään rekursiivisesti.\n' + 
            f'Nyt kutsu listaan_lukuja([1,2]) ei johda uusiin funktion listaan_lukuja kutsuihin.')

    def test_4_testaa_arvoilla1(self):
        test_case = [1,2,3]
        val= test_case[:]
        corr = [1,2,3,4,5]

        from src.listaan_lukuja import listaan_lukuja
        listaan_lukuja(val)

        self.assertEqual(val, corr, f'Listan sisällön pitäisi olla \n{corr}\n' + 
            f'kun sitä kutsutaan parametrilla\n{test_case}\nnyt listan sisältö on\n' + 
            f'{val}')

    def test_5_testaa_arvoilla2(self):
        test_case = [1,3,5,7,9,11]
        val= test_case[:]
        corr = [1,3,5,7,9,11,12,13,14,15]

        from src.listaan_lukuja import listaan_lukuja
        listaan_lukuja(val)

        self.assertEqual(val, corr, f'Listan sisällön pitäisi olla \n{corr}\n' + 
            f'kun sitä kutsutaan parametrilla\n{test_case}\nnyt listan sisältö on\n' + 
            f'{val}')

    def test_6_testaa_arvoilla3(self):
        test_case = [10,20,30,40,50,60,70,80,90,100,110]
        val= test_case[:]
        corr = [10,20,30,40,50,60,70,80,90,100,110,111,112,113,114]

        from src.listaan_lukuja import listaan_lukuja
        listaan_lukuja(val)

        self.assertEqual(val, corr, f'Listan sisällön pitäisi olla \n{corr}\n' + 
            f'kun sitä kutsutaan parametrilla\n{test_case}\nnyt listan sisältö on\n' + 
            f'{val}')

    def test_7_testaa_arvoilla4(self):
        test_case = [1,2,3,4,5]
        val= test_case[:]
        corr = [1,2,3,4,5]

        from src.listaan_lukuja import listaan_lukuja
        listaan_lukuja(val)

        self.assertEqual(val, corr, f'Listan sisällön pitäisi olla \n{corr}\n' + 
            f'kun sitä kutsutaan parametrilla\n{test_case}\nnyt listan sisältö on\n' + 
            f'{val}')


    




    

   

    








    
if __name__ == '__main__':
    unittest.main()
