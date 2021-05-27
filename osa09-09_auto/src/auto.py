# TEE RATKAISUSI TÄHÄN:

class Auto:
    
    def __init__(self):
        self.__bensaa = 0
        self.__km = 0

    def tankkaa(self):
        self.__bensaa = 60

    def aja(self, km):
        pystyy_ajamaan = km
        if km > self.__bensaa:
            pystyy_ajamaan = self.__bensaa
        self.__bensaa -= pystyy_ajamaan
        self.__km += pystyy_ajamaan

    def __repr__(self):
        return f"auto: ajettu {self.__km} km, bensaa {self.__bensaa} litraa"

if __name__ == "__main__":
    auto = Auto()
    print(auto)
    auto.tankkaa()
    print(auto)
    auto.aja(20)
    print(auto)
    auto.aja(50)
    print(auto)
    auto.aja(10)
    print(auto)
    auto.tankkaa()
    auto.tankkaa()
    print(auto)
