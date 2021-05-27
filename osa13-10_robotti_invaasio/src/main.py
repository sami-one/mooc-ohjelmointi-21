# TEE RATKAISUSI TÄHÄN:
import pygame, random
class Robo:
    def __init__(self):
        self.x = random.randint(0, WIDTH - robo.get_width())
        self.y = 0 - robo.get_height()
        self.nopeus = 1
        self.ruudussa = True

    def liike(self):        
        if self.y + robo.get_height() == HEIGHT:           
            if self.x < int(WIDTH / 2):
                 self.x -= self.nopeus
            else:
                 self.x += self.nopeus
        else:
             self.y += self.nopeus             
        if self.x < 0 - robo.get_width() or self.x > WIDTH:    
             self.ruudussa = False

pygame.init()
kello = pygame.time.Clock()
WIDTH = 640
HEIGHT = 480
naytto = pygame.display.set_mode((WIDTH, HEIGHT))
robo = pygame.image.load("robo.png")
robot = []

while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            pygame.quit()
    naytto.fill((0, 0, 0))      
    tippuuko = random.randint(0,40)
    if tippuuko == 40:
        robot.append(Robo())
    for robotti in robot:
        if robotti.ruudussa:
            robotti.liike()
            naytto.blit(robo, (robotti.x, robotti.y))
        else:
            robot.remove(robotti)

    pygame.display.flip()     
    kello.tick(60)