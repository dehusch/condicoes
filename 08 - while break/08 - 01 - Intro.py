#forma sem break!
cont = 1
while cont <= 10:
    print(cont)
    cont += 1
print('Acabou')
#forma sem break somando o valor do fim do while
n = 0
s = 0
while n != 999:
  n = int(input('Digite um numero: '))
  s = s + n #neste caso se digitar 999 ele vai somar também o 999 e vai parar!
print(f"A soma vale{s}")

#break
n = 0
s = 0
while True: #Torna o loop infinito
  n = int(input('Digite um numero: '))
  if n == 999:
    break
  s = s + n
print(f"A soma vale{s}")