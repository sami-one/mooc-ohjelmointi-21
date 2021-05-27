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

class MatkalaukkuTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=[AssertionError("Syötteen pyytämistä ei odotettu")]):
           cls.module = load_module(exercise, 'fi')

    @points('8.tavara_matkalaukku_lastiruuma_osa2')
    def test1_matkalaukku_olemassa(self):
        try:
            from src.koodi import Matkalaukku
        except:
            self.assertTrue(False, "Ohjelmastasi pitäisi löytyä luokka nimeltä Matkalaukku")

    @points('8.tavara_matkalaukku_lastiruuma_osa2')
    def test2_matkalaukku_konstruktori(self):
        try:
            from src.koodi import Matkalaukku
            laukku = Matkalaukku(25)
        except Exception as e:
            self.assertTrue(False, 'Luokan Tavara konstuktorin kutsuminen arvoilla Matkalaukku(25)' +
                f' palautti virheen: {e}\nVarmista että konstruktori on määritelty oikein')

    @points('8.tavara_matkalaukku_lastiruuma_osa2')
    def test3_tyhja_matkalaukku_str(self):
            from src.koodi import Matkalaukku
            laukku = Matkalaukku(25)

            corr1 = "0 tavaraa (0 kg)"
            val = str(laukku)

            self.assertTrue(corr1 == val, f"Metodin __str__ pitäisi palauttaa merkkijono\n{corr1}\nkun olio luotiin kutsulla\n" + 
                f'Matkalaukku(25)\nNyt metodi palauttaa merkkijonon\n{val}')

    @points('8.tavara_matkalaukku_lastiruuma_osa2')
    def test4_matkalaukku_lisaa_tavara(self):
        try:
            from src.koodi import Tavara
            from src.koodi import Matkalaukku
            koodi = """
laukku = Matkalaukku(25)
tavara = Tavara("Aapiskukko", 2)
laukku.lisaa_tavara(tavara)
"""
            tavara = Tavara("Aapiskukko", 2)
            laukku = Matkalaukku(25)
            laukku.lisaa_tavara(tavara)

        except Exception as e:
            self.assertTrue(False, f'Koodin\n{koodi}\nsuoritus aiheutti virheen\n{e}\nOnhan metodi lisaa_tavara(self, tavara) määritelty?')

        corr0 = "1 tavaraa (2 kg)"
        corr1 = "1 tavara (2 kg)"
        val = str(laukku)

        self.assertTrue(corr1 == val or corr0 == val, f"Matkalaukun metodin __str__ pitäisi palauttaa merkkijono\n{corr1}\nkun on suoritetu koodi\n{koodi}\n" + 
            f'Nyt metodi palauttaa merkkijonon\n{val}')       

        corr0 = "1 tavaraa (2 kg)"
        corr1 = "1 tavara (2 kg)"
        val = str(laukku)

        self.assertTrue(corr1 == val or corr0 == val, f"Matkalaukun metodin __str__ pitäisi palauttaa merkkijono\n{corr1}\nkun on suoritetu koodi\n{koodi}\n" + 
            f'Nyt metodi palauttaa merkkijonon\n{val}')       

        tavara2 = Tavara("Tiiliskivi", 5)
        try:
            laukku.lisaa_tavara(tavara2)
        except:
            self.fail(f"Varmista että seuraavan koodin suorittaminen onnistuu\n{koodi}")

        koodi += """tavara2 = Tavara("Tiiliskivi", 5)
laukku.lisaa_tavara(tavara2)
"""

        corr1 = "2 tavaraa (7 kg)"
        val = str(laukku)

        self.assertTrue(corr1 == val, f"Matkalaukun metodin __str__ pitäisi palauttaa merkkijono\n{corr1}\nkun on suoritetu koodi\n{koodi}\n" + 
            f'Nyt metodi palauttaa merkkijonon\n{val}')               

        tavara3 = Tavara("iPhone", 1)
        laukku.lisaa_tavara(tavara3)

        koodi += """tavara3 = Tavara("iPhone", 1)
laukku.lisaa_tavara(tavara3)
"""

        corr1 = "3 tavaraa (8 kg)"
        val = str(laukku)

        self.assertTrue(corr1 == val, f"Matkalaukun metodin __str__ pitäisi palauttaa merkkijono\n{corr1}\nkun on suoritetu koodi\n{koodi}\n" + 
            f'Nyt metodi palauttaa merkkijonon\n{val}')               

    @points('8.tavara_matkalaukku_lastiruuma_osa2')
    def test5_matkalaukkuun_ei_voi_lisata_liikaa(self):
        from src.koodi import Tavara
        from src.koodi import Matkalaukku
        koodi = """
laukku = Matkalaukku(4)
tavara = Tavara("Tietosanakirja", 5)
laukku.lisaa_tavara(tavara)
"""

        laukku = Matkalaukku(4)
        tavara = Tavara("Tietosanakirja", 5)
        laukku.lisaa_tavara(tavara)

        corr1 = "0 tavaraa (0 kg)"
        val = str(laukku)

        self.assertTrue(corr1 == val, f"Matkalaukun metodin __str__ pitäisi palauttaa merkkijono\n{corr1}\nkun on suoritetu koodi\n{koodi}\n" + 
            f'Nyt metodi palauttaa merkkijonon\n{val}\nHuomaa, että matkalaukkuun ei saa lisätä sen kapasiteettia enempää tavaraa!')       

        koodi = """
laukku = Matkalaukku(3)
tavara1 = Tavara("Kivi", 1)
tavara2 = Tavara("Maitotölkki", 1)
laukku.lisaa_tavara(tavara1)
laukku.lisaa_tavara(tavara2)
tavara3 = Tavara("Vasara", 2)
laukku.lisaa_tavara(tavara3)
"""    

        laukku = Matkalaukku(3)
        tavara1 = Tavara("Kivi", 1)
        tavara2 = Tavara("Maitotölkki", 1)
        laukku.lisaa_tavara(tavara1)
        laukku.lisaa_tavara(tavara2)
        tavara3 = Tavara("Vasara", 2)
        laukku.lisaa_tavara(tavara3)

        corr1 = "2 tavaraa (2 kg)"
        val = str(laukku)

        self.assertTrue(corr1 == val, f"Matkalaukun metodin __str__ pitäisi palauttaa merkkijono\n{corr1}\nkun on suoritetu koodi\n{koodi}\n" + 
            f'Nyt metodi palauttaa merkkijonon\n{val}\nHuomaa, että matkalaukkuun ei saa lisätä sen kapasiteettia enempää tavaraa!')       

    @points('8.tavara_matkalaukku_lastiruuma_osa3')
    def test6_matkalaukku_missa_yksi_tavara(self):

        from src.koodi import Tavara
        from src.koodi import Matkalaukku
        koodi = """
laukku = Matkalaukku(25)
tavara = Tavara("Aapiskukko", 2)
laukku.lisaa_tavara(tavara)
"""
        tavara = Tavara("Aapiskukko", 2)
        laukku = Matkalaukku(25)
        laukku.lisaa_tavara(tavara)

        corr1 = "1 tavara (2 kg)"
        val = str(laukku)

        self.assertTrue(corr1 == val, f"Matkalaukun metodin __str__ pitäisi palauttaa merkkijono\n{corr1}\nkun on suoritetu koodi\n{koodi}\n" + 
            f'Nyt metodi palauttaa merkkijonon\n{val}\nLue tarkasti osan 3 tehtävänanot!')    

    @points('8.tavara_matkalaukku_lastiruuma_osa4')
    def test6_matkalaukku_paino(self):
        try:
            from src.koodi import Tavara
            from src.koodi import Matkalaukku
            koodi = """
laukku = Matkalaukku(25)
tavara = Tavara("Aapiskukko", 2)
laukku.lisaa_tavara(tavara)
laukku.paino()
"""

            laukku = Matkalaukku(25)
            tavara = Tavara("Aapiskukko", 2)
            laukku.lisaa_tavara(tavara)
            paino = laukku.paino()

        except Exception as e:
            self.assertTrue(False, f'Koodin\n{koodi}\nsuoritus aiheutti virheen\n{e}\nOnhan metodi paino(self) määritelty?')
         
        self.assertTrue(paino == 2, f'Kun suoritetaan\n{koodi}\nmetodin pitäsi palauttaa 2, paluuarvo oli {paino}')

        koodi = """
laukku = Matkalaukku(25)
tavara1 = Tavara("Kivi", 1)
tavara2 = Tavara("Maitotölkki", 1)
laukku.lisaa_tavara(tavara1)
laukku.lisaa_tavara(tavara2)
tavara3 = Tavara("Vasara", 2)
laukku.lisaa_tavara(tavara3)
paino = laukku.paino()
"""

        laukku = Matkalaukku(25)
        tavara1 = Tavara("Kivi", 1)
        tavara2 = Tavara("Maitotölkki", 1)
        laukku.lisaa_tavara(tavara1)
        laukku.lisaa_tavara(tavara2)
        tavara3 = Tavara("Vasara", 2)
        laukku.lisaa_tavara(tavara3)
        paino = laukku.paino()
        self.assertTrue(paino == 4, f'Kun suoritetaan\n{koodi}\nmetodin pitäsi palauttaa 4, paluuarvo oli {paino}')

    @points('8.tavara_matkalaukku_lastiruuma_osa4')
    def test6_matkalaukku_tulosta_tavarat(self):
        try:
            from src.koodi import Tavara
            from src.koodi import Matkalaukku
            koodi = """
laukku = Matkalaukku(25)
tavara = Tavara("Aapiskukko", 2)
laukku.lisaa_tavara(tavara)
laukku.tulosta_tavarat()
"""

            laukku = Matkalaukku(25)
            tavara = Tavara("Aapiskukko", 2)
            laukku.lisaa_tavara(tavara)
            laukku.tulosta_tavarat()

        except Exception as e:
            self.assertTrue(False, f'Koodin\n{koodi}\nsuoritus aiheutti virheen\n{e}\nOnhan metodi tulosta_tavarat(self) määritelty?')
         
        out = get_stdout()
        self.assertTrue(0<len(out), f'Kun suoritetaan\n{koodi}\nmetodin pitäsi tulostaa yksi rivi\nNyt ei tulosteta mitään')
       
        lines = [x for x in out.split('\n') if len(x)>0]
        self.assertTrue(1 == len(lines), f'Kun suoritetaan\n{koodi}\nmetodin pitäsi tulostaa yksi rivi\nTulostus oli\n{out}')

        odotettu = "Aapiskukko (2 kg)"
        self.assertTrue(out == odotettu, f'Kun suoritetaan\n{koodi}\nmetodin pitäsi tulostaa\n{odotettu}\nTulostus oli\n{out}')

    @points('8.tavara_matkalaukku_lastiruuma_osa4')
    def test7_matkalaukku_tulosta_tavarat2(self):
        try:
            from src.koodi import Tavara
            from src.koodi import Matkalaukku
            koodi = """
laukku = Matkalaukku(25)
tavara1 = Tavara("Kivi", 1)
tavara2 = Tavara("Maitotölkki", 1)
laukku.lisaa_tavara(tavara1)
laukku.lisaa_tavara(tavara2)
tavara3 = Tavara("Vasara", 2)
laukku.lisaa_tavara(tavara3)
"""

            laukku = Matkalaukku(25)
            tavara1 = Tavara("Kivi", 1)
            tavara2 = Tavara("Maitotölkki", 1)
            laukku.lisaa_tavara(tavara1)
            laukku.lisaa_tavara(tavara2)
            tavara3 = Tavara("Vasara", 2)
            laukku.lisaa_tavara(tavara3)
            laukku.tulosta_tavarat()

        except Exception as e:
            self.assertTrue(False, f'Koodin\n{koodi}\nsuoritus aiheutti virheen\n{e}\nOnhan metodi tulosta_tavarat(self) määritelty?')
         
        out = get_stdout()
        lines = [x for x in out.split('\n') if len(x)>0]
        self.assertTrue(3 == len(lines), f'Kun suoritetaan\n{koodi}\nmetodin pitäsi tulostaa kolme riviä\nTulostus oli\n{out}')

        tt = [ f"{t}" for t in [tavara1, tavara2, tavara3]]
        odotettu = "\n".join(tt)

        self.assertTrue(sorted(lines) == sorted(tt), f'Kun suoritetaan\n{koodi}\nmetodin pitäsi tulostaa\n{odotettu}\nTulostus oli\n{out}')

    @points('8.tavara_matkalaukku_lastiruuma_osa5')
    def test9_matkalaukku_raskain_tavara(self):
        try:
            from src.koodi import Tavara
            from src.koodi import Matkalaukku
            koodi = """
laukku = Matkalaukku(25)
tavara = Tavara("Aapiskukko", 2)
laukku.lisaa_tavara(tavara)
laukku.raskain_tavara()
"""

            laukku = Matkalaukku(25)
            tavara = Tavara("Aapiskukko", 2)
            laukku.lisaa_tavara(tavara)
            try:
                r = laukku.raskain_tavara()
            except:
                self.fail(f"Varmista että seuraavan koodin suorittaminen onnistuu\n{koodi}")

        except Exception as e:
            self.assertTrue(False, f'Koodin\n{koodi}\nsuoritus aiheutti virheen\n{e}\nOnhan metodi raskain_tavara(self) määritelty?')
        
        try:
           r.nimi() 
        except:
            koodi2 = """
laukku = Matkalaukku(25)
tavara = Tavara("Aapiskukko", 2)
laukku.lisaa_tavara(tavara)
raskain = laukku.raskain_tavara()
print(raskain.nimi())
"""
            self.fail(f"Palauttaahan metodi raskain_tavara(self) oikean tyyppisen olion? Varmista että seuraavan koodin suorittaminen onnistuu\n{koodi2}")

        self.assertTrue(r.nimi() == "Aapiskukko", f'Kun suoritetaan\n{koodi}\nmetodin pitäsi palauttaa {tavara}, paluuarvo oli {r}')

    @points('8.tavara_matkalaukku_lastiruuma_osa5')
    def test10_matkalaukku_raskain_tavara_2(self):
        from src.koodi import Tavara
        from src.koodi import Matkalaukku
        koodi = """
laukku = Matkalaukku(25)
tavara1 = Tavara("Aapiskukko", 2)
laukku.lisaa_tavara(tavara1)
tavara2 = Tavara("Moukari", 10)
laukku.lisaa_tavara(tavara2)
tavara3 = Tavara("Kivi", 3)
laukku.lisaa_tavara(tavara3)
laukku.raskain_tavara()
"""

        laukku = Matkalaukku(25)
        tavara1 = Tavara("Aapiskukko", 2)
        laukku.lisaa_tavara(tavara1)
        tavara2 = Tavara("Moukari", 10)
        laukku.lisaa_tavara(tavara2)
        tavara3 = Tavara("Kivi", 3)
        laukku.lisaa_tavara(tavara3)
        try:
            r = laukku.raskain_tavara()
        except:
            self.fail(f"Varmista että seuraavan koodin suorittaminen onnistuu\n{koodi}")

        self.assertTrue(r.nimi() == "Moukari", f'Kun suoritetaan\n{koodi}\nmetodin pitäsi palauttaa {tavara2}, paluuarvo oli {r}')

if __name__ == '__main__':
    unittest.main()
