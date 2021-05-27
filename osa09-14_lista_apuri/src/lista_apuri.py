# TEE RATKAISUSI TÄHÄN:
class ListaApuri:

    @classmethod
    def suurin_frekvenssi(cls, lista: list):
        frek = {}
        for i in lista:
            frek[lista.count(i)] = i
        if frek == {}:
            return "lista oli tyhjä"
        return frek[max(frek)]

    @classmethod
    def tuplia(cls, lista: list):
        tulos = 0
        for i in set(lista):
            montako = lista.count(i)
            if montako >= 2:
                tulos += 1
        return tulos