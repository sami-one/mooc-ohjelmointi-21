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

@points('10.puhelinluettelo_osa2_3')
class Puhelinluettelo2_Osa2Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=["0"]):
           cls.module = load_module(exercise, 'fi')

    def test_1_toimii_numero_loytyy(self):
        syote = ["1", "Erkki", "02-123456", "2",  "Erkki", "0"]
        with patch('builtins.input', side_effect=syote):
            try:
                reload_module(self.module)
            except:
                self.fail(f"varmista että ohjelma toimii syötteellä\n{s(syote)}")
                
            output = get_stdout()
            odotettu = "02-123456"
            self.assertTrue(odotettu in output, f"Ohjelmasi tulostuksessa pitäisi olla\n{odotettu}\nsyötteellä\n{s(syote)}\nTulostus oli\n{output}")   
            odotettu = "osoite ei tiedossa"
            self.assertTrue(odotettu in output, f"Ohjelmasi tulostuksessa pitäisi olla\n{odotettu}\nsyötteellä\n{s(syote)}\nTulostus oli\n{output}")   

    def test_2_toimii_ositteen_lisays(self):
        syote = ["3", "Erkki", "Linnankatu 10", "2",  "Erkki", "0"]
        with patch('builtins.input', side_effect=syote):
            try:
                reload_module(self.module)
            except:
                self.fail(f"varmista että ohjelma toimii syötteellä\n{s(syote)}")
                
            output = get_stdout()
            odotettu = "numero ei tiedossa"
            self.assertTrue(odotettu in output, f"Ohjelmasi tulostuksessa pitäisi olla\n{odotettu}\nsyötteellä\n{s(syote)}\nTulostus oli\n{output}")   
            odotettu = "Linnankatu 10"
            self.assertTrue(odotettu in output, f"Ohjelmasi tulostuksessa pitäisi olla\n{odotettu}\nsyötteellä\n{s(syote)}\nTulostus oli\n{output}")   
 
    def test_2_toimii_jos_osoite_ja_numero(self):
        syote = ["3", "Emilia", "Mannerheimintie 100", "1", "Emilia", "044-121212","2", "Emilia", "0"]
        with patch('builtins.input', side_effect=syote):
            try:
                reload_module(self.module)
            except:
                self.fail(f"varmista että ohjelma toimii syötteellä\n{s(syote)}")
                
            output = get_stdout()
            odotettu = "044-121212"
            self.assertTrue(odotettu in output, f"Ohjelmasi tulostuksessa pitäisi olla\n{odotettu}\nsyötteellä\n{s(syote)}\nTulostus oli\n{output}")   
            odotettu = "Mannerheimintie 100"
            self.assertTrue(odotettu in output, f"Ohjelmasi tulostuksessa pitäisi olla\n{odotettu}\nsyötteellä\n{s(syote)}\nTulostus oli\n{output}")   
            odotettu = "numero ei tiedossa"
            self.assertFalse(odotettu in output, f"Ohjelmasi tulostuksessa EI pitäisi olla\n{odotettu}\nsyötteellä\n{s(syote)}\nTulostus oli\n{output}")   
            odotettu = "osoite ei tiedossa"
            self.assertFalse(odotettu in output, f"Ohjelmasi tulostuksessa EI pitäisi olla\n{odotettu}\nsyötteellä\n{s(syote)}\nTulostus oli\n{output}")   


    def test_4_toimii_tuntemattomalla(self):
        syote = ["2",  "Erkki", "0"]
        with patch('builtins.input', side_effect=syote):
            try:
                reload_module(self.module)
            except:
                self.fail(f"varmista että ohjelma toimii syötteellä\n{s(syote)}")
                
            output = get_stdout()
            odotettu = "numero ei tiedossa"
            self.assertTrue(odotettu in output, f"Ohjelmasi tulostuksessa pitäisi olla\n{odotettu}\nsyötteellä\n{s(syote)}\nTulostus oli\n{output}")   
            odotettu = "osoite ei tiedossa"
            self.assertTrue(odotettu in output, f"Ohjelmasi tulostuksessa pitäisi olla\n{odotettu}\nsyötteellä\n{s(syote)}\nTulostus oli\n{output}")   

if __name__ == '__main__':
    unittest.main()
