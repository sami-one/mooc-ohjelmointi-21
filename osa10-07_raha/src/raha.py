# TEE RATKAISUSI TÄHÄN:
class Raha:

    def __init__(self, eurot, sentit):
        self.__eurot = eurot
        self.__sentit = sentit

    def __eq__(self, toinen):
        if self.__eurot == toinen.__eurot and self.__sentit == toinen.__sentit:
            return True
        return False

    def __gt__(self, toinen):
        if self.__eurot > toinen.__eurot:
            return True
        elif self.__eurot == toinen.__eurot and self.__sentit > toinen.__sentit:
            return True
        return False

    def __lt__(self, toinen):
        if self == toinen:
            return False
        return not self > toinen

    def __ne__(self, toinen):
        return not self == toinen

    def __add__(self, toinen):
        e = 0
        c = self.__sentit + toinen.__sentit
        if c >= 100:
            c -= 100
            e = 1
        e = e + self.__eurot + toinen.__eurot
        return Raha(e, c)

    def __sub__(self, toinen):
        if toinen > self:
            raise ValueError(f"negatiivinen tulos ei sallittu") 
        e = 0
        c = self.__sentit - toinen.__sentit
        if c < 0:
            c += 100
            e = -1
        e = e + self.__eurot - toinen.__eurot
        return Raha(e, c)

    def __repr__(self):
        c = self.__sentit
        if c < 10:
            c = "0" + str(c)
        return f"{self.__eurot}.{c} eur"

if __name__ == "__main__":
    e1 = Raha(4, 5)
    e2 = Raha(2, 95)

    e3 = e1 + e2
    e4 = e1 - e2

    print(e3)
    print(e4)

    #e5 = e2-e1
    print(e1)
    e1.eurot = 1000
    print(e1)