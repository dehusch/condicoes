def aumentar(preco=0, taxa=0, formato=False):
    res = preco + (preco * taxa/100)
    return res if formato is False else moeda(res)


def diminuir(preco=0, taxa=0, formato=False):
    res = preco - (preco * taxa/100)
    return res if formato is False else moeda(res)


def dobro(preco=0, formato=False):
    res = preco * 2
    return res if formato is False else moeda(res)


def metade(preco=0, formato=False):
    res = preco / 2
    return res if formato is False else moeda(res)


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.',',')

#\t é tabulação na linha para ficar alinhado
def resumo(preco=0, taxaAumento=10, taxaReduc=5):
    print(f'Preço analisado: \t{moeda(preco)}')
    print(f'O dobro é: \t\t{dobro(preco, True)}')
    print(f'A metade é: \t\t{metade(preco, True)}')
    print(f'Com {taxaAumento}% de aumento: \t{aumentar(preco, taxaAumento, True)}')
    print(f'Com {taxaReduc}% de reducao: \t{diminuir(preco, taxaReduc, True)}')

    