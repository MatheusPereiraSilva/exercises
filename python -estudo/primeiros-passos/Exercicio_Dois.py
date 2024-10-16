'''
  Exercícios de Match Case
  Usando o sistema Match Case crie um programa que
  retorne para o nosso usuário qual tipo de bebida eles está
  bebendo, por exemplo:

  Coca, Pepsi, guaraná…. Refrigerante
  Morango, Maçã, Laranja… Suco
  Cerveja, Rum….. Bebidas Alcoólicas
'''

bebida = input("Qual bebida você comprou? ")

# Usando o Match Case

match bebida:
  case 'Coca' | 'Pepsi' | 'Guaraná':
    print("Você está bebendo um refrigerante")
  case 'Morango' | 'Maçã' | 'Laranja':
    print("Você está bebendo um suco")
  case 'Cerveja' | 'Rum':
    print("Você está bebendo um bebida alcoólica")

