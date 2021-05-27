# Tee ratkaisusi tähän:
class  Lukutilasto:
    def __init__(self):
        self.lukuja = 0
        self.luvut = []

    def lisaa_luku(self, luku:int):
        self.lukuja += 1
        self.luvut.append(luku)

    def lukujen_maara(self):
        return self.lukuja

    def summa(self):
        return sum(self.luvut)

    def keskiarvo(self):
        try:
            self.ka = self.summa()/self.lukuja
            return self.ka
        except ZeroDivisionError:
            return 0

tilasto = Lukutilasto() 
tilasto_parilliset = Lukutilasto()
tilasto_parittomat = Lukutilasto()


while True:    
    luku = int(input("Anna lukuja: "))
    if luku == -1:
        break 
    tilasto.lisaa_luku(luku)
    if luku % 2 == 0:
        tilasto_parilliset.lisaa_luku(luku)
    else:
        tilasto_parittomat.lisaa_luku(luku)


print("Summa:", tilasto.summa())
print("Keskiarvo:", tilasto.keskiarvo())
print("Parillisten summa:", tilasto_parilliset.summa())
print("Parittomien summa:", tilasto_parittomat.summa())