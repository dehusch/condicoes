valores = list()
maior = 0
menor = 0
for v in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
    if v == 0:
        maior = menor = valores[v]
    else:
        if valores[v] > maior:
            maior = valores[v]
        if valores[v] < menor:
            men = valores[v]
print(f'Voce digitou os valores: {valores}')
print(f'O maior valor é {maior} na(s) posicão(ões) ', end='')
for c, v, in enumerate(valores):
    if v == maior:
        print(f'{c}, ', end='')
print()
print(f'O menor valor é {menor} na(s) posição(ões) ', end='')
for c, v, in enumerate(valores):
    if v == menor:
        print(f'{c}, ', end='')
print()
print('FIM')
