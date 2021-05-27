# TEE RATKAISUSI TÄHÄN:
def jarjesta_tuotantokausien_mukaan(alkiot):
    def jarjesta(alkio):
        return alkio["kausia"]
    return sorted(alkiot, key=jarjesta)