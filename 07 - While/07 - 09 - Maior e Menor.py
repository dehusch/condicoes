#Um programa que leia varios numeros inteiros e mostre a media, o maior numero
#o menor numero e perguntar se quer continuar a digitar os numeros:
resp = 'S'
soma = quant = media = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um numero: '))
    soma = soma + num
    quant = quant + 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
media = soma / quant
print(f'Voce digitou {quant} numeros e a media é {media:.2f}')
print(f'O maior valor é {maior} e o menor valor é {menor}')

#another way

valor = 0
contador = 0
soma = 0
media = 0
maior = 0
menor = 0
resposta = "S"
while resposta == "S":
  valor = int(input('Digite um valor: '))
  resposta = str(input('Quer continurar [S/N]: ')).upper()
  contador = contador + 1
  soma = soma + valor
  media = soma / contador
  if contador == 1:
    maior = menor = valor
  else:
    if valor > maior:
      maior = valor
    if valor < menor:
      menor = valor

print(f"Voce digitou {contador} e a media é {media}")
print(f"O maior valor foi {maior} e o menor valor foi {menor}")
print("Fim")