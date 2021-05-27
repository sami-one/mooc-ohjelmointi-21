# tee ratkaisu tänne
# Muista import-lause:
# from datetime import date
from datetime import date


def vuodet_listaan(lista):

    years = []
    for d in lista:
       years.append(d.year)
    return sorted(years)


if __name__ == "__main__":
    d1 = date(2019, 2, 3)
    d2 = date(2006, 10, 10)
    d3 = date(1993, 5, 9)

    vuodet = vuodet_listaan([d1, d2, d3])
    print(vuodet)