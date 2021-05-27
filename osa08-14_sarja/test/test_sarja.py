import unittest
from unittest.mock import patch

from tmc import points, reflect
from tmc.utils import load, load_module, reload_module, get_stdout, check_source, sanitize
from functools import reduce
import os
import os.path
import textwrap
from random import choice, randint
from datetime import date, datetime, timedelta

exercise = 'src.sarja'
classname = "Sarja"

def f(attr: list):
    return ",".join(attr)

class SarjaTest(unittest.TestCase):
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

    @points('8.sarta_osa1')
    def test1_luokka_olemassa(self):
        try:
            from src.sarja import Sarja
        except:
            self.assertTrue(False, "Ohjelmastasi pitäisi löytyä luokka nimeltä Sarja")

    @points('8.sarta_osa1')
    def test2_konstruktori(self):
        try:
            from src.sarja import Sarja
            sarja = Sarja("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
        except Exception as e:
            self.fail('Luokan Sarja konstuktorin kutsuminen arvoilla Sarja("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])' +
                f' palautti virheen: {e}\nVarmista että konstruktori on määritelty oikein')

    @points('8.sarta_osa1')
    def test3_testaa_str(self):
        test_case = ("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
        try:
            from src.sarja import Sarja
            koodi = f'Sarja("{test_case[0]}", {test_case[1]}, {test_case[2]})'
            sarja = Sarja(test_case[0], test_case[1], test_case[2])

            genret = ", ".join(test_case[2])
            corr = f'{test_case[0]} ({test_case[1]} esityskautta)\ngenret: {genret}\nei arvosteluja'
            val = str(sarja)

            self.assertEqual(sanitize(corr), sanitize(val), f"Metodin __str__ pitäisi palauttaa merkkijono\n{corr}\nkun olio kutsulla\n" + 
                f"{koodi}\nNyt metodi palauttaa merkkijonon\n{val}")

        except Exception as e:
            self.assertTrue(False, f'Metodin __str__ kutsuminen palautti virheen: {e}\nkun olio luotiin kutsulla\n{koodi}')

    @points('8.sarta_osa1')
    def test3_testaa_str2(self):
        test_case = ("South Park", 24, ["Animation", "Comedy"])
        try:
            from src.sarja import Sarja
            koodi = f'Sarja("{test_case[0]}", {test_case[1]}, {test_case[2]})'
            sarja = Sarja(test_case[0], test_case[1], test_case[2])

            genret = ", ".join(test_case[2])
            corr = f'{test_case[0]} ({test_case[1]} esityskautta)\ngenret: {genret}\nei arvosteluja'
            val = str(sarja)

            self.assertEqual(sanitize(corr), sanitize(val), f"Metodin __str__ pitäisi palauttaa merkkijono\n{corr}\nkun olio kutsulla\n" + 
                f"{koodi}\nNyt metodi palauttaa merkkijonon\n{val}")

        except Exception as e:
            self.assertTrue(False, f'Metodin __str__ kutsuminen palautti virheen: {e}\nkun olio luotiin kutsulla\n{koodi}')


    @points('8.sarta_osa2')
    def test5_arvostele_olemassa(self):
        try:
            from src.sarja import Sarja
            koodi = """
s = Sarja("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
s.arvostele(5)
"""
     
            s = Sarja("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
            s.arvostele(5)

        except Exception as e:
            self.assertTrue(False, f'Koodin\n{koodi}\nsuoritus aiheutti virheen\n{e}\nOnhan metodi arvostele(self, arvosana: int) määritelty?')

    @points('8.sarta_osa2')
    def test5_arvostele(self):
        from src.sarja import Sarja
        koodi = """
s = Sarja("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
s.arvostele(5)
"""

        test_case = ("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])

        s = Sarja("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
        s.arvostele(5)

        arv = "arvosteluja 1, keskiarvo 5.0 pistettä"
        
        genret = ", ".join(test_case[2])
        corr = f'{test_case[0]} ({test_case[1]} esityskautta)\ngenret: {genret}\n{arv}'
        val = str(s)

        self.assertTrue(sanitize(corr) == sanitize(val), f"Metodin __str__ pitäisi palauttaa merkkijono\n{corr}\nkun olio kutsulla\n" + 
            f"{koodi}\nNyt metodi palauttaa merkkijonon\n{val}")


        s.arvostele(3)

        koodi += "s.arvostele(3)\n"
        arv = "arvosteluja 2, keskiarvo 4.0 pistettä"

        corr = f'{test_case[0]} ({test_case[1]} esityskautta)\ngenret: {genret}\n{arv}'
        val = str(s)

        self.assertTrue(sanitize(corr) == sanitize(val), f"Metodin __str__ pitäisi palauttaa merkkijono\n{corr}\nkun olio kutsulla\n" + 
            f"{koodi}\nNyt metodi palauttaa merkkijonon\n{val}")

        s.arvostele(2)

        koodi += "s.arvostele(2)\n"
        arv = "arvosteluja 3, keskiarvo 3.3 pistettä"

        corr = f'{test_case[0]} ({test_case[1]} esityskautta)\ngenret: {genret}\n{arv}'
        val = str(s)

        self.assertTrue(sanitize(corr) == sanitize(val), f"Metodin __str__ pitäisi palauttaa merkkijono\n{corr}\nkun olio kutsulla\n" + 
            f"{koodi}\nNyt metodi palauttaa merkkijonon\n{val}")

        s.arvostele(5)

        koodi += "s.arvostele(5)\n"
        arv = "arvosteluja 4, keskiarvo 3.8 pistettä"

        corr = f'{test_case[0]} ({test_case[1]} esityskautta)\ngenret: {genret}\n{arv}'
        val = str(s)

        self.assertTrue(sanitize(corr) == sanitize(val), f"Metodin __str__ pitäisi palauttaa merkkijono\n{corr}\nkun olio kutsulla\n" + 
            f"{koodi}\nNyt metodi palauttaa merkkijonon\n{val}")

    @points('8.sarta_osa3')
    def test6_funktio_arvosana_vahintaan_olemassa(self):
        try:
            from src.sarja import arvosana_vahintaan
        except:
            self.assertTrue(False, "Ohjelmastasi pitäisi löytyä funktio nimeltä arvosana_vahintaan(arvosana: float, sarjat: list)")

    @points('8.sarta_osa3')
    def test7_funktio_arvosana_vahintaan(self):
        from src.sarja import arvosana_vahintaan
        from src.sarja import Sarja

        s1 = Sarja("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
        s1.arvostele(5)

        s2 = Sarja("South Park", 24, ["Animation", "Comedy"])
        s2.arvostele(3)

        s3 = Sarja("Friends", 10, ["Romance", "Comedy"])
        s3.arvostele(2)

        sarjat = [s1, s2, s3]

        koodi = """
s1 = Sarja("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
s1.arvostele(5)
s2 = Sarja("South Park", 24, ["Animation", "Comedy"])
s2.arvostele(3)
s3 = Sarja("Friends", 10, ["Romance", "Comedy"])
s3.arvostele(2)
sarjat = [s1, s2, s3]

vastaus = arvosana_vahintaan(4.5, sarjat)
"""
        try:
            vastaus = arvosana_vahintaan(4.5, sarjat)
        except:
            self.fail(f"Varmista, että seuraavan koodin suoritus onnistuu\n{koodi}")
        
        self.assertTrue(type(vastaus) == list, "Funktion arvosana_vahintaan(arvosana: float, sarjat: list) tulee palauttaa lista")

        odotettu = 1
        self.assertTrue(len(vastaus)==odotettu, f"Kun suoritetaan koodi\n{koodi}\npalautetun listan pituuden pitäisi olla {odotettu}, se oli kuitenkin {len(vastaus)}")
        self.assertTrue(vastaus[0].nimi=="Dexter", f"Kun suoritetaan koodi\n{koodi}\npalautetun listan ainoan sarjan pitäisi olla Dexter, se kuitenkin on {vastaus[0].nimi}")

        koodi = """
s1 = Sarja("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
s1.arvostele(5)
s2 = Sarja("South Park", 24, ["Animation", "Comedy"])
s2.arvostele(3)
s3 = Sarja("Friends", 10, ["Romance", "Comedy"])
s3.arvostele(2)
sarjat = [s1, s2, s3]

vastaus = arvosana_vahintaan(1.5, sarjat)
"""
        try:
            vastaus = arvosana_vahintaan(2.5, sarjat)
        except:
            self.fail(f"Varmista, että seuraavan koodin suoritus onnistuu\n{koodi}")
        
        self.assertTrue(type(vastaus) == list, "Funktion arvosana_vahintaan(arvosana: float, sarjat: list) tulee palauttaa lista")

        odotettu = 2
        self.assertTrue(len(vastaus)==odotettu, f"Kun suoritetaan koodi\n{koodi}\npalautetun listan pituuden pitäisi olla {odotettu}, se oli kuitenkin {len(vastaus)}")
        ehto = (vastaus[0].nimi=="Dexter" and vastaus[1].nimi=="South Park") or (vastaus[1].nimi=="Dexter" and vastaus[0].nimi=="South Park")
        self.assertTrue(ehto, f"Kun suoritetaan koodi\n{koodi}\npalautella listalla pitäisi olla Dexter ja South park, listalla oli {vastaus[0].nimi} ja {vastaus[1].nimi}")

    @points('8.sarta_osa3')
    def test8_funktio_sisaltaa_genren_olemassa(self):
        try:
            from src.sarja import sisaltaa_genren
        except:
            self.assertTrue(False, "Ohjelmastasi pitäisi löytyä funktio nimeltä sisaltaa_genren(genre: str, sarjat: list)")

    @points('8.sarta_osa3')
    def test9_funktio_sisaltaa_genret(self):
        from src.sarja import sisaltaa_genren
        from src.sarja import Sarja

        s1 = Sarja("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
        s1.arvostele(5)

        s2 = Sarja("South Park", 24, ["Animation", "Comedy"])
        s2.arvostele(3)

        s3 = Sarja("Friends", 10, ["Romance", "Comedy"])
        s3.arvostele(2)

        sarjat = [s1, s2, s3]

        koodi = """
s1 = Sarja("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
s1.arvostele(5)
s2 = Sarja("South Park", 24, ["Animation", "Comedy"])
s2.arvostele(3)
s3 = Sarja("Friends", 10, ["Romance", "Comedy"])
s3.arvostele(2)
sarjat = [s1, s2, s3]

vastaus = sisaltaa_genren("Crime", sarjat)
"""
        try:
            vastaus = sisaltaa_genren("Crime", sarjat)
        except:
            self.fail(f"Varmista, että seuraavan koodin suoritus onnistuu\n{koodi}")

        self.assertTrue(type(vastaus) == list, "Funktion sisaltaa_genren(genre: str, sarjat: list) tulee palauttaa lista")

        odotettu = 1
        self.assertTrue(len(vastaus)==odotettu, f"Kun suoritetaan koodi\n{koodi}\npalautetun listan pituuden pitäisi olla {odotettu}, se oli kuitenkin {len(vastaus)}")
        self.assertTrue(vastaus[0].nimi=="Dexter", f"Kun suoritetaan koodi\n{koodi}\npalautetun listan ainoan sarjan pitäisi olla Dexter, se kuitenkin on {vastaus[0].nimi}")

        koodi = """
s1 = Sarja("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
s1.arvostele(5)
s2 = Sarja("South Park", 24, ["Animation", "Comedy"])
s2.arvostele(3)
s3 = Sarja("Friends", 10, ["Romance", "Comedy"])
s3.arvostele(2)
sarjat = [s1, s2, s3]

vastaus = sisaltaa_genren("Programming", sarjat)
"""
        try:
            vastaus = sisaltaa_genren("Programming", sarjat)
        except:
            self.fail(f"Varmista, että seuraavan koodin suoritus onnistuu\n{koodi}")


        odotettu = 0
        self.assertTrue(len(vastaus)==odotettu, f"Kun suoritetaan koodi\n{koodi}\npalautetun listan pituuden pitäisi olla {odotettu}, se oli kuitenkin {len(vastaus)}")

        koodi = """
s1 = Sarja("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
s1.arvostele(5)
s2 = Sarja("South Park", 24, ["Animation", "Comedy"])
s2.arvostele(3)
s3 = Sarja("Friends", 10, ["Romance", "Comedy"])
s3.arvostele(2)
sarjat = [s1, s2, s3]

vastaus = sisaltaa_genren("Comedy", sarjat)
"""
        try:
            vastaus = sisaltaa_genren("Comedy", sarjat)
        except:
            self.fail(f"Varmista, että seuraavan koodin suoritus onnistuu\n{koodi}")
        
        self.assertTrue(type(vastaus) == list, "Funktion arvosana_vahintaan(arvosana: float, sarjat: list) tulee palauttaa lista")

        odotettu = 2
        self.assertTrue(len(vastaus)==odotettu, f"Kun suoritetaan koodi\n{koodi}\npalautetun listan pituuden pitäisi olla {odotettu}, se oli kuitenkin {len(vastaus)}")
        ehto = (vastaus[0].nimi=="Friends" and vastaus[1].nimi=="South Park") or (vastaus[1].nimi=="Friends" and vastaus[0].nimi=="South Park")
        self.assertTrue(ehto, f"Kun suoritetaan koodi\n{koodi}\npalautella listalla pitäisi olla Friends ja South park, listalla oli {vastaus[0].nimi} ja {vastaus[1].nimi}")

if __name__ == '__main__':
    unittest.main()