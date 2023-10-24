def pesquisar(paises):
  pais=input("digite o pais:")
  if pais in paises:
    print(paises[pais])
paises={
  "brasil": "distrito federal",
  "eua": "whashington",
  "canada": "toronto",
  "argentina": "buenos aires",
  "chile": "santiago",
  "mexico": "mexico city",
  "peru": "lima",
  "colombia": "bogota",
  "uruguai": "montevideu",
  "china": "beijing",
  "russia": "moscow",
}
pesquisar(paises)
