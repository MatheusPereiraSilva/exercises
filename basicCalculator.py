while True:
    print('\nCalculadora Simples:')
    print('1 - Adição')
    print('2 - Subtração')
    print('3 - Multiplicação')
    print('4 - Divisão')
    print('5 - Sair')

    escolha = input('Escolha uma operação: ')

    if escolha == '5':
        print('Até mais!')
        break
    num1 = float(input('Digite o primeiro número: '))
    num2 = float(input('Digite o segundo número: '))

    if escolha == '1':
        resultado = num1 + num2
        print(f'O resultado é: {resultado}')
    elif escolha == '2':
        resultado = num1 - num2
        print(f'O resultado é: {resultado}')
    elif escolha == '3':
        resultado = num1 * num2
        print(f'O resultado é: {resultado}')
    elif escolha == '4':
        if num2 != 0:
            resultado = num1 / num2
            print(f'O resultado é: {resultado}')
        else:
            print('Erro de divisão por zero')
    else:
        print('Opção inválida. Tente novamente')