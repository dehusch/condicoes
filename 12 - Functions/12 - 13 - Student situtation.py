def notas(*n, sit=False):
    '''
    Funcao para analisar a situacao de varios alunos
    param n: uma ou mais notas dos alunos
    param sit: valor opcional para mostrar a situacao
    return: dicionario com varias informacoes da turma
    '''
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)
    if sit:
        if r ['media'] >= 7:
            r['situacao'] = 'BOA'
        elif r['media'] >= 5:
            r['situacao'] = 'RAZOAVEL'
        else:
            r['situacao'] = 'RUIM'
    return r


#Programa principal
resp = notas(5.5, 6, 4, 2, 10, 8, sit=True)
print(resp)