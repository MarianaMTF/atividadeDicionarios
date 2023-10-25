def pesquisar(estados):
  repetidos=[]
  for cidade, estado in estados.items():
    if estado not in repetidos:
      repetidos.append(estado)
    else:
      repetidos.remove(estado)
  return repetidos
estados={
  "vitoria": "espirito santo",
  "sao paulo": "sao paulo",
  "rio de janeiro": "rio de janeiro",
  "serra": "espirito santo",
  "sao jose": "sao paulo"
}
repetidos=pesquisar(estados)
print(repetidos)
