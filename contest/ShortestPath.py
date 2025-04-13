import heapq

n, m = map(int, input().split())
A = list(map(int, input().split()))

adj = {i: [] for i in range(1, n + 1)}

for _ in range(m):
    u, v, b = map(int, input().split())
    adj[u].append((v, b))
    adj[v].append((u, b))

infinito = float("inf")
custos = {i: infinito for i in range(1, n + 1)}
custos[1] = A[0] 

fila = [(A[0], 1)]

while fila:
    custo_atual, no_atual = heapq.heappop(fila)

    if custo_atual > custos[no_atual]:
        continue 

    for vizinho, peso_aresta in adj[no_atual]:
        custo_total = custo_atual + peso_aresta + A[vizinho - 1]
        if custo_total < custos[vizinho]:
            custos[vizinho] = custo_total
            heapq.heappush(fila, (custo_total, vizinho))

res = [str(custos[i]) for i in range(2, n + 1)]
print(" ".join(res))
