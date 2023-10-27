mangas=[{"titulo": "naruto", "autor": "masashi kishimoto", "ano": 2002}, {"titulo": "death note", "autor": "tsugumi ohba", "ano": 2006}, {"titulo": "shingeki no kyojin", "autor": "hajime isayama", "ano": 2013}, {"titulo": "one piece", "autor": "eiichiro oda", "ano": 1999}]
for manga in mangas:
    for chave, valor in manga.items():
        print(f"{chave}:{valor}")
