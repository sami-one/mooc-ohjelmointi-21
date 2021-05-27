# TEE RATKAISUSI TÄHÄN:
def yleisimmat_sanat(tiedoston_nimi: str, raja: int):
    file = open(tiedoston_nimi, "r") 
    str = ""
    for rivi in file:
        str += rivi

    str = str.replace("\n", " ")
    uusijono =  "".join([merkki for merkki in str if merkki not in ".,"])

    paloitteltu = uusijono.split(" ")
    return {sana : paloitteltu.count(sana) for sana in paloitteltu if paloitteltu.count(sana) >= raja}