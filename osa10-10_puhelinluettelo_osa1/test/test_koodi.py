import unittest
from unittest.mock import patch

from tmc import points, reflect
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import os.path
import textwrap
from random import choice, randint
from datetime import date, datetime, timedelta

exercise = 'src.koodi'

def f(attr: list):
    return ",".join(attr)

def s(l: list):
    return "\n".join(l)

def clear_file():
    with open("luettelo.txt", "w"):
        pass

@points('10.puhelinluettelo_osa1')
class PuhelinluetteloTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=["0"]):
           cls.module = load_module(exercise, 'fi')

    def test_1_pysahtyy(self):
        clear_file()
        syote = ["0"]
        with patch('builtins.input', side_effect=syote):
            try:
                reload_module(self.module)
            except:
                self.fail(f"varmista että ohjelma toimii syötteellä\n{s(syote)}")  

    def test_2_haku_toimii_lisayksen_jalkeen(self):
        clear_file()
        syote = ["1", "Erkki", "02-123456", "2",  "Erkki", "0"]
        with patch('builtins.input', side_effect=syote):
            try:
                reload_module(self.module)
            except:
                self.fail(f"varmista että ohjelma toimii syötteellä\n{s(syote)}")
                
            output = get_stdout()
            self.assertFalse(len(output)==0,f'Koodisi ei tulosta mitään syötteellä\n{s(syote)}\nTässä tehtävässä ei tule sijoittaa mitään koodia if __name__ == "__main__" -lohkon sisälle')

            odotettu = "02-123456"
            self.assertTrue(odotettu in output, f"Ohjelmasi tulostuksessa pitäisi olla\n{odotettu}\nsyötteellä\n{s(syote)}\nTulostus oli\n{output}")   

    def test_3_numeron_perusteella_1(self):
        clear_file()
        syote = ["1", "Erkki", "02-123456", "3",  "02-123456", "0"]
        with patch('builtins.input', side_effect=syote):
            try:
                reload_module(self.module)
            except:
                self.fail(f"varmista että ohjelma toimii syötteellä\n{s(syote)}")
                
            output = get_stdout()
            odotettu = "Erkki"
            self.assertTrue(odotettu in output, f"Ohjelmasi tulostuksessa pitäisi olla\n{odotettu}\nsyötteellä\n{s(syote)}\nTulostus oli\n{output}")   

    def test_3_numeron_perusteella_2(self):
        clear_file()
        syote = ["1", "Emilia", "09-123456", "3",  "09-123456", "0"]
        with patch('builtins.input', side_effect=syote):
            try:
                reload_module(self.module)
            except:
                self.fail(f"varmista että ohjelma toimii syötteellä\n{s(syote)}")
                
            output = get_stdout()
            odotettu = "Emilia"
            self.assertTrue(odotettu in output, f"Ohjelmasi tulostuksessa pitäisi olla\n{odotettu}\nsyötteellä\n{s(syote)}\nTulostus oli\n{output}")   
    
    def test_3_numeron_perusteella_3(self):
        clear_file()
        syote = ["1", "Emilia", "045-333444", "1", "Emilia", "09-123456", "3",  "09-123456", "0"]
        with patch('builtins.input', side_effect=syote):
            try:
                reload_module(self.module)
            except:
                self.fail(f"varmista että ohjelma toimii syötteellä\n{s(syote)}")
                
            output = get_stdout()
            odotettu = "Emilia"
            self.assertTrue(odotettu in output, f"Ohjelmasi tulostuksessa pitäisi olla\n{odotettu}\nsyötteellä\n{s(syote)}\nTulostus oli\n{output}")   
            odotettu = "tuntematon numero"
            self.assertFalse(odotettu in output, f"Ohjelmasi tulostuksessa ei saisi olla riviä\n{odotettu}\nsyötteellä\n{s(syote)}\nTulostus oli\n{output}") 

    def test_3_numeron_perusteella_3(self):
        clear_file()
        syote = ["1", "Emilia", "045-333444", "1", "Erkki", "09-123456", "3",  "040-332211", "0"]
        with patch('builtins.input', side_effect=syote):
            try:
                reload_module(self.module)
            except:
                self.fail(f"varmista että ohjelma toimii syötteellä\n{s(syote)}")
                
            output = get_stdout()
            odotettu = "tuntematon numero"
            self.assertTrue(odotettu in output, f"Ohjelmasi tulostuksessa pitäisi olla\n{odotettu}\nsyötteellä\n{s(syote)}\nTulostus oli\n{output}")   
            odotettu = "Erkki"
            self.assertFalse(odotettu in output, f"Ohjelmasi tulostuksessa ei saisi olla riviä\n{odotettu}\nsyötteellä\n{s(syote)}\nTulostus oli\n{output}") 

if __name__ == '__main__':
    unittest.main()