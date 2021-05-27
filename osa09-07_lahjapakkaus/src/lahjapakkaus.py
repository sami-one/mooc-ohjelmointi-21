# TEE RATKAISUSI TÄHÄN:
class Lahja:

    def __init__(self, nimi, paino):
        self.nimi = nimi
        self.paino = paino

    
    def __repr__(self):
        return f"{self.nimi} ({self.paino} kg)"


class Pakkaus:

    def __init__(self):
        self.yhtpaino = 0

    def lisaa_lahja(self, lahja: Lahja):
        self.yhtpaino += lahja.paino

    def yhteispaino(self):
        return self.yhtpaino



#if __name__ == "__main__":