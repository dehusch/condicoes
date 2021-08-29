import moedaparam
p = float(input('Digite o preço: R$'))
print(f'A metade é = {moedaparam.metade(p, True)}')
print(f'O dobro é = {moedaparam.dobro(p, True)}')
print(f'Aumentando 10% = {moedaparam.aumentar(p, 10, True)}')
print(f'Diminuindo 13% = {moedaparam.diminuir(p, 13, True)}')