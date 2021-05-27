# TEE PELI TÄHÄN

 

 

'''

RIKKAAKSI KUOLEMAN UHALLA

 

Pelissä kerätään rahaa ja väistellään hirviöitä. 

 

Robottia liikutellaan vasemmalle ja oikealle nuolinäppääimillä.

 

Peli voitetaan jos saadaan kerättyä 5 rahaa ja hävitään jos osutaan monsteriin.

 

Pelin vaikeutta voit lisätä

- lisäämällä nopeutta (oletus 2.5)

- lisäämällä monstereita (oletus keskimäärin 1 monsteri / 80 tapahtumaa)

- vähentämällä rahoja (oletus keskimäärin 1 raha / 120 tapahtumaa)

'''

 

########################################################################

# vaikeuden säätäminen

'''säädä halutessasi peliä vaikeammaksi alla-olevien ohjeiden mukaan'''

 

# mitä nopeampi, sitä vaikeampi. esim. 3 on jo aika nopea

nopeus=2.5

# pitä pienempi luku, sitä enemmän monstereita. Esim. 50 on jo monta robottia

monsterimaara=80

# mitä suurempi luku, sitä vähemmän rahaa. Esim. 160 on suhteellisen harvakseltaan

rahamaara=120

 

########################################################################3

#Paketit ja polut

 

#haetaan paketteja

import random

import pygame

import os

 

#tämä varmistaa, että working directory on sama kuin missä tämä file on

os.chdir(os.path.dirname(os.path.abspath(__file__)))

 

 

###########################################################################33

# alustetaan peli, näyttö ja hahmot

 

pygame.init()

w_d, h_d = 640, 480

naytto = pygame.display.set_mode((w_d, h_d))

 

##robotin alustus

robo = pygame.image.load("robo.png") 

h_r=robo.get_height()

w_r=robo.get_width()

x_r = w_d/2-w_r

y_r = h_d-h_r

 

##monsterin alustus

monsterX = pygame.image.load("hirvio.png") 

h_m=monsterX.get_height() 

w_m=monsterX.get_width() 

 

##rahan alustus (kivi=raha)

kivi = pygame.image.load('kolikko.png') 

h_k=kivi.get_height()

w_k=kivi.get_width()

 

 

##################################################################

## luodaan apuluokkia ja funktioita yksittäisille objekteille

 

# luokka on sama rahalle, monsterille (ja aiemmin kivelle)

class Kivi:

    def __init__(self):

        self.x=random.randint(0,w_d-w_k)

        self.y=-h_k

        self.x_suunta=0

        self.y_suunta=1

        self.onko_ollut_pohjalla=False

    

    def __repr__(self):

        return f'x {self.x} y {self.y} x_suunta {self.x_suunta} y_suunta {self.y_suunta} pohjalla {self.onko_ollut_pohjalla}'

 

# funktio joka liikuttaa alas taivaalta tippuvaa objektia

def move_kivi(ME:Kivi):

    ME.y += ME.y_suunta

    ME.x += ME.x_suunta

    if ME.y-h_k >= h_d:

        if ME.onko_ollut_pohjalla==False:

            ME.onko_ollut_pohjalla=True

 

# näytetään kivi (raha)

def display_kivi(ME:Kivi):

    naytto.blit(kivi, (ME.x, ME.y))

 

# näytetään monsteri

def display_monsteri(ME:Kivi):

    naytto.blit(monsterX, (ME.x, ME.y)) 

 

##################################################################

# alustetaan ohjelma

game_over=False

victory=False

kivi_list=[]

monsteri_list=[]

oikealle = False

vasemmalle = False

pisteet=0

kello = pygame.time.Clock()

 

# laitetaan ohjelma käyntiin

