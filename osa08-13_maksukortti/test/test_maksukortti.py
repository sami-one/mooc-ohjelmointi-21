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

exercise = 'src.maksukortti'
classname = "Maksukortti"

def f(attr: list):
    return ",".join(attr)

class MaksukorttiTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=[AssertionError("Syötteen pyytämistä ei odotettu")]):
           cls.module = load_module(exercise, 'fi')

    def test_0a_paaohjelma_kunnossa(self):
        with open("src/maksukortti.py") as t:
            if "if __name__" in t.read():
                self.assertTrue(False, 'Pääohjelmaa ei saa kirjoittaa lohkon if __name__ == "__main__": sisälle')

    @points('8.maksukortti_osa1')
    def test1_luokka_olemassa(self):
        try:
            from src.maksukortti import Maksukortti
        except:
            self.assertTrue(False, "Ohjelmastasi pitäisi löytyä luokka nimeltä Maksukortti")

    @points('8.maksukortti_osa1')
    def test2_konstruktori(self):
        try:
            from src.maksukortti import Maksukortti
            kortti = Maksukortti(100)
            self.assertTrue(True, "")
        except Exception as e:
            self.assertTrue(False, 'Luokan Maksukortti konstuktorin kutsuminen arvoilla Maksukortti(100)' +
                f' palautti virheen: {e}\nVarmista että konstruktori on määritelty oikein')

    @points('8.maksukortti_osa1')
    def test3_testaa_str(self):
        test_cases = (100, 25, 0, 10, 23)
        for test_case in test_cases:
            try:
                from src.maksukortti import Maksukortti
                kortti = Maksukortti(test_case)

                corr = f'Kortilla on rahaa {test_case:.1f} euroa'
                val = str(kortti)

                self.assertEqual(corr, val, f"Metodin __str__ pitäisi palauttaa merkkijono\n{corr}\nkun olio luotiin kutsulla\n" + 
                    f"Maksukortti({test_case})\nNyt metodi palauttaa merkkijonon\n{val}")

            except Exception as e:
                self.assertTrue(False, f'Metodin __str__ kutsuminen palautti virheen: {e}\nkun olio luotiin kutsulla\nMaksukortti({test_case})')

    @points('8.maksukortti_osa2')
    def test4_syo_edullisesti_olemassa(self):
        try:
            from src.maksukortti import Maksukortti 
            koodi = """
kortti = Maksukortti(10)
kortti.syo_edullisesti()"""

            kortti = Maksukortti(10)
            kortti.syo_edullisesti()  

        except Exception as e:
            self.assertTrue(False, f'Koodin\n{koodi}\nsuoritus aiheutti virheen\n{e}\nOnhan metodi syo_edullisesti(self) määritelty?')

    @points('8.maksukortti_osa2')
    def test5_syo_edullisesti(self):
            from src.maksukortti import Maksukortti
            rahaa = 7
            koodi = """
kortti = Maksukortti(7)
kortti.syo_edullisesti()
"""

            kortti = Maksukortti(rahaa)
            kortti.syo_edullisesti()

            rahaa -= 2.6
            corr = f'Kortilla on rahaa {rahaa:.1f} euroa'
            val = str(kortti)

            self.assertEqual(corr, val, f"Metodin __str__ pitäisi palauttaa merkkijono\n{corr}\nkun on suoritettu koodi\n{koodi}\n" + 
                f"Nyt metodi palauttaa merkkijonon\n{val}")

            kortti.syo_edullisesti()
            koodi += "kortti.syo_edullisesti()\n"
            rahaa -= 2.6
            corr = f'Kortilla on rahaa {rahaa:.1f} euroa'
            val = str(kortti)
            self.assertEqual(corr, val, f"Metodin __str__ pitäisi palauttaa merkkijono\n{corr}\nkun on suoritettu koodi\n{koodi}\n" + 
                f"Nyt metodi palauttaa merkkijonon\n{val}")
            
            kortti.syo_edullisesti()
            koodi += "kortti.syo_edullisesti()\n"
            corr = f'Kortilla on rahaa {rahaa:.1f} euroa'
            val = str(kortti)
            self.assertEqual(corr, val, f"Metodin __str__ pitäisi palauttaa merkkijono\n{corr}\nkun on suoritettu koodi\n{koodi}\n" + 
                f"Nyt metodi palauttaa merkkijonon\n{val}")

    @points('8.maksukortti_osa2')
    def test6_syo_maukkaasti_olemassa(self):
        try:
            from src.maksukortti import Maksukortti 
            koodi = """
kortti = Maksukortti(10)
kortti.syo_maukkaasti()"""

            kortti = Maksukortti(10)
            kortti.syo_maukkaasti()  

        except Exception as e:
            self.assertTrue(False, f'Koodin\n{koodi}\nsuoritus aiheutti virheen\n{e}\nOnhan metodi syo_maukkaasti(self) määritelty?')

    @points('8.maksukortti_osa2')
    def test7_syo_maukkaasti(self):
            from src.maksukortti import Maksukortti
            rahaa = 10
            koodi = """
kortti = Maksukortti(10)
kortti.syo_maukkaasti()
"""

            kortti = Maksukortti(rahaa)
            kortti.syo_maukkaasti()

            rahaa -= 4.6
            corr = f'Kortilla on rahaa {rahaa:.1f} euroa'
            val = str(kortti)

            self.assertEqual(corr, val, f"Metodin __str__ pitäisi palauttaa merkkijono\n{corr}\nkun on suoritettu koodi\n{koodi}\n" + 
                f"Nyt metodi palauttaa merkkijonon\n{val}")

            kortti.syo_maukkaasti()
            koodi += "kortti.syo_maukkaasti()\n"
            rahaa -= 4.6
            corr = f'Kortilla on rahaa {rahaa:.1f} euroa'
            val = str(kortti)
            self.assertEqual(corr, val, f"Metodin __str__ pitäisi palauttaa merkkijono\n{corr}\nkun on suoritettu koodi\n{koodi}\n" + 
                f"Nyt metodi palauttaa merkkijonon\n{val}")
            
            kortti.syo_maukkaasti()
            koodi += "kortti.syo_maukkaasti()\n"
            corr = f'Kortilla on rahaa {rahaa:.1f} euroa'
            val = str(kortti)
            self.assertEqual(corr, val, f"Metodin __str__ pitäisi palauttaa merkkijono\n{corr}\nkun on suoritettu koodi\n{koodi}\n" + 
                f"Nyt metodi palauttaa merkkijonon\n{val}")

    @points('8.maksukortti_osa3')
    def test8_lataa_rahaa_olemassa(self):
        try:
            from src.maksukortti import Maksukortti 
            koodi = """
kortti = Maksukortti(10)
kortti.lataa_rahaa(5)"""

            kortti = Maksukortti(10)
            kortti.lataa_rahaa(5)  

        except Exception as e:
            self.assertTrue(False, f'Koodin\n{koodi}\nsuoritus aiheutti virheen\n{e}\nOnhan metodi lataa_rahaa(self, summa: float) määritelty?')

    @points('8.maksukortti_osa3')
    def test9_lataa_raha(self):
            from src.maksukortti import Maksukortti
            rahaa = 10
            koodi = """
kortti = Maksukortti(10)
kortti.lataa_rahaa(5)
"""

            kortti = Maksukortti(10)
            kortti.lataa_rahaa(5)  

            rahaa += 5
            corr = f'Kortilla on rahaa {rahaa:.1f} euroa'
            val = str(kortti)

            self.assertEqual(corr, val, f"Metodin __str__ pitäisi palauttaa merkkijono\n{corr}\nkun on suoritettu koodi\n{koodi}\n" + 
                f"Nyt metodi palauttaa merkkijonon\n{val}")

            kortti.lataa_rahaa(75)  
            koodi += "kortti.lataa_rahaa(75)\n"
            rahaa += 75
            corr = f'Kortilla on rahaa {rahaa:.1f} euroa'
            val = str(kortti)

            self.assertEqual(corr, val, f"Metodin __str__ pitäisi palauttaa merkkijono\n{corr}\nkun on suoritettu koodi\n{koodi}\n" + 
                f"Nyt metodi palauttaa merkkijonon\n{val}")

            kortti.lataa_rahaa(20)  
            koodi += "kortti.lataa_rahaa(20)\n"
            rahaa += 20
            corr = f'Kortilla on rahaa {rahaa:.1f} euroa'
            val = str(kortti)

            self.assertEqual(corr, val, f"Metodin __str__ pitäisi palauttaa merkkijono\n{corr}\nkun on suoritettu koodi\n{koodi}\n" + 
                f"Nyt metodi palauttaa merkkijonon\n{val}")

    @points('8.maksukortti_osa3')
    def test10_lataa_raha_negatiivinen(self):
            from src.maksukortti import Maksukortti
            rahaa = 10
            koodi = """
kortti = Maksukortti(10)
kortti.lataa_rahaa(-25)
"""

            ok = False
            kortti = Maksukortti(10)
            try:
                kortti.lataa_rahaa(-25)  
            except ValueError:
                rahaa += 5
                ok = True
                
            self.assertTrue(ok, f"Koodin\n{koodi}\nsuorituksen pitäisi aiheuttaa ValueError")

    @points('8.maksukortti_osa4')
    def test11_paaohjelma(self):
        try:
            reload_module(self.module)
            output_all = get_stdout()
        except:
            self.assertTrue(False, f"Varmista, että ohjelmasi pystyy suorittamaan")

        mssage = """\nHuomaa, että tässä tehtävässä mitään koodia EI TULE SIJOITTAA lohkon
if __name__ == "__main__":
sisälle
        """

        self.assertTrue(len(output_all)>0, f"Ohjelmasi ei tulosta mitään!\n{mssage}")  
        output = [line.strip() for line in output_all.split("\n") if len(line) > 0]

        oikea = [
            "Pekka: Kortilla on rahaa 15.4 euroa",
            "Matti: Kortilla on rahaa 27.4 euroa",
            "Pekka: Kortilla on rahaa 35.4 euroa",
            "Matti: Kortilla on rahaa 22.8 euroa",
            "Pekka: Kortilla on rahaa 30.2 euroa",
            "Matti: Kortilla on rahaa 72.8 euroa"
        ]

        self.assertTrue(len(oikea) == len(output),f"Ohjelmasi tulisi tulostaa {len(oikea)} riviä, se tulosti {len(output)} riviä. Tulostus oli\n{output_all}")

        for i in range(0, len(oikea)):
            t = output[i]
            o = oikea[i]
            self.assertTrue(t == o,f"Ohjelmasi tulostama rivi {i+1} on väärä. Sen pitäisi olla\n{o}\nSe oli kuitenkin\n{t}\nOhjelman koko tulostus oli\n{output_all}")               

    @points('8.maksukortti_osa4')
    def test12_paaohjelma2(self):

        src_file = os.path.join('src', 'maksukortti.py')
        kielletty = [
            "Pekka: Kortilla on rahaa 15.4 euroa",
            "Matti: Kortilla on rahaa 27.4 euroa",
            "Pekka: Kortilla on rahaa 35.4 euroa",
            "Matti: Kortilla on rahaa 22.8 euroa",
            "Pekka: Kortilla on rahaa 30.2 euroa",
            "Matti: Kortilla on rahaa 72.8 euroa"
        ]        
        with open(src_file) as f:
            for line in f:
                for k in kielletty:
                    if k in line:
                        self.assertTrue(False, f"tehtävässä on käytettävä Maksukortti-olioita eli koodistasi ei saa olla riviä\n{line}")                

        vaadittu = [
            "= Maksukortti(20)",
            ".syo_edullisesti()",
            ".syo_maukkaasti()",
            ".lataa_rahaa(20)"
        ]
        lines = []
        with open(src_file) as f:
            for line in f:
                lines.append(line)
    
        for v in vaadittu:
            on = False
            for line in lines:
                if v in line:
                    on = True              
            self.assertTrue(on, f"tehtävässä on käytettävä Maksukortti-olioita eli koodissasi pitäisi löytyä rivi, jolla on\n{v}")   

if __name__ == '__main__':
    unittest.main()

   
