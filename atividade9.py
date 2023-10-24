def adicionar(alunos):
  while True:
    nome=input("digite o nome(digite sair para encerrar):")
    if nome=="sair":
      break
    nota=float(input("digite sua nota:"))
    alunos[nome]=nota
  return alunos
def media(alunos):
  notas=[]
  for aluno, nota in alunos.items():
    notas.append(nota)
  media=sum(notas)/len(notas)
  return media
alunos={}
alunos=adicionar(alunos)
media_notas=media(alunos)
print(f"a media das notas é {media_notas}")
