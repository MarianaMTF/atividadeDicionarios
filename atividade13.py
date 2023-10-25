def estoque(produtos):
  for produto, quantidade in produtos.items():
    if quantidade<50:
      print(f"{produto} abaixo do estoque")
produtos={
  "arroz": 20,
  "feijao": 30,
  "macarrao": 40,
  "carne": 50,
  "oleo": 60,
  "acucar": 70,
  "cafe": 80,
  "leite": 90,
  "agua": 100
}
estoque(produtos)
