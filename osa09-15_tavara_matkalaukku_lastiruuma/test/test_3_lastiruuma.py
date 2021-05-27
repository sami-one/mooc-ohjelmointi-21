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

class LastiruumaTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=[AssertionError("Syötteen pyytämistä ei odotettu")]):
           cls.module = load_module(exercise, 'fi')

    @points('8.tavara_matkalaukku_lastiruuma_osa6')
    def test1_lastiruuma_olemassa(self):
        try:
            from src.koodi import Lastiruuma
        except:
            self.assertTrue(False, "Ohjelmastasi pitäisi löytyä luokka nimeltä Lastiruuma")

    @points('8.tavara_matkalaukku_lastiruuma_osa6')
    def test2_lastiruuma_konstruktori(self):
        try:
            from src.koodi import Lastiruuma
            ruuma = Lastiruuma(100)
        except Exception as e:
            self.assertTrue(False, 'Luokan Tavara konstuktorin kutsuminen arvoilla Lastiruuma(100)' +
                f' palautti virheen: {e}\nVarmista että konstruktori on määritelty oikein')

    @points('8.tavara_matkalaukku_lastiruuma_osa6')
    def test3_tyhja_ruuma_str(self):
            from src.koodi import Lastiruuma
            ruuma = Lastiruuma(100)

            corr1 = "0 matkalaukkua, tilaa 100 kg"
            val = str(ruuma)

            self.assertTrue(corr1 == val, f"Metodin __str__ pitäisi palauttaa merkkijono\n{corr1}\nkun olio luotiin kutsulla\n" + 
                f'Lastiruuma(100)\nNyt metodi palauttaa merkkijonon\n{val}')

    @points('8.tavara_matkalaukku_lastiruuma_osa6')
    def test4_ruuma_lisaa_tavara(self):
        try:
            from src.koodi import Tavara
            from src.koodi import Matkalaukku
            from src.koodi import Lastiruuma
            ruuma = Lastiruuma(100)
            koodi = """
ruuma = Lastiruuma(100)
laukku = Matkalaukku(25)
tavara = Tavara("Aapiskukko", 2)
laukku.lisaa_tavara(tavara)
ruuma.lisaa_matkalaukku(laukku)
"""
            ruuma = Lastiruuma(100)
            laukku = Matkalaukku(25)
            tavara = Tavara("Aapiskukko", 2)
            laukku.lisaa_tavara(tavara)
            ruuma.lisaa_matkalaukku(laukku)

        except Exception as e:
            self.assertTrue(False, f'Koodin\n{koodi}\nsuoritus aiheutti virheen\n{e}\nOnhan metodi lisaa_matkalaukku(self, laukku) määritelty?')

        corr1 = "1 matkalaukku, tilaa 98 kg"
        val = str(ruuma)

        self.assertTrue(corr1 == val, f"Metodin __str__ pitäisi palauttaa merkkijono\n{corr1}\nkun on suoritetu koodi\n{koodi}\n" + 
            f'Nyt metodi palauttaa merkkijonon\n{val}')     

        koodi = """
ruuma = Lastiruuma(50)
laukku = Matkalaukku(25)
tavara = Tavara("Aapiskukko", 2)
laukku.lisaa_tavara(tavara)
ruuma.lisaa_matkalaukku(laukku)
laukku2 = Matkalaukku(10)
laukku2.lisaa_tavara(Tavara("Kivi", 1))
laukku2.lisaa_tavara(Tavara("Hiiri", 2))
ruuma.lisaa_matkalaukku(laukku2)
"""

        ruuma = Lastiruuma(50)
        laukku = Matkalaukku(25)
        tavara = Tavara("Aapiskukko", 2)
        laukku.lisaa_tavara(tavara)
        ruuma.lisaa_matkalaukku(laukku)
        laukku2 = Matkalaukku(10)
        laukku2.lisaa_tavara(Tavara("Kivi", 1))
        laukku2.lisaa_tavara(Tavara("Hiiri", 2))
        ruuma.lisaa_matkalaukku(laukku2)

        corr1 = "2 matkalaukkua, tilaa 45 kg"
        val = str(ruuma)

        self.assertTrue(corr1 == val, f"Metodin __str__ pitäisi palauttaa merkkijono\n{corr1}\nkun on suoritetu koodi\n{koodi}\n" + 
            f'Nyt metodi palauttaa merkkijonon\n{val}')     

    @points('8.tavara_matkalaukku_lastiruuma_osa6')
    def test_5_ruumaan_ei_mene_liikaa(self):
        try:
            from src.koodi import Tavara
            from src.koodi import Matkalaukku
            from src.koodi import Lastiruuma
            ruuma = Lastiruuma(100)
            koodi = """
ruuma = Lastiruuma(10)
laukku = Matkalaukku(25)
tavara = Tavara("Alasin", 24)
laukku.lisaa_tavara(tavara)
ruuma.lisaa_matkalaukku(laukku)
"""
            ruuma = Lastiruuma(10)
            laukku = Matkalaukku(25)
            tavara = Tavara("Alasin", 24)
            laukku.lisaa_tavara(tavara)
            ruuma.lisaa_matkalaukku(laukku)

        except Exception as e:
            self.assertTrue(False, f'Koodin\n{koodi}\nsuoritus aiheutti virheen\n{e}\nOnhan metodi lisaa_matkalaukku(self, laukku) määritelty?')

        corr1 = "0 matkalaukkua, tilaa 10 kg"
        val = str(ruuma)

        self.assertTrue(corr1 == val, f"Metodin __str__ pitäisi palauttaa merkkijono\n{corr1}\nkun on suoritetu koodi\n{koodi}\n" + 
            f'Nyt metodi palauttaa merkkijonon\n{val}\nHuomaa, että lastiruumaan ei saa laittaa liikaa tavaraa!')    

    @points('8.tavara_matkalaukku_lastiruuma_osa7')
    def test_6_tulosta_tavarat_ruumasta(self):
        try:
            from src.koodi import Tavara
            from src.koodi import Matkalaukku
            from src.koodi import Lastiruuma
            ruuma = Lastiruuma(100)
            koodi = """
ruuma = Lastiruuma(100)
laukku = Matkalaukku(25)
tavara = Tavara("Aapiskukko", 2)
laukku.lisaa_tavara(tavara)
ruuma.lisaa_matkalaukku(laukku)
ruuma.tulosta_tavarat()
"""
            ruuma = Lastiruuma(100)
            laukku = Matkalaukku(25)
            tavara = Tavara("Aapiskukko", 2)
            laukku.lisaa_tavara(tavara)
            ruuma.lisaa_matkalaukku(laukku)
            ruuma.tulosta_tavarat()

        except Exception as e:
            self.assertTrue(False, f'Koodin\n{koodi}\nsuoritus aiheutti virheen\n{e}\nOnhan metodi tulosta_tavarat(self) määritelty?')

        out = get_stdout()
        self.assertTrue(0<len(out), f'Kun suoritetaan\n{koodi}\nmetodin pitäsi tulostaa yksi rivi\nNyt ei tulosteta mitään')
       
        lines = [x for x in out.split('\n') if len(x)>0]
        self.assertTrue(1 == len(lines), f'Kun suoritetaan\n{koodi}\nmetodin pitäsi tulostaa yksi rivi\nTulostus oli\n{out}')
       
        odotettu = "Aapiskukko (2 kg)"
        self.assertTrue(out == odotettu, f'Kun suoritetaan\n{koodi}\nmetodin pitäsi tulostaa\n{odotettu}\nTulostus oli\n{out}')

    @points('8.tavara_matkalaukku_lastiruuma_osa7')
    def test_6_tulosta_tavarat_ruumasta2(self):
        try:
            from src.koodi import Tavara
            from src.koodi import Matkalaukku
            from src.koodi import Lastiruuma
            ruuma = Lastiruuma(100)
            koodi = """
ruuma = Lastiruuma(50)
laukku = Matkalaukku(25)
tavara = Tavara("Aapiskukko", 2)
laukku.lisaa_tavara(tavara)
ruuma.lisaa_matkalaukku(laukku)
laukku2 = Matkalaukku(10)
laukku2.lisaa_tavara(Tavara("Kivi", 1))
laukku2.lisaa_tavara(Tavara("Hiiri", 2))
ruuma.lisaa_matkalaukku(laukku2)
ruuma.tulosta_tavarat()
"""

            ruuma = Lastiruuma(50)
            laukku = Matkalaukku(25)
            tavara1 = Tavara("Aapiskukko", 2)
            laukku.lisaa_tavara(tavara1)
            ruuma.lisaa_matkalaukku(laukku)
            laukku2 = Matkalaukku(10)
            tavara2 = Tavara("Kivi", 1)
            laukku2.lisaa_tavara(tavara2)
            tavara3 =Tavara("Hiiri", 2)
            laukku2.lisaa_tavara(tavara3)
            ruuma.lisaa_matkalaukku(laukku2)
            ruuma.tulosta_tavarat()

        except Exception as e:
            self.assertTrue(False, f'Koodin\n{koodi}\nsuoritus aiheutti virheen\n{e}\nOnhan metodi tulosta_tavarat(self) määritelty?')

        out = get_stdout()
        self.assertTrue(0<len(out), f'Kun suoritetaan\n{koodi}\nmetodin pitäsi tulostaa yksi rivi\nNyt ei tulosteta mitään')
       
        lines = [x for x in out.split('\n') if len(x)>0]
        self.assertTrue(3 == len(lines), f'Kun suoritetaan\n{koodi}\nmetodin pitäsi tulostaa kolme riviä\nTulostus oli\n{out}')
       
        tt = [ f"{t}" for t in [tavara1, tavara2, tavara3]]
        odotettu = "\n".join(tt)
        self.assertTrue(sorted(lines) == sorted(tt), f'Kun suoritetaan\n{koodi}\nmetodin pitäsi tulostaa\n{odotettu}\nTulostus oli\n{out}')


if __name__ == '__main__':
    unittest.main()
