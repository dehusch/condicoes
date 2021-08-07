time = ("América-MG", "Sao Paulo", "Athletico", "Atlético-GO", "Atlético-MG", "Bahia", "Ceará", "Chapecoense")
print(f'Estes são os times da tabela do Campeonato Brasileiro: ')
print(time)
print(f'Estes são os 5 primeiros: {time[0: 5]} ')
print(f'Os ultimos quatro colocados: {time[-4:]}')
print(f'Classificação em ordem alfabetica: {sorted(time)}')
print(f'O Chapecoense esta na {time.index("Chapecoense")+1}')#Aqui tem que ter Aspas duplas e aspas simples.