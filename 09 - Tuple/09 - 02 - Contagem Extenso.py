numero = ("Zero", "Um", "Dois", "Tres", "Quatro", "Cinco", "Seis", "Sete", "Oito", "Nove", "Dez")
escolha = int(input("Digite um numero entre O e 10:"))
while escolha > 10 or escolha < 0:
    print(f'Você digitou errado digite um número valido')
    escolha = int(input("Digite um numero entre O e 10:"))
print(numero[escolha])
print("FIM")
#outro metodo
cont = ("Zero", "Um", "Dois", "Tres", "Quatro", "Cinco", "Seis", "Sete", "Oito", "Nove", "Dez")
while True:
    num = int(input('Digite um numero entre 0 e 10: '))
    if 0 <= num <= 10:
        break
    print('Tente novamente!\n')
print(f'Voce digitou o numero {cont[num]}')
