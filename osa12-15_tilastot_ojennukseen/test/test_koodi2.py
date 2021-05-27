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

def s(l: list):
    return "\n".join(l)

@points('12.tilastot_ojennukseen_osa2')
class TilastotOjennukseen2Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=["osa.json", "0"]):
           cls.module = load_module(exercise, 'fi')

    def test_01_joukkueen_pelaajat_1(self):
        syote = ["osa.json", "4" , "WSH", "0"]
        with patch('builtins.input', side_effect=syote):
            try:
                reload_module(self.module)
            except:
                self.fail(f"varmista että ohjelma toimii syötteellä\n{s(syote)}")

            output = get_stdout()
            self.assertFalse(len(output)==0,'Koodisi ei tulosta mitään. Eihän se vaan ole if __name__ == "__main__" -lohkon sisällä?')

            exp = """Jakub Vrana          WSH  25 + 27 =  52
Jonas Siegenthaler   WSH   2 +  7 =   9"""

            for rivi in exp.split("\n"):
                if not rivi in output:
                    self.fail(f"Ohjelman pitäisi tulostaa rivi\n{rivi}\nKun ohjelma suoritetaan syötteellä\n{s(syote)}\nTulostus oli\n{output}")   
            
            output_lines = output.split('\n')
            exp_lines = exp.split("\n")
            
            n = output_lines.index(exp_lines[0])
            for i in range(len(exp_lines)):
                try:
                    oo = output_lines[n+i]
                except:
                    self.fail(f"Kun ohjelma suoritetaan syötteellä\n{s(syote)}\nTulostus \n{output}\nei ole oikeassa järjestyksessä, sen kuuluisi olla\n{exp}")  
                ee = exp_lines[i]
                self.assertEqual(oo, ee, f"Kun ohjelma suoritetaan syötteellä\n{s(syote)}\nTulostus \n{output}\nei ole oikeassa järjestyksessä, sen kuuluisi olla\n{exp}")  

    def test_02_joukkueen_pelaajat_2(self):
        syote = ["osa.json", "4" , "DAL", "0"]
        with patch('builtins.input', side_effect=syote):
            try:
                reload_module(self.module)
            except:
                self.fail(f"varmista että ohjelma toimii syötteellä\n{s(syote)}")

            output = get_stdout()

            exp = """John Klingberg       DAL   6 + 26 =  32
Taylor Fedun         DAL   2 +  7 =   9"""

            for rivi in exp.split("\n"):
                if not rivi in output:
                    self.fail(f"Ohjelman pitäisi tulostaa rivi\n{rivi}\nKun ohjelma suoritetaan syötteellä\n{s(syote)}\nTulostus oli\n{output}")   
            
            output_lines = output.split('\n')
            exp_lines = exp.split("\n")
            
            n = output_lines.index(exp_lines[0])
            for i in range(len(exp_lines)):
                try:
                    oo = output_lines[n+i]
                except:
                    self.fail(f"Kun ohjelma suoritetaan syötteellä\n{s(syote)}\nTulostus \n{output}\nei ole oikeassa järjestyksessä, sen kuuluisi olla\n{exp}")  
                ee = exp_lines[i]
                self.assertEqual(oo, ee, f"Kun ohjelma suoritetaan syötteellä\n{s(syote)}\nTulostus \n{output}\nei ole oikeassa järjestyksessä, sen kuuluisi olla\n{exp}")  

    def test_03_maan_pelaajat_1(self):
        syote = ["osa.json", "5" , "CAN", "0"]
        with patch('builtins.input', side_effect=syote):
            try:
                reload_module(self.module)
            except:
                self.fail(f"varmista että ohjelma toimii syötteellä\n{s(syote)}")

            output = get_stdout()

            exp = """Jared McCann         PIT  14 + 21 =  35
Travis Zajac         NJD   9 + 16 =  25
Taylor Fedun         DAL   2 +  7 =   9
Mark Jankowski       CGY   5 +  2 =   7
Logan Shaw           WPG   3 +  2 =   5"""

            for rivi in exp.split("\n"):
                if not rivi in output:
                    self.fail(f"Ohjelman pitäisi tulostaa rivi\n{rivi}\nKun ohjelma suoritetaan syötteellä\n{s(syote)}\nTulostus oli\n{output}")   
            
            output_lines = output.split('\n')
            exp_lines = exp.split("\n")
            
            n = output_lines.index(exp_lines[0])
            for i in range(len(exp_lines)):
                try:
                    oo = output_lines[n+i]
                except:
                    self.fail(f"Kun ohjelma suoritetaan syötteellä\n{s(syote)}\nTulostus \n{output}\nei ole oikeassa järjestyksessä, sen kuuluisi olla\n{exp}")  
                ee = exp_lines[i]
                self.assertEqual(oo, ee, f"Kun ohjelma suoritetaan syötteellä\n{s(syote)}\nTulostus \n{output}\nei ole oikeassa järjestyksessä, sen kuuluisi olla\n{exp}")  

    def test_04_maan_pelaajat_2(self):
        syote = ["osa.json", "5" , "SWE", "0"]
        with patch('builtins.input', side_effect=syote):
            try:
                reload_module(self.module)
            except:
                self.fail(f"varmista että ohjelma toimii syötteellä\n{s(syote)}")

            output = get_stdout()

            exp = """John Klingberg       DAL   6 + 26 =  32
Jonathan Davidsson   OTT   0 +  1 =   1"""

            for rivi in exp.split("\n"):
                if not rivi in output:
                    self.fail(f"Ohjelman pitäisi tulostaa rivi\n{rivi}\nKun ohjelma suoritetaan syötteellä\n{s(syote)}\nTulostus oli\n{output}")   
            
            output_lines = output.split('\n')
            exp_lines = exp.split("\n")
            
            n = output_lines.index(exp_lines[0])
            for i in range(len(exp_lines)):
                try:
                    oo = output_lines[n+i]
                except:
                    self.fail(f"Kun ohjelma suoritetaan syötteellä\n{s(syote)}\nTulostus \n{output}\nei ole oikeassa järjestyksessä, sen kuuluisi olla\n{exp}")  
                ee = exp_lines[i]
                self.assertEqual(oo, ee, f"Kun ohjelma suoritetaan syötteellä\n{s(syote)}\nTulostus \n{output}\nei ole oikeassa järjestyksessä, sen kuuluisi olla\n{exp}")  
    
    def test_05_maan_pelaajat_iso_tiedosto_1(self):
        syote = ["kaikki.json", "5" , "AUS", "0"]
        with patch('builtins.input', side_effect=syote):
            try:
                reload_module(self.module)
            except:
                self.fail(f"varmista että ohjelma toimii syötteellä\n{s(syote)}")

            output = get_stdout()

            exp = """Nathan Walker        STL   1 +  1 =   2"""

            for rivi in exp.split("\n"):
                if not rivi in output:
                    self.fail(f"Ohjelman pitäisi tulostaa rivi\n{rivi}\nKun ohjelma suoritetaan syötteellä\n{s(syote)}\nTulostus oli\n{output}")   
            
            output_lines = output.split('\n')
            exp_lines = exp.split("\n")
            
            n = output_lines.index(exp_lines[0])
            for i in range(len(exp_lines)):
                try:
                    oo = output_lines[n+i]
                except:
                    self.fail(f"Kun ohjelma suoritetaan syötteellä\n{s(syote)}\nTulostus \n{output}\nei ole oikeassa järjestyksessä, sen kuuluisi olla\n{exp}")  
                ee = exp_lines[i]
                self.assertEqual(oo, ee, f"Kun ohjelma suoritetaan syötteellä\n{s(syote)}\nTulostus \n{output}\nei ole oikeassa järjestyksessä, sen kuuluisi olla\n{exp}")  

    def test_06_maan_pelaajat_iso_tiedosto_2(self):
        syote = ["kaikki.json", "5" , "AUT", "0"]
        with patch('builtins.input', side_effect=syote):
            try:
                reload_module(self.module)
            except:
                self.fail(f"varmista että ohjelma toimii syötteellä\n{s(syote)}")

            output = get_stdout()

            exp = """Michael Raffl        PHI   8 + 12 =  20
Michael Grabner      ARI   8 +  3 =  11"""

            for rivi in exp.split("\n"):
                if not rivi in output:
                    self.fail(f"Ohjelman pitäisi tulostaa rivi\n{rivi}\nKun ohjelma suoritetaan syötteellä\n{s(syote)}\nTulostus oli\n{output}")   
            
            output_lines = output.split('\n')
            exp_lines = exp.split("\n")
            
            n = output_lines.index(exp_lines[0])
            for i in range(len(exp_lines)):
                try:
                    oo = output_lines[n+i]
                except:
                    self.fail(f"Kun ohjelma suoritetaan syötteellä\n{s(syote)}\nTulostus \n{output}\nei ole oikeassa järjestyksessä, sen kuuluisi olla\n{exp}")  
                ee = exp_lines[i]
                self.assertEqual(oo, ee, f"Kun ohjelma suoritetaan syötteellä\n{s(syote)}\nTulostus \n{output}\nei ole oikeassa järjestyksessä, sen kuuluisi olla\n{exp}")  

if __name__ == '__main__':
    unittest.main()