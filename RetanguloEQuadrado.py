largura = int(input('Digite a largura do retângulo: '))
altura = int(input('Digite a autura do retângulo: '))
for i in range(altura):
    for j in range(largura):
        print('*', end=" ")

    print()

alturaTriangulo = int(input('Digite a altura do triânculo: '))

for w in range(alturaTriangulo):
    espacos = alturaTriangulo - w - 1
    asteriscos = 2 * w + 1
    print(' ' * espacos + '*' * asteriscos)
