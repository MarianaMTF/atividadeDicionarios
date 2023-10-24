def adicionar(dicionario):
  for i in range(1, 4):
    chave=input("digite algo:")
    valor=input("digite o valor:")
    dicionario[chave]=valor
  return dicionario
dicionario={}
dicionario=adicionar(dicionario)
print(dicionario)
