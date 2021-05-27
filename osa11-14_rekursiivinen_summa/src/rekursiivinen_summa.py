# TEE RATKAISUSI TÄHÄN:
def summa(luku: int):
    if luku <= 1:
        return luku

    return luku + summa(luku - 1)