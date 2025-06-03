import  random
numero_secreto1 = random.randint(1, 10)
numero_secreto2 = random.randint(1, 10)

tentativas = 5

adivinhou1 = False
adivinhou2 = False

while tentativas > 0 and (not adivinhou1 or not adivinhou2):
    print(f'Tentativas restantes: {tentativas}')
    palpite1 = int(input('Adivinhe o primeiro número secreto (1 0 10): '))
    palpite2 = int(input('Adivinhe o segundo número secreto (1 0 10): '))

    if palpite1 == numero_secreto1:
        print('Você adivinhou o primeiro número!')
        adivinhou1 = True
    if palpite2 == numero_secreto2:
        print('Você adivinhou o segundo número!')
        adivinhou2 = True
    if not adivinhou1 or not adivinhou2:
        print('Tente Novamente!')
    tentativas -=1

if adivinhou1 and adivinhou2:
    print(f'Parabéns! Você adivinhou os números \nNúmero 1: {numero_secreto1} \nNúmero 2: {numero_secreto2} \nCom {tentativas} tntativas restantes')
else:
    print(f'Você não acertou, os números eram \nNúmero 1: {numero_secreto1} \nNúmero 2: {numero_secreto2}')