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

@points('11.tilauskirja_osa1')
class TehtavaTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=["0"]):
           cls.module = load_module(exercise, 'fi')

    def test_0a_paaohjelma_kunnossa(self):
        ok, line = check_source(self.module)
        message = """Funktioita testaava koodi tulee sijoittaa lohkon
if __name__ == "__main__":
sisälle. Seuraava rivi tulee siirtää:
"""
        self.assertTrue(ok, message+line)

    def test1_tehtava_olemassa(self):
        try:
            from src.koodi import Tehtava
        except:
            self.assertTrue(False, "Ohjelmastasi pitäisi löytyä luokka nimeltä Tehtava")

    def test2_konstruktori(self):
        try:
            from src.koodi import Tehtava
            t = Tehtava("koodaa hello world", "Erkki", 3)
        except Exception as e:
            self.assertTrue(False, 'Luokan Tavara konstuktorin kutsuminen arvoilla Tehtava("koodaa hello world", "Erkki", 3)' +
                f' aiheutti virheen: {e}\nVarmista että konstruktori on määritelty oikein')
        
        try:
            koodi = """
t = Tehtava("koodaa hello world", "Erkki", 3)
t.koodari
"""
            tulos = t.koodari
        except Exception as e:
            self.fail(f"Koodin {koodi}suoritus aiheuttaa virheen {e}")
        odotettu = "Erkki" 
        self.assertTrue(tulos == odotettu, f"Kun suoritetaan {koodi}\nodotettiin {odotettu} tulos on {tulos}")

        try:
            koodi = """
t = Tehtava("koodaa hello world", "Erkki", 3)
t.kuvaus
"""
            tulos = t.kuvaus 
        except Exception as e:
            self.fail(f"Koodin {koodi}suoritus aiheuttaa virheen {e}")
        odotettu = "koodaa hello world"
        self.assertTrue(tulos == odotettu, f"Kun suoritetaan {koodi}\nodotettiin {odotettu} tulos on {tulos}")

        try:
            koodi = """
t = Tehtava("koodaa hello world", "Erkki", 3)
t.kuvaus
"""
            tulos = t.tyomaara 
        except Exception as e:
            self.fail(f"Koodin {koodi}suoritus aiheuttaa virheen {e}")
        odotettu = 3
        self.assertTrue(tulos == odotettu, f"Kun suoritetaan {koodi}\nodotettiin {odotettu} tulos on {tulos}")

        try:
            koodi = """
t = Tehtava("koodaa hello world", "Erkki", 3)
t.id
"""
            tulos = t.id 
        except Exception as e:
            self.fail(f"Koodin {koodi}suoritus aiheuttaa virheen {e}")

    def test3_id(self):
        try:
            from src.koodi import Tehtava
            t1 = Tehtava("koodaa hello world", "Erkki", 3)
            t2 = Tehtava("koodaa facebook", "Erkki", 4)
            t3 = Tehtava("ohjelmoi mobiilipeli", "Erkki", 5)
        except Exception as e:
            self.assertTrue(False, 'Luokan Tavara konstuktorin kutsuminen arvoilla Tehtava("koodaa hello world", "Erkki", 3)' +
                f' palautti virheen: {e}\nVarmista että konstruktori on määritelty oikein')
        
        try:
            koodi = """
t1 = Tehtava("koodaa hello world", "Erkki", 3)
t2 = Tehtava("koodaa facebook", "Erkki", 4)
t3 = Tehtava("ohjelmoi mobiilipeli", "Erkki", 5)
"""
            id1 = t1.id
            id2 = t2.id
            id3 = t3.id
        except Exception as e:
            self.fail(f"Koodin {koodi}suoritus aiheuttaa virheen {e}")
        odotettu = "Erkki" 
        self.assertTrue(id1 != id2, f"Kun suoritetaan {koodi}kaikkien tehtävien id-kentillä pitäisi olla eri arvot. Nyt arvot ovat {id1}, {id2} ja {id2}")
        self.assertTrue(id1 != id3, f"Kun suoritetaan {koodi}kaikkien tehtävien id-kentillä pitäisi olla eri arvot. Nyt arvot ovat {id1}, {id2} ja {id2}")
        self.assertTrue(id2 != id3, f"Kun suoritetaan {koodi}kaikkien tehtävien id-kentillä pitäisi olla eri arvot. Nyt arvot ovat {id1}, {id2} ja {id2}")

    def test_4_metodi_on_valmis(self):
        from src.koodi import Tehtava
        koodi = """
t = Tehtava("koodaa hello world", "Erkki", 3)
t.on_valmis() 
"""
        t = Tehtava("koodaa hello world", "Erkki", 3)
        try:
            val = t.on_valmis()
        except Exception as e:
            self.fail(f'Koodin {koodi}suoritus aiheutti virheen\n{e}\nOnhan metodi määritelty?')
        taip = str(type(val)).replace("<class '","").replace("'>","")
        self.assertTrue(type(val) == type(True), f"Kon suoritetaan{koodi}paluuarvon pitäisi olla totuusarvo, nyt sen tyyppi on {taip}")
        self.assertFalse(val, f"Kon suoritetaan{koodi}paluuarvon pitäisi olla False, nyt se on {val}")

    def test_5_metodi_merkkaa_valmiiksi(self):
        from src.koodi import Tehtava
        koodi = """
t = Tehtava("koodaa hello world", "Erkki", 3)
t.merkkaa_valmiiksi() 
"""
        t = Tehtava("koodaa hello world", "Erkki", 3)
        try:
            t.merkkaa_valmiiksi() 
        except Exception as e:
            self.fail(f'Koodin {koodi}suoritus aiheutti virheen\n{e}\nOnhan metodi määritelty?')

        koodi = """
t = Tehtava("koodaa hello world", "Erkki", 3)
t.merkkaa_valmiiksi()
t.on_valmis() 
"""

        val = t.on_valmis()
        self.assertTrue(val, f"Kon suoritetaan{koodi}paluuarvon pitäisi olla False, nyt se on {val}")

    def test_6_str(self):
        from src.koodi import Tehtava
        koodi = """
t = Tehtava("koodaa hello world", "Antti", 3)
print(t)
"""
        t = Tehtava("koodaa hello world", "Antti", 3)
        try:
            f"{t}"
        except Exception as e:
            self.fail(f'Koodin {koodi}suoritus aiheutti virheen\n{e}\nOnhan metodi määritelty?')

        odotettu = f"{t.id}: koodaa hello world (3 tuntia), koodari Antti EI VALMIS" 
        oli = f"{t}"
        self.assertTrue(odotettu == oli, f"Olion merkkijonoeritys virheellinen. Kun kutsuttiin{koodi}\nodotettiin\n{odotettu}\nmutta merkkijonoesitys oli\n{oli}")

        koodi = """
t = Tehtava("koodaa hello world", "Antti", 3)
t.merkkaa_valmiiksi()
print(t)
"""
        t.merkkaa_valmiiksi() 
        odotettu = f"{t.id}: koodaa hello world (3 tuntia), koodari Antti VALMIS" 
        oli = f"{t}"
        self.assertTrue(odotettu == oli, f"Olion merkkijonoeritys virheellinen. Kun kutsuttiin{koodi}\nodotettiin\n{odotettu}\nmutta merkkijonoesitys oli\n{oli}")


if __name__ == '__main__':
    unittest.main()

