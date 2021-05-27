# TEE RATKAISUSI TÄHÄN:
import pygame, random
def robotit():
    for i in range(1000):
        naytto.blit(robo, ((random.randint(0, 640-leveys), random.randint(0, 480-korkeus) )))

pygame.init()
naytto = pygame.display.set_mode((640, 480))

robo = pygame.image.load("robo.png")
leveys = robo.get_width()
korkeus = robo.get_height()

naytto.fill((0,0,0))
robotit()

pygame.display.flip()

while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            exit()