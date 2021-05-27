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

@points('11.tilauskirja_osa3')
class TilauskirjaOsa3Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=["0"]):
           cls.module = load_module(exercise, 'fi')

    def test_1_merkkaa_valmiiksi(self):
        reload_module(self.module)
        from src.koodi import Tilauskirja, Tehtava
        koodi = """
t = Tilauskirja()
t.lisaa_tilaus("koodaa webbikauppa", "Antti", 10)
t.merkkaa_valmiiksi(1)
"""
        t = Tilauskirja()
        t.lisaa_tilaus("koodaa webbikauppa", "Antti", 10)

        til = t.kaikki_tilaukset()
        id = til[0].id
        koodi += f"\n"
        
        try:
            t.merkkaa_valmiiksi(id)
        except Exception as e:
            self.fail(f'Koodin {koodi}suoritus aiheutti virheen\n{e}\nOnhan metodi merkkaa_valmiiksi(self, id: int) määritelty?')
        
        koodi = """
t = Tilauskirja()
t.lisaa_tilaus("koodaa webbikauppa", "Antti", 10)
t.merkkaa_valmiiksi(1)
t.kaikki_tilaukset()
"""

        val = t.kaikki_tilaukset()

        t1 = ("koodaa webbikauppa", "Antti", 10, True) 
        all_ok = ook(val, [t1])

        odotettu = s([tt(t1)])

        self.assertTrue(all_ok, f"Kun suoritetaan {koodi}\npitäisi palauttaa lista, jolta löytyvät seuraavat tehtävät\n{odotettu}\nnyt palautettiin\n{ss(val)}")

        koodi = """
t = Tilauskirja()
t.lisaa_tilaus("koodaa webbikauppa", "Antti", 10)
t.lisaa_tilaus("tee mobiilipeli", "Erkki", 5)
t.merkkaa_valmiiksi(1)
t.merkkaa_valmiiksi(2)
t.kaikki_tilaukset()
"""

        t.lisaa_tilaus("tee mobiilipeli", "Erkki", 5)
        til = t.kaikki_tilaukset()
        id1 = til[0].id
        id2 = til[1].id

        try:
            t.merkkaa_valmiiksi(id1)
            t.merkkaa_valmiiksi(id2)
        except Exception as e:
            self.fail(f'Koodin {koodi}suoritus aiheutti virheen\n{e}\nOnhan metodi merkkaa_valmiiksi(self, id: int) määritelty?')
        
        val = t.kaikki_tilaukset()

        t2 = ("tee mobiilipeli", "Erkki", 5, True)
        all_ok = ook(val, [t1, t2])

        odotettu = s([tt(t1), tt(t2)])

        self.assertTrue(all_ok, f"Kun suoritetaan {koodi}\npitäisi palauttaa lista, jolta löytyvät seuraavat tehtävät\n{odotettu}\nnyt palautettiin\n{ss(val)}")

    def test_2_merkkaa_valmiiksi_poikkeus(self):
        reload_module(self.module)
        from src.koodi import Tilauskirja, Tehtava
        koodi = """
t = Tilauskirja()
t.lisaa_tilaus("koodaa webbikauppa", "Antti", 10)
t.merkkaa_valmiiksi(999)
"""
        t = Tilauskirja()
        t.lisaa_tilaus("koodaa webbikauppa", "Antti", 10)

        til = t.kaikki_tilaukset()
        id = til[0].id + 1
        koodi += f"\n"
        
        ok = False
        try:
            t.merkkaa_valmiiksi(id)
        except ValueError:
            ok = True
        except Exception as e:
            self.fail(f'Koodin {koodi}suoritus aiheutti virheen\n{e}\nOnhan metodi merkkaa_valmiiksi(self, id: int) määritelty?')
        self.assertTrue(ok, f'Koodin {koodi}suorituksen pitäisi tuottaa poikkeus ValueError')

    def test_3_ei_valmiit(self):
        from src.koodi import Tilauskirja, Tehtava

        koodi = """
t = Tilauskirja()
t.ei_valmiit_tilaukset()
"""
        t = Tilauskirja()
        try:
            t.ei_valmiit_tilaukset()
        except Exception as e:
            self.fail(f'Koodin {koodi}suoritus aiheutti virheen\n{e}\nOnhan metodi ei_valmiit_tilaukset(self) määritelty?')

        koodi = """
t = Tilauskirja()
t.lisaa_tilaus("koodaa webbikauppa", "Antti", 10)
t.ei_valmiit_tilaukset()
"""
        t = Tilauskirja()
        t.lisaa_tilaus("koodaa webbikauppa", "Antti", 10)
        try:
            val = t.ei_valmiit_tilaukset()
        except Exception as e:
            self.fail(f'Koodin {koodi}suoritus aiheutti virheen\n{e}\nOnhan metodi ei_valmiit_tilaukset(self) määritelty?')

        taip = str(type(val)).replace("<class '","").replace("'>","")
        self.assertTrue(type(val) == type([]), f"Kon suoritetaan{koodi}paluuarvon pitäisi olla lista, nyt sen tyyppi on {taip}")
        odotettu = 1
        self.assertTrue(len(val)==odotettu, f"Kun suoritetaan {koodi}\npitäisi palauttaa lista, jonka pituus on {odotettu}, listan pituus oli {len(val)}")
        
        ttt = Tehtava("koodaa hello world", "Erkki", 3)
        taip = str(type(val[0])).replace("<class '","").replace("'>","")
        self.assertTrue(type(val[0]) == type(ttt), f"Kon suoritetaan{koodi}palutetun listan alkion tyypin pitäisi olla Tehtava, nyt sen tyyppi on {taip}")

        odotettu = 1
        self.assertTrue(len(val)==odotettu, f"Kun suoritetaan {koodi}\npitäisi palauttaa lista, jonka pituus on {odotettu}, listan pituus oli {len(val)}")

        t1 = ("koodaa webbikauppa", "Antti", 10, False) 
        all_ok = ook(val, [t1])

        odotettu = s([tt(t1)])

        self.assertTrue(all_ok, f"Kun suoritetaan {koodi}\npitäisi palauttaa lista, jolta löytyvät seuraavat tehtävät\n{odotettu}\nnyt palautettiin\n{ss(val)}")

        koodi = """
t = Tilauskirja()
t.lisaa_tilaus("koodaa webbikauppa", "Antti", 10)
t.lisaa_tilaus("tee mobiilipeli", "Erkki", 5)
t.lisaa_tilaus("koodaa parempi facebook", "joona", 5000)
t.ei_valmiit_tilaukset()
"""

        t.lisaa_tilaus("tee mobiilipeli", "Erkki", 5)
        t.lisaa_tilaus("koodaa parempi facebook", "joona", 5000)
        t2 = ("tee mobiilipeli", "Erkki", 5, False)
        t3 = ("koodaa parempi facebook", "joona", 5000, False)
        try:
            val = t.ei_valmiit_tilaukset()
        except Exception as e:
            self.fail(f'Koodin {koodi}suoritus aiheutti virheen\n{e}\nOnhan metodi ei_valmiit_tilaukset(self) määritelty?')

        odotettu = 3
        self.assertTrue(len(val)==odotettu, f"Kun suoritetaan {koodi}\npitäisi palauttaa lista, jonka pituus on {odotettu}, listan pituus oli {len(val)}")

        all_ok = ook(val, [t1, t2, t3])

        odotettu = s([tt(t1), tt(t2),  tt(t3)])

        self.assertTrue(all_ok, f"Kun suoritetaan {koodi}\npitäisi palauttaa lista, jolta löytyvät seuraavat tehtävät\n{odotettu}\nnyt palautettiin\n{ss(val)}")

        koodi = """
t = Tilauskirja()
t.lisaa_tilaus("koodaa webbikauppa", "Antti", 10)
t.lisaa_tilaus("tee mobiilipeli", "Erkki", 5)
t.lisaa_tilaus("koodaa parempi facebook", "joona", 5000)
t.merkkaa_valmiiksi(1)
t.merkkaa_valmiiksi(2)
t.ei_valmiit_tilaukset()
"""

        til = t.kaikki_tilaukset()
        id1 = til[0].id
        id2 = til[1].id

        try:
            t.merkkaa_valmiiksi(id1)
            t.merkkaa_valmiiksi(id2)
        except Exception as e:
            self.fail(f'Koodin {koodi}suoritus aiheutti virheen\n{e}\nOnhan metodi merkkaa_valmiiksi(self, id: int) määritelty?')
       
        try:
            val = t.ei_valmiit_tilaukset()
        except Exception as e:
            self.fail(f'Koodin {koodi}suoritus aiheutti virheen\n{e}\nOnhan metodi ei_valmiit_tilaukset(self) määritelty?')

        odotettu = 1
        self.assertTrue(len(val)==odotettu, f"Kun suoritetaan {koodi}\npitäisi palauttaa lista, jonka pituus on {odotettu}, listan pituus oli {len(val)}")

        all_ok = ook(val, [t3])

        odotettu = s([tt(t3)])

        self.assertTrue(all_ok, f"Kun suoritetaan {koodi}\npitäisi palauttaa lista, jolta löytyvät seuraavat tehtävät\n{odotettu}\nnyt palautettiin\n{ss(val)}")


    def test_4_valmiit(self):
        reload_module(self.module)
        from src.koodi import Tilauskirja, Tehtava

        koodi = """
t = Tilauskirja()
t.ei_valmiit_tilaukset()
"""
        t = Tilauskirja()
        try:
            t.valmiit_tilaukset()
        except Exception as e:
            self.fail(f'Koodin {koodi}suoritus aiheutti virheen\n{e}\nOnhan metodi valmiit_tilaukset(self) määritelty?')

        koodi = """
t = Tilauskirja()
t.lisaa_tilaus("koodaa webbikauppa", "Antti", 10)
t.merkkaa_valmiiksi(1)
t.valmiit_tilaukset()
"""
        t = Tilauskirja()
        t.lisaa_tilaus("koodaa webbikauppa", "Antti", 10)

        til = t.kaikki_tilaukset()
        id1 = til[0].id

        try:
            t.merkkaa_valmiiksi(id1)
        except Exception as e:
            self.fail(f'Koodin {koodi}suoritus aiheutti virheen\n{e}\nOnhan metodi merkkaa_valmiiksi(self, id: int) määritelty?')
       
        try:
            val = t.valmiit_tilaukset()
        except Exception as e:
            self.fail(f'Koodin {koodi}suoritus aiheutti virheen\n{e}\nOnhan metodi ei_valmiit_tilaukset(self) määritelty?')

        taip = str(type(val)).replace("<class '","").replace("'>","")
        self.assertTrue(type(val) == type([]), f"Kon suoritetaan{koodi}paluuarvon pitäisi olla lista, nyt sen tyyppi on {taip}")
        odotettu = 1
        self.assertTrue(len(val)==odotettu, f"Kun suoritetaan {koodi}\npitäisi palauttaa lista, jonka pituus on {odotettu}, listan pituus oli {len(val)}")
        
        ttt = Tehtava("koodaa hello world", "Erkki", 3)
        taip = str(type(val[0])).replace("<class '","").replace("'>","")
        self.assertTrue(type(val[0]) == type(ttt), f"Kon suoritetaan{koodi}palutetun listan alkion tyypin pitäisi olla Tehtava, nyt sen tyyppi on {taip}")

        odotettu = 1
        self.assertTrue(len(val)==odotettu, f"Kun suoritetaan {koodi}\npitäisi palauttaa lista, jonka pituus on {odotettu}, listan pituus oli {len(val)}")

        t1 = ("koodaa webbikauppa", "Antti", 10, True) 
        all_ok = ook(val, [t1])

        odotettu = s([tt(t1)])

        self.assertTrue(all_ok, f"Kun suoritetaan {koodi}\npitäisi palauttaa lista, jolta löytyvät seuraavat tehtävät\n{odotettu}\nnyt palautettiin\n{ss(val)}")

        koodi = """
t = Tilauskirja()
t.lisaa_tilaus("koodaa webbikauppa", "Antti", 10)
t.lisaa_tilaus("tee mobiilipeli", "Erkki", 5)
t.lisaa_tilaus("koodaa parempi facebook", "joona", 5000)
t.merkkaa_valmiiksi(1)
t.merkkaa_valmiiksi(2)
t.valmiit_tilaukset()
"""
        t = Tilauskirja()
        t.lisaa_tilaus("koodaa webbikauppa", "Antti", 10)
        t.lisaa_tilaus("tee mobiilipeli", "Erkki", 5)
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
            val = t.valmiit_tilaukset()
        except Exception as e:
            self.fail(f'Koodin {koodi}suoritus aiheutti virheen\n{e}\nOnhan metodi ei_valmiit_tilaukset(self) määritelty?')

        odotettu = 2
        self.assertTrue(len(val)==odotettu, f"Kun suoritetaan {koodi}\npitäisi palauttaa lista, jonka pituus on {odotettu}, listan pituus oli {len(val)}")
        
        t1 = ("koodaa webbikauppa", "Antti", 10, True) 
        t2 = ("tee mobiilipeli", "Erkki", 5, True) 

        all_ok = ook(val, [t1, t2])

        odotettu = s([tt(t1), tt(t1)])

        self.assertTrue(all_ok, f"Kun suoritetaan {koodi}\npitäisi palauttaa lista, jolta löytyvät seuraavat tehtävät\n{odotettu}\nnyt palautettiin\n{ss(val)}")

if __name__ == '__main__':
    unittest.main()