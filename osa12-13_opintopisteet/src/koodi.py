from functools import reduce

class Suoritus:
    def __init__(self, kurssi: str, arvosana: int, opintopisteet: int):
        self.kurssi = kurssi
        self.arvosana = arvosana
        self.opintopisteet = opintopisteet

    def __str__(self):
        return f"{self.kurssi} ({self.opintopisteet} op) arvosana {self.arvosana}"

# Tee ratkaisusi tähän:

def kaikkien_opintopisteiden_summa(lista):
    int_lista = [suoritus.opintopisteet for suoritus in lista]
    return reduce(lambda x, y: x + y, int_lista)

def hyvaksyttyjen_opintopisteiden_summa(lista):
    filter_lista = filter(lambda suoritus: suoritus.arvosana > 0, lista)
    int_lista = [suoritus.opintopisteet for suoritus in filter_lista if suoritus.arvosana > 0]
    return reduce(lambda x, y: x + y, int_lista) 
    
def keskiarvo(lista):
    filter_lista = filter(lambda suoritus: suoritus.arvosana > 0, lista)
    int_lista = [suoritus.arvosana for suoritus in filter_lista ]
    return reduce(lambda x, y: x + y, int_lista) / len(int_lista)
