# TEE RATKAISUSI TÄHÄN:
import pygame
class Robo:
    def __init__(self, alku_x, alku_y, nopeus):
        self.x = alku_x
        self.y = alku_y
        self.nopeus = nopeus

    def liike(self):
        self.x += self.nopeus
        if (self.nopeus > 0 and self.x+robo.get_width() >= 640) or (self.nopeus < 0 and self.x <= 0):
            self.nopeus = -self.nopeus

pygame.init()
naytto = pygame.display.set_mode((640, 480))

robo = pygame.image.load("robo.png")

robo1 = Robo(0, 60, 1)
robo2 = Robo(0, 150, 2)

kello = pygame.time.Clock()


while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            exit()

    naytto.fill((0, 0, 0))      
    robo1.liike()
    robo2.liike()
    naytto.blit(robo, (robo1.x, robo1.y))
    naytto.blit(robo, (robo2.x, robo2.y))    

    pygame.display.flip()     
    kello.tick(60)