import unittest
from unittest.mock import patch

from tmc import points, reflect
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import os.path
import textwrap
from random import choice, randint
from datetime import date

exercise = 'src.maksukortti_ja_kassapaate'

def f(attr: list):
    return ",".join([str(x) for x in attr]) 


class MaksukorttiJaKassapaateTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=[AssertionError("Syötteen pyytämistä ei odotettu")]):
           cls.module = load_module(exercise, 'fi')

    @points('9.maksukortti_ja_kassapaate_osa1')
    def test_0a_paaohjelma_kunnossa(self):
        ok, line = check_source(self.module)
        message = """Funktioita testaava koodi tulee sijoittaa lohkon
if __name__ == "__main__":
sisälle. Seuraava rivi tulee siirtää:
"""
        self.assertTrue(ok, message+line)

    @points('9.maksukortti_ja_kassapaate_osa1')
    def test_1_luokka_maksukortti_olemassa(self):
        try:
            from src.maksukortti_ja_kassapaate import Maksukortti
            h = Maksukortti(1.0)
        except Exception as e:
            self.fail(f'Konstruktorikutsu Maksukortti(1.0) antoi virheen \n{e}')
        try:
            h.lataa_rahaa(1)
        except Exception as e:
            self.fail(f'Metodikutsu lataa_rahaa(1) antoi virheen \n{e}')
         

    @points('9.maksukortti_ja_kassapaate_osa1')
    def test_2_tyhma_kortti(self):
        test_cases = [(100,50), (100, 150), (200, 50, 100), (1000, 500, 600), 
            (500, 100, 200, 200, 100), (10, 2, 3, 2, 1, 3)]
        for test_case in test_cases:
            from src.maksukortti_ja_kassapaate import Maksukortti
            kortti = Maksukortti(test_case[0])
            corr_bool = []
            corr_saldo = [] 
            val_bool = [] 
            val_saldo = []
            saldo = test_case[0]

            for n in test_case[1:]:
                val_bool.append(str(kortti.ota_rahaa(n)))
                val_saldo.append(str(kortti.saldo))
                
                if saldo >= n:
                    saldo -= n
                    corr_bool.append(str(True))
                else:
                    corr_bool.append(str(False))
                corr_saldo.append(str(saldo))

            self.assertEqual(corr_bool, val_bool, f'Kortti luotiin kutsulla Maksukortti({test_case[0]}).\n'+
                f'Sen jälkeen kutsuttiin metodia ota_rahaa arvo(i)lla {f(test_case[1:])}\n' +
                f'Metodin olisi pitänyt palauttaa {",".join(corr_bool)}\n' +
                f'mutta se palautti {",".join(val_bool)}')

            self.assertEqual(corr_saldo, val_saldo, f'Kortti luotiin kutsulla Maksukortti({test_case[0]}).\n'+
                f'Sen jälkeen kutsuttiin metodia ota_rahaa arvo(i)lla {f(test_case[1:])}\n' +
                f'Saldon olisi pitänyt olla {",".join(corr_saldo)}\n' +
                f'mutta se oli {",".join(val_saldo)}')
                


    
    @points('9.maksukortti_ja_kassapaate_osa2')
    def test_3a_luokka_kassapaate_olemassa(self):
        try:
            from src.maksukortti_ja_kassapaate import Kassapaate
            h = Kassapaate()
        except Exception as e:
            self.fail(f'Konstruktorikutsu Kassapaate() antoi virheen \n{e}')

    @points('9.maksukortti_ja_kassapaate_osa2')
    def test_3b_kateiskauppa1(self):
        test_cases = [(10, True), (10,False), (50, True), (30, False), (100, True), (1, True), (1.50, False)]
        from src.maksukortti_ja_kassapaate import Kassapaate
        kassa = Kassapaate()
        
        op = "" 
        se = 0 
        sm = 0
        for test_case in test_cases:
            if test_case[1]:
                val = kassa.syo_edullisesti(test_case[0])
                corr = test_case[0]
                if test_case[0] >= 2.50:
                    corr -= 2.50
                    op += "\n" + "syo_edullisesti()"
                    se += 1
                self.assertEqual(corr,val,f'Metodin syo_edullisesti() pitäiti palauttaa {corr}, ' +
                    f'kun sitä kutsutaan parametrilla {test_case[0]}. n' +
                    f'Nyt metodi palautti {val}.')
            else:
                val = kassa.syo_maukkaasti(test_case[0])
                corr = test_case[0]
                if test_case[0] >= 4.30:
                    corr -= 4.30
                    op += "\n" + "syo_maukkaasti()"
                    sm += 1
                self.assertEqual(corr,val,f'Metodin syo_maukkaasti() pitäisi palauttaa {corr}, ' +
                    f'kun sitä kutsutaan parametrilla {test_case[0]}. n' +
                    f'Nyt metodi palautti {val}.')

        self.assertEqual(kassa.edulliset, se, f'Attribuutin edulliset arvon pitäisi olla {se}\n' +
            f'kun metodeja kutsuttiin seuraavasti:{op}\nNyt sen arvo on {kassa.edulliset}')
        
        self.assertEqual(kassa.maukkaat, sm, f'Attribuutin maukkaat arvon pitäisi olla {sm}\n' +
            f'kun metodeja kutsuttiin seuraavasti:{op}\nNyt sen arvo on {kassa.maukkaat}')    

    @points('9.maksukortti_ja_kassapaate_osa2')
    def test_3c_kateiskauppa_random(self):
        test_cases = []
        for i in range(randint(10,15)):
            test_cases.append((randint(1,9), randint(1,2) == 1))
        from src.maksukortti_ja_kassapaate import Kassapaate
        kassa = Kassapaate()
        
        op = "" 
        se = 0 
        sm = 0
        for test_case in test_cases:
            if test_case[1]:
                val = kassa.syo_edullisesti(test_case[0])
                corr = test_case[0]
                if test_case[0] >= 2.50:
                    corr -= 2.50
                    op += "\n" + "syo_edullisesti()"
                    se += 1
                self.assertEqual(corr,val,f'Metodin syo_edullisesti() pitäiti palauttaa {corr}, ' +
                    f'kun sitä kutsutaan parametrilla {test_case[0]}. n' +
                    f'Nyt metodi palautti {val}.')
            else:
                val = kassa.syo_maukkaasti(test_case[0])
                corr = test_case[0]
                if test_case[0] >= 4.30:
                    corr -= 4.30
                    op += "\n" + "syo_maukkaasti()"
                    sm += 1
                self.assertEqual(corr,val,f'Metodin syo_maukkaasti() pitäisi palauttaa {corr}, ' +
                    f'kun sitä kutsutaan parametrilla {test_case[0]}. n' +
                    f'Nyt metodi palautti {val}.')

        self.assertEqual(kassa.edulliset, se, f'Attribuutin edulliset arvon pitäisi olla {se}\n' +
            f'kun metodeja kutsuttiin seuraavasti:{op}\nNyt sen arvo on {kassa.edulliset}')
        
        self.assertEqual(kassa.maukkaat, sm, f'Attribuutin maukkaat arvon pitäisi olla {sm}\n' +
            f'kun metodeja kutsuttiin seuraavasti:{op}\nNyt sen arvo on {kassa.maukkaat}')   


    @points('9.maksukortti_ja_kassapaate_osa3')
    def test_4_kortilla_maksaminen(self):
        test_cases = [(10, True), (20, False), (10, True, True), (10, False, False),
        (30, False, False, False, True, True), (5, True, True, True), (10, False, False, False),
        (20, False, True, False, True, True, True, False)]

        for test_case in test_cases:
            from src.maksukortti_ja_kassapaate import Kassapaate, Maksukortti
            kassa = Kassapaate()
            kortti = Maksukortti(test_case[0])
            saldo = test_case[0]
            op = f"Maksukortti({test_case[0]})"
            se = 0 
            sm = 0

            for tapahtuma in test_case[1:]:
                orig_saldo = saldo
                if tapahtuma:
                    kassa.syo_edullisesti_kortilla(kortti)
                    if saldo >= 2.50:
                        saldo -= 2.50
                        op += "\nsyo_edullisesti_kortilla()"
                        se += 1
                    self.assertEqual(saldo, kortti.saldo, f'Kortin saldon pitäisi olla {saldo}, kun se oli {orig_saldo},' + 
                        f' ja kutsuttiin metodia syo_edullisesti_kortilla. Nyt saldo on kuitenkin {kortti.saldo}')
                else:
                    kassa.syo_maukkaasti_kortilla(kortti)
                    if saldo >= 4.30:
                        saldo -= 4.30
                        op += "\nsyo_maukkaasti_kortilla()"
                        sm += 1
                    self.assertEqual(saldo, kortti.saldo, f'Kortin saldon pitäisi olla {saldo}, kun se oli {orig_saldo},' + 
                        f' ja kutsuttiin metodia syo_edullisesti_kortilla. Nyt saldo on kuitenkin {kortti.saldo}') 
            
            self.assertEqual(kassa.edulliset, se, f'Attribuutin edulliset arvon pitäisi olla {se}\n' +
            f'kun metodeja kutsuttiin seuraavasti:{op}\nNyt sen arvo on {kassa.edulliset}')
        
        self.assertEqual(kassa.maukkaat, sm, f'Attribuutin maukkaat arvon pitäisi olla {sm}\n' +
            f'kun metodeja kutsuttiin seuraavasti:{op}\nNyt sen arvo on {kassa.maukkaat}')  

    @points('9.maksukortti_ja_kassapaate_osa4')
    def test_5_lataa_rahaa(self):
        test_cases = [(0, 10), (10, 30), (100, 100), (10, 2000), (5, 5.50), (2.50, 172.25)]
        for test_case in test_cases:
            from src.maksukortti_ja_kassapaate import Kassapaate, Maksukortti
            kassa = Kassapaate()
            kortti = Maksukortti(test_case[0])
            kassa.lataa_rahaa_kortille(kortti, test_case[1])
            corr = sum(test_case)
            val = kortti.saldo

            self.assertEqual(val, corr, f'Kortin saldon pitäisi olla {corr}, kun se oli aluksi {test_case[0]}\n' + 
                f'ja kutsuttiin metodia lataa_rahaa_kortille({test_case[1]}).\n' +
                f'Nyt saldo on kuitenkin {val}.')

                

                
if __name__ == '__main__':
    unittest.main()
