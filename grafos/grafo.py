from collections import deque

grafo = {
    'voce': ['alice', 'bob', 'claire'],
    'bob': ['anuj', 'peggy'],
    'alice': ['peggy'],
    'claire': ['thom', 'jonny'],
    'anuj': [],
    'peggy': [],
    'thom': [],
    'jonny': []
}

def pessoa_e_vendedor(nome):
    return nome[-1] == 'm'

def pesquisa(nome):
    lista_pesquisa = deque()
    lista_pesquisa += grafo[nome]
    verificados = set()

    while lista_pesquisa:
        pessoa = lista_pesquisa.popleft()
        if pessoa not in verificados:
            if pessoa_e_vendedor(pessoa):
                print(pessoa + " é um vendedor de manga")
                return True
            else:
                lista_pesquisa += grafo[pessoa]
                verificados.add(pessoa)
    return False

print(pesquisa('voce'))
