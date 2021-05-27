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

@points('10.puhelinluettelo_osa2_2')
class Puhelinluettelo2_Osa2Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=["0"]):
           cls.module = load_module(exercise, 'fi')

    def test_1_pysahtyy(self):
        syote = ["0"]
        with patch('builtins.input', side_effect=syote):
            try:
                reload_module(self.module)
            except:
                self.fail(f"varmista että ohjelma toimii syötteellä\n{s(syote)}")
                
            output = get_stdout()

    def test_2_toimii_numero_loytyy(self):
        syote = ["1", "Erkki", "02-123456", "2",  "Erkki", "0"]
        with patch('builtins.input', side_effect=syote):
            try:
                reload_module(self.module)
            except:
                self.fail(f"varmista että ohjelma toimii syötteellä\n{s(syote)}")
                
            output = get_stdout()
            odotettu = "02-123456"
            self.assertTrue(odotettu in output, f"Ohjelmasi tulostuksessa pitäisi olla\n{odotettu}\nsyötteellä\n{s(syote)}\nTulostus oli\n{output}")   

    def test_3_toimii_monta_numeroa(self):
        syote = ["1", "Emilia", "09-123456", "1", "Emilia", "040-999999", "2", "Emilia", "0"]
        with patch('builtins.input', side_effect=syote):
            try:
                reload_module(self.module)
            except:
                self.fail(f"varmista että ohjelma toimii syötteellä\n{s(syote)}")
                
            output = get_stdout()
            odotettu = "09-123456"
            self.assertTrue(odotettu in output, f"Ohjelmasi tulostuksessa pitäisi olla\n{odotettu}\nsyötteellä\n{s(syote)}\nTulostus oli\n{output}")   
            odotettu = "040-999999"
            self.assertTrue(odotettu in output, f"Ohjelmasi tulostuksessa pitäisi olla\n{odotettu}\nsyötteellä\n{s(syote)}\nTulostus oli\n{output}")   

    def test_4_toimii_ei_numeroa_1(self):
        syote = ["2", "Pekka", "0"]
        with patch('builtins.input', side_effect=syote):
            try:
                reload_module(self.module)
            except:
                self.fail(f"varmista että ohjelma toimii syötteellä\n{s(syote)}")
                
            output = get_stdout()
            odotettu = "numero ei tiedossa"
            self.assertTrue(odotettu in output, f"Ohjelmasi tulostuksessa pitäisi olla\n{odotettu}\nsyötteellä\n{s(syote)}\nTulostus oli\n{output}")   

    def test_5_toimii_ei_numeroa_2(self):
        syote = ["1", "Emilia", "09-123456", "1", "Emilia", "040-999999", "2", "Pekka", "0"]
        with patch('builtins.input', side_effect=syote):
            try:
                reload_module(self.module)
            except:
                self.fail(f"varmista että ohjelma toimii syötteellä\n{s(syote)}")
                
            output = get_stdout()
            odotettu = "numero ei tiedossa"
            self.assertTrue(odotettu in output, f"Ohjelmasi tulostuksessa pitäisi olla\n{odotettu}\nsyötteellä\n{s(syote)}\nTulostus oli\n{output}")   

            odotettu = "09-123456"
            self.assertFalse(odotettu in output, f"Ohjelmasi tulostuksessa EI pitäisi olla\n{odotettu}\nsyötteellä\n{s(syote)}\nTulostus oli\n{output}")   
            odotettu = "040-999999"
            self.assertFalse(odotettu in output, f"Ohjelmasi tulostuksessa EI pitäisi olla\n{odotettu}\nsyötteellä\n{s(syote)}\nTulostus oli\n{output}")   

    def test_6_henkilo_kaytossa(self):
        src_file = os.path.join('src', 'koodi.py')
        lines = []
        p = False

        with open(src_file) as f:
            for line in f:
                if "class Puhelinluettelo"  in line and not ("STUB: class Puhelinluettelo:" in line):
                    p = True
                elif p and "class " in line:
                    p = False 
                elif p:
                    lines.append(line)

        vaadittu = [
            "Henkilo("
        ]

        for v in vaadittu:
            on = False
            for line in lines:
                if v in line:
                    on = True              
            self.assertTrue(on, f"Luokan Puhelinluettelo on käytettävä Henkilo-luokan olioita tallettamaan henkilöiden tiedot!")   
       
        kielletty = [
            ".append("
        ]

        for v in kielletty:
            on = False
            for line in lines:
                if v in line:         
                    self.fail(f"Luokan Puhelinluettelo on käytettävä Henkilo-luokan olioita tallettamaan henkilöiden tiedot. Seuraava rivi on epäilyttävä ja se ei kuulu luokan koodiin\n{line}")   

if __name__ == '__main__':
    unittest.main()

