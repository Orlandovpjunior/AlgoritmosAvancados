import heapq

n,m = map(int, input().split())

adj = {i: {} for i in range(1, n + 1)}
infinito = float("inf")

custos = {i: infinito for i in range(1, n + 1)}
custos[1] = 0

pais = {i: None for i in range(1, n + 1)}

for _ in range(m):
    a, b, c = map(int, input().split())
    adj[a][b] = c

fila = [(0,1)]
heapq.heapify(fila)

while fila:
    custo_atual, nodo_atual = heapq.heappop(fila)

    for node, custo in adj[nodo_atual].items():
        novo_custo = custo_atual + custo

        if novo_custo < custos[node]:
            custos[node] = novo_custo
            pais[node] = nodo_atual
            heapq.heappush(fila, (novo_custo, node))

if custos[n] == infinito:
    print(-1)
else:
    caminho = []

    atual = n

    while atual is not None:
        caminho.append(atual)
        atual = pais[atual]
    
    caminho.reverse()
    print(*caminho)
