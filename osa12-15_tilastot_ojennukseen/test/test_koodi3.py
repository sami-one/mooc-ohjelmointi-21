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

@points('12.tilastot_ojennukseen_osa3')
class TilastotOjennukseen3Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=["osa.json", "0"]):
           cls.module = load_module(exercise, 'fi')

    def test_01_eniten_pisteita_1(self):
        syote = ["osa.json", "6" , "2", "0"]
        with patch('builtins.input', side_effect=syote):
            try:
                reload_module(self.module)
            except:
                self.fail(f"varmista että ohjelma toimii syötteellä\n{s(syote)}")

            output = get_stdout()
            self.assertFalse(len(output)==0,'Koodisi ei tulosta mitään. Eihän se vaan ole if __name__ == "__main__" -lohkon sisällä?')

            exp = """Jakub Vrana          WSH  25 + 27 =  52
Jared McCann         PIT  14 + 21 =  35"""

            for rivi in exp.split("\n"):
                if not rivi in output:
                    self.fail(f"Ohjelman pitäisi tulostaa rivi\n{rivi}\nKun ohjelma suoritetaan syötteellä\n{s(syote)}\nTulostus oli\n{output}")   
            
            eiodotettu = "John Klingberg       DAL   6 + 26 =  32"
            self.assertFalse(eiodotettu in output, f"Ohjelmasi tulostuksessa ei saa olla\n{eiodotettu}\nsyötteellä\n{s(syote)}\nTulostus oli\n{output}\nEttei vaan ohjelmasi tulosta liian monta pelaajaa?")
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

    def test_02_eniten_pisteita_2(self):
        syote = ["osa.json", "6" , "4", "0"]
        with patch('builtins.input', side_effect=syote):
            try:
                reload_module(self.module)
            except:
                self.fail(f"varmista että ohjelma toimii syötteellä\n{s(syote)}")

            output = get_stdout()
            self.assertFalse(len(output)==0,'Koodisi ei tulosta mitään. Eihän se vaan ole if __name__ == "__main__" -lohkon sisällä?')

            exp = """Jakub Vrana          WSH  25 + 27 =  52
Jared McCann         PIT  14 + 21 =  35
John Klingberg       DAL   6 + 26 =  32
Travis Zajac         NJD   9 + 16 =  25"""

            for rivi in exp.split("\n"):
                if not rivi in output:
                    self.fail(f"Ohjelman pitäisi tulostaa rivi\n{rivi}\nKun ohjelma suoritetaan syötteellä\n{s(syote)}\nTulostus oli\n{output}")   
            
            eiodotettu = "Conor Sheary         BUF  10 + 13 =  23"
            self.assertFalse(eiodotettu in output, f"Ohjelmasi tulostuksessa ei saa olla\n{eiodotettu}\nsyötteellä\n{s(syote)}\nTulostus oli\n{output}\nEttei vaan ohjelmasi tulosta liian monta pelaajaa?")
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

    def test_03_eniten_pisteita_iso_syote(self):
        syote = ["kaikki.json", "6" , "4", "0"]
        with patch('builtins.input', side_effect=syote):
            try:
                reload_module(self.module)
            except:
                self.fail(f"varmista että ohjelma toimii syötteellä\n{s(syote)}")

            output = get_stdout()
            self.assertFalse(len(output)==0,'Koodisi ei tulosta mitään. Eihän se vaan ole if __name__ == "__main__" -lohkon sisällä?')

            exp = """Leon Draisaitl       EDM  43 + 67 = 110
Connor McDavid       EDM  34 + 63 =  97
Artemi Panarin       NYR  32 + 63 =  95
David Pastrnak       BOS  48 + 47 =  95"""

            for rivi in exp.split("\n"):
                if not rivi in output:
                    self.fail(f"Ohjelman pitäisi tulostaa rivi\n{rivi}\nKun ohjelma suoritetaan syötteellä\n{s(syote)}\nTulostus oli\n{output}")   
            
            eiodotettu = "Nathan MacKinnon     COL  35 + 58 =  933"
            self.assertFalse(eiodotettu in output, f"Ohjelmasi tulostuksessa ei saa olla\n{eiodotettu}\nsyötteellä\n{s(syote)}\nTulostus oli\n{output}\nEttei vaan ohjelmasi tulosta liian monta pelaajaa?")
            output_lines = output.split('\n')
            exp_lines = exp.split("\n")
            
            n = output_lines.index(exp_lines[0])
            for i in range(2):
                try:
                    oo = output_lines[n+i]
                except:
                    self.fail(f"Kun ohjelma suoritetaan syötteellä\n{s(syote)}\nTulostus \n{output}\nei ole oikeassa järjestyksessä, sen kuuluisi olla\n{exp}")  
                ee = exp_lines[i]
                self.assertEqual(oo, ee, f"Kun ohjelma suoritetaan syötteellä\n{s(syote)}\nTulostus \n{output}\nei ole oikeassa järjestyksessä, sen kuuluisi olla\n{exp}")  


    def test_04_eniten_maaleja_1(self):
        syote = ["osa.json", "7" , "3", "0"]
        with patch('builtins.input', side_effect=syote):
            try:
                reload_module(self.module)
            except:
                self.fail(f"varmista että ohjelma toimii syötteellä\n{s(syote)}")

            output = get_stdout()
            self.assertFalse(len(output)==0,'Koodisi ei tulosta mitään. Eihän se vaan ole if __name__ == "__main__" -lohkon sisällä?')

            exp = """Jakub Vrana          WSH  25 + 27 =  52
Jared McCann         PIT  14 + 21 =  35
Conor Sheary         BUF  10 + 13 =  23"""

            for rivi in exp.split("\n"):
                if not rivi in output:
                    self.fail(f"Ohjelman pitäisi tulostaa rivi\n{rivi}\nKun ohjelma suoritetaan syötteellä\n{s(syote)}\nTulostus oli\n{output}")   
            
            eiodotettu = "Travis Zajac         NJD   9 + 16 =  25"
            self.assertFalse(eiodotettu in output, f"Ohjelmasi tulostuksessa ei saa olla\n{eiodotettu}\nsyötteellä\n{s(syote)}\nTulostus oli\n{output}\nEttei vaan ohjelmasi tulosta liian monta pelaajaa?")
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

    def test_05_eniten_maaleja_2(self):
        syote = ["osa.json", "7" , "7", "0"]
        with patch('builtins.input', side_effect=syote):
            try:
                reload_module(self.module)
            except:
                self.fail(f"varmista että ohjelma toimii syötteellä\n{s(syote)}")

            output = get_stdout()
            self.assertFalse(len(output)==0,'Koodisi ei tulosta mitään. Eihän se vaan ole if __name__ == "__main__" -lohkon sisällä?')

            exp = """Jakub Vrana          WSH  25 + 27 =  52
Jared McCann         PIT  14 + 21 =  35
Conor Sheary         BUF  10 + 13 =  23
Travis Zajac         NJD   9 + 16 =  25
John Klingberg       DAL   6 + 26 =  32
Mark Jankowski       CGY   5 +  2 =   7
Adam Lowry           WPG   4 +  6 =  10"""

            for rivi in exp.split("\n"):
                if not rivi in output:
                    self.fail(f"Ohjelman pitäisi tulostaa rivi\n{rivi}\nKun ohjelma suoritetaan syötteellä\n{s(syote)}\nTulostus oli\n{output}")   
            
            eiodotettu = "Drake Batherson      OTT   3 +  7 =  10"
            self.assertFalse(eiodotettu in output, f"Ohjelmasi tulostuksessa ei saa olla\n{eiodotettu}\nsyötteellä\n{s(syote)}\nTulostus oli\n{output}\nEttei vaan ohjelmasi tulosta liian monta pelaajaa?")
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
    
    def test_05_eniten_maaleja_iso_syote_1(self):
        syote = ["kaikki.json", "7" , "3", "0"]
        with patch('builtins.input', side_effect=syote):
            try:
                reload_module(self.module)
            except:
                self.fail(f"varmista että ohjelma toimii syötteellä\n{s(syote)}")

            output = get_stdout()
            self.assertFalse(len(output)==0,'Koodisi ei tulosta mitään. Eihän se vaan ole if __name__ == "__main__" -lohkon sisällä?')

            exp = """Alex Ovechkin        WSH  48 + 19 =  67
David Pastrnak       BOS  48 + 47 =  95
Auston Matthews      TOR  47 + 33 =  80"""

            for rivi in exp.split("\n"):
                if not rivi in output:
                    self.fail(f"Ohjelman pitäisi tulostaa rivi\n{rivi}\nKun ohjelma suoritetaan syötteellä\n{s(syote)}\nTulostus oli\n{output}")   
            
            eiodotettu = "Leon Draisaitl       EDM  43 + 67 = 110"
            self.assertFalse(eiodotettu in output, f"Ohjelmasi tulostuksessa ei saa olla\n{eiodotettu}\nsyötteellä\n{s(syote)}\nTulostus oli\n{output}\nEttei vaan ohjelmasi tulosta liian monta pelaajaa?")
            output_lines = output.split('\n')
            exp_lines = exp.split("\n")
            
            n = output_lines.index(exp_lines[0])
            for i in range(len(exp_lines)):
                try:
                    oo = output_lines[n+i]
                except:
                    self.fail(f"Kun ohjelma suoritetaan syötteellä\n{s(syote)}\nTulostus \n{output}\nei ole oikeassa järjestyksessä, sen kuuluisi olla\n{exp}")  
                ee = exp_lines[i]
                self.assertEqual(oo, ee, f"Kun ohjelma suoritetaan syötteellä\n{s(syote)}\nTulostus \n{output}\nei ole oikeassa järjestyksessä, sen kuuluisi olla\n{exp}. Jos maalimäärä on tasan, ratkaisee se kummalla on vähemmän otteluita")  

    def test_06_eniten_maaleja_iso_syote_2(self):
        syote = ["kaikki.json", "7" , "9", "0"]
        with patch('builtins.input', side_effect=syote):
            try:
                reload_module(self.module)
            except:
                self.fail(f"varmista että ohjelma toimii syötteellä\n{s(syote)}")

            output = get_stdout()
            self.assertFalse(len(output)==0,'Koodisi ei tulosta mitään. Eihän se vaan ole if __name__ == "__main__" -lohkon sisällä?')

            exp = """Alex Ovechkin        WSH  48 + 19 =  67
David Pastrnak       BOS  48 + 47 =  95
Auston Matthews      TOR  47 + 33 =  80
Leon Draisaitl       EDM  43 + 67 = 110
Mika Zibanejad       NYR  41 + 34 =  75
Sebastian Aho        CAR  38 + 28 =  66
Kyle Connor          WPG  38 + 35 =  73
Jack Eichel          BUF  36 + 42 =  78
Nathan MacKinnon     COL  35 + 58 =  93"""

            for rivi in exp.split("\n"):
                if not rivi in output:
                    self.fail(f"Ohjelman pitäisi tulostaa rivi\n{rivi}\nKun ohjelma suoritetaan syötteellä\n{s(syote)}\nTulostus oli\n{output}")   
            
            eiodotettu = "Connor McDavid       EDM  34 + 63 =  97"
            self.assertFalse(eiodotettu in output, f"Ohjelmasi tulostuksessa ei saa olla\n{eiodotettu}\nsyötteellä\n{s(syote)}\nTulostus oli\n{output}\nEttei vaan ohjelmasi tulosta liian monta pelaajaa?")
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