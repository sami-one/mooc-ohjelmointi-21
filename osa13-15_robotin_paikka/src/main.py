# TEE RATKAISUSI TÄHÄN:
import pygame, random

pygame.init()
naytto = pygame.display.set_mode((640, 480))

robo = pygame.image.load("robo.png")

rob_lev = robo.get_width()
robo_kor = robo.get_height()
random_x = random.randint(0, 640 - rob_lev)
random_y = random.randint(0, 480 - robo_kor)
naytto.blit(robo, (random_x, random_y))
pygame.display.flip()
while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            exit()
        if tapahtuma.type == pygame.MOUSEBUTTONDOWN:
            hiiri_x = tapahtuma.pos[0]
            hiiri_y = tapahtuma.pos[1]
            if hiiri_x >= random_x and hiiri_x <= random_x + rob_lev and hiiri_y >= random_y and hiiri_y <= random_y + robo_kor:
                random_x = random.randint(0, 640 - rob_lev)
                random_y = random.randint(0, 480 - robo_kor)
                naytto.fill((0, 0, 0))
                naytto.blit(robo, (random_x, random_y))
                pygame.display.flip()
               
            
