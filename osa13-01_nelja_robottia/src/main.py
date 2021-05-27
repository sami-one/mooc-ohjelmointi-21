# Tämän osan tehtävissä ei ole automaattisia testejä, vaan testi antaa pisteet
# automaattisesti, kun lähetät ratkaisun palvelimelle. Lähetä ratkaisu vasta
# sitten, kun se on valmis ja vastaa tehtävänannon vaatimuksia. Vaikka tehtävissä
# ei ole testejä, kurssin henkilökunta näkee lähetetyt ratkaisut.

# TEE RATKAISUSI TÄHÄN:
import pygame
def robotit():
    naytto.blit(robo, (0, 0))
    naytto.blit(robo, (640-leveys, 0))
    naytto.blit(robo, (0, 480-korkeus))
    naytto.blit(robo, (640-leveys, 480-korkeus))

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