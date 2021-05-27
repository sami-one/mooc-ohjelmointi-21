# TEE RATKAISUSI TÄHÄN:
import pygame, random
  
pygame.init()
naytto = pygame.display.set_mode((640, 480))

robo = pygame.image.load("robo.png")
robo_lev = robo.get_width()
robo_kor = robo.get_height()
x = 0
y = 480-robo.get_height()

oikealle = False
vasemmalle = False
alas = False
ylos = False

kello = pygame.time.Clock()

while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            pygame.quit()

        elif tapahtuma.type == pygame.KEYDOWN:
            if tapahtuma.key == pygame.K_RIGHT:
                oikealle = True
            if tapahtuma.key == pygame.K_LEFT:
                vasemmalle = True
            if tapahtuma.key == pygame.K_DOWN:
                alas = True
            if tapahtuma.key == pygame.K_UP:
                ylos = True

        elif tapahtuma.type == pygame.KEYUP:           
            if tapahtuma.key == pygame.K_RIGHT:
                oikealle = False
            if tapahtuma.key == pygame.K_LEFT:
                vasemmalle = False
            if tapahtuma.key == pygame.K_DOWN:
                alas = False
            if tapahtuma.key == pygame.K_UP:
                ylos = False
         
    if oikealle:
            x += 2
    if vasemmalle:
            x -= 2
    if alas :
            y += 2
    if ylos :
            y -= 2
                
    naytto.fill((0, 0, 0))
    naytto.blit(robo, (x, y))
    pygame.display.flip()
    kello.tick(60)
