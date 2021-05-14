#se jogador escolhe par e a soma do numjogador e numpc / (divido) por 2 = 0, JOGADOR GANHA
#se jogador escolhe impar e a soma do numjogador e numpc / (divido) por 2 != 0, JOGADOR PERDE
from random import randint
cont = 0
while True:
    jogador = str(input("Escolha PAR ou IMPAR [P/I]: ")).upper()
    numjogador = int(input("Escolha um numero de 1 a 10: "))
    numpc = randint(0, 10)
    soma = numjogador + numpc
    result = soma % 2
    print(f"O computador escolheu {numpc}")
    print(f"A soma dos numeros foi {soma}")
    if jogador == "P":
        if result == 0:
            cont = cont + 1
            print("VOCE GANHOU!")
        if result != 0:
            print("VOCE PERDEU")
            print(f"Voce ganhou {cont} vezes")
            break
    if jogador == "I":
        if result != 0:
            cont = cont + 1
            print("VOCE GANHOU")
        if result == 0:
            print("VOCE PERDEU")
            print(f"Voce ganhou {cont} vezes")
        break
#
#OUTRA FORMA
#
# copy from https://gist.github.com/EduardoLimas
#
#Neste caso é utilizado o while "variavel" not in "String"
#
from random import randint
print('-=' * 20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-=' * 20)
v = 0
while True:
    opcao = ' '
    while opcao not in 'pi':
        opcao = str(input('Você quer par ou ímpar? (P/I) ')).lower().strip()[0]
    jogador = int(input('Digite um valor: '))
    pc = randint(0, 10)
    total = pc + jogador
    print(f'Você jogou {jogador} e o computador jogou {pc}. Total deu {total}.', end=' ')
    print('DEU PAR.' if total % 2 == 0 else 'DEU ÍMPAR.')
    if opcao in 'p':
        if total % 2 == 0:
            print('\033[1;32mVOCÊ GANHOU! Vamos continuar.\033[m')
            v += 1
        else:
            print('\033[1;31mVocê perdeu!\033[m')
            break
    if opcao in 'i':
        if total % 2 == 1:
            print('\033[1;32mVOCÊ GANHOU! Vamos continuar.\033[m')
            v += 1
        else:
            print('\033[1;31mVocê perdeu!\033[m')
            break
print(f'\033[1;35mACABOU!\033[m Você venceu {v} vezes')