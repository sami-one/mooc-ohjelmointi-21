# TEE RATKAISUSI TÄHÄN:
import pygame, math
class Robo:

    def __init__(self, alku_x, alku_y, kulma):
        self.x = alku_x
        self.y = alku_y
        self.kulma = kulma

    def liiku(self):
        self.kulma += 0.01
        self.x = 320+math.cos(self.kulma)*piiri -robo.get_width()/2
        self.y = 240+math.sin(self.kulma)*piiri -robo.get_height()/2

pygame.init()
naytto = pygame.display.set_mode((640, 480))

robo = pygame.image.load("robo.png")
piiri = 140

kulma = 0
robot = []
for i in range(10):
    x = 320 + math.cos(kulma) * piiri - robo.get_width()/2
    y = 240 + math.sin(kulma) * piiri - robo.get_height()/2
    robot.append(Robo(x, y, kulma))
    kulma += 2* math.pi / 10

kello = pygame.time.Clock()

while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            exit()
    naytto.fill((0, 0, 0))

    for r in robot:
        r.liiku()
        naytto.blit(robo, (r.x, r.y)) 

    pygame.display.flip()     
    kello.tick(80)
