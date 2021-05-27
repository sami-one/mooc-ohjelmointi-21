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

class Puhelinluettelo2_Osa2Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=["0"]):
           cls.module = load_module(exercise, 'fi')

    @points('10.opintorekisteri_osa1')
    def test_0_pysahtyy(self):
        syote = ["0"]
        with patch('builtins.input', side_effect=syote):
            try:
                reload_module(self.module)
            except:
                self.fail(f"varmista että ohjelma toimii syötteellä\n{s(syote)}")
                
            output = get_stdout()

    @points('10.opintorekisteri_osa1')
    def test_1_lisays_toimii_1(self):
        syote = ["1", "Ohpe", "3", "5", "0"]
        with patch('builtins.input', side_effect=syote):
            try:
                reload_module(self.module)
            except:
                self.fail(f"varmista että ohjelma toimii syötteellä\n{s(syote)}")

            output = get_stdout()
            self.assertFalse(len(output)==0,'Koodisi ei tulosta mitään. Eihän se vaan ole if __name__ == "__main__" -lohkon sisällä?')

    @points('10.opintorekisteri_osa1')
    def test_2_lisatty_loytyy(self):
        syote = ["1", "Ohpe", "3", "5", "2", "Ohpe", "0"]
        with patch('builtins.input', side_effect=syote):
            try:
                reload_module(self.module)
            except:
                self.fail(f"varmista että ohjelma toimii syötteellä\n{s(syote)}")
                
            output = get_stdout()
            odotettu = "Ohpe (5 op) arvosana 3"
            self.assertTrue(odotettu in output, f"Ohjelmasi tulostuksessa pitäisi olla\n{odotettu}\nsyötteellä\n{s(syote)}\nTulostus oli\n{output}")   

    @points('10.opintorekisteri_osa1')
    def test_3_korotus_toimii(self):
        syote = ["1", "Ohpe", "3", "5","1","Ohpe", "5", "5", "2", "Ohpe", "0"]
        with patch('builtins.input', side_effect=syote):
            try:
                reload_module(self.module)
            except:
                self.fail(f"varmista että ohjelma toimii syötteellä\n{s(syote)}")
                
            output = get_stdout()
            odotettu = "Ohpe (5 op) arvosana 5"
            self.assertTrue(odotettu in output, f"Ohjelmasi tulostuksessa pitäisi olla\n{odotettu}\nsyötteellä\n{s(syote)}\nTulostus oli\n{output}")   
            odotettu = "Ohpe (5 op) arvosana 3"
            self.assertFalse(odotettu in output, f"Ohjelmasi tulostuksessa EI pitäisi olla\n{odotettu}\nsyötteellä\n{s(syote)}\nTulostus oli\n{output}")   

    @points('10.opintorekisteri_osa1')
    def test_4_arvosana_ei_huonone(self):
        syote = ["1", "Ohpe", "3", "5", "1","Ohpe", "1", "5", "2", "Ohpe", "0"]
        with patch('builtins.input', side_effect=syote):
            try:
                reload_module(self.module)
            except:
                self.fail(f"varmista että ohjelma toimii syötteellä\n{s(syote)}")
                
            output = get_stdout()
            odotettu = "Ohpe (5 op) arvosana 3"
            self.assertTrue(odotettu in output, f"Ohjelmasi tulostuksessa pitäisi olla\n{odotettu}\nsyötteellä\n{s(syote)}\nTulostus oli\n{output}")   
            odotettu = "Ohpe (5 op) arvosana 1"
            self.assertFalse(odotettu in output, f"Ohjelmasi tulostuksessa EI pitäisi olla\n{odotettu}\nsyötteellä\n{s(syote)}\nTulostus oli\n{output}")   

    @points('10.opintorekisteri_osa1')
    def test_5_olematon_suoritus(self):
        syote = ["1", "Ohpe", "3", "5", "2", "Java-ohjelmointi","0"]
        with patch('builtins.input', side_effect=syote):
            try:
                reload_module(self.module)
            except:
                self.fail(f"varmista että ohjelma toimii syötteellä\n{s(syote)}")

            output = get_stdout()
            odotettu = "ei suoritusta"
            self.assertTrue(odotettu in output, f"Ohjelmasi tulostuksessa pitäisi olla\n{odotettu}\nsyötteellä\n{s(syote)}\nTulostus oli\n{output}")   
            odotettu = "Ohpe (5 op) arvosana"
            self.assertFalse(odotettu in output, f"Ohjelmasi tulostuksessa EI pitäisi olla\n{odotettu}\nsyötteellä\n{s(syote)}\nTulostus oli\n{output}")   

    @points('10.opintorekisteri_osa2')
    def test_6_tilasto_1(self):
        syote = ["1", "Ohpe", "3", "5", "3","0"]
        with patch('builtins.input', side_effect=syote):
            try:
                reload_module(self.module)
            except:
                self.fail(f"varmista että ohjelma toimii syötteellä\n{s(syote)}")

            output = get_stdout()
            exp = """
suorituksia 1 kurssilta, yhteensä 5 opintopistettä
keskiarvo 3
arvosanajakauma
5:
4:
3: x
2:
1:
"""

            for rivi in exp.split("\n"):
                if not rivi in output:
                    self.fail(f"Ohjelman pitäisi tulostaa rivi\n{rivi}\nsyötteellä\n{s(syote)}\nTulostus oli\n{output}")   

    @points('10.opintorekisteri_osa2')
    def test_7_tilasto_2(self):
        syote = ["1", "Ohpe", "3", "5", "1", "Ohja", "5", "5", "3", "0"]
        with patch('builtins.input', side_effect=syote):
            try:
                reload_module(self.module)
            except:
                self.fail(f"varmista että ohjelma toimii syötteellä\n{s(syote)}")

            output = get_stdout()
            exp = """
suorituksia 2 kurssilta, yhteensä 10 opintopistettä
keskiarvo 4
arvosanajakauma
5: x
4:
3: x
2:
1:
"""

            for rivi in exp.split("\n"):
                if not rivi in output:
                    self.fail(f"Ohjelman pitäisi tulostaa rivi\n{rivi}\nsyötteellä\n{s(syote)}\nTulostus oli\n{output}")   

    @points('10.opintorekisteri_osa2')
    def test_7_tilasto_3(self):
        syote = ["1", "Ohpe", "3", "5", "1", "Ohpe", "5", "5", "3", "1", "Tira", "5", "10", "3", "1", "Tilpe", "1", "5", "3", "0"]
        with patch('builtins.input', side_effect=syote):
            try:
                reload_module(self.module)
            except:
                self.fail(f"varmista että ohjelma toimii syötteellä\n{s(syote)}")

            output = get_stdout()
            exp = """
suorituksia 3 kurssilta, yhteensä 20 opintopistettä
keskiarvo 3.7
arvosanajakauma
5: xx
4:
3:
2:
1: x
"""

            for rivi in exp.split("\n"):
                if not rivi in output:
                    self.fail(f"Ohjelman pitäisi tulostaa rivi\n{rivi}\nsyötteellä\n{s(syote)}\nTulostus oli\n{output}")   

    @points('10.opintorekisteri_osa2')
    def test_8_tilasto_4(self):
        syote = ["1", "Ohpe", "3", "5", 
                 "1", "Ohpe", "5", "5", 
                 "1", "Tira", "5", "10",
                 "1", "Tilpe", "1", "5", 
                 "1", "Lama", "4", "5", 
                 "1", "JYM", "2", "5",
                 "1", "Käjä", "4", "5", 
                 "1", "Lapio", "2", "1", 
                 "3", "0"]
        with patch('builtins.input', side_effect=syote):
            try:
                reload_module(self.module)
            except:
                self.fail(f"varmista että ohjelma toimii syötteellä\n{s(syote)}")

            output = get_stdout()
            exp = """
suorituksia 7 kurssilta, yhteensä 36 opintopistettä
keskiarvo 3.3
arvosanajakauma
5: xx
4: xx
3:
2: xx
1: x
"""

            for rivi in exp.split("\n"):
                if not rivi in output:
                    self.fail(f"Ohjelman pitäisi tulostaa rivi\n{rivi}\nsyötteellä\n{s(syote)}\nTulostus oli\n{output}")   

if __name__ == '__main__':
    unittest.main()
