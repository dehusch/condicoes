#Crie um programa e informe se a frase é ou não palindrome
#Exemplo: Apos a sopa
#desconsiderar os espaços e os acentos
frase = str(input('Digite uma frase: ')).strip().upper() #strip tira os espacos anterior e upper coloca tudo em maiusculo
palavras = frase.split() #Aqui a frase sera dividida em palavras
junto = ''.join(palavras) #Aqui todas as palavras sao juntadas sem espaço ('')
inverso = ''
for letra in range(len(junto) -1, -1, -1):#Aqui começa de tras pra frente
    inverso = inverso + junto[letra]
print(junto, inverso)
if inverso == junto:
    print('Temos um palindromo')
else:
    print('Isso não é um palindromo')

