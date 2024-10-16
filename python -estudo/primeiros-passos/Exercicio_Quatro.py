'''
  Exercício sobre Loops
  Crie um programa em que o python solicite ao usuário um
  número e, em seguida, exiba a tabuada desse número
  utilizando os Loops de repetição.
'''

numero = int(input("Qaul número você deseja? "))

for i in range(1, 11):
  print(f"{numero} x {i} = {numero * i}")