from collections import deque

def eh_bipartido(start, adj, cor):
    fila = deque()
    fila.append(start)
    cor[start] = 0

    while fila:
        v = fila.popleft()

        for vizinho  in adj[v]:
            if cor[vizinho] == -1:
                cor[vizinho] = 1 - cor[v]
                fila.append(vizinho)
            elif cor[vizinho] == cor[v]:
                return False
    return True

n,m = map(int, input().split())

adj = {i: [] for i in range(1, n + 1)}

for i in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

cor = [-1] * (n + 1)

for i in range(1, n + 1):
    if cor[i] == -1:
        bipartido = eh_bipartido(i,adj, cor)
        if bipartido == False: 
            break

print("SIM" if bipartido else "NAO")