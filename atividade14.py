def mais(frutas):
  maior=0
  f=None
  for fruta, quantidade in frutas.items():
    if maior<quantidade:
      maior=quantidade
      f=fruta
  print(f"{f} é a fruta que mais tem {maior}")
frutas={
  "banana": 5,
  "maçã": 7,
  "morango": 4,
  "uva": 9,
  "kiwi": 2,
  "melancia": 3,
  "abacaxi": 1,
  "melão": 6,
  "abacate": 8
}
mais(frutas)
