
def sulut_tasapainossa(merkkijono: str):
    
    if len(merkkijono) == 0:
        return True    
    if merkkijono[0] in ")]" or merkkijono[-1] in "([" :
        return False
    if merkkijono[0] not in "([":
        return sulut_tasapainossa(merkkijono[1:])
    if merkkijono[-1] not in ")]":
        return sulut_tasapainossa(merkkijono[:-1])
    if (merkkijono[0]=="(" and merkkijono[-1]=="]") or (merkkijono[0]=="[" and merkkijono[-1]==")"):
        return False
    # poistetaan ensimmäinen ja viimeinen merkki
    return sulut_tasapainossa(merkkijono[1:-1])