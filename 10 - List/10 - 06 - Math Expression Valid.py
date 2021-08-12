#check if an expression is closed correctly
expr = str(input('Digite a expressao: '))
mem = list()
for sim in expr:
    if sim == '(':
        mem.append('(')
    elif sim == ')':
        if len(mem) > 0:
            mem.pop()
        else:
            mem.append(')')
            break
if len(mem) == 0:
    print('Sua expressao esta ok!')
else:
    print('Sua expressao esta errada!')