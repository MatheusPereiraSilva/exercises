saldo = 1000.00
while True:
    print('\nCaixa Eletrônico')
    print('1 - Verificar Saldo')
    print('2 - Depositar Dinheiro')
    print('3 - Sacar Dinheiro')
    print('4 - Sair')
    opcao = input('Escolha uma opção (1-4): ')

    if opcao == '1':
        print(f'Seu saldo é R${saldo:.2f}')
    elif opcao == '2':
        deposito = float(input('Digite o valor do depósito: R$'))
        if deposito > 0:
            saldo += deposito
            print(f'Depósito de R${deposito:.2f} realizado com sucesso!')
        else:
            print('Valor de depósito inválido')
    elif opcao == '3':
        saque = float(input('Digite o valor do saque: R$'))
        if saque > 0 and saque <= saldo:
            saldo -= saque
            print(f'Saque de R${saque:.2f} realizado com sucesso!')
        else:
            print('Valor de saque inválido ou saldo insuficiente')
    elif opcao == '4':
        print('Obrigado por utilizar o nosso caixa eletrônico. Até mais!')
        break
    else:
        print('Opção inválida. Por favor, tente novamente.')