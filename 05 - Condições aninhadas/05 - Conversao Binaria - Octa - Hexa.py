#Faça um programa que leia um numero inteiro qualquer e peça ao usuario para escolher
#qual é a base de conversão, Binaria, Octa ou Hexa-Decimal
#[1] - Binario
#[2] - Octal
#[3] - Hexadeximal
num = int(input('Digite um numero inteiro: '))
print('''Escolha uma das bases de conversão:
[1] - Binario
[2] - Octal
[3] - Hexadecimal''')
opcao = int(input('Digite sua opcao: '))
if opcao == 1:
    print('{} convertido para BINARIO é {}'.format(num, bin(num)[2:])) #[2:] Fatiamento de string
elif opcao == 2:
    print('{} convertido para OCTAL é {}'.format(num, oct(num)[2:]))#[2:] Fatiamento de string
elif opcao == 3:
    print('{} convertido para HEXADECIMAL é {}'.format(num, hex(num)[2:]))#[2:] Fatiamento de string
else:
    print('Opção desconhecida!')