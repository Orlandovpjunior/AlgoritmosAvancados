from collections import deque

grafo = {
    1: [2, 3],
    2: [4, 5],
    3: [6, 7],
    4: [8, 9],
    5: [],
    6: [10],
    7: [],
    8: [],
    9: [],
    10: []
}

def verifica_num(numero):
    return numero == 10

def pesquisa(numero):
    lista_pesquisa = deque()
    lista_pesquisa.append(numero)
    verificados = set()

    while lista_pesquisa:
        v = lista_pesquisa.popleft()
        if v not in verificados:
            if verifica_num(numero):
                print(f"{v} Existe no grafo")
                return True
            else:
                lista_pesquisa.append(grafo[v])
                verificados.add(v)
    return False

print(pesquisa(10))


