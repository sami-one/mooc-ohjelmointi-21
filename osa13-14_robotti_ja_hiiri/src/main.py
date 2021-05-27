# TEE RATKAISUSI TÄHÄN:
import pygame

pygame.init()
naytto = pygame.display.set_mode((640, 480))

robo = pygame.image.load("robo.png")


robo_x = 0
robo_y = 0
hiiri_x = 0
hiiri_y = 0

kello = pygame.time.Clock()

while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.MOUSEMOTION:
            hiiri_x = tapahtuma.pos[0]
            hiiri_y = tapahtuma.pos[1]
        if tapahtuma.type == pygame.QUIT:
            exit(0)

    robo_x = hiiri_x -robo.get_width()/2
    robo_y = hiiri_y - robo.get_height()/2
    
    naytto.fill((0, 0, 0))
    naytto.blit(robo, (robo_x, robo_y))
    pygame.display.flip()

    kello.tick(160)