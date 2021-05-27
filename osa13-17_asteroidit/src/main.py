# TEE RATKAISUSI TÄHÄN:
import pygame, random

class Robo:
    def __init__(self):
        self.x = int(WIDTH/2)
        self.y = HEIGHT-robo.get_height()
        self.nopeus = 4
        self.oikealle = False           
        self.vasemmalle = False
   
    def key_events(self, tapahtuma):
        if tapahtuma.type == pygame.KEYDOWN:
            if tapahtuma.key == pygame.K_RIGHT:
                self.oikealle = True
            if tapahtuma.key ==  pygame.K_LEFT:
                self.vasemmalle = True
        if tapahtuma.type == pygame.KEYUP:
            if tapahtuma.key ==  pygame.K_RIGHT:
                self.oikealle = False
            if tapahtuma.key ==  pygame.K_LEFT:
                self.vasemmalle = False
                
    def liiku(self):
        if self.oikealle and self.x <= WIDTH - self.nopeus:
            self.x += self.nopeus   
        if self.vasemmalle and self.x >= self.nopeus:
            self.x -= self.nopeus   

class Kivi:
    def __init__(self):
        self.x = random.randint(0, WIDTH - kivi.get_width())  
        self.y = 0
        self.nopeus = 1
        self.ruudulla = True
        self.loppu = False
    
    def liiku(self):
        self.y += self.nopeus
        if self.y + kivi.get_height() >= HEIGHT:
            self.loppu = True
        return self.loppu

    def osuma(self, robon_x, robon_y):   
        ast_reuna = self.x + kivi.get_width()
        ast_ala = self.y + kivi.get_height()
        robo_reuna = robon_x + robo.get_width()
        if ast_reuna >= robon_x and self.x <= robo_reuna and ast_ala >= robon_y :
            self.ruudulla = False
        return not self.ruudulla 

def loppu():
    while True:
       for event in pygame.event.get():            
          if event.type == pygame.QUIT:
             exit()

pygame.init()
pygame.display.set_caption("Asteroidit")
WIDTH = 650
HEIGHT = 450
naytto = pygame.display.set_mode((WIDTH, HEIGHT))
robo = pygame.image.load("robo.png")
kivi = pygame.image.load("kivi.png")
kello = pygame.time.Clock()
pisteet = 0
fontti = pygame.font.SysFont("Arial", 24)
r = Robo()
asteroidit = []

while True:    
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            exit()
        r.key_events(tapahtuma)

    naytto.fill((0, 0, 0))          
    r.liiku()      
    naytto.blit(robo, (r.x, r.y))    
    score = "Pisteet: " + str(pisteet)
    teksti = fontti.render(score, True, (255, 0, 0))
    naytto.blit(teksti, (520, 5))   
    uusi_asteroidi = random.randint(0, 200) 
    if uusi_asteroidi == 0 and len(asteroidit) <= 2 or len(asteroidit) == 0:
        asteroidit.append(Kivi())       
    for asteroidi in asteroidit:        
        if asteroidi.loppu:
            loppu()
        if asteroidi.ruudulla:
            asteroidi.liiku()
            if asteroidi.osuma(r.x, r.y):
                pisteet += 1
        else:
            asteroidit.remove(asteroidi)
        naytto.blit(kivi, (asteroidi.x, asteroidi.y))
         
    pygame.display.flip()     
    kello.tick(60)