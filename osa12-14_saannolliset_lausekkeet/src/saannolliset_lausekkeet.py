# TEE RATKAISUSI TÄHÄN:
import re
def on_viikonpaiva(mjono: str):
    lauseke = re.compile("ma|ti|ke|to|pe|la|su")
    if lauseke.search(mjono):
        return True
    return False

def kaikki_vokaaleja(mjono: str):
    lauseke = re.compile("[aeiouyäöå]")  
    for merkki in  mjono:
         if not lauseke.search(merkki):
            return False
    return True

def kellonaika(mjono: str):
    lauseke1_yleis = re.compile("[0-2]{1}[0-9]{1}:[0-5]{1}[0-9]{1}:[0-5]{1}[0-9]{1}")  
    lauseke2_tunnit = re.compile("^[2]{1}[4-9]{1}")
    if lauseke2_tunnit.search(mjono):
        return False
    if lauseke1_yleis.search(mjono):
        return True
    return False