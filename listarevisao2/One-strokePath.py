n, m = map(int, input().split())

adj = {i: [] for i in range(1, n + 1)}

for _ in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

def dfs(v, visitados, count):
    if count == n:
        return 1

    total = 0
    for vizinho in adj[v]:
        if not visitados[vizinho]:
            visitados[vizinho] = True
            total += dfs(vizinho, visitados, count + 1)
            visitados[vizinho] = False
    return total

visitados = [False] * (n + 1)
visitados[1] = True

res = dfs(1, visitados, 1)
print(res)
