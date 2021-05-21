nota50 = 50
nota20 = 20
nota10 = 10
nota1 = 1
valor = int(input("Digite o valor para sacar: "))
while True:
    nota50 = valor // nota50
    nota20 = (valor % 50) // nota20
    nota10 = (valor % 20) // nota10
    nota1 = (valor % 10) // nota1
    break
print(f"Notas de 50: {nota50}")
print(f"Notas de 20: {nota20}")
print(f"Notas de 10: {nota10}")
print(f"Notas de 1: {nota1}")
#
#Outra Forma
#
saque = int(input("Digite o valor para sacar: "))
saida = 0

while saida < saque :
    saidanota50 = nota


