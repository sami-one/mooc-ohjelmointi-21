import unittest
from unittest.mock import patch

from tmc import points, reflect
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import os.path
import textwrap
from random import choice, randint, shuffle
from datetime import date

exercise = 'src.sanapeli'

def f(attr: list):
    return "\n".join([str(x) for x in attr]) 


class SanapeliTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=[AssertionError("Syötteen pyytämistä ei odotettu")]):
           cls.module = load_module(exercise, 'fi')

    @points('10.sanapeli_osa1')
    def test_00a_paaohjelma_kunnossa(self):
        ok, line = check_source(self.module)
        message = """Funktioita testaava koodi tulee sijoittaa lohkon
if __name__ == "__main__":
sisälle. Seuraava rivi tulee siirtää:
"""
        self.assertTrue(ok, message+line)

    @points('10.sanapeli_osa1')
    def test_00b_luokka_sanapeli_olemassa(self):
        try:
            from src.sanapeli import Sanapeli
            a = Sanapeli(1)
        except Exception as e:
            self.fail(f'Konstruktorikutsu Sanapeli(1) antoi virheen \n{e}\n' + 
            'Ethän ole muuttanut luokan Sanapeli määrittelyä?')

    @points('10.sanapeli_osa1')
    def test_01_luokka_pisin_olemassa(self):
        try:
            from src.sanapeli import PisinSana
            a = PisinSana(1)
        except Exception as e:
            self.fail(f'Konstruktorikutsu PisinSana(0) antoi virheen \n{e}\n' + 
            'Varmista, että luokka on määritelty.')

    @points('10.sanapeli_osa1')
    def test_02_pisin_perinta(self):
        from src.sanapeli import Sanapeli, PisinSana
        self.assertTrue(issubclass(PisinSana,Sanapeli), f"Luokan PisinSana pitäisi " +
            'periä luokka SanaPeli!')

    @points('10.sanapeli_osa1')
    def test_03_pisin_metodi_uudestaan(self):
        from src.sanapeli import Sanapeli, PisinSana
        self.assertTrue(Sanapeli.kierroksen_voittaja is not PisinSana.kierroksen_voittaja, 
            f'Metodi kierroksen_voittaja pitää toteuttaa uudestaan luokassa ' + 
            'PisinSana!')

    @points('10.sanapeli_osa1')
    def test_04_pisin_pelaa_ei_muutettu(self):
        from src.sanapeli import Sanapeli, PisinSana
        self.assertTrue(Sanapeli.pelaa is PisinSana.pelaa, 
            f'Metodia pelaa() ei saa toteuttaa uudestaan luokassa ' + 
            'PisinSana!')

    @points('10.sanapeli_osa1')
    def test_05_pisin_toimii(self):
        test_cases = [("ensimmäinen","toka","kolmas","4.",2,0), 
            ("kettu","tiikeri","laama","kameli","karhu","elefantti",0,3), 
            ("tupu","hupu","mortti","vertti",0,0),
            ("auto","laiva","helikopteri","lentokone","juna","raitiovaunu",1,2)]
        for test_case in test_cases:
            from src.sanapeli import PisinSana
            with patch('builtins.input', side_effect=list(test_case[:-2])):
                peli = PisinSana(len(test_case)//2 - 1)
                peli.pelaa()

                output = get_stdout()
                val = [x.strip() for x in output.split("\n") if len(x.strip()) > 0][-2:]
                corr = [f"pelaaja 1: {test_case[-2]}", f"pelaaja 2: {test_case[-1]}"]

                val_str = "\n".join(val)
                corr_str = "\n".join(corr)
                test_str = "\n".join(test_case[:-2])

                self.assertEqual(val, corr, f'Pelin pitäisi tulostaa\n{corr_str}\n' + 
                    f'mutta se tulostaa\n{val_str}\nkun syöte on \n{test_str}')   

    @points('10.sanapeli_osa2')
    def test_06_luokka_vokaalit_olemassa(self):
        try:
            from src.sanapeli import EnitenVokaaleja
            a = EnitenVokaaleja(1)
        except Exception as e:
            self.fail(f'Konstruktorikutsu EnitenVokaaleja(0) antoi virheen \n{e}\n' + 
            'Varmista, että luokka on määritelty.')

    @points('10.sanapeli_osa2')
    def test_07_vokaalit_perinta(self):
        from src.sanapeli import Sanapeli, EnitenVokaaleja
        self.assertTrue(issubclass(EnitenVokaaleja,Sanapeli), f"Luokan EnitenVokaaleja pitäisi " +
            'periä luokka SanaPeli!')

    @points('10.sanapeli_osa2')
    def test_08_vokaalit_metodi_uudestaan(self):
        from src.sanapeli import Sanapeli, EnitenVokaaleja
        self.assertTrue(Sanapeli.kierroksen_voittaja is not EnitenVokaaleja.kierroksen_voittaja, 
            f'Metodi kierroksen_voittaja pitää toteuttaa uudestaan luokassa ' + 
            'EnitenVokaaleja!')

    @points('10.sanapeli_osa2')
    def test_09_vokaalit_pelaa_ei_muutettu(self):
        from src.sanapeli import Sanapeli, EnitenVokaaleja
        self.assertTrue(Sanapeli.pelaa is EnitenVokaaleja.pelaa, 
            f'Metodia pelaa() ei saa toteuttaa uudestaan luokassa ' + 
            'EnitenVokaaleja!')

    @points('10.sanapeli_osa3')
    def test_11_vokaalit_toimii(self):
        test_cases = [("aaaa!","mitä","aeiou","häh",2,0), 
            ("kettu","tiikeri","laamat","kaatua","grrrrrr","hui",0,3), 
            ("tupu","hupu","mortti","vertti",0,0),
            ("auto","laiva","helikopteri","lentokone","juna","raitiovaunu",1,1)]
        for test_case in test_cases:
            from src.sanapeli import EnitenVokaaleja
            with patch('builtins.input', side_effect=list(test_case[:-2])):
                peli = EnitenVokaaleja(len(test_case)//2 - 1)
                peli.pelaa()

                output = get_stdout()
                val = [x.strip() for x in output.split("\n") if len(x.strip()) > 0][-2:]
                corr = [f"pelaaja 1: {test_case[-2]}", f"pelaaja 2: {test_case[-1]}"]

                val_str = "\n".join(val)
                corr_str = "\n".join(corr)
                test_str = "\n".join(test_case[:-2])

                self.assertEqual(val, corr, f'Pelin pitäisi tulostaa\n{corr_str}\n' + 
                    f'mutta se tulostaa\n{val_str}\nkun syöte on \n{test_str}')              
    
    @points('10.sanapeli_osa3')
    def test_12_luokka_kps_olemassa(self):
        try:
            from src.sanapeli import KiviPaperiSakset
            a = KiviPaperiSakset(1)
        except Exception as e:
            self.fail(f'Konstruktorikutsu KiviPaperiSakset(0) antoi virheen \n{e}\n' + 
            'Varmista, että luokka on määritelty.')

    @points('10.sanapeli_osa3')
    def test_13_kps_perinta(self):
        from src.sanapeli import Sanapeli, KiviPaperiSakset
        self.assertTrue(issubclass(KiviPaperiSakset,Sanapeli), f"Luokan KiviPaperiSakset pitäisi " +
            'periä luokka SanaPeli!')

    @points('10.sanapeli_osa3')
    def test_14_kps_metodi_uudestaan(self):
        from src.sanapeli import Sanapeli, KiviPaperiSakset
        self.assertTrue(Sanapeli.kierroksen_voittaja is not KiviPaperiSakset.kierroksen_voittaja, 
            f'Metodi kierroksen_voittaja pitää toteuttaa uudestaan luokassa ' + 
            'KiviPaperiSakset!')

    @points('10.sanapeli_osa3')
    def test_15_kps_pelaa_ei_muutettu(self):
        from src.sanapeli import Sanapeli, KiviPaperiSakset
        self.assertTrue(Sanapeli.pelaa is KiviPaperiSakset.pelaa, 
            f'Metodia pelaa() ei saa toteuttaa uudestaan luokassa ' + 
            'KiviPaperiSakset!')

    @points('10.sanapeli_osa3')
    def test_16_kps_toimii(self):
        test_cases = [("kivi","sakset","paperi","kivi","sakset","paperi",3,0), 
            ("paperi","sakset","kivi","paperi",0,2), 
            ("kivi","kivi","paperi","paperi","sakset","sakset",0,0),
            ("kivi","laiva","dynamiitti","sakset","auto","mopo",1,1)]
        for test_case in test_cases:
            from src.sanapeli import KiviPaperiSakset
            with patch('builtins.input', side_effect=list(test_case[:-2])):
                peli = KiviPaperiSakset(len(test_case)//2 - 1)
                peli.pelaa()

                output = get_stdout()
                val = [x.strip() for x in output.split("\n") if len(x.strip()) > 0][-2:]
                corr = [f"pelaaja 1: {test_case[-2]}", f"pelaaja 2: {test_case[-1]}"]

                val_str = "\n".join(val)
                corr_str = "\n".join(corr)
                test_str = "\n".join(test_case[:-2])

                self.assertEqual(val, corr, f'Pelin pitäisi tulostaa\n{corr_str}\n' + 
                    f'mutta se tulostaa\n{val_str}\nkun syöte on \n{test_str}')
    
    
if __name__ == '__main__':
    unittest.main()
