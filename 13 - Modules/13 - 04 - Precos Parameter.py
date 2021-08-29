import moedaparam
p = float(input('Digite o preço: R$'))
print(f'A metade é = {moedaformat.moeda(moedaformat.metade(p))}')
print(f'O dobro é = {moedaformat.moeda(moedaformat.dobro(p))}')
print(f'Aumentando 10% = {moedaformat.moeda(moedaformat.aumentar(p, 10))}')
print(f'Diminuindo 13% = {moedaformat.moeda(moedaformat.diminuir(p, 13))}')