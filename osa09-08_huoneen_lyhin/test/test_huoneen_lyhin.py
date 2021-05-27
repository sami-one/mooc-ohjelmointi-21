import unittest
from unittest.mock import patch

from tmc import points, reflect
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import os.path
import textwrap
from random import choice, randint
from datetime import date

exercise = 'src.huoneen_lyhin'

def f(attr: list):
    return ",".join([str(x) for x in attr]) 


class HuoneenLyhinTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=[AssertionError("Syötteen pyytämistä ei odotettu")]):
           cls.module = load_module(exercise, 'fi')

    @points('9.huoneen_lyhin_osa1')
    def test_0a_paaohjelma_kunnossa(self):
        ok, line = check_source(self.module)
        message = """Funktioita testaava koodi tulee sijoittaa lohkon
if __name__ == "__main__":
sisälle. Seuraava rivi tulee siirtää:
"""
        self.assertTrue(ok, message+line)

    @points('9.huoneen_lyhin_osa1')
    def test_1_luokat_olemassa(self):
        try:
            from src.huoneen_lyhin import Henkilo
            h = Henkilo("Keijo",150)
        except Exception as e:
            self.fail(f'Konstruktorikutsu Henkilo("Keijo",150) antoi virheen \n{e}\n' +
                'Ethän ole muuttanut luokkaa Henkilo?')

        try:
            from src.huoneen_lyhin import Huone
            h = Huone()
        except Exception as e:
            self.fail(f'Konstruktorikutsu Huone() antoi virheen \n{e}\n' +
                'Tarkista, että luokka on olemassa.')

    @points('9.huoneen_lyhin_osa1')
    def test_2_huoneen_metodit_olemassa1(self):
        from src.huoneen_lyhin import Huone, Henkilo
        huone = Huone()
        try:
            huone.lisaa(Henkilo("Keijo", 150))
        except Exception as e:
            self.fail(f'Metodikutsu lisaa(Henkilo("Keijo", 150)) aiheutti virheen\n{e}')

        try:
            val = huone.on_tyhja()
            taip = str(type(val)).replace("<class '","").replace("'>","")
            self.assertTrue(type(val) == bool, f'Metodin on_tyhja() pitäisi palauttaa arvo, ' + 
                f'jonka tyyppi on bool, nyt se palauttaa arvon {val}, jonka tyyppi on {taip}.')
        except Exception as e:
            self.fail(f'Metodikutsu on_tyhja aiheutti virheen\n{e}')

        try:
            huone.tulosta_tiedot()
        except Exception as e:
            self.fail(f'Metodikutsu tulosta_tiedot aiheutti virheen\n{e}\nkun huone on tyhjä')


    @points('9.huoneen_lyhin_osa1')
    def test_3_henkilon_lisays_tulostus(self):
        from src.huoneen_lyhin import Huone, Henkilo
        huone = Huone()
        self.assertTrue(huone.on_tyhja(), f'Metodin on_tyhja() pitäisi palauttaa True, kun huoneeseen ' + 
            'ei ole lisätty yhtään henkilöä. Nyt se palautti False.')

        test_cases = [("Arto", 180), ("Jani", 175), ("Liisa", 150), ("Kimmo", 204), ("Jaana", 171), ("Aune", 149)]
        henkilot = ""
        tested = []
        for test_case in test_cases:
            tested.append(test_case)
            huone.lisaa(Henkilo(test_case[0], test_case[1]))
            henkilot += f"\n{test_case[0]} ({test_case[1]} cm)"

            self.assertFalse(huone.on_tyhja(), f'"Metodin on_tyhja() pitäisi palauttaa False, kun huoneeseen ' +
                f'on lisätty henkilöitä - nyt se palautti True.' + 
                f'\nkun seuraavat henkilöt on lisätty huoneeseen:\n{henkilot}\n')

            huone.tulosta_tiedot()
            output = get_stdout()

            for t in tested:
                self.assertTrue(t[0] in output and str(t[1]) in output, f'Tulosteesta pitäisi löytyä merkkijonot\n' +
                    f'{t[0]} ja {t[1]}\nkun seuraavat henkilöt on lisätty huoneeseen:\n{henkilot}\n' + 
                    f'nyt tuloste on\n{output}')
            


    @points('9.huoneen_lyhin_osa2')
    def test_4_metodi_lyhin_olemassa(self):
        from src.huoneen_lyhin import Huone, Henkilo
        huone = Huone()
        try:
            val = huone.lyhin()
            taip = str(type(val)).replace("<class '","").replace("'>","")
            self.assertTrue(val is None, f'Metodin lyhin pitäisi palauttaa arvo None, ' + 
                f'kun huone on tyhjä, nyt se palauttaa arvon {val}, jonka tyyppi on {taip}.')
        except Exception as e:
            self.fail('Metodikutsu lyhin aiheutti virheen\n{e}\n' + 
                'kun huone on tyhjä.')
        
        try:
            huone.lisaa(Henkilo("Anu",120))
            huone.lisaa(Henkilo("Pena",150))
            val = huone.lyhin()
            taip = str(type(val)).replace("<class '","").replace("'>","")
            self.assertTrue("Henkilo" in str(type(val)), f'Metodin lyhin pitäisi palauttaa arvo, ' + 
                f'jonka tyyppi on Henkilo, nyt se palauttaa arvon {val}, jonka tyyppi on {taip}.' + 
                f'kun huoneeseen on lisätty seuraavat henkilöt:\n' +
                'Henkilo("Anu",120)\n' +
                'Henkilo("Pena",150)')
        except Exception as e:
            self.fail(f'Metodikutsu lyhin aiheutti virheen\n{e}\n'+ 
                f'kun huoneeseen on lisätty seuraavat henkilöt:\n' +
                'Henkilo("Anu",120)\n' +
                'Henkilo("Pena",150)')

    @points('9.huoneen_lyhin_osa2')
    def test_5_testaa_lyhin(self):
        from src.huoneen_lyhin import Huone, Henkilo
        huone = Huone()
        test_cases = [("Arto", 180), ("Jani", 175), ("Liisa", 150), ("Kimmo", 204), ("Jaana", 171), ("Aune", 149)]

        henkilot = ""
        tested = []
        for test_case in test_cases:
            tested.append(test_case)
            huone.lisaa(Henkilo(test_case[0], test_case[1]))
            henkilot += f"\n{test_case[0]} ({test_case[1]} cm)"

            lyhin = huone.lyhin()
            taip = str(type(lyhin)).replace("<class '","").replace("'>","")
            self.assertTrue("Henkilo" in str(type(lyhin)), f'Metodin lyhin pitäisi palauttaa arvo, ' + 
                f'jonka tyyppi on Henkilo, nyt se palauttaa arvon {lyhin}, jonka tyyppi on {taip}.' + 
                f'kun huoneeseen on lisätty seuraavat henkilöt:\n{henkilot}')

            try:
                val = lyhin.nimi
            except:
                self.fail(f'Metodin lyhin() pitäisi palauttaa henkilo-olio \nNyt se ' + 
                f'palauttaa {lyhin}, jonka tyyppi on {type(lyhin)} kun seuraavat henkilöt on lisätty:{henkilot}.')                

            corr = min(tested, key = lambda x : x[1])[0]

            self.assertEqual(val, corr, f'Metodin lyhin() pitäisi palauttaa henkilo, jonka nimi on {corr}. \nNyt se ' + 
                f'palauttaa henkilön, jonka nimi on {val}, kun seuraavat henkilöt on lisätty:{henkilot}.')

    @points('9.huoneen_lyhin_osa3')
    def test_6_metodi_poista_lyhin_olemassa(self):
        from src.huoneen_lyhin import Huone, Henkilo
        huone = Huone()
        try:
            val = huone.poista_lyhin()
            taip = str(type(val)).replace("<class '","").replace("'>","")
            self.assertTrue(val is None, f'Metodin poista_lyhin pitäisi palauttaa arvo None, ' + 
                f'kun huone on tyhjä, nyt se palauttaa arvon {val}, jonka tyyppi on {taip}.')
        except Exception as e:
            self.fail('Metodikutsu poista_lyhin aiheutti virheen\n{e}' + 
                'kun huone on tyhjä.')
        
        try:
            huone.lisaa(Henkilo("Anu",120))
            huone.lisaa(Henkilo("Pena",150))
            val = huone.poista_lyhin()
            taip = str(type(val)).replace("<class '","").replace("'>","")
            self.assertTrue("Henkilo" in str(type(val)), f'Metodin poista_lyhin pitäisi palauttaa arvo, ' + 
                f'jonka tyyppi on Henkilo, nyt se palauttaa arvon {val}, jonka tyyppi on {taip}.' + 
                f'kun huoneeseen on lisätty seuraavat henkilöt:\n' +
                'Henkilo("Anu",120)\n' +
                'Henkilo("Pena",150)')
        except Exception as e:
            self.fail('Metodikutsu poista_lyhin aiheutti virheen\n{e}\n'+ 
                f'kun huoneeseen on lisätty seuraavat henkilöt:\n' +
                'Henkilo("Anu",120)\n' +
                'Henkilo("Pena",150)')

    @points('9.huoneen_lyhin_osa3')
    def test_7_testaa_poista_lyhin(self):
        from src.huoneen_lyhin import Huone, Henkilo
        huone = Huone()
        test_cases = [("Arto", 180), ("Jani", 175), ("Liisa", 150), ("Kimmo", 204), ("Jaana", 171), ("Aune", 149)]

        tested = []
        henkilot = ""
        for test_case in test_cases:
            huone.lisaa(Henkilo(test_case[0], test_case[1]))
            henkilot += f"\n{test_case[0]} ({test_case[1]} cm)"
            tested.append(test_case)
        
        prev_output = ""
        for i in range(len(test_cases)):
            val = huone.poista_lyhin()
            corr = min(tested, key = lambda x : x[1])
            
            self.assertEqual(val.nimi, corr[0], f'Metodin poista_lyhin() pitäisi palauttaa henkilo, jonka nimi on {corr[0]}. \nNyt se ' + 
                f'palauttaa henkilön, jonka nimi on {val.nimi}, kun seuraavat henkilöt olivat huoneessa {tested}.')
            
            tested.remove(corr)

            huone.tulosta_tiedot()
            output = get_stdout().replace(prev_output, "")
            prev_output += output
            output_list = [x for x in output.split("\n") if len(x.strip()) > 0 and not x.startswith("Huoneessa")]

            self.assertEqual(len(output_list), len(tested), f'Huoneessa pitäisi olla nyt {len(tested)} henkilöä, kun seuraavat henkilöt lisättiin:' +
                f'{henkilot}\nja metodia poista_lyhin on kutsuttu {i + 1} kertaa.\nNyt metodi tulosta_tiedot kuitenkin tulostaa\n{output}')
            
if __name__ == '__main__':
    unittest.main()
