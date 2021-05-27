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

@points('11.tilauskirjasovellus_osa2')
class Tilauskirjasovellus2Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=["0"]):
           cls.module = load_module(exercise, 'fi')

    def test_1_tuntumaara_ei_int(self):
        syote = [
            "1", "koodaa uusi facebook", "joona x", 
            "0"
        ]
        with patch('builtins.input', side_effect=syote):
            try:
                reload_module(self.module)
            except:
                self.fail(f"varmista että ohjelma toimii syötteellä\n{s(syote)}")

            output = get_stdout()
            odotettu = "virheellinen syöte"
            self.assertTrue(odotettu in output, f"Ohjelmasi tulostuksessa pitäisi olla\n{odotettu}\nsyötteellä\n{s(syote)}\nTulostus oli\n{output}")   

    def test_2_tuntumaara_puuttuu(self):
        syote = [
            "1", "koodaa uusi facebook", "joona", 
            "0"
        ]
        with patch('builtins.input', side_effect=syote):
            try:
                reload_module(self.module)
            except:
                self.fail(f"varmista että ohjelma toimii syötteellä\n{s(syote)}")

            output = get_stdout()
            odotettu = "virheellinen syöte"
            self.assertTrue(odotettu in output, f"Ohjelmasi tulostuksessa pitäisi olla\n{odotettu}\nsyötteellä\n{s(syote)}\nTulostus oli\n{output}")   

    def test_3_lisays_onnistuu_virheen_jalkeen(self):
        syote = [
            "1", "koodaa uusi facebook", "joona",
            "1", "koodaa uusi facebook", "joona 10", 
            "3",
            "0"
        ]
        with patch('builtins.input', side_effect=syote):
            try:
                reload_module(self.module)
            except:
                self.fail(f"varmista että ohjelma toimii syötteellä\n{s(syote)}")

            output = get_stdout()
            odotettu = "virheellinen syöte"
            self.assertTrue(odotettu in output, f"Ohjelmasi tulostuksessa pitäisi olla\n{odotettu}\nsyötteellä\n{s(syote)}\nTulostus oli\n{output}")   
            odotettu = "lisätty"
            self.assertTrue(odotettu in output, f"Ohjelmasi tulostuksessa pitäisi olla\n{odotettu}\nsyötteellä\n{s(syote)}\nTulostus oli\n{output}")   
            odotettu = tt("koodaa uusi facebook", "joona 10", False)
            self.assertTrue(odotettu in output, f"Ohjelmasi tulostuksessa pitäisi olla\n{odotettu}\nsyötteellä\n{s(syote)}\nTulostus oli\n{output}")  

    def test_4_merkitese_valmiiksi_ei_int(self):
        syote = [
            "1", "koodaa uusi facebook", "joona 10", 
            "4", "xx",
            "0"
        ]
        with patch('builtins.input', side_effect=syote):
            try:
                reload_module(self.module)
            except:
                self.fail(f"varmista että ohjelma toimii syötteellä\n{s(syote)}")

            output = get_stdout()
            odotettu = "virheellinen syöte"
            self.assertTrue(odotettu in output, f"Ohjelmasi tulostuksessa pitäisi olla\n{odotettu}\nsyötteellä\n{s(syote)}\nTulostus oli\n{output}")

            eiodotettu = "merkitty valmiiksi"
            self.assertFalse(eiodotettu in output, f"Ohjelmasi tulostuksessa ei saa olla\n{eiodotettu}\nsyötteellä\n{s(syote)}\nTulostus oli\n{output}")   


    def test_5_merkitese_valmiiksi_ei_olemassa(self):
        syote = [
            "1", "koodaa uusi facebook", "joona 10", 
            "4", "100",
            "0"
        ]
        with patch('builtins.input', side_effect=syote):
            try:
                reload_module(self.module)
            except:
                self.fail(f"varmista että ohjelma toimii syötteellä\n{s(syote)}")

            output = get_stdout()
            odotettu = "virheellinen syöte"
            self.assertTrue(odotettu in output, f"Ohjelmasi tulostuksessa pitäisi olla\n{odotettu}\nsyötteellä\n{s(syote)}\nTulostus oli\n{output}")

            eiodotettu = "merkitty valmiiksi"
            self.assertFalse(eiodotettu in output, f"Ohjelmasi tulostuksessa ei saa olla\n{eiodotettu}\nsyötteellä\n{s(syote)}\nTulostus oli\n{output}")   

    def test_5_merkitese_valmiiksi_toipuu_virheesta(self):
        syote = [
            "1", "koodaa uusi facebook", "joona 10", 
            "4", "100",
            "4", "1",
            "0"
        ]
        with patch('builtins.input', side_effect=syote):
            try:
                reload_module(self.module)
            except:
                self.fail(f"varmista että ohjelma toimii syötteellä\n{s(syote)}")

            output = get_stdout()
            odotettu = "virheellinen syöte"
            self.assertTrue(odotettu in output, f"Ohjelmasi tulostuksessa pitäisi olla\n{odotettu}\nsyötteellä\n{s(syote)}\nTulostus oli\n{output}")

            odotettu = "merkitty valmiiksi"
            self.assertTrue(odotettu in output, f"Ohjelmasi tulostuksessa pitäisi olla\n{odotettu}\nsyötteellä\n{s(syote)}\nTulostus oli\n{output}")

    def test_6_tuntematon_koodari(self):
        syote = [
            "1", "koodaa uusi facebook", "joona 10", 
            "6", "Brian",
            "0"
        ]
        with patch('builtins.input', side_effect=syote):
            try:
                reload_module(self.module)
            except:
                self.fail(f"varmista että ohjelma toimii syötteellä\n{s(syote)}")

            output = get_stdout()
            odotettu = "virheellinen syöte"
            self.assertTrue(odotettu in output, f"Ohjelmasi tulostuksessa pitäisi olla\n{odotettu}\nsyötteellä\n{s(syote)}\nTulostus oli\n{output}")