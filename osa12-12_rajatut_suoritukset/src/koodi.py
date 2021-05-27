class Suoritus:
    def __init__(self, opiskelijan_nimi: str, kurssi: str, arvosana: int):
        self.opiskelijan_nimi = opiskelijan_nimi
        self.kurssi = kurssi
        self.arvosana = arvosana

    def __str__(self):
        return f"{self.opiskelijan_nimi}, arvosana kurssilta {self.kurssi} {self.arvosana}"

def hyvaksytyt(suoritukset: list):
    return filter(lambda s : s.arvosana >= 1, suoritukset)

def suoritus_arvosanalla(suoritukset: list, arvosana: int):
    return filter(lambda s : s.arvosana == arvosana, suoritukset)

def kurssin_suorittajat(suoritukset: list, kurssi: str):
    s =  filter(lambda s: s.arvosana > 0 and s.kurssi == kurssi, suoritukset)
    return sorted(map(lambda suoritus : suoritus.opiskelijan_nimi, s))