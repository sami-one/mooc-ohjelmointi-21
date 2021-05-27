# Tee ratkaisusi tähän:
class Kello:

    def __init__(self, h, m, s):
        self.h = h
        self.m = m
        self.s = s

    def tick(self):
        self.s += 1
        if self.s ==60:
            self.s = 0
            self.m += 1
        if self.m ==60:
            self.m = 0
            self.h +=1
        if self.h == 24:
            self.h = 0

    def nollako(self, i):
        if i < 10:
            return "0"+str(i)
        else:
            return str(i)
        
    def aseta(self, h, m):
        self.h = h
        self.m = m
        self.s = 0

    def __repr__(self):
        return f"{self.nollako(self.h)}:{self.nollako(self.m)}:{self.nollako(self.s)}"

if __name__ == "__main__":
    kello = Kello(23, 59, 55)
    print(kello)
    for i in range(8):
        kello.tick()
        print(kello)
    
    kello.aseta(1, 1)
    print(kello)