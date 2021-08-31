from lib.interface import *

while True:
    resposta = menu(['Listar Pessoas', 'Cadastrar Pessoas', 'Sair do Sistema'])
    if resposta == 1:
        print('Opcao 1')
    elif resposta == 2:
        print('Opcao 2')
    elif resposta == 3:
        print('Saindo do programa')
        break
    else:
        print('Erro! Digite uma opção valida!')
