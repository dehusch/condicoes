def nasc(n):
    global ano
    ano = 2021 - n
    if ano <= 18:
        return True
    else:
        return False


num = int(input('Digite o ano que voce nasceu: '))
print(nasc(num))
if nasc(num):
    print(f'Você tem {ano} anos! Não pode votar!')
else:
    print(f'Você tem {ano} anos! Pode votar!')