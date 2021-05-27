# TEE RATKAISUSI TÄHÄN:
def suodata_kielletyt(merkkijono: str, kielletyt: str):
    lista = [merkki for merkki in merkkijono if merkki not in kielletyt]
    return "".join(lista)