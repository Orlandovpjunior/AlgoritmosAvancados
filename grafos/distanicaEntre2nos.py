from collections import deque

def bfs_distancia(grafo, inicio, fim):
    fila = deque([(inicio, 0)])
    visitados = set()

    while fila:
        no, distancia = fila.popleft()

        if no == fim:
            return distancia
        
        if no not in visitados:
            visitados.add(no)

            for vizinho in grafo[no]:
                if vizinho not in visitados:
                    fila.append((vizinho, distancia + 1))
    return -1

n, m = map(int, input().split())

grafo = {i: [] for i in range(1, n + 1)}

for _ in range(m):
    u, v = map(int, input().split())
    grafo[u].append(v)
    grafo[v].append(u) 

origem, destino = map(int, input().split())

print(bfs_distancia(grafo, origem, destino))