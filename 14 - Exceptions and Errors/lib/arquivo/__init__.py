from lib.interface import *

def arquivoExiste(nome):
    try:
        a = open(nome, 'rt') #Funcao open interna do python 'rt' = read mode
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+') #Funcao interna do python 'wt+' cria o arquivo write mode
        a.close
    except:
        print('Houve um erro ao criar o arquivo')
    else:
        print(f'Arquivo {nome} criado com sucesso')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        print(a.read())