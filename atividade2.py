def adicionar(dicionario):
  while True:
    nome=input("digite o nome(digite sair para encerrar):")
    if nome == "sair":
      break
    idade=int(input("digite a idade:"))
    dicionario[nome]=idade
  return dicionario
dicionario={}
dicionario=adicionar(dicionario)
print(dicionario)
