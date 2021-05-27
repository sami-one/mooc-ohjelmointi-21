# TEE RATKAISUSI TÄHÄN:
import pygame, math
from datetime import datetime

class Viisari:
    def __init__(self, pituus, nopeus, alkuaika, leveys):
        self.pituus = pituus
        self.kulma = 2* math.pi / 60 * (alkuaika -15)
        self.nopeus = nopeus
        self.leveys = leveys

    def liike(self):
        self.kulma += self.nopeus
        self.x = 320+math.cos(self.kulma)*self.pituus
        self.y = 240+math.sin(self.kulma)*self.pituus

    def koords(self):
        return self.x, self.y

class Aika:
    def __init__(self):
        self.h = datetime.now().strftime("%H")
        self.m = datetime.now().strftime("%M")
        self.s = datetime.now().strftime("%S")

    def aikaInt(self):
        return (int(self.h), int(self.m), int(self.s))

    def aikaStr(self):
        return datetime.now().strftime("%H:%M:%S")     

pygame.init()
WIDTH = 640
HEIGHT = 480
naytto = pygame.display.set_mode((WIDTH, HEIGHT))
keski = (int(WIDTH/2), int(HEIGHT/2))
kello = pygame.time.Clock()

klo = Aika()
h, m, s = klo.aikaInt()

sViisari = Viisari(190, 2 * math.pi / 60, s-1, 1)
mViisari = Viisari(180, 2 * math.pi / (60 * 60), m, 2)
hViisari = Viisari(155, 2 * math.pi / (60 * 60 * 12), h * 5, 4)
viisarit = [sViisari, mViisari, hViisari]

while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            exit()

    naytto.fill((0, 0, 0)) 
    klo = Aika()
    pygame.display.set_caption(klo.aikaStr())
    pygame.draw.circle(naytto, (255, 0, 0), keski, 202)
    pygame.draw.circle(naytto, (0, 0, 0), keski, 199)
    pygame.draw.circle(naytto, (255, 0, 0), keski, 10)

    for viisari in viisarit:
        viisari.liike()
        pygame.draw.line(naytto, (0, 0, 255), (viisari.koords()), keski, viisari.leveys)    
                
    pygame.display.flip()     
    kello.tick(1)
