class Asunto:
    def __init__(self, huoneita: int, nelioita: int, neliohinta:int, kuvaus: str):
        self.huoneita = huoneita
        self.nelioita = nelioita
        self.neliohinta = neliohinta
        self.kuvaus = kuvaus

    def suurempi(self, verrattava):
        return self.nelioita > verrattava.nelioita

    def hintaero(self, verrattava):
        # Funktio abs palauttaa itseisarvon
        ero = abs((self.neliohinta * self.nelioita) - (verrattava.neliohinta * verrattava.nelioita))
        return ero

    def kalliimpi(self, verrattava):
        ero = (self.neliohinta * self.nelioita) - (verrattava.neliohinta * verrattava.nelioita)
        return ero > 0

    def __repr__(self):
        return (f'Asunto(huoneita = {self.huoneita}, nelioita = {self.nelioita}, ' + 
            f'neliohinta = {self.neliohinta}, kuvaus = {self.kuvaus})')

# TEE RATKAISUSI TÄHÄN:
def halvemmat(asunnot: list, verrattava: Asunto):
    return [(asunto, verrattava.neliohinta*verrattava.nelioita - asunto.neliohinta*asunto.nelioita) for asunto in asunnot if asunto.neliohinta*asunto.nelioita < verrattava.neliohinta*verrattava.nelioita]