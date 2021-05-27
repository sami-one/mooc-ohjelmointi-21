# TEE RATKAISUSI TÄHÄN:
def hae(tuotteet: list, kriteeri: callable):
    return [tuote for tuote in tuotteet if kriteeri(tuote)]