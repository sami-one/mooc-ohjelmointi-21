# Tee ratkaisusi tähän:
class Sekuntikello:
    def __init__(self):
        self.sekunnit = 0
        self.minuutit = 0

    def tick(self):
        self.sekunnit += 1
        if self.sekunnit == 60:
            self.sekunnit = 0
            self.minuutit += 1
        if self.minuutit == 60:
            self.minuutit = 0

    def __repr__(self):
        m = self.minuutit 
        s = self.sekunnit
        if m < 10:
            m = "0"+ str(self.minuutit)
        if s < 10:
            s = "0"+ str(self.sekunnit)
        return f"{m}:{s}"



if __name__ == "__main__":
    kello = Sekuntikello()
    for i in range(0, 3600):
        print(kello)
        kello.tick()