# TEE RATKAISUSI TÄHÄN:
def parilliset(alku: int, maksimi: int):
    luku = alku
    if luku % 2 != 0:
        luku += 1
    while luku <= maksimi:
        yield luku
        luku += 2