while True:

    for tapahtuma in pygame.event.get():

        if tapahtuma.type == pygame.KEYDOWN:

            if tapahtuma.key == pygame.K_LEFT:

                vasemmalle = True

            if tapahtuma.key == pygame.K_RIGHT:

                oikealle = True

 

        if tapahtuma.type == pygame.KEYUP:

            if tapahtuma.key == pygame.K_LEFT:

                vasemmalle = False

            if tapahtuma.key == pygame.K_RIGHT:

                oikealle = False

 

        if tapahtuma.type == pygame.QUIT:

            exit()

 

    #siirretään robottia oikealle tai vasemmalle riippuen siitä onko nuolinäppäin pohjassa

    if oikealle:

        if x_r<w_d-w_r:

            x_r += 3

    if vasemmalle:

        if x_r>0:

            x_r -= 3

 

    # # arvotaan joka hetki tuleeko uusi raha

    if random.randint(0,rahamaara)==1:

        kivi_list.append(Kivi())

 

    #arvotaan joka hetki, tuleeeko uusi monsteri

    if random.randint(0,monsterimaara)==2:

        monsteri_list.append(Kivi())

 

    # poistetaan ne taivaankappaleet, jotka tippuneet ohi maanpinnan

    kivi_list = [x for x in kivi_list if x.onko_ollut_pohjalla==False]

    monsteri_list = [x for x in monsteri_list if x.onko_ollut_pohjalla==False]

 

    # siirretään kiveä/rahaa ja monsteria alas

    for stone in kivi_list:

        move_kivi(stone)

 

    for monsteri in monsteri_list:

        move_kivi(monsteri)

    

    # katsotaan tuliko osuma ja lisätään pisteitä

    drop_indices=[]

    for i,stone in enumerate(kivi_list):

        if (x_r-w_k <= stone.x <= x_r+w_r) and (y_r-h_k <= stone.y <= y_r+h_r):

            drop_indices.append(i)

            pisteet+=1

 

    # poistetaan ne kivet/rahat joihin osunut

    kivi_list = [j for i, j in enumerate(kivi_list) if i not in drop_indices]

 

    # katsotaan osuiku monsteriin ja asetetaan game_over parameteri todeksi tarvittaessa

    for i,monster in enumerate(monsteri_list):

        if (x_r-w_m <= monster.x <= x_r+w_r) and (y_r-h_m <= monster.y <= y_r+h_r): #NB!

            game_over=True

            break

 

    # poistetaan kivet/rahat ja monsterit jos peli päättynyt

    if game_over==True or victory==True:

        kivi_list=[]

        monsteri_list=[]

 

    # alustetaan tekstit

    ## pisteteksti

    fontti = pygame.font.SysFont("Arial", 24)

    teksti = fontti.render(f'Pisteet: {pisteet}', True, (255, 0, 0))

 

    ## häviämistekstit

    fontti_game_over = pygame.font.SysFont("Arial", 70)

    teksti_game_over = fontti_game_over.render(f'Game over!', True, (255, 0, 0))

 

    ##voittotekstit

    teksti_victory1 = fontti_game_over.render(f'Sinä voitit!', True, (255, 0, 0))

    teksti_victory2 = fontti.render(f'Käräsit {pisteet} rahaa, olet rikas. Onneksi olkoon.', True, (255, 0, 0))

 

    # mikäli pisteitä on 5 (tai enemmän), peli voitetaan

    if pisteet>=5:

        victory=True

 

    ########################

    # piirretään näyttöön grafiikat jokaiselle tapahtumalle

    naytto.fill((72,61,139))

    pygame.display.set_caption('Rikkaaksi kuoleman uhalla')

    if game_over==True:

        naytto.blit(teksti_game_over, (w_d/2-160, h_d/2-80))

        naytto.blit(teksti, (w_d/2-50, h_d/2+50))

 

    elif victory==True:

        naytto.blit(teksti_victory1, (w_d/2-160, h_d/2-80))

        naytto.blit(teksti_victory2, (100, h_d/2+50))

 

    else:   

        for x in kivi_list:

            display_kivi(x)

        for x in monsteri_list:

            display_monsteri(x)

        naytto.blit(teksti, (w_d-120, 0))

 

    naytto.blit(robo, (x_r, y_r))

    pygame.display.flip()

    kello.tick(60*nopeus)