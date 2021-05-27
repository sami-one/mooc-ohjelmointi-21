# TEE RATKAISUSI TÄHÄN:
def jarjesta_pisteiden_mukaan(alkiot):
    def jarjesta(alkio):
        return alkio["pisteet"]
    return sorted(alkiot, key=jarjesta, reverse = True)