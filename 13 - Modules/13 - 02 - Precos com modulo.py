import moeda
p = float(input('Digite o preço: R$'))
print(f'A metade é {moeda.metade(p)}')
print(f'O dobro é {moeda.dobro(p)}')
print(f'Aumentando 10%{moeda.aumentar(p)}')
print(f'Diminuindo 13%{moeda.diminuir(p)}')