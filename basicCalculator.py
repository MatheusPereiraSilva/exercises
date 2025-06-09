def calculadora(operacao):
    def soma(*args):
        return sum(args)
    def subtrair(*args):
        resultado = args[0]
        for numero in args[1:]:
             resultado -= numero
        return resultado
    def multiplicacao(*args):
        resultado = 1
        for num in args:
            resultado *= num
        return resultado
    def divisao(*args):
        resultado = args[0]
        for num in args[1: ]:
            if num == 0:
                raise ValueError("Divisão por zero não é permitida")
            resultado /= num
        return resultado
    if operacao == 'soma':
        return soma
    elif operacao == 'subtrair':
        return subtrair
    elif operacao == 'multiplicação':
        return  multiplicacao
    elif operacao == 'divisão':
        return divisao
    else:
        def operacaoNaoSuportada(*args):
            return 'Operação não supoertada'
        return operacaoNaoSuportada
adicionar = calculadora('soma')
print(adicionar(6, 4 ,2))
subtrair = calculadora('subtrair')
print(subtrair(8,4,2))
multiplicar = calculadora('multiplicação')
print(multiplicar(3, 2, 5))
divisao = calculadora('divisão')
print(divisao(80, 5))
