class ManipuladorDeLista:
  def __init__(self):
    self.lista = []

  def adicionar(self, elemento):
    self.lista.append(elemento)

  def remover(self, elemento):
    try:
      self.lista.remove(elemento)
      print(f'{elemento} pulou fora!')
    except ValueError:
      print('Tem isso ai na lista não!')
  def encontrar_maior(self):
    if self.lista:
      return max(self.lista)
    else:
      return 'Lista vazia meu bom'
  def encontrar_menor(self):
    if self.lista:
      return min(self.lista)
    else:
      return 'Lista vazia meu bom'
  def media(self):
    if self.lista:
      return sum(self.lista) / len(self.lista)
    else:
      print('Lista vazia meu chapa')
  def mostrar(self):
    return self.lista

def menu():
  manipulador = ManipuladorDeLista()

  while True:
    print("\nMenu")
    print("1. Add Elemento")
    print("2. Remover Elemento")
    print("3. Encontrar maior")
    print("4. Encontrar menor")
    print("5. Calcular média")
    print("6. Mostrar lista")
    print("7. Sair")

    escolha = input("Escolha uma opcção: ")

    if escolha == '1':
      try:
        elemento = int(input('Diga ai o que quer add: '))
        manipulador.adicionar(elemento)
      except ValueError:
        print('Deu ruim no bagulho')
    elif escolha =='2':
      try:
        removeu = int(input('Fala ai o quer remover: '))
        manipulador.remover(removeu)
      except ValueError:
        print('Deu ruim no bagulho')
    elif escolha == '3':
      print(f'O maior é o: {manipulador.encontrar_maior()}')
    elif escolha == '4':
      print(f'O menor é o: {manipulador.encontrar_menor()}')
    elif escolha == '5':
      print(f'e media é: {manipulador.media()}')
    elif escolha == '6':
      print(f"A lista é: {manipulador.mostar()}")
    elif escolha == '7':
      print('Até mais meu parceiro.')
      break
    else:
      print('Escolheu errado ai meu bom')
if __name__ == '__name__':
  menu()