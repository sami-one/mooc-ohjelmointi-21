# TEE RATKAISUSI TÄHÄN:
import pygame, random
class Hirvio:
    def __init__(self):
        self.x = random.randint(0, WIDTH - otokka.get_width())  
        self.y = 0
        self.nopeus = 1
        self.ruudulla = True
        self.loppu = False

    def liiku(self):
        self.y += self.nopeus
        if self.y + otokka.get_height() >= HEIGHT:
            self.loppu = True
        return self.loppu

    def osuma(self, robon_x, robon_y):   
        ast_reuna = self.x + otokka.get_width()
        ast_ala = self.y + otokka.get_height()
        robo_reuna = robon_x + robo.get_width()
        if ast_reuna >= robon_x and self.x <= robo_reuna and ast_ala >= robon_y :
            self.ruudulla = False
        return not self.ruudulla 

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

class Kolikko:
    def __init__(self):
        self.x = random.randint(0, WIDTH - raha.get_width())  
        self.y = 0
        self.nopeus = 1
        self.ruudulla = True
        self.loppu = False
    
    def liiku(self):
        self.y += self.nopeus
        if self.y + raha.get_height() >= HEIGHT:
            self.loppu = True
        return self.loppu

    def osuma(self, robon_x, robon_y):   
        ast_reuna = self.x + raha.get_width()
        ast_ala = self.y + raha.get_height()
        robo_reuna = robon_x + robo.get_width()
        if ast_reuna >= robon_x and self.x <= robo_reuna and ast_ala >= robon_y :
            self.ruudulla = False
        return not self.ruudulla

def alku():
    naytto.fill((255,255,255))
    tekstit = []
    tekstit.append("Collect dropping coins")
    tekstit.append("Each coin you collect gives you 1 point")
    tekstit.append("If you don't catch coin you will lose 1 point")
    tekstit.append("If you catch monster the game ends")
    tekstit.append("Move robot with arrow keys")
    tekstit.append("Press any key to start")
    y = 90
    for teksti in tekstit:
        t = fontti.render(teksti, True, (0,0,0))
        naytto.blit(t, (50, y))
        y += 45
    pygame.display.flip()

    while True:
        for tapahtuma in pygame.event.get(): 
            if tapahtuma.type == pygame.QUIT:
                exit()
            else:                
                if tapahtuma.type == pygame.KEYDOWN:     
                    return  
def loppu(pisteet):
    naytto.fill((0,0,0))
    fontti_iso = pygame.font.SysFont("Arial", 64)
    teksti = fontti_iso.render("Game Over", True, (205, 205, 205))
    naytto.blit(teksti, (150, 140))
    teksti = fontti.render(f"Score: {pisteet}", True, (205, 205, 205))
    naytto.blit(teksti, (260, 220))
    teksti = fontti.render(f"Press any key to start again", True, (205, 205, 205))
    naytto.blit(teksti, (170, 280))
    pygame.display.update()
    pygame.time.delay(500)
    pygame.event.clear()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                return
            elif event.type == pygame.QUIT:
                exit()

pygame.init()
pygame.display.set_caption("Coin chase")
WIDTH = 650
HEIGHT = 450
naytto = pygame.display.set_mode((WIDTH, HEIGHT))
robo = pygame.image.load("robo.png")
raha = pygame.image.load("kolikko.png")
otokka = pygame.image.load("hirvio.png")
kello = pygame.time.Clock()
fontti = pygame.font.SysFont("Arial", 24)
r = Robo()
kolikot = []
hirviot = []

def main():
    pisteet = 0
    nopeus = 90
    while True:    
        for tapahtuma in pygame.event.get():
            if tapahtuma.type == pygame.QUIT:
                exit()
            r.key_events(tapahtuma)
        naytto.fill((255, 255, 255))          
        r.liiku()      
        naytto.blit(robo, (r.x, r.y))    
        score = "Pisteet: " + str(pisteet)
        teksti = fontti.render(score, True, (255, 0, 0))
        naytto.blit(teksti, (520, 5))   
        uusi_kolikko = random.randint(0, 200) 
        if uusi_kolikko == 0 and len(kolikot) <= 5 or len(kolikot) == 0:
            kolikot.append(Kolikko())       
        for kolikko in kolikot:        
            if kolikko.loppu:
                pisteet -= 1
                kolikot.remove(kolikko)
            if kolikko.ruudulla:
                kolikko.liiku()
                if kolikko.osuma(r.x, r.y):
                    pisteet += 1
            else:
                kolikot.remove(kolikko)
            naytto.blit(raha, (kolikko.x, kolikko.y))
        
        uusi_hirvio = random.randint(0, 400) 
        if uusi_hirvio == 0 and len(hirviot) <= 1 or len(hirviot) == 0:
            hirviot.append(Hirvio())       
        for hirvio in hirviot:        
            if hirvio.loppu:
                hirviot.remove(hirvio)
            if hirvio.ruudulla:
                hirvio.liiku()
                if hirvio.osuma(r.x, r.y):
                    for hirvio in hirviot:
                        hirviot.remove(hirvio)
                    for kolikko in kolikot:
                        kolikot.remove(kolikko)
                    loppu(pisteet)
                    main()
            else:
                hirviot.remove(hirvio)
            naytto.blit(otokka, (hirvio.x, hirvio.y))

        pygame.display.flip()     
        kello.tick(nopeus)
alku()
main()