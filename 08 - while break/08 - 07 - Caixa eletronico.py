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
val1 = int(input("Digite o valor para sacar: "))
total = val1
ced = 50
totced = 0
while True:
    if total >= ced:
        total = total - ced
        totced = totced + 1
    else:
        if totced > 0:
            print(f"Total de {totced} cedulas de R${ced}")
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
print("Fim do programa")
