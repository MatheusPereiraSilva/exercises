class Event:
  def __init__(self, capacidade=10):
    self.capacidade = capacidade
    self.lugares_disponiveis = capacidade

  def reservar(self):
    if self.lugares_disponiveis == 0:
      print('Tem lugar não !')
      return
    self.lugares_disponiveis -= 1
    print('Lugar reservado com sucesso!')

  def cancelar(self):
    if self.lugares_disponiveis == self.capacidade:
      print('Tem reserva não!')
      return
    self.lugares_disponiveis += 1
    print('Lugar cancelado com sucesso!')
  def mostrar(self):
    return print(f"Lugares disponíveis: {self.lugares_disponiveis}")

reservar = Event()
for _ in range(3):
  reservar.reservar()
reservar.mostrar()