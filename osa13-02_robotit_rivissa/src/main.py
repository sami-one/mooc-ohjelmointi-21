# TEE RATKAISUSI TÄHÄN:
import pygame
def robotit():
    x = 70
    y = 100
    for i in range(10):
        naytto.blit(robo, (x, y))
        x += leveys

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