import moeda
p = float(input('Digite o preço: R$'))
print(f'A metade é = {moeda.metade(p):.2f}')
print(f'O dobro é = {moeda.dobro(p):.2f}')
print(f'Aumentando 10% = {moeda.aumentar(p):.2f}')
print(f'Diminuindo 13% = {moeda.diminuir(p):.2f}')