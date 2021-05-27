# TEE RATKAISUSI TÄHÄN:
import random
def sanageneraattori(kirjaimet: str, pituus: int, maara: int):
    return (valitut(pituus,kirjaimet) for i in range(maara))

def valitut(pituus, kirjaimet):
    return "".join([random.choice(kirjaimet) for i in range(pituus)])

#def sanageneraattori(kirjaimet: str, pituus: int, maara:int):

    #return ("".join([choice(kirjaimet ) for i in range(pituus)]) for j in range(maara))

 