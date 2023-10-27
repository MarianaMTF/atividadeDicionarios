def ordenar_ano(filmes):
    filmes={ano: filme for filme, ano in filmes.items()}
    ordenados=dict(sorted(filmes.items()))
    for filme, ano in ordenados.items():
        print(f"{filme}:{ano}")
filmes={
    "diario de uma paixão": 2004,
    "panico": 1996,
    "la la land": 2016,
    "star wars": 1977
}
ordenar_ano(filmes)
