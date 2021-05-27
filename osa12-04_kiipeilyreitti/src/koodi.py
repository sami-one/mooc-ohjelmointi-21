class Kiipeilyreitti:
    def __init__(self, nimi: str, pituus: int, grade: str):
        self.nimi = nimi
        self.pituus = pituus
        self.grade = grade

    def __str__(self):
        return f"{self.nimi}, pituus {self.pituus} metriä, grade {self.grade}"

# Tee ratkaisusi tähän:
def pituuden_mukaan(reitit: list):
    def pituusjarjestys(reitti):
        return reitti.pituus
    return sorted(reitit, key=pituusjarjestys, reverse=True)

 

def vaikeuden_mukaan(reitit: list):
    def vaikeusjarjestys(reitti):
        return (reitti.grade, reitti.pituus)
    return sorted(reitit, key=vaikeusjarjestys, reverse=True)