from collections import deque

def bfs(start, visited, adj):

    fila = deque()
    fila.append(start)
    visited[start] = True

    while fila:
        v = fila.popleft()

        for vizinho in adj[v]:
            if not visited[vizinho]:
                fila.append(vizinho)
                visited[vizinho] = True

componentes = 0

n, m = map(int, input().split())
adj = {i: [] for i in range(1, n + 1)}
visited = [False] * (n + 1)

for i in range(1, n + 1):
    if not visited[i]:
        bfs(i, visited, adj)
        componentes += 1

print("SIM" if componentes == 1 else "NAO")
