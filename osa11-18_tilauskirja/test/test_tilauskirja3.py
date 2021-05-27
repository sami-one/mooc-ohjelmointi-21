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

@points('11.tilauskirja_osa4')
class TilauskirjaOsa4Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=["0"]):
           cls.module = load_module(exercise, 'fi')

    def test_1_koodarin_status(self):
        reload_module(self.module)
        from src.koodi import Tilauskirja, Tehtava
        koodi = """
t = Tilauskirja()
t.lisaa_tilaus("koodaa webbikauppa", "Antti", 10)
t.koodarin_status("Antti")
"""
        t = Tilauskirja()
        t.lisaa_tilaus("koodaa webbikauppa", "Antti", 10)
        try:
            val = t.koodarin_status("Antti")
        except Exception as e:
            self.fail(f'Koodin {koodi}suoritus aiheutti virheen\n{e}\nOnhan metodi koodarin_status(self, koodari: str) määritelty?')
        
        taip = str(type(val)).replace("<class '","").replace("'>","")
        self.assertTrue(type(val) == type(()), f"Kon suoritetaan{koodi}paluuarvon pitäisi olla tuple, nyt sen tyyppi on {taip}")
        
        odotettu = 4
        self.assertTrue(len(val)==odotettu, f"Kun suoritetaan {koodi}\npitäisi palauttaa tuple, jonka pituus on {odotettu}, palautetun tuplen pituus oli {len(val)}")
        valx = val
        for i in [0,1,2,3]:
            val = valx[i]
            taip = str(type(val)).replace("<class '","").replace("'>","")
            self.assertTrue(type(val) == type(1), f"Kon suoritetaan{koodi}palautetun tuplen pitäisi sisältää kokonaislukuja, nyt mukana on arvo, jonka tyyppi on {taip}. Palautettu tuple on {valx}")    
        
        val = valx
        odotettu = (0, 1, 0, 10)
        self.assertTrue(val==odotettu, f"Kun suoritetaan {koodi}\npitäisi palauttaa {odotettu}, nuyt palautettiin {val}")

    def test_2_koodarin_status(self):
        reload_module(self.module)
        from src.koodi import Tilauskirja, Tehtava
        koodi = """
t = Tilauskirja()
t.lisaa_tilaus("koodaa webbikauppa", "Antti", 10)
t.lisaa_tilaus("tee mobiilipeli", "Antti", 5)
t.lisaa_tilaus("koodaa pygamella jotain", "Antti", 50)
t.lisaa_tilaus("koodaa parempi facebook", "joona", 5000)
t.merkkaa_valmiiksi(1)
t.merkkaa_valmiiksi(2)
t.koodarin_status("Antti")
"""
        t = Tilauskirja()
        t.lisaa_tilaus("koodaa webbikauppa", "Antti", 10)
        t.lisaa_tilaus("tee mobiilipeli", "Antti", 5)
        t.lisaa_tilaus("koodaa pygamella jotain", "Antti", 50)
        t.lisaa_tilaus("koodaa parempi facebook", "joona", 5000)

        til = t.kaikki_tilaukset()
        id1 = til[0].id
        id2 = til[1].id

        try:
            t.merkkaa_valmiiksi(id1)
            t.merkkaa_valmiiksi(id2)
        except Exception as e:
            self.fail(f'Koodin {koodi}suoritus aiheutti virheen\n{e}\nOnhan metodi merkkaa_valmiiksi(self, id: int) määritelty?')
       
        try:
            val = t.koodarin_status("Antti")
        except Exception as e:
            self.fail(f'Koodin {koodi}suoritus aiheutti virheen\n{e}\nOnhan metodi koodarin_status(self, koodari: str) määritelty?')
        
        odotettu =  (2, 1, 15, 50)
        self.assertTrue(val==odotettu, f"Kun suoritetaan {koodi}\npitäisi palauttaa {odotettu}, nuyt palautettiin {val}")

    def test_4_koodarin_status_tuottaa_poikkeuksen(self):
        reload_module(self.module)
        from src.koodi import Tilauskirja, Tehtava
        koodi = """
t = Tilauskirja()
t.lisaa_tilaus("koodaa webbikauppa", "Antti", 10)
t.koodarin_status("JohnDoe")
"""
        t = Tilauskirja()
        t.lisaa_tilaus("koodaa webbikauppa", "Antti", 10)
        ok = False
        try:
            val = t.koodarin_status("JohnDoe")
        except ValueError:
            ok = True
        except Exception as e:
            self.fail(f'Koodin {koodi}suoritus aiheutti virheen\n{e}')
        self.assertTrue(ok, f'Koodin {koodi}suorituksen pitäisi tuottaa poikkeus ValueError')

if __name__ == '__main__':
    unittest.main()