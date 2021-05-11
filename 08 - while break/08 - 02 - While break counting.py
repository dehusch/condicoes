n = 0
s = 0
c = 0
while True: #Torna o loop infinito
  n = int(input('Digite um numero: '))
  if n == 999:
    break
  s = s + n
  c = c + 1
print(f"Você digitou {c} vez(es) e a soma vale{s}")