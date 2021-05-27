# Tee ratkaisusi tähän:
class Sarja:

    def __init__(self, nimi, kausia, genret):
        self.nimi = nimi
        self.kausia = kausia
        self.genret = genret
        self.arvostelutListana = []  

    def genretStringina(self):
        str = ""
        for g in self.genret:
            str += g + ", "
        return str[:-2]

    def ka(self): 
        return sum(self.arvostelutListana)/len(self.arvostelutListana)

    def arvosteluja(self):
       if self.arvostelutListana == []:
           return "ei arvosteluja"
       else:
          
           return f"arvosteluja {len(self.arvostelutListana)}, keskiarvo {self.ka():.1f} pistettä"

    def arvostele(self, arvosana):       
        self.arvostelutListana.append(arvosana)  


    def __repr__(self):
        return f"{self.nimi} ({self.kausia} esityskautta)\ngenret: {self.genretStringina()}\n{self.arvosteluja()}"


def arvosana_vahintaan(arvosana: float, sarjat: list):
    l = []
    for s in sarjat:
        if s.ka() >= arvosana:
            l.append(s)
    return l

def sisaltaa_genren(genre: str, sarjat: list):
    l = []
    for s in sarjat:
        if genre in s.genret:
            l.append(s)
    return l
            
                          
if __name__ == "__main__":

    dexter = Sarja("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
    print(dexter)
    dexter.arvostele(4)
    dexter.arvostele(5)
    dexter.arvostele(5)
    dexter.arvostele(3)
    dexter.arvostele(0)
    print(dexter)

    s1 = Sarja("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
    s1.arvostele(5)

    s2 = Sarja("South Park", 24, ["Animation", "Comedy"])
    s2.arvostele(3)

    s3 = Sarja("Friends", 10, ["Romance", "Comedy"])
    s3.arvostele(2)

    sarjat = [s1, s2, s3]

    print("arvosana vähintään 4.5:")
    for sarja in arvosana_vahintaan(4.5, sarjat):
        print(sarja.nimi)

    print("genre Comedy:")
    for sarja in sisaltaa_genren("Comedy", sarjat):
        print(sarja.nimi)