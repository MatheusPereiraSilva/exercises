tabuleiro = []
for i in range(3):
  linha = []
  for j in range(3):
    linha.append(' ')
  tabuleiro.append(linha)
def exibirTabuleiro():
  for linha in tabuleiro:
    print('|'.join(linha))
    print('-'*5)

def verificarVencedor(jogador):
  for i in range(3):
    todasCelulasLinha = True
    todasCelulasColunas = True
    for j in range(3):
      if tabuleiro[i][j] != jogador:
        todasCelulasLinha = False
      if tabuleiro[j][i] != jogador:
        todasCelulasColunas = False
    if todasCelulasLinha or todasCelulasColunas:
      return True
    if tabuleiro[0][0] == jogador and tabuleiro[1][1] == jogador and tabuleiro[2][2] == jogador:
      return True
    if tabuleiro[0][2] == jogador and tabuleiro[1][1] == jogador and tabuleiro[2][0] == jogador:
      return True
    return False

def jogador(jogador):
  while True:
    jogada = input(f'Jogador {jogador}, escolha a linha ecoluna (ex: 0 2): ')
    try:
      linha, coluna = map(int, jogada.split())
      if tabuleiro[linha][coluna] == ' ':
        tabuleiro[linha][coluna] = jogador
        break
      else:
        print('Posição já ocupada. Tente novamente.')
    except:
      print('Entrada inválida')

jogador_atual = 'X'

for _ in range(9):
  exibirTabuleiro()
  jogador(jogador_atual)
  if verificarVencedor(jogador_atual):
    exibirTabuleiro()
    print(f'Jogador {jogador_atual} venceu!')
    break
  jogador_atual = 'O' if jogador_atual == 'X' else 'X'
else:
  exibirTabuleiro()
  print('Empate')