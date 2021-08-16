#Create seven random numbers and set in an only single list
#sort the number in odds and evens
#at the end, shows the odds and evens number separated in crescent sort
numbers = [[], []]
value = 0
for c in range(1, 8):
    value = int(input(f'Digite o {c}º valor: '))
    if value % 2 == 0:
        numbers[0].append(value)
    else:
        numbers[1].append(value)
numbers[0].sort()
numbers[1].sort()
print(f'Os valores pares: {numbers[0]}')
print(f'Os valores impares: {numbers[1]}')
