def pienin_keskiarvo(henkilo1: dict, henkilo2: dict, henkilo3: dict):

    keskiarvot = {}
    for h in (henkilo1, henkilo2, henkilo3):                  
        sum = 0
        for item in h.items():  
            if "tulos" in item[0]:
                sum += item[1]
        keskiarvot[sum/3] = h
    return keskiarvot[min(keskiarvot)]
    



if __name__ == "__main__":
    h1 = {"nimi": "Keijo", "tulos1": 2, "tulos2": 3, "tulos3": 3}
    h2 = {"nimi": "Reijo", "tulos1": 5, "tulos2": 1, "tulos3": 8}
    h3 = {"nimi": "Veijo", "tulos1": 3, "tulos2": 1, "tulos3": 1}

    print(pienin_keskiarvo(h1, h2, h3))