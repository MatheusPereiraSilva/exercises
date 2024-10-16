'''
  Exercícios de Condicionais

  Com a ajuda das condições, crie um programa em que o
  python solicite a idade do seu usuário e atribua ele a
  alguma classe. As classes serão baseadas em um
  sistemas escolar ou seja:

  6 anos >> 1° ano | 7 anos >> 2° ano | 8 anos >> 3° ano
  9 anos >> 4° ano | 10 anos >> 5° ano | 11 anos >> 6° ano
  12 anos >> 7° ano | 13 anos >> 8° ano | 14 anos >> 9° ano
  15 anos >> 1° Ensino Médio | 16 anos >> 2° Ensino Médio |
  17 anos >> 3° Ensino Médio.
'''

# Solicita a idade do usuário

idade = int(input("Qual a sua idade? "))

# Define a função que determina a classe
def definir_classe(idade):
  if idade == 6:
    print("1º ano")
  elif idade == 7:
    print("2º ano")
  elif idade == 8:
    print("3º ano")
  elif idade == 9:
    print("4º ano")
  elif idade == 10:
    print("5º ano")
  elif idade == 11:
    print("6º ano")
  elif idade == 12:
    print("7º ano")
  elif idade == 13:
    print("8º ano")
  elif idade == 14:
    print("9º ano")
  elif idade == 15:
    print("1° Ensino Médio")
  elif idade == 16:
    print("2° Ensino Médio")
  elif idade == 17:
    print("3° Ensino Médio")
  else:
    print("Sua idade não corresponde a uma das classes estabelecidas.")

# Chama a função com a idade do usuário

definir_classe(idade)