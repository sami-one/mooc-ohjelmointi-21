import unittest
from unittest.mock import patch

from tmc import points, reflect
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import os.path
import textwrap
from random import choice, randint, shuffle
from datetime import date

exercise = 'src.salainen_taikajuoma'

def f(attr: list):
    return "\n".join([str(x) for x in attr]) 

@points('10.salainen_taikajuoma')
class TaikajuomaTest(unittest.TestCase):
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

    def test_1_luokka_taikajuoma_olemassa(self):
        try:
            from src.salainen_taikajuoma import Taikajuoma
            a = Taikajuoma("Vissy")
        except Exception as e:
            self.fail(f'Konstruktorikutsu Taikajuoma("Vissy") antoi virheen \n{e}\n' + 
            'Ethän ole muuttanut luokan Taikajuoma määrittelyä?')

    def test_2_luokka_salainen_taikajuoma_olemassa(self):
        try:
            from src.salainen_taikajuoma import SalainenTaikajuoma
            a = SalainenTaikajuoma("Supervissy", "abc")
        except Exception as e:
            self.fail(f'Konstruktorikutsu SalainenTaikajuoma("Supervissy", "abc") antoi virheen \n{e}\n' + 
            'Varmista, että luokka on olemassa ja että siitä voi luoda olion.')

    def test_3_perinta(self):
        from src.salainen_taikajuoma import Taikajuoma, SalainenTaikajuoma
        self.assertTrue(issubclass(SalainenTaikajuoma, Taikajuoma), 
            f"Luokan SalainenTaikajuoma pitäisi " +
            'periä luokka Taikajuoma!')

    def test_4_uudelleentoteutus(self):
        from src.salainen_taikajuoma import Taikajuoma, SalainenTaikajuoma
        self.assertTrue(Taikajuoma.lisaa_aines is not SalainenTaikajuoma.lisaa_aines, 
            "Metodi lisaa_aines pitää toteuttaa uudestaan luokassa SalainenTaikajuoma!")
        self.assertTrue(Taikajuoma.tulosta_resepti is not SalainenTaikajuoma.tulosta_resepti, 
            "Metodi tulosta_resepti pitää toteuttaa uudestaan luokassa SalainenTaikajuoma!")


    def test_5_lisaa_tulosta_toimivat_1(self):
        from src.salainen_taikajuoma import SalainenTaikajuoma
        test_cases = [("Eukalyptus",4),("Sisupastillit",24),("Taikapöly",4.5)]
        nimi = "Hengenrrrraikastus"
        ssana = "pokkushokkus"
        juoma = SalainenTaikajuoma(nimi, ssana)
        corr = nimi + ":"
        test_str = ""
        for test_case in test_cases:
            juoma.lisaa_aines(test_case[0], test_case[1], ssana)
            corr += f"\n{test_case[0]} {test_case[1]} grammaa"

        juoma.tulosta_resepti(ssana)
        output = "\n".join([x.strip() for x in get_stdout().split("\n") if len(x.strip()) > 0])
        test_str = "\n".join([str(x) for x in test_cases])

        self.assertEqual(output, corr, f'Metodin tulosta_resepti() pitäisi tulostaa\n' + 
            f'{corr}\n, mutta se tulostaa\n{output}\nkun reseptiin lisättiin ainekset:\n' +
            test_str)


    def test_6_lisaa_tulosta_toimivat_1(self):
        from src.salainen_taikajuoma import SalainenTaikajuoma
        test_cases = [("Korianteri",6),("Mustetta",14),("Kärpässientä",3.5)]
        nimi = "Sotkius"
        ssana = "abraka-abraka"
        juoma = SalainenTaikajuoma(nimi, ssana)
        corr = nimi + ":"
        test_str = ""
        for test_case in test_cases:
            juoma.lisaa_aines(test_case[0], test_case[1], ssana)
            corr += f"\n{test_case[0]} {test_case[1]} grammaa"

        juoma.tulosta_resepti(ssana)
        output = "\n".join([x.strip() for x in get_stdout().split("\n") if len(x.strip()) > 0])
        test_str = "\n".join([str(x) for x in test_cases])

        self.assertEqual(output, corr, f'Metodin tulosta_resepti() pitäisi tulostaa\n' + 
            f'{corr}\n, mutta se tulostaa\n{output}\nkun reseptiin lisättiin ainekset:\n' +
            test_str)

    def test_7_lisaa_vaara_salasana(self):
        from src.salainen_taikajuoma import SalainenTaikajuoma
        nimi = "Testius Maksimus"
        ssana = "testi123"
        juoma = SalainenTaikajuoma(nimi, ssana)
        try:
            juoma.lisaa_aines("Kärpässieni", 1.0, "testi321")
            self.fail(f"Metodin lisaa_aines() pitäisi antaa virhe ValueError " +
                f'kun luokka on alustettu seuraavasti:\n' +
                f'juoma = SalainenTaikajuoma("{nimi}", "{ssana}")\n' +
                f'ja metodia kutsutaan seuraavasti:\n' + 
                'juoma.lisaa_aines("Kärpässieni", 1.0, "testi321")')
        except ValueError:
            pass

    def test_8_tulosta_vaara_salasana(self):
        from src.salainen_taikajuoma import SalainenTaikajuoma
        nimi = "Testius Maksimus"
        ssana = "pokkus hokkus"
        juoma = SalainenTaikajuoma(nimi, ssana)
        juoma.lisaa_aines("Kärpässieni", 1.0, "pokkus hokkus")
        try:
            juoma.tulosta_resepti("hokkus pokkus")
            self.fail(f"Metodin tulosta_resepti() pitäisi antaa virhe ValueError " +
                f'kun luokka on alustettu seuraavasti:\n' +
                f'juoma = SalainenTaikajuoma("{nimi}", "{ssana}")\n' +
                f'ja on lisätty yksi aines:\n' + 
                'juoma.lisaa_aines("Kärpässieni", 1.0, "pokkus hokkus")\nja ' +
                'metodia kutsutaan seuraavasti:\n'
                'juoma.tulosta_resepti("hokkus pokkus")')
        except ValueError:
            pass


    
    
if __name__ == '__main__':
    unittest.main()
