import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import os.path
import textwrap
from random import choice, randint

exercise = 'src.vanhempi_kirja'
function = "vanhempi_kirja"


@points('8.vanhempi_kirja')
class VanhempiKirjaTest(unittest.TestCase):
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
            from src.vanhempi_kirja import vanhempi_kirja
        except:
            self.assertTrue(False, "Ohjelmastasi pitäisi löytyä funktio nimeltä vanhempi_kirja(kirja1: Kirja, kirja2: Kirja)")

    def test1b_luokkamaarittely_olemassa(self):
        try:
            from src.vanhempi_kirja import Kirja
        except:
            self.assertTrue(False, "Ohjelmassa pitää olla määriteltynä luokka Kirja!")

    def test2_palautusarvon_tyyppi(self):
        try:
            from src.vanhempi_kirja import vanhempi_kirja
            from src.vanhempi_kirja import Kirja
            
            val = vanhempi_kirja(Kirja("Python","P. Python", "tieto", 2000), Kirja("Java", "J.Java", "tieto", 2001))
            taip = str(type(val)).replace("<class '","").replace("'>","")
            self.assertTrue(val == None, f"Funktion vanhempi_kirja ei pitäisi palauttaa arvoa," +  
                f" nyt se palauttaa arvon {val} joka on tyyppiä {taip}\n kun sitä kutsutaan parametreilla\n" + 
                'vanhempi_kirja(Kirja("Python","P. Python", "tieto", 2000), Kirja("Java", "J.Java", "tieto", 2001))')
        except Exception as e:
            self.assertTrue(False, f"Funktio antoi virheen kun sitä kutsuttiin parametrin arvolla [[1,1],[2,2]]:\n{e}")


    def test3_testaa_eka_vanhempi(self):
        test_cases = ((("Seitsemän veljestä", "Aleksis Kivi", "Romaani", 1870), 
                       ("Sinuhe egyptiläinen", "Mika Waltari", "Romaani", 1945)),
                       (("Kyberias", "Stanislaw Lem", "Sci-fi", 1965), 
                       ("Kotona maailmankaikkeudessa", "Esko Valtaoja", "Tiede", 2001)))
        for test_case in test_cases:
            with patch('builtins.input', side_effect=[AssertionError("Syötteen pyytämistä ei odotettu")]):
                reload_module(self.module)
                vanhempi_kirja = load(exercise, function, 'fi')
                from src.vanhempi_kirja import Kirja

                k1,k2 = test_case
                kirja1 = Kirja(k1[0],k1[1],k1[2],k1[3])
                kirja2 = Kirja(k2[0],k2[1],k2[2],k2[3])
                vanhempi = kirja1
                ei_vanhempi = kirja2

                corr = f"{vanhempi.nimi} on vanhempi, se kirjoitettiin {vanhempi.kirjoitusvuosi}"

                vanhempi_kirja(kirja1,kirja2)
                
                output = get_stdout()
                output = output.replace("\n","").strip()

                self.assertTrue("vanhempi" in output and vanhempi.nimi in output and ei_vanhempi.nimi not in output and 
                    str(vanhempi.kirjoitusvuosi) in output and str(ei_vanhempi.kirjoitusvuosi) not in output, 
                    f"Ohjelman tuloste\n{output}\nei vastaa mallivastausta\n{corr}\nkun kirjat ovat\n{test_case}")

    def test4_testaa_toka_vanhempi(self):
        test_cases = ((("Kahdeksan veljestä", "Aleksis Kivelä", "Romaani", 1993), 
                       ("Sinuhe egyptiläinen", "Mika Waltari", "Romaani", 1945)),
                       (("Loiri", "Jari Tervo", "Elämäkerta", 2019), 
                       ("Kotona maailmankaikkeudessa", "Esko Valtaoja", "Tiede", 2001)))
        for test_case in test_cases:
            with patch('builtins.input', side_effect=[AssertionError("Syötteen pyytämistä ei odotettu")]):
                reload_module(self.module)
                vanhempi_kirja = load(exercise, function, 'fi')
                from src.vanhempi_kirja import Kirja

                k1,k2 = test_case
                kirja1 = Kirja(k1[0],k1[1],k1[2],k1[3])
                kirja2 = Kirja(k2[0],k2[1],k2[2],k2[3])
                vanhempi = kirja2
                ei_vanhempi = kirja1

                corr = f"{vanhempi.nimi} on vanhempi, se kirjoitettiin {vanhempi.kirjoitusvuosi}"

                vanhempi_kirja(kirja1,kirja2)
                
                output = get_stdout()
                output = output.replace("\n","").strip()

                self.assertTrue("vanhempi" in output and vanhempi.nimi in output and ei_vanhempi.nimi not in output and 
                    str(vanhempi.kirjoitusvuosi) in output and str(ei_vanhempi.kirjoitusvuosi) not in output, 
                    f"Ohjelman tuloste\n{output}\nei vastaa mallivastausta\n{corr}\nkun kirjat ovat\n{test_case}")

    def test5_testaa_yhta_vanhat(self):
        test_cases = ((("Kahdeksan veljestä", "Aleksis Kivelä", "Romaani", 1993), 
                       ("Sinuhe ruotsalainen", "Mikko Waltanen", "Romaani", 1993)),
                       (("Loiri", "Jari Tervo", "Elämäkerta", 2019), 
                       ("Veteen syntyneet", "Akseli Heikkilä", "Romaani", 2019)))
        for test_case in test_cases:
            with patch('builtins.input', side_effect=[AssertionError("Syötteen pyytämistä ei odotettu")]):
                reload_module(self.module)
                vanhempi_kirja = load(exercise, function, 'fi')
                from src.vanhempi_kirja import Kirja

                k1,k2 = test_case
                kirja1 = Kirja(k1[0],k1[1],k1[2],k1[3])
                kirja2 = Kirja(k2[0],k2[1],k2[2],k2[3])
               
                corr = f"{kirja1.nimi} ja {kirja2.nimi} kirjoitettiin {kirja1.kirjoitusvuosi}"

                vanhempi_kirja(kirja1,kirja2)
                
                output = get_stdout()
                output = output.replace("\n","").strip()

                self.assertTrue("ja" in output and kirja1.nimi in output and kirja2.nimi in output and 
                    str(kirja1.kirjoitusvuosi) in output, 
                    f"Ohjelman tuloste\n{output}\nei vastaa mallivastausta\n{corr}\nkun kirjat ovat\n{test_case}")
                
    

if __name__ == '__main__':
    unittest.main()
