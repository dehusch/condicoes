#Vote ranged age
#16 <
#16 > 18
#18 > 65
#65 >
def voto(year):
    from datetime import date
    atual = date.today().year
    idade = atual - year
    if idade < 16:
        return f'Com {idade} anos: Não vota'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: Voto opcional'
    else:
        return f'Com {idade} anos: Voto Obrigatorio'


birth = int(input('Em que ano você nasceu?: '))
print(voto(birth))
#
#
#
#
#
#How I thought it was....
#
#
def nasc(n):
    global ano
    ano = 2021 - n
    if ano <= 16:
        return True
    else:
        return False


num = int(input('Digite o ano que voce nasceu: '))
print(nasc(num))
if nasc(num):
    print(f'Você tem {ano} anos! Não pode votar!')
else:
    print(f'Você tem {ano} anos! Pode votar!')