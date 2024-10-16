'''
  Exercício sobre Boolean:

  Usando o sistema booleano, crie um programa baseado
  em notas escolares com as seguintes especificações:
  O usuário deverá colocar duas notas (A e B), você deverá
  criar uma função que some essas notas e depois as divida
  por 2 assim obtendo a média desse aluno. Se a média for
  maior ou igual a 6, exiba a mensagem de que ele foi
  aprovado. Caso for menor do que 6, diga que foi reprovado
'''

# Coleta as notas do aluno
notaA = int(input('Qual a sua primeira nota? '))
notaB = int(input('Qual a sua segunda nota? '))

media = (notaA + notaB) / 2

# Verifica se o aluno foi aprovado ou reprovado
if media >= 6:
  print('Você foi aprovado!')
else: 
  print('Você foi reprovado!')