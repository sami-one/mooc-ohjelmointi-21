# TEE RATKAISUSI TÄHÄN:
import pygame
def robotit():
    x_alku = 50
    y = 100
    for i in range(10):
        x = x_alku
        for j in range(10):
            naytto.blit(robo, (x, y))
            x += leveys -8
        y += 20
        x_alku += 10

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