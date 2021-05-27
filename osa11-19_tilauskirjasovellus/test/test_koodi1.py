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

def tt(d, kh, s):
    status = "EI VALMIS" if not s else "VALMIS"
    k, h, *x = kh.split(' ')
    return f"{d} ({h} tuntia), koodari {k} {status}"

@points('11.tilauskirjasovellus_osa1')
class Tilauskirjasovellus1Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=["0"]):
           cls.module = load_module(exercise, 'fi')

    def test_01_pysahtyy(self):
        syote = ["0"]
        with patch('builtins.input', side_effect=syote):
            try:
                reload_module(self.module)
            except:
                self.fail(f"varmista että ohjelma toimii syötteellä\n{s(syote)}")

    def test_02_ohje_tulostetaan(self):
        syote = ["0"]
        with patch('builtins.input', side_effect=syote):
            try:
                reload_module(self.module)
            except:
                self.fail(f"varmista että ohjelma toimii syötteellä\n{s(syote)}")

            output = get_stdout()
            self.assertFalse(len(output)==0,'Koodisi ei tulosta mitään. Eihän se vaan ole if __name__ == "__main__" -lohkon sisällä?')

            exp = """komennot:
0 lopetus
1 lisää tilaus
2 listaa valmiit
3 listaa ei valmiit
4 merkitse tehtävä valmiiksi
5 koodarit
6 koodarin status
"""

            for rivi in exp.split("\n"):
                if not rivi in output:
                    self.fail(f"Ohjelman pitäisi tulostaa rivi\n{rivi}\nsyötteellä\n{s(syote)}\nTulostus oli\n{output}")   
            
            eiodotettu = "lisätty!"
            self.assertFalse(eiodotettu in output, f"Ohjelmasi tulostuksessa ei saa olla\n{eiodotettu}\nsyötteellä\n{s(syote)}\nTulostus oli\n{output}")   

    def test_03_lisays_toimii(self):
        syote = ["1", "koodaa uusi facebook", "joona 10", "0"]
        with patch('builtins.input', side_effect=syote):
            try:
                reload_module(self.module)
            except:
                self.fail(f"varmista että ohjelma toimii syötteellä\n{s(syote)}")

            output = get_stdout()
            odotettu = "lisätty!"
            self.assertTrue(odotettu in output, f"Ohjelmasi tulostuksessa pitäisi olla\n{odotettu}\nsyötteellä\n{s(syote)}\nTulostus oli\n{output}")   

    def test_04_ei_valmiit_1(self):
        syote = ["1", "koodaa uusi facebook", "joona 10", "3","0"]
        with patch('builtins.input', side_effect=syote):
            try:
                reload_module(self.module)
            except:
                self.fail(f"varmista että ohjelma toimii syötteellä\n{s(syote)}")

            output = get_stdout()
            odotettu = tt("koodaa uusi facebook", "joona 10", False)
            self.assertTrue(odotettu in output, f"Ohjelmasi tulostuksessa pitäisi olla\n{odotettu}\nsyötteellä\n{s(syote)}\nTulostus oli\n{output}")   

    def test_05_ei_valmiit_2(self):
        syote = [
            "1", "koodaa uusi facebook", "joona 10", 
            "1", "koodaa uusi twitter", "elina 95",
            "3","0"]
        with patch('builtins.input', side_effect=syote):
            try:
                reload_module(self.module)
            except:
                self.fail(f"varmista että ohjelma toimii syötteellä\n{s(syote)}")

            output = get_stdout()
            odotettu = tt("koodaa uusi facebook", "joona 10", False)
            self.assertTrue(odotettu in output, f"Ohjelmasi tulostuksessa pitäisi olla\n{odotettu}\nsyötteellä\n{s(syote)}\nTulostus oli\n{output}")   
            odotettu = tt("koodaa uusi twitter", "elina 95", False)
            self.assertTrue(odotettu in output, f"Ohjelmasi tulostuksessa pitäisi olla\n{odotettu}\nsyötteellä\n{s(syote)}\nTulostus oli\n{output}")   

    def test_06_merkkaa_valmiiksi(self):
        syote = ["1", "koodaa uusi facebook", "joona 10", "4", "1","3","0"]
        with patch('builtins.input', side_effect=syote):
            try:
                reload_module(self.module)
            except:
                self.fail(f"varmista että ohjelma toimii syötteellä\n{s(syote)}")

            output = get_stdout()

            odotettu = "merkitty valmiiksi"
            self.assertTrue(odotettu in output, f"Ohjelmasi tulostuksessa pitäisi olla\n{odotettu}\nsyötteellä\n{s(syote)}\nTulostus oli\n{output}")   

            eiodotettu = tt("koodaa uusi facebook", "joona 10", False)
            self.assertFalse(eiodotettu in output, f"Ohjelmasi tulostuksessa ei saa olla\n{eiodotettu}\nsyötteellä\n{s(syote)}\nTulostus oli\n{output}")   

    def test_07_valmiit(self):
        syote = ["1", "koodaa uusi facebook", "joona 10", "4", "1","2","0"]
        with patch('builtins.input', side_effect=syote):
            try:
                reload_module(self.module)
            except:
                self.fail(f"varmista että ohjelma toimii syötteellä\n{s(syote)}")

            output = get_stdout()

            odotettu = "merkitty valmiiksi"
            self.assertTrue(odotettu in output, f"Ohjelmasi tulostuksessa pitäisi olla\n{odotettu}\nsyötteellä\n{s(syote)}\nTulostus oli\n{output}")   

            odotettu = tt("koodaa uusi facebook", "joona 10", True)
            self.assertTrue(odotettu in output, f"Ohjelmasi tulostuksessa pitäisi olla\n{odotettu}\nsyötteellä\n{s(syote)}\nTulostus oli\n{output}")   

    def test_08_koodarit(self):
        syote = ["1", "koodaa uusi facebook", "joona 10", "5", "0"]
        with patch('builtins.input', side_effect=syote):
            try:
                reload_module(self.module)
            except:
                self.fail(f"varmista että ohjelma toimii syötteellä\n{s(syote)}")

            output = get_stdout()

            odotettu = "joona"
            self.assertTrue(odotettu in output, f"Ohjelmasi tulostuksessa pitäisi olla\n{odotettu}\nsyötteellä\n{s(syote)}\nTulostus oli\n{output}")   

    def test_09_koodarit_tilastot(self):
        syote = ["1", "koodaa uusi facebook", "joona 10", "6", "joona","0"]
        with patch('builtins.input', side_effect=syote):
            try:
                reload_module(self.module)
            except:
                self.fail(f"varmista että ohjelma toimii syötteellä\n{s(syote)}")

            output = get_stdout()

            odotettu = "työt: valmiina 0 ei valmiina 1, tunteja: tehty 0 tekemättä 10"
            self.assertTrue(odotettu in output, f"Ohjelmasi tulostuksessa pitäisi olla\n{odotettu}\nsyötteellä\n{s(syote)}\nTulostus oli\n{output}")   

    def test_10_koodarit_tilastot2(self):
        syote = [
            "1", "koodaa uusi facebook", "joona 10", 
            "1", "koodaa uusi twitter", "joona 95",
            "4", "1",
            "6", "joona","0"]
        with patch('builtins.input', side_effect=syote):
            try:
                reload_module(self.module)
            except:
                self.fail(f"varmista että ohjelma toimii syötteellä\n{s(syote)}")

            output = get_stdout()

            odotettu = "työt: valmiina 1 ei valmiina 1, tunteja: tehty 10 tekemättä 95"
            self.assertTrue(odotettu in output, f"Ohjelmasi tulostuksessa pitäisi olla\n{odotettu}\nsyötteellä\n{s(syote)}\nTulostus oli\n{output}")   


    def test_11_valmiita(self):
        syote = ["1", "koodaa uusi facebook", "joona 10", "2" ,"0"]
        with patch('builtins.input', side_effect=syote):
            try:
                reload_module(self.module)
            except:
                self.fail(f"varmista että ohjelma toimii syötteellä\n{s(syote)}")

            output = get_stdout()

            odotettu = "ei valmiita"
            self.assertTrue(odotettu in output, f"Ohjelmasi tulostuksessa pitäisi olla\n{odotettu}\nsyötteellä\n{s(syote)}\nTulostus oli\n{output}")   

    def test_12_ei_valmiit_2(self):
        syote = [
            "1", "koodaa uusi facebook", "joona 10", 
            "1", "koodaa uusi twitter", "elina 95",
            "4","1",
            "4","2",
            "2","0"]
        with patch('builtins.input', side_effect=syote):
            try:
                reload_module(self.module)
            except:
                self.fail(f"varmista että ohjelma toimii syötteellä\n{s(syote)}")

            output = get_stdout()
            odotettu = tt("koodaa uusi facebook", "joona 10", True)
            self.assertTrue(odotettu in output, f"Ohjelmasi tulostuksessa pitäisi olla\n{odotettu}\nsyötteellä\n{s(syote)}\nTulostus oli\n{output}")   
            odotettu = tt("koodaa uusi twitter", "elina 95", True)
            self.assertTrue(odotettu in output, f"Ohjelmasi tulostuksessa pitäisi olla\n{odotettu}\nsyötteellä\n{s(syote)}\nTulostus oli\n{output}")   

if __name__ == '__main__':
    unittest.main()