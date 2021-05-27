# TEE RATKAISUSI TÄHÄN:
class Lottorivi:
    def __init__(self, kierros, numerot):
        self.kierros = kierros
        self.numerot = numerot

    def osumien_maara(self, pelattu_rivi: list):
        return len([nro for nro in pelattu_rivi if nro in self.numerot])

    def osumat_paikoillaan(self, pelattu_rivi):
        return [nro if nro in self.numerot else -1 for nro in pelattu_rivi]