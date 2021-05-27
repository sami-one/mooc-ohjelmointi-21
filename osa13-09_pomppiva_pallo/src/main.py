# TEE RATKAISUSI TÄHÄN:
import pygame

pygame.init()
naytto = pygame.display.set_mode((640, 480))
kello = pygame.time.Clock()

pallo = pygame.image.load("pallo.png")
x = 0
y = 0
nopeus = [3, 3]
while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            exit()

    x += nopeus[0]
    y += nopeus[1]
    if x+pallo.get_width() > 640 or x < 0:
        nopeus[0] = -nopeus[0]

    if y+pallo.get_height() > 480 or y < 0:
        nopeus[1] = -nopeus[1]

    naytto.fill((0, 0, 0)) 
    naytto.blit(pallo, (x, y))
 
    pygame.display.flip()
    kello.tick(60)