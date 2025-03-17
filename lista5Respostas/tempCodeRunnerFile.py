t = int(input())

for _ in range(t):
    ver, edg = map(int, input().split())

    grau = {}
    count = {}
    grafo = {i: [] for i in range(1, ver + 1)}

    for _ in range(edg):
        u, v = map(int, input().split())
        grau[u] = grau.get(u, 0) + 1
        grau[v] = grau.get(v, 0) + 1
        grafo[u].append(v)
        grafo[v].append(u)
    
    maior_grau = max(grau.values())
    folha = next(v for v in grau if grau[v] == 1)

    vizinho = grafo[folha][0]
    y = grau[vizinho] - 1

    print(maior_grau, y)

