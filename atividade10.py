def pesquisar(dicionario):
  usuario=input("digite a palavra chave:")
  if usuario in dicionario:
    print(dicionario[usuario])
dicionario={
  "python": "linguagem de programação",
  "tupla": "conjunto de dados",
  "dicionario": "conjunto de chaves e valores",
  "lista": "conjunto de dados"
}
pesquisar(dicionario)
