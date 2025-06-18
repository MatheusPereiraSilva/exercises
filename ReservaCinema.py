cinema = []

for i in range(5):
  fileira = []
  for j in range(10):
    fileira.append('D')
  cinema.append(fileira)
while True:
  print('Menu:')
  print('1. Ver Disposição dos Assentos')
  print('2. Reservar Assento')
  print('3. Sair')
  escolha = input('Escolha uma opção: ')
  if escolha == '1':
    for fileira in cinema:
      for assento in fileira:
        print(assento, end=' ')
      print()
  elif escolha == '2':
    fileira = int(input('Digite o número da fileira (0-4): '))
    assento = int(input('Digite o número do assento (0-9): '))
    if cinema[fileira][assento] == 'D':
      cinema[fileira][assento] = 'R'
      print('Assento reservado com sucesso!')
    else:
      print('Assento já esta reservado!')
  elif escolha == '3':
    print('Obrigado por usar o nosso sistema!')
    break
  else:
    print('Opção inválida!')