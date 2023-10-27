def mais_gols(jogadores):
    mais=0
    j=None
    for jogador, gol in jogadores.items():
        if gol>mais:
            mais=gol
            j=jogador
    print(f"{j} fez mais gols, {mais}")
jogadores={
    "fred": 199,
    "cano": 80,
    "ganso": 22,
    "jhon arias": 21,
    "nenê": 28
}
for jogador, gol in jogadores.items():
    print(f"{jogador}:{gol}")
mais_gols(jogadores)
