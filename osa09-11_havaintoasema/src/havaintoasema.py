# TEE RATKAISUSI TÄHÄN:
class Havaintoasema:

    def __init__(self, nimi):
        self.__nimi = nimi
        self.__havainnot = []
    
    def lisaa_havainto(self, havainto: str):
        self.__havainnot.append(havainto)

    def viimeisin_havainto(self):
        if self.__havainnot == []:
            return ""
        return self.__havainnot[-1]

    def havaintojen_maara(self):
        return len(self.__havainnot)

    def __repr__(self):
        return f"{self.__nimi}, {self.havaintojen_maara()} havaintoa"

if __name__ == "__main__":
    asema = Havaintoasema("Kumpula")
    asema.lisaa_havainto("Sadetta 10mm")
    asema.lisaa_havainto("Aurinkoista")
    print(asema.viimeisin_havainto())

    asema.lisaa_havainto("Ukkosta")
    print(asema.viimeisin_havainto())

    print(asema.havaintojen_maara())
    print(asema)