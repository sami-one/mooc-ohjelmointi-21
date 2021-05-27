# TEE RATKAISUSI TÄHÄN:
class Aanite:

    def __init__(self, pituus):
        if pituus >= 0:
            self.__pituus = pituus
        else:
            raise ValueError("Ei voi olla negatiivinen!")

    @property
    def pituus(self):
        return self.__pituus

    @pituus.setter
    def pituus(self, pituus):
        if pituus >= 0:
            self.__pituus = pituus
        else:
            raise ValueError("Ei voi olla negatiivinen!")

    



