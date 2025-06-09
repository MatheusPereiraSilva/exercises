numeros = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numerosImpares = list(filter(lambda x: x % 2 != 0, numeros))
print(numerosImpares)
numerosAoQuadrado = list(map(lambda impares: impares**2, numerosImpares))
print(numerosAoQuadrado)

nomes = ['Aline', 'Marcos', 'Alceu', 'Pedro', 'Allan', 'Bruno', 'Ana', 'Alex', 'Charles']
nomesComA = list(filter(lambda nome: nome[0] == "A", nomes))
print(nomesComA)
listaAlice = list(filter(lambda alice: alice == 'Aline', nomes))
print(listaAlice)

num = [1, 2, 3, 4, 5]
numQuadrado = list(map(lambda e: e**2, num))
print(numQuadrado)

palavras = ['Arroz', 'Bacon', 'Caminhão', 'Carroça', 'Marionete']
comprimentos = list(map(lambda palavra: len(palavra), palavras))
print(comprimentos)
