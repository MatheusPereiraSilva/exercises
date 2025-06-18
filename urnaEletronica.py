urna = [['Grimley', 0], ['Raygon', 0], ['Kai', 0]]

for i in range(4):
  voto = input('Quem deve ser o Rei? Grimley (que já tem 3 castelos, Raygon um tarado, Kai um bêbado louco) ')
  encontrado = False
  for candidato in urna:
    if candidato[0] == voto:
      candidato[1] += 1
      encontrado = True
      break
  if not encontrado:
    print('Você está bêbado, volte quando estiver sóbrio')
print('\nResultados')
votosMaximos = -1
vencedor = ''

for candidato in urna:
  print(f'{candidato[0]}: {candidato[1]} votos')

  if candidato[1] > votosMaximos:
    votosMaximos = candidato[1]
    vencedor = candidato[0]
print(f'\nO novo rei é {vencedor} com {votosMaximos} votos, saudem o rei!!!')