def adicionar(contatos):
  while True:
    nome=input("digite o nome(digite sair para encerrar):")
    if nome=="sair":
      break
    telefone=input("digite o telefone:")
    contatos[nome]=telefone
  return contatos
def novo(contatos):
  nome=input("digite o nome:")
  telefone=input("digite o telefone:")
  contatos[nome]=telefone
  return contatos
contatos={}
contatos=adicionar(contatos)
contatos=novo(contatos)
print(contatos)
