class Pessoa:
  def __init__(self, nome):
    self.nome = nome
    self.acordado = False
    self.dirigindo = False
    self.comendo = False
  def acordar(self):
    if not self.acordado:
      self.acordado = True
      print(f"{self.nome} acordou")
    else:
      print(f"{self.nome} já está acordado")
  def comer(self):
    if self.acordado and not self.dirigindo:
      self.comendo = True
      print(f"{self.nome} esta comendo")
    else:
      print(f"{self.nome} esta dirigindo ou dormindo")
  def stop_eating(self):
    if self.comendo:
      self.comendo = False
      print(f"{self.nome} parou de comer")
    else:
      print(f"{self.nome} não esta comendo")
  def drive(self):
    if not self.dirigindo:
      self.dirigindo = True
      print(f"{self.nome} esta dirigindo")
    else:
      print(f"{self.nome} não esta no carro")
  def stop_drive(self):
    if self.dirigindo:
      self.dirigindo = False
      print(f"{self.nome} estacionou")
    else:
      print(f"{self.nome} já está parado")
  def sleep(self):
    if self.acordado and not self.dirigindo and not self.comendo:
      self.acordado = False
      print(f"{self.nome} dormiu")
    else:
      print(f"{self.nome} esta ocupado")

rei = Pessoa("Grimley")
rei.acordar()
rei.comer()
rei.stop_eating()
rei.drive()
rei.stop_drive()
rei.sleep()