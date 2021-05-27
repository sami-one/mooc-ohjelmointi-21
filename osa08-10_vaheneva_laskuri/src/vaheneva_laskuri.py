# Tee ratkaisusi tähän:
class VahenevaLaskuri:
    def __init__(self, arvo_alussa: int):
        self.arvo = arvo_alussa

    def tulosta_arvo(self):
        print("arvo:", self.arvo)

    def vahenna(self):
        pass

    # ja tänne muut metodit
class VahenevaLaskuri:
    def __init__(self, arvo_alussa: int):
        self.arvo = arvo_alussa
        self.arvo_alussa = arvo_alussa

    def tulosta_arvo(self):
        print("arvo:", self.arvo)

    def vahenna(self):
        if self.arvo > 0:
            self.arvo -= 1
    

    def nollaa(self):
        self.arvo = 0

    def palauta_alkuperainen_arvo(self):
        self.arvo = self.arvo_alussa