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
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3}')
    finally:
        a.close()

def cadastrar(arq, nome='Desconhecido', idade=0):
    try:
        a = open(arq, 'at+') # at+ = Append text adicionar '+'
    except:
        print('Houve um erro na abertura do arquivo!')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um erro na adicao de dados')
        else:
            print(f'Novo registro de {nome} adicionado.')
            a.close()