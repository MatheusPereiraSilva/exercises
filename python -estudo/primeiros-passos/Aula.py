# comentário de uma linha
''' 
    Comentário de múltiplas linhas
    Aqui podemos escrever muitas linhas de
    comentários
'''
# variaveis
nome = 'Matheus Pereira'

# impressão de variavel
print(nome)

# números, inputs e operadores
x = int(input('Qual o valor de x? '))
y = int(input('Qual o valor de y? '))
z =  x + y
print(z)
'''
  operadores:
  + adição
  - subtração
  * multiplicação
  / divisão
  % resto da divisão
  ** exponenciação
  // divisão inteira
  -------------------
  comparadores:
  == igualdade
  >= maior ou igual
  <= menor ou igual
  < menor
  > maior
  not negação
'''
# listas sãotáveis - alteráveis
lista = [1, 2, 3, 4, 5]
lista_string = ['oi', 'teste']
lista_vazia = []
lista_aninhada = [[1,2,3], [4,5,6], [7,8,9]]
 # funções das listas
lista.append(7)
lista.remove(2)
print(len(lista)) # retorna o tamanho de itens do array, string (retorna o numero de letras), etc...,
print(max(lista)) # retorna o maior valor da array
print(min(lista)) # retorna o menor valor da array
print(sum(lista)) # retorna a soma dos valores da array
# lista.clear() limpa a lista
print(lista)

# slicing
print(lista[0]) # primeiro item
print(lista[::]) # lista toda
print(lista[2:5]) # dos itens 2 até o 5 do indice
print(lista[3:]) # a partir do item 3
print(lista[:5]) # até o item 5

# tuplas imutavéis - não alteráveis
tuplas = (1, 2, 3, 4, 5)
tupla_string = ('oi', 'ou', 'oe')
tupla_aninhada = ((1,2), ('b', 'a'), (True, False))
tupla = (10, 20)
x, y = tupla

print(len(tuplas))
print(tuplas)

# dicionários - não ordenados
dicionario = {
  'nome': 'Matheus',
  'idade': 28,
  'cidade': 'Curitiba'
}
dicionario['profissao'] = 'Programador'


print(dicionario['nome'])
print(dicionario)

chaves = dicionario.keys()
valores = dicionario.values()
pares = dicionario.items()

print(chaves)
print(valores)
print(pares)

dicionario2 = {
  'usuarios1': {
  'nome': 'Matheus',
  'idade': 28,
  'cidade': 'Curitiba',
  'profissao': 'Programador'
  },
  'usuarios2': {
  'nome': 'Grimley',
  'idade': 22,
  'cidade': 'Seus Castelos',
  'profissao': 'Rei'
  }
}

# funções
animais = []

def cadastrar_animal(nome, especie, idade):
  animal = {
    'Nome': nome,
    'Especie': especie,
    'Idade': idade
  }
  animais.append(animal)
  print(f'Animal {nome} cadastrado com sucesso!')

cadastrar_animal('Rex', 'Cachorro', 3)
cadastrar_animal('Ariel', 'Gato', 2)
cadastrar_animal('Chico', 'Ave', 5)

# condições
z = int(input("Qual a sua idade? "))

if z >= 18 and z <= 60: # pode ser escrito também da seguinte forma 18 <= idade >= 60
  print("Você pode entrar no brinquedo. Aproveite!!!")
elif z >= 100 or z <= 0:
  print("Você existe mesmo? ")
else:
  print("Você não pode entrar no brinquedo.")


# condicionais match, case
tipo = input("Qual o tipo de produto que você comprou? ")
match tipo:
  case 'Laranja':
    print("Fruta")
  case 'Maçã':
    print("Fruta")
  case 'Cenoura':
    print("Legume")
  case 'Batata':
    print("Legume")

match tipo:
  case 'Laranja' | 'Maça' | 'Limão':
    print("Fruta")
  case 'Cenoura' | 'Batata' | 'Abóbora':
    print("Legume")

# boolean
def sistema():
  q = int(input("Qual o valor de q? "))
  if Par(q):
    print(f' o valor de {q} é par.')
  else:
    print(f'O valor de {q} é impar.')

def Par(w):
  if w % 2 == 0:
    return True
  else:
    return False

def ParDois(w):
  return True if w % 2 == 0 else False

sistema()

# loop
# While, For, While True
# While - não sabe o número total derepetições
# For - você sabe o número total derepetições
e = 5
while e != 15:
  print('e é diferente')
  e += 1

for r in [1,2,3,4,5]:
  print(f'O valor de r é {r}')

for t in range(10):
  print('printou')

while True:
  idade2 = int(input("Qual sua idade?? "))
  if idade2 <= 18:
    print("Você é menor de idade.")
  else:
    break

# Try, Except
while True:
  try:
    t = int(input("Qual é o valor de t? "))
  except ValueError:
    print("Você poderia colocar um número inteiro?")
  else: 
    break

print(f'o valor {t} é um número inteiro')
# se eu coloco um input dentro da função print ele le meu input e depois imprime o resultado
print("Olá, " + input("Qual o seu nome? "))
# a saída será: Olá, {resposta do input}
