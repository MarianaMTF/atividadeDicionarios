def adicionar(dicionario):
  while True:
    nome=input("digite o nome(digite sair para encerrar):")
    if nome == "sair":
      break
    idade=int(input("digite a idade:"))
    dicionario[nome]=idade
  return dicionario
def encontrar(dicionario):
  nome=input("digite o nome:")
  if nome in dicionario:
    print(f"{nome}:{dicionario[nome]} anos")
dicionario={}
dicionario=adicionar(dicionario)
encontrar(dicionario)
