# TEE RATKAISUSI TÄHÄN:
def alkuluku(luku):
    if luku < 2:
        return False
    for jakaja in range(2, luku):
        if luku % jakaja == 0:
            return False
    return True

def alkuluvut():
    luku = 1
    while True:
        if alkuluku(luku):
            yield luku
        luku += 1    