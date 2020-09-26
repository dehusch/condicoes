num1 = int(input('Digite o primeiro numero: '))
num2 = int(input('Digite o segundo numero: '))
opcao = 0
while opcao != 5:
    print('''    [1] - SOMA
    [2] - multiplicar
    [3] - maior
    [4] - novos numeros
    [5] - Sair''')
    opcao = int(input('Qual é sua opção?: '))
    if opcao == 1:
        soma = num1 + num2
        print(f'A soma entre {num1} e {num2} é {soma}')
    elif opcao == 2:
        mult = num1 * num2
        print(f'A multiplicação entre {num1} e {num2} é {mult}')
    elif opcao == 3:
        if num1 > num2:
            maior = num1
        else:
            maior = num2
        print(f'Entre {num1} e {num2}, o maior é {maior}')
    elif opcao == 4:
        print('Informe os numeros novamente!')
        num1 = int(input('Digite o primeiro valor: '))
        num2 = int(input('Digite o segundo numero: '))
    elif opcao == 5:
        print('Finalizando!!!')
print('Fim do programa')