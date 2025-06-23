class Carro:
  def __init__(self, marca, modelo, cor):
    self.marca = marca
    self.modelo = modelo
    self.cor = cor
    self.velocidade = 0
  def acelerar(self):
    self.velocidade += 10
    print(f"Velocidade atual: {self.velocidade} Km/h")
  def frear(self):
    self.velocidade -=10
    if self.velocidade < 0:
      self.velocidade = 0
    print(f"Velocidade atual: {self.velocidade} Km/h")
  def exibir_info(self):
    print(f"Marca: {self.marca}, Modelo: {self.modelo}, Cor: {self.cor}, Velocidade: {self.velocidade} Km/h")

lista_carros = []

while True:
  print("\n--- Menu ---")
  print("1. Adicionar novo carro")
  print("2. Exibir informações dos carros")
  print("3. Acelerar um carro")
  print("4. Frear um carro")
  print("5. sair")
  escolha = input("Escolha uma opção: ")

  if escolha == '1':
    marca = input("Digite a marca do carro: ")
    modelo = input("Digite o modelo do carro: ")
    cor = input("Digite a cor do carro: ")

    novo_carro = Carro(marca, modelo, cor)
    lista_carros.append(novo_carro)
  elif escolha == '2':
    if lista_carros:
      for carro in lista_carros:
        carro.exibir_info()
    else:
      print("Nenhum carro adicionado ainda.")
  elif escolha == '3':
    car = input("Qual modelo deseja acelerar? ")
    for carro in lista_carros:
      if carro.modelo == car:
        carro.acelerar()
        break
      else:
        print("Modelo não encontrado.")
  elif escolha == '4':
    car = input("Qual modelo deseja frear? ")
    for carro in lista_carros:
      if carro.modelo == car:
        carro.frear()
        break
      else:
        print("Modelo não encontrado.")
  elif escolha == '5':
    print("Obrigado por usar o programa")
    break
  else:
    print("Opção inválida. Tente novamente")