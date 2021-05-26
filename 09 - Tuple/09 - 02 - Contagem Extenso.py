numero = ("Zero", "Um", "Dois", "Tres", "Quatro", "Cinco", "Seis", "Sete", "Oito", "Nove", "Dez")
escolha = int(input("Digite um numero entre O e 10:"))
while escolha > 10 or escolha < 0:
    print(f'Você digitou errado digite um número valido')
    escolha = int(input("Digite um numero entre O e 10:"))
print(numero[escolha])
print("FIM")