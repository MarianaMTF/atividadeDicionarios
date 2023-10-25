def total(refeicao):
  calorias_toal=0
  for comida, caloria in refeicao.items():
    calorias_toal+=caloria
  print(f"a quantidade de calorias é {calorias_toal} calorias")
refeicao={
  "pão": 50,
  "queijo": 150,
  "presunto": 200,
  "carne": 300,
  "ovo": 50,
  "leite": 50,
  "café": 50
}
total(refeicao)
