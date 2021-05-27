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

exercise = 'src.sekuntikello'
classname = "Sekuntikello"

def f(attr: list):
    return ",".join(attr)

@points('8.sekuntikello')
class SekuntielloTest(unittest.TestCase):
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

    def test1_luokka_olemassa(self):
        try:
            from src.sekuntikello import Sekuntikello
        except:
            self.assertTrue(False, "Ohjelmastasi pitäisi löytyä luokka nimeltä Sekuntikello")

        def test2_konstruktori(self):
            try:
                from src.sekuntikello import Sekuntikello
                kello = Sekuntikello()
            except Exception as e:
                self.assertTrue(False, 'Luokan Sekuntikello konstuktorin kutsuminen Sekuntikello()' +
                    f' aiheutti virheen: {e}')

    def test3_testaa_str(self):
        try:
            from src.sekuntikello import Sekuntikello
            kello = Sekuntikello()

            corr = "00:00"
            val = str(kello)

            self.assertEqual(corr, val, f"Metodin __str__ pitäisi palauttaa merkkijono {corr}\nkun olio luotiin kutsulla\n" + 
                f"Sekuntikello().\nNyt metodi palauttaa merkkijonon {val}.")

        except Exception as e:
            self.assertTrue(False, 'Metodin __str__ kutsuminen' +
                f' palautti virheen: {e}\nkun kello alustettiin kutsllla Sekuntikello()')

    def test5_tick_olemassa(self):

        try:
            from src.sekuntikello import Sekuntikello
            koodi = """
kello = Sekuntikello()                
kello.tick()
"""

            kello = Sekuntikello()
            kello.tick()  

        except Exception as e:
            self.assertTrue(False, f'Koodin\n{koodi}\nsuoritus aiheutti virheen\n{e}\nOnhan metodi tick(self) määritelty?')

    def test6_testaa_tikitys(self):
            try:
                from src.sekuntikello import Sekuntikello
                kello = Sekuntikello()
                kello.tick()

                koodi = """
kello = Sekuntikello()                
kello.tick()                
""" 
                corr = "00:01"
                val = str(kello)

                self.assertEqual(corr, val, f"Metodin __str__ pitäisi palauttaa merkkijono\n{corr}\nkun suoritettiin koodi\n{koodi}\nNyt metodi palauttaa merkkijonon\n{val}")

                kello.tick()
                kello.tick()

                koodi += "kello.tick()\nkello.tick()\n"   

                corr = "00:03"
                val = str(kello)

                self.assertEqual(corr, val, f"Metodin __str__ pitäisi palauttaa merkkijono\n{corr}\nkun suoritettiin koodi\n{koodi}\nNyt metodi palauttaa merkkijonon\n{val}")

                kello = Sekuntikello()
                for i in range(60):
                    kello.tick()
                
                koodi = """
kello = Sekuntikello()
for i in range(60):
    kello.tick()         
""" 

                corr = "01:00"
                val = str(kello)

                self.assertEqual(corr, val, f"Metodin __str__ pitäisi palauttaa merkkijono\n{corr}\nkun suoritettiin koodi\n{koodi}\nNyt metodi palauttaa merkkijonon\n{val}")

                kello.tick()

                koodi += "kello.tick()\nkello.tick()\n"   

                corr = "01:01"
                val = str(kello)

                self.assertEqual(corr, val, f"Metodin __str__ pitäisi palauttaa merkkijono\n{corr}\nkun suoritettiin koodi\n{koodi}\nNyt metodi palauttaa merkkijonon\n{val}")

                kello = Sekuntikello()
                for i in range(60*59+59):
                    kello.tick()
                
                koodi = """
kello = Sekuntikello()
# mennään eteenpäin sekuntia vaille tunti
for i in range(60*59+59):
    kello.tick()         
""" 

                corr = "59:59"
                val = str(kello)

                self.assertEqual(corr, val, f"Metodin __str__ pitäisi palauttaa merkkijono\n{corr}\nkun suoritettiin koodi\n{koodi}\nNyt metodi palauttaa merkkijonon\n{val}")

                koodi += "kello.tick()\n"   

                kello.tick()
                corr = "00:00"
                val = str(kello)

                self.assertEqual(corr, val, f"Metodin __str__ pitäisi palauttaa merkkijono\n{corr}\nkun suoritettiin koodi\n{koodi}\nNyt metodi palauttaa merkkijonon\n{val}")


            except Exception as e:
                self.assertTrue(False, 'Metodin tick() kutsuminen' +
                f' palautti virheen: {e}\nkun suoritettiin koodi\n{koodi}')

if __name__ == '__main__':
    unittest.main()
