from collections import deque

n, m = map(int, input().split())

grafo = {i: [] for i in range(1, n + 1)}
grau_de_entrada = {i: 0 for i in range(1, n + 1)}

for _ in range(m):
    a,b = map(int, input().split())
    grafo[a].append(b)
    grau_de_entrada[b] += 1

lista = deque([curso for curso in grau_de_entrada if grau_de_entrada[curso] == 0])

sequencia = []
visitados = set()

while lista:
    v = lista.popleft()
    sequencia.append(v)

    if v in visitados:
        continue
    visitados.add(v)

    for vizinho in grafo[v]:
        grau_de_entrada[vizinho] -= 1
        if grau_de_entrada[vizinho] == 0:
            lista.append(vizinho)

if len(sequencia) == n:
    print(*sequencia)
else:
    print("IMPOSSIBLE")
