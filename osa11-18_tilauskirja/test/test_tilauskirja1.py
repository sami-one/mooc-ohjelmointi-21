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

def ss(l: list):
    return "\n".join([f'{s}' for s in l])

def tt(x):
    status = "EI VALMIS" if not x[3] else "VALMIS"
    return f"{x[0]} ({x[1]} tuntia), koodari {x[2]} {status}"

def ook(val, tt):
    if len(val) != len(tt):
        return False
    for v in val:
        ouk = False
        for t in tt:
            if ok(v, t[0], t[1], t[2], t[3]):
                ouk = True
        if not ouk:
            return False
    
    return True
        
def ok(tehtava, kuvaus, koodari, tyomaara, status=False):
    return tehtava.kuvaus == kuvaus and tehtava.koodari == koodari and tehtava.tyomaara == tyomaara and tehtava.on_valmis() == status

@points('11.tilauskirja_osa2')
class TilauskirjaOsa2Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=["0"]):
           cls.module = load_module(exercise, 'fi')

    def test_1_tilauskirja_olemassa(self):
        reload_module(self.module)
        try:
            from src.koodi import Tilauskirja
        except:
            self.assertTrue(False, "Ohjelmastasi pitäisi löytyä luokka nimeltä Tilauskirja")
        try:
            Tilauskirja()
        except Exception as e:
            self.assertTrue(False, 'Luokan Tilauskirja konstuktorin kutsuminen Tilauskirja()' +
                f' aiheutti virheen: {e}\nVarmista että konstruktori on määritelty oikein')
        
    def test_2_lisaa_tilaus_ja_kaikki_tilaukset_olemassa(self):
        reload_module(self.module)
        from src.koodi import Tilauskirja,  Tehtava
        koodi = """
t = Tilauskirja()
t.lisaa_tilaus("koodaa webbikauppa", "Antti", 10)
"""
        t = Tilauskirja()
        try:
            t.lisaa_tilaus("koodaa webbikauppa", "Antti", 10)
        except Exception as e:
            self.fail(f'Koodin {koodi}suoritus aiheutti virheen\n{e}\nOnhan metodi lisaa_tilaus(self, kuvaus, koodari, tyomaara) määritelty?')
        
        koodi = """
t = Tilauskirja()
t.kaikki_tilaukset()
"""
        t = Tilauskirja()
        try:
            t.kaikki_tilaukset()
        except Exception as e:
            self.fail(f'Koodin {koodi}suoritus aiheutti virheen\n{e}\nOnhan metodi kaikki_tilaukset(self) määritelty?')

        koodi = """
t = Tilauskirja()
t.lisaa_tilaus("koodaa webbikauppa", "Antti", 10)
t.kaikki_tilaukset()
"""
        t = Tilauskirja()
        t.lisaa_tilaus("koodaa webbikauppa", "Antti", 10)
        try:
            val = t.kaikki_tilaukset()
        except Exception as e:
            self.fail(f'Koodin {koodi}suoritus aiheutti virheen\n{e}\nOnhan metodi kaikki_tilaukset(self) määritelty?')

        taip = str(type(val)).replace("<class '","").replace("'>","")
        self.assertTrue(type(val) == type([]), f"Kon suoritetaan{koodi}paluuarvon pitäisi olla lista, nyt sen tyyppi on {taip}")
        odotettu = 1
        self.assertTrue(len(val)==odotettu, f"Kun suoritetaan {koodi}\npitäisi palauttaa lista, jonka pituus on {odotettu}, listan pituus oli {len(val)}")
        
        ttt = Tehtava("koodaa hello world", "Erkki", 3)
        taip = str(type(val[0])).replace("<class '","").replace("'>","")
        self.assertTrue(type(val[0]) == type(ttt), f"Kon suoritetaan{koodi}palutetun listan alkion tyypin pitäisi olla Tehtava, nyt sen tyyppi on {taip}")

    def test_3_lisaa_tilaus_ja_kaikki_tilaukset_tomii(self):
        reload_module(self.module)
        from src.koodi import Tilauskirja, Tehtava
        koodi = """
t = Tilauskirja()
t.lisaa_tilaus("koodaa webbikauppa", "Antti", 10)
t.lisaa_tilaus("tee mobiilipeli", "Erkki", 5)
t.kaikki_tilaukset()
"""
        t = Tilauskirja()
        t.lisaa_tilaus("koodaa webbikauppa", "Antti", 10)
        t.lisaa_tilaus("tee mobiilipeli", "Erkki", 5)
        try:
            val = t.kaikki_tilaukset()
        except Exception as e:
            self.fail(f'Koodin {koodi}suoritus aiheutti virheen\n{e}\nOnhan metodi kaikki_tilaukset(self) määritelty?')
        odotettu = 2
        self.assertTrue(len(val)==odotettu, f"Kun suoritetaan {koodi}\npitäisi palauttaa lista, jonka pituus on {odotettu}, listan pituus oli {len(val)}")

        t1 = ("koodaa webbikauppa", "Antti", 10, False) 
        t2 = ("tee mobiilipeli", "Erkki", 5, False) 
        all_ok = ook(val, [t1, t2])

        odotettu = s([tt(t1), tt(t2)])

        self.assertTrue(all_ok, f"Kun suoritetaan {koodi}\npitäisi palauttaa lista, jolta löytyvät seuraavat tehtävät\n{odotettu}\nnyt palautettiin\n{ss(val)}")

        koodi = """
t = Tilauskirja()
t.lisaa_tilaus("koodaa webbikauppa", "Antti", 10)
t.lisaa_tilaus("tee mobiilipeli", "Erkki", 5)
t.lisaa_tilaus("koodaa parempi facebook", "joona", 5000)
t.kaikki_tilaukset()
"""

        
        t.lisaa_tilaus("koodaa parempi facebook", "joona", 5000)
        try:
            val = t.kaikki_tilaukset()
        except Exception as e:
            self.fail(f'Koodin {koodi}suoritus aiheutti virheen\n{e}\nOnhan metodi kaikki_tilaukset(self) määritelty?')
        odotettu = 3
        self.assertTrue(len(val)==odotettu, f"Kun suoritetaan {koodi}\npitäisi palauttaa lista, jonka pituus on {odotettu}, listan pituus oli {len(val)}")

        t3 = ("koodaa parempi facebook", "joona", 5000, False)
        all_ok = ook(val, [t1, t2, t3])

        odotettu = s([tt(t1), tt(t2),  tt(t3)])

        self.assertTrue(all_ok, f"Kun suoritetaan {koodi}\npitäisi palauttaa lista, jolta löytyvät seuraavat tehtävät\n{odotettu}\nnyt palautettiin\n{ss(val)}")

    def test_3_koodarit_olemassa(self):
        reload_module(self.module)
        from src.koodi import Tilauskirja,  Tehtava
        koodi = """
t = Tilauskirja()
t.koodarit()
"""
        t = Tilauskirja()
        try:
            val = t.koodarit()
        except Exception as e:
            self.fail(f'Koodin {koodi}suoritus aiheutti virheen\n{e}\nOnhan metodi koodarit(self) määritelty?')
        
        taip = str(type(val)).replace("<class '","").replace("'>","")
        self.assertTrue(type(val) == type([]), f"Kon suoritetaan{koodi}paluuarvon pitäisi olla lista, nyt sen tyyppi on {taip}")
        odotettu = 0
        self.assertTrue(len(val)==odotettu, f"Kun suoritetaan {koodi}\npitäisi palauttaa lista, jonka pituus on {odotettu}, listan pituus oli {len(val)}")

    def test_3_koodarit_toimii(self):
        from src.koodi import Tilauskirja,  Tehtava

        koodi = """
t = Tilauskirja()
t.lisaa_tilaus("koodaa webbikauppa", "Antti", 10)
t.lisaa_tilaus("tee mobiilipeli", "Erkki", 5)
t.koodarit()
"""   
        t = Tilauskirja()
        t.lisaa_tilaus("koodaa webbikauppa", "Antti", 10)
        t.lisaa_tilaus("tee mobiilipeli", "Erkki", 5)
        try:
            val = t.koodarit()
        except Exception as e:
            self.fail(f'Koodin {koodi}suoritus aiheutti virheen\n{e}\nOnhan metodi koodarit(self) määritelty?')
        
        odotettu = 2
        self.assertTrue(len(val)==odotettu, f"Kun suoritetaan {koodi}\npitäisi palauttaa lista, jonka pituus on {odotettu}, listan pituus oli {len(val)}")

        taip = str(type(val[0])).replace("<class '","").replace("'>","")
        self.assertTrue(type(val[0]) == type(""), f"Kon suoritetaan{koodi}palutetun listan alkion tyypin pitäisi olla Tehtava, nyt sen tyyppi on {taip}")
    
        odotettu = ["Antti", "Erkki"]
        self.assertTrue(sorted(val)==odotettu, f"Kun suoritetaan {koodi}\npitäisi palauttaa lista, jonka sisättö om {odotettu} nyt palautettiin {val}")   

        koodi = """
t = Tilauskirja()
t.lisaa_tilaus("koodaa webbikauppa", "Antti", 10)
t.lisaa_tilaus("tee mobiilipeli", "Erkki", 5)
t.lisaa_tilaus("tee hello world", "Antti", 1)
t.koodarit()
"""   

        t.lisaa_tilaus("tee hello world", "Antti", 1)
        try:
            val = t.koodarit()
        except Exception as e:
            self.fail(f'Koodin {koodi}suoritus aiheutti virheen\n{e}\nOnhan metodi koodarit(self) määritelty?')
        
        odotettu = 2
        self.assertTrue(len(val)==odotettu, f"Kun suoritetaan {koodi}\npitäisi palauttaa lista, jonka pituus on {odotettu}, listan pituus oli {len(val)}. Palautettu lista oli\n{s(val)}")

        odotettu = ["Antti", "Erkki"]
        self.assertTrue(sorted(val)==odotettu, f"Kun suoritetaan {koodi}\npitäisi palauttaa lista, jonka sisättö om {odotettu} nyt palautettiin {val}")   

if __name__ == '__main__':
    unittest.main()
