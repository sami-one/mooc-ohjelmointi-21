# TEE RATKAISUSI TÄHÄN:
import pygame
pygame.init()
naytto = pygame.display.set_mode((640, 480))

robo = pygame.image.load("robo.png")

x = 0
y = 0
nopeus = 1
kello = pygame.time.Clock()

while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            exit()

    naytto.fill((0,0,0))
    naytto.blit(robo, (x, y))
    pygame.display.flip()

    #Ensin oikeelle
    if x+robo.get_width() < 640 and y == 0:
        x += nopeus
    #Sitten alaspäin
    elif x == 640-robo.get_width() and y+robo.get_height() < 480:
        y +=nopeus
    #Vasemmalle
    elif x > 0 and y+robo.get_height() == 480:
        x -= nopeus
    #Ylös
    elif x == 0 and y > 0:
        y -= nopeus
        
    kello.tick(60) 