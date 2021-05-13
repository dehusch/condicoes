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
#print(f"{numpc}")
#print(f"{soma}")
#print(f"{result}")
#se jogador escolhe par e a soma do numjogador e numpc / (divido) por 2 = 0, JOGADOR GANHA
#se jogador escolhe impar e a soma do numjogador e numpc / (divido) por 2 != 0, JOGADOR PERDE