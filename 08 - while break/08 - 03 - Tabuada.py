num = 1
while True:
    num = int(input('Digite um valor: '))
    if num <= 0:
        break
    for c in range (0, 11):
        print(f"{num} x {c} = {num*c}")
print("FIM")