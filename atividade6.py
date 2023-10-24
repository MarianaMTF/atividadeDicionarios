def adicionar(compras):
  while True:
    compra=input("digite o produto(digite sair para encerrar):")
    if compra=="sair":
      break
    valor=float(input("digite o valor:"))
    compras[compra]=valor
  return compras
def valor_total(compras):
  total=0
  for compra, valor in compras.items():
    total+=valor
  print(f"o valor total das compras é {total}")
compras={}
compras=adicionar(compras)
valor_total(compras)
