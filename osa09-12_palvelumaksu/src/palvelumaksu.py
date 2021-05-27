# TEE RATKAISUSI TÄHÄN:
class Pankkitili:

    def __init__(self, tilinomistaja: str, tilinumero: str, saldo: float):
        self.__tilinomistaja = tilinomistaja
        self.__tilinumero = tilinumero
        self.__saldo = saldo


    def talleta(self, summa: float):
        self.__saldo += summa
        self.__palvelumaksu()

    def nosta(self, summa: float):
        if self.__saldo>= summa:
            self.__saldo -= summa
        self.__palvelumaksu()

    @property
    def saldo(self):
        return self.__saldo

    def __palvelumaksu(self):
        self.__saldo *= 0.99