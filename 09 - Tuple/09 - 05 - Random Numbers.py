from random import randint
numeros = (randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100))
print(f'Os numeros gerados foram: {numeros}')
print(f'O menor numero é: {(sorted(numeros)[0])}')
print(f'O maior numero é: {(sorted(numeros)[4])}')
#
#Outra maneira
#
print("*"*10)
print("Outra maneira")
print("*"*10)
print("Os valores foram: ", end='')
for n in numeros:
    print(f'{n} ', end='')
print(f"\nO maior valor sorteado foi {max(numeros)}")
print(f"O menor valor sorteado foi {min(numeros)}")
