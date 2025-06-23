class FormatadorFrase:
  def __init__(self, frase):
    self.frase = frase
  def para_maisuculas(self):
    self.frase = self.frase.upper()
  def para_minusculas(self):
    self.frase = self.frase.lower()
  def capitalizar(self):
    self.frase = self.frase.capitalize()
  def titulo(self):
    self.frase = self.frase.title()
  def vogais(self):
    vogais = 'aeiouáéíóúàèìòùãõêîôûâ'
    contagem = 0
    frase_minuscula = self.frase.lower()
    for letra in frase_minuscula:
      if letra in vogais:
        contagem += 1
    return contagem
  def consoantes(self):
    consoantes = 'bcdfghjklmnpqrstvwyzç'
    contagem = 0
    frase_minuscula = self.frase.lower()
    for letra in frase_minuscula:
      if letra in consoantes:
        contagem += 1
    return contagem
  def total_a(self):
    letra_a = 'aAáãâàÀÁÃÂ'
    contagem = 0
    for letra in self.frase:
      if letra in letra_a:
        contagem += 1
    return contagem
  def palavra(self):
    alvo = input('Qual palavra deseja buscar? ')
    return self.frase.lower().count(alvo.lower())
  def obter_frase(self):
    return self.frase

def menu():
  print('\nBem vindo ao Formatador de Frase')
  frase = input('Por favor, digite uma frase: ')
  formatador = FormatadorFrase(frase)

  while True:
    print('\nEscolha uma opção para formatar a sua frase:')
    print('1. Converter para maiúsculas')
    print('2. Converter para minúsculas')
    print('3. Capitalizar texto')
    print('4. Conveter para formato título')
    print('5. Contar vogais')
    print('6. Contar consoantes')
    print('7. Contar letra "A"')
    print('8. Pesquisar palavra')
    print('9. Mostrar frase atual')
    print('10. Sair')
    escolha = input('\nEscolha uma opção: ')
    if escolha == '1':
      formatador.para_maisuculas()
    elif escolha == '2':
      formatador.para_minusculas()
    elif escolha == '3':
      formatador.capitalizar()
    elif escolha == '4':
      formatador.titulo()
    elif escolha == '5':
      print(f"Total de vogais: {formatador.vogais()}")
    elif escolha == '6':
      print(f"Total de consoantes: {formatador.consoantes()}")
    elif escolha == '7':
      print(f"Total de letras a: {formatador.total_a()}")
    elif escolha =='8':
      formatador.palavra()
    elif escolha == '9':
      formatador.obter_frase()
    elif escolha == '10':
      print('Saindo')
      break
    print('Frase Atual', formatador.obter_frase())
if __name__ == "__main__":
  menu()