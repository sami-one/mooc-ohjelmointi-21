class Palloilija:
    def __init__(self, nimi: str, pelinumero: int, maalit: int, syotot: int, minuutit: int):
        self.nimi = nimi
        self.pelinumero = pelinumero
        self.maalit = maalit
        self.syotot = syotot
        self.minuutit = minuutit

    def __str__(self):
        return (f'Palloilija(nimi={self.nimi}, pelinumero={self.pelinumero}, '
            f'maalit={self.maalit}, syotot={self.syotot}, minuutit={self.minuutit})')

# TEE RATKAISUSI TÄHÄN:
def eniten_maaleja(palloilijat):
    return max(palloilijat, key=lambda palloilija: palloilija.maalit).nimi

def eniten_pisteita(palloilijat):
        p = max(palloilijat, key=lambda palloilija: palloilija.maalit + palloilija.syotot)
        return (p.nimi, p.pelinumero)

def vahiten_minuutteja(palloilijat):
    return min(palloilijat, key=lambda palloilija: palloilija.minuutit)